# -*- coding: utf-8 -*-
"""
[텍스트 마이닝 1] 『세종실록』 지리지에서 구(口) 데이터 추출하기

원문 텍스트에서 '口'와 '。' 사이의 한문 숫자를 찾아 CSV로 저장합니다.
Windows / macOS 모두 동일하게 동작합니다.
"""

import csv
import re
from pathlib import Path

# ── 경로 설정 ────────────────────────────────────────────────
# 이 스크립트 위치를 기준으로 경로를 잡으므로, 경로를 직접 고칠 필요가 없습니다.
BASE = Path(__file__).resolve().parent.parent
txt_path = BASE / "data" / "text-mining" / "practice_1.txt"
output_csv = BASE / "data" / "text-mining" / "sejong_gu_data_sample.csv"

# ── 1단계: TXT 파일 읽어오기 ─────────────────────────────────
with open(txt_path, "r", encoding="utf-8") as file:
    lines = file.readlines()  # 파일의 모든 줄을 리스트로 저장

print("TXT 파일이 성공적으로 로드되었습니다!")
print(f"총 {len(lines)}개의 줄을 읽었습니다.")

# ── 2단계: '구(口)' 문자가 포함된 줄 찾기 ────────────────────
gu_lines = [line.strip() for line in lines if "口" in line]

print(f"총 {len(gu_lines)}개의 '구(口)' 데이터가 발견되었습니다!")

# ── 3단계: '구(口)'와 '。' 사이의 텍스트 추출 ────────────────
gu_numbers = []
for line in gu_lines:
    match = re.search(r"口(.*?)。", line)  # '口'와 '。' 사이의 모든 텍스트 찾기
    if match:
        gu_numbers.append(match.group(1).strip())

print(f"총 {len(gu_numbers)}개의 데이터가 추출되었습니다!")
print(gu_numbers[:5])  # 앞부분만 출력해서 확인

# ── 4단계: CSV 파일로 저장 ───────────────────────────────────
with open(output_csv, mode="w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["구(口) 데이터"])
    for row in gu_numbers:
        writer.writerow([row])

print(f"추출된 데이터가 {output_csv} 파일로 저장되었습니다!")
