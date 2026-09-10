#!/usr/bin/env python3
"""Markdown format checks for ComfyUI node documentation.

Checks every .md file under comfyui_embedded_docs/docs/ for the recurring
AI-generation defects that have shipped to production:

1. Outer ```markdown fences wrapping the whole document (renders as a code block)
2. Translated data-type names in table cells (MODEL -> MODELO/МОДЕЛЬ/モデル/...)
3. Translated output identifiers in Outputs tables (positive -> positivo/正向/...)
4. Duplicate H1 headings (corrupts the document outline)
5. English Required-column residue in translations (| Yes | / | No | where localized)
6. Missing source fingerprint footer (en.md must carry the SHA-256 of its source)

Exit code 1 if any error-level check fails. Warnings do not fail the run.
"""
import os
import re
import subprocess
import sys
from pathlib import Path

DOCS_DIR = Path(__file__).resolve().parents[2] / "comfyui_embedded_docs" / "docs"

# --- data-type names must stay English (programmatic schema identifiers) ---
TRANSLATED_TYPES = {
    # es / pt-BR
    "MODELO", "CADENA", "IMAGEN", "IMAGEM", "ENTERO", "FLOTANTE", "MÁSCARA",
    "MASCARA", "CONDICIONAMIENTO", "LATENTE", "BOOLEANO", "SEQUÊNCIA",
    "CONDICIONAMENTO",
    # fr
    "CHAÎNE", "CHAINE", "MODÈLE", "FLOTTANT", "ENTIER",
    # ru
    "МОДЕЛЬ", "СТРОКА", "ИЗОБРАЖЕНИЕ", "МАСКА", "ЦЕЛОЕ", "ДРОБНОЕ",
    "ЛАТЕНТ", "ЛОГИЧЕСКОЕ", "БУЛЕВО",
    # ja / ko / zh
    "モデル", "画像", "文字列", "整数", "マスク", "モデル",
    "이미지", "모델", "문자열", "정수", "마스크",
    "模型", "图像", "字符串", "遮罩", "蒙版",
}

# --- output identifiers must stay English ---
TRANSLATED_OUTPUTS = {
    "positivo", "negativo", "positif", "négatif", "salida", "salidas",
    "позитивный", "негативный", "ポジティブ", "ネガティブ",
    "긍정", "부정", "正向", "负向",
}

# Languages whose Required column must NOT contain English Yes/No.
# (es "No", fr "Non", pt-BR "Não" are valid localizations.)
EN_RESIDUE_LANGS = {"zh", "zh-TW", "ja", "ko", "ru", "ar", "tr", "fa", "pt-BR"}

FP_RE = re.compile(r"Source fingerprint[^\n]*`([a-f0-9]{64})`")


def check_file(path: Path):
    """Return (errors, warnings) for one doc file."""
    errors, warnings = [], []
    rel = path.relative_to(DOCS_DIR.parent)
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        errors.append(f"{rel}: file is not valid UTF-8")
        return errors, warnings

    lang = path.stem  # en, zh, ja, pt-BR, ...

    # 1. outer markdown fence
    if re.search(r"^```markdown\s*$", text, re.M):
        errors.append(f"{rel}: document wrapped in ```markdown fence "
                      f"(strips to render properly)")

    # 2. translated data-type names in table cells
    for line in text.splitlines():
        if line.startswith("|"):
            for cell in line.split("|"):
                if cell.strip() in TRANSLATED_TYPES:
                    errors.append(f"{rel}: translated data type "
                                  f"'{cell.strip()}' (keep English schema names)")
                    break

    # 3. translated output identifiers in Outputs tables
    in_outputs = False
    for line in text.splitlines():
        if line.startswith("## "):
            in_outputs = "output" in line.lower() or "出力" in line or "输出" in line
            continue
        if in_outputs and line.startswith("|"):
            cells = [c.strip().strip("`") for c in line.split("|")[1:-1]]
            if cells and cells[0] in TRANSLATED_OUTPUTS:
                errors.append(f"{rel}: translated output identifier "
                              f"'{cells[0]}' (keep English programmatic names)")

    # 4. duplicate H1
    h1s = re.findall(r"^# .+", text, re.M)
    if len(h1s) > 1:
        errors.append(f"{rel}: {len(h1s)} H1 headings (expected exactly 1)")

    # 5. English Yes/No residue in the Required column of translations
    if lang in EN_RESIDUE_LANGS:
        for i, line in enumerate(text.splitlines(), 1):
            if line.startswith("|") and re.search(r"\|\s*Yes\s*\|", line):
                errors.append(f"{rel}:{i}: English 'Yes' in Required column "
                              f"(translate: 是/はい/예/Да/نعم/...)")

    # 6. fingerprint footer (en.md only; translations inherit via sync)
    if lang == "en" and not FP_RE.search(text):
        warnings.append(f"{rel}: missing 'Source fingerprint (SHA-256)' footer")

    return errors, warnings


def main():
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--changed-only", action="store_true",
        help="Only check files changed vs the PR base (used on PRs; avoids "
             "failing on pre-existing defects elsewhere in the repo)")
    parser.add_argument(
        "--base", default="origin/main",
        help="Base ref for --changed-only (default: origin/main)")
    args = parser.parse_args()

    if not DOCS_DIR.is_dir():
        print(f"docs directory not found: {DOCS_DIR}", file=sys.stderr)
        return 1

    files = sorted(DOCS_DIR.rglob("*.md"))

    if args.changed_only:
        changed = set(
            l.strip() for l in subprocess.run(
                ["git", "diff", "--name-only", f"{args.base}...HEAD", "--",
                 "comfyui_embedded_docs/docs/"],
                capture_output=True, text=True, check=True,
            ).stdout.splitlines()
            if l.strip().endswith(".md")
        )
        files = [f for f in files
                 if str(f.relative_to(Path.cwd())) in changed]
        print(f"Checking {len(files)} files changed vs {args.base}")

    all_errors, all_warnings = [], []
    n_files = 0
    for path in files:
        n_files += 1
        errs, warns = check_file(path)
        all_errors += errs
        all_warnings += warns

    for w in all_warnings:
        print(f"warn: {w}")
    for e in all_errors:
        print(f"erro: {e}")

    print(f"\nChecked {n_files} files: "
          f"{len(all_errors)} errors, {len(all_warnings)} warnings")
    return 1 if all_errors else 0


if __name__ == "__main__":
    sys.exit(main())
