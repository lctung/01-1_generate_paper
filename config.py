from pathlib import Path

# 自動抓取本專案根目錄
ROOT = Path(__file__).resolve().parent

# ROOT底下的子資料夾
DIR_GEN_CP950 = ROOT / "1_generate_CP950"
DIR_GEN_MANUSCRIPT = ROOT / "2_generate_manuscript"

# 常用資料夾
DIR_FONTS = DIR_GEN_MANUSCRIPT / "font_type"
DIR_CP950_JSON = DIR_GEN_MANUSCRIPT / "CP950"
DIR_FINAL_PDF = DIR_GEN_MANUSCRIPT / "manuscripts-final"

# 各稿紙標題資料夾因為要抓 info.json，所以沒有放在這
# dir_title = f"{config.DIR_GEN_MANUSCRIPT}/{title}"

# 常用檔案
PATH_MANUSCRIPT_PAPER = DIR_GEN_CP950 / "manuscript.txt"
PATH_CHARACTER_PAPER = DIR_GEN_CP950 / "character.txt"
PATH_CHARACTER_HISTORY = DIR_GEN_CP950/ "character_history.txt"
PATH_INFO_JSON = DIR_GEN_MANUSCRIPT / "info.json"