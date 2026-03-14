import ast
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "requirements.in"

EXCLUDE_DIRS = {
    ".git", ".venv", "venv", "__pycache__", ".ipynb_checkpoints",
    "data", "models", "reports", "outputs", "dist", "build"
}

IMPORT_TO_PACKAGE = {
    "sklearn": "scikit-learn",
    "dotenv": "python-dotenv",
    "yaml": "PyYAML",
    "PIL": "Pillow",
}

LOCAL_MODULES = {"titanic_surv"}
stdlib = set(getattr(sys, "stdlib_module_names", set()))

def should_skip(path: Path) -> bool:
    return any(part in EXCLUDE_DIRS for part in path.parts)

def extract_imports_from_code(code: str) -> set[str]:
    mods = set()
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return mods
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for n in node.names:
                mods.add(n.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom) and node.module:
            mods.add(node.module.split(".")[0])
    return mods

def extract_imports_from_py(path: Path) -> set[str]:
    return extract_imports_from_code(path.read_text(encoding="utf-8", errors="ignore"))

def extract_imports_from_ipynb(path: Path) -> set[str]:
    mods = set()
    nb = json.loads(path.read_text(encoding="utf-8", errors="ignore"))
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        src = cell.get("source", [])
        code = "".join(src) if isinstance(src, list) else str(src)
        mods |= extract_imports_from_code(code)
    return mods

def normalize(mod: str):
    if not mod or mod in LOCAL_MODULES or mod in stdlib:
        return None
    return IMPORT_TO_PACKAGE.get(mod, mod)

def main():
    imports = set()

    for py in ROOT.rglob("*.py"):
        if should_skip(py):
            continue
        imports |= extract_imports_from_py(py)

    for nb in ROOT.rglob("*.ipynb"):
        if should_skip(nb):
            continue
        imports |= extract_imports_from_ipynb(nb)

    pkgs = sorted({p for m in imports if (p := normalize(m))})
    for forced in ["jupyter", "ipykernel"]:
        if forced not in pkgs:
            pkgs.append(forced)

    pkgs = sorted(set(pkgs))
    OUT.write_text("\n".join(pkgs) + "\n", encoding="utf-8")
    print(f"Wrote {OUT} with {len(pkgs)} packages.")

if __name__ == "__main__":
    main()