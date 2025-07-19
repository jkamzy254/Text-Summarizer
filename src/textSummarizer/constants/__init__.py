from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[3]  # Go up from 'Proj/constants/__init__.py' to project root
CONFIG_FILE_PATH = ROOT_DIR / "config" / "config.yaml"
PARAMS_FILE_PATH = ROOT_DIR / "params.yaml"