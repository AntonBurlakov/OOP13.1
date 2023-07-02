from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIX = Path.joinpath(ROOT, 'src')
DATA_ITEMS = Path.joinpath(FIX, 'items.csv')
