from tqdm import tqdm
from pikepdf import Pdf
import json
import os
import sys
from pathlib import Path
# 為了抓 config.py，設定 sys.path 在 ROOT
sys.path.append(str(Path(__file__).resolve().parents[1]))
import config # 在 config.py 中填入所有路徑

with open(config.PATH_INFO_JSON,'r', encoding='utf-8') as f:
    info = json.load(f)
title = info["TITLE"]
stu_id = info['ID']
stu_name = info['NAME']

dir_title = f"{config.DIR_GEN_MANUSCRIPT}/{title}" # 該稿紙的專用資料夾

pdfs = [
    Pdf.open(f"{dir_title}/{title}-PDF/{i:03d}.svg.pdf") for i in tqdm(range(1, info["TOTAL_PAGES"] + 1))
]
output = Pdf.new()

for each in tqdm(pdfs):
    output.pages.extend(each.pages)

result_path = config.DIR_FINAL_PDF
if not os.path.exists(result_path):
    os.makedirs(result_path)

output.save(f"{result_path}/{stu_id}_{stu_name}_{title}.pdf")