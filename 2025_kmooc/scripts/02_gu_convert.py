# -*- coding: utf-8 -*-
"""
[텍스트 마이닝 2] 한문 숫자를 아라비아 숫자로 변환하기

01_gu_extract.py 가 만든 CSV를 읽어, 한문 숫자를 아라비아 숫자로 바꿔 저장합니다.
예) 一十萬七百九十  ->  100790
"""

import csv
import re
from pathlib import Path

# ── 경로 설정 ────────────────────────────────────────────────
BASE = Path(__file__).resolve().parent.parent
input_csv = BASE / "data" / "text-mining" / "sejong_gu_data_sample.csv"
output_csv = BASE / "data" / "text-mining" / "sejong_gu_data_converted.csv"

# ── 1단계: 한문 숫자 매핑 ────────────────────────────────────
digits = {
    '零': 0, '〇': 0, '一': 1, '二': 2, '三': 3, '四': 4,
    '五': 5, '六': 6, '七': 7, '八': 8, '九': 9
}

units = {
    '十': 10,
    '百': 100,
    '千': 1000
}

large_units = {
    '兆': 1000000000000,
    '億': 100000000,
    '萬': 10000
}


def parse_section(section: str) -> int:
    """한문 숫자 섹션을 아라비아 숫자로 변환"""
    result = 0
    num = 0
    for char in section:
        if char in digits:
            num = digits[char]
        elif char in units:
            unit = units[char]
            if num == 0:
                num = 1
            result += num * unit
            num = 0
        else:
            pass  # 알 수 없는 문자 무시
    result += num
    return result


def hanja_to_number(hanja_str: str) -> int:
    """전체 한문 숫자 문자열을 아라비아 숫자로 변환"""
    hanja_str = re.sub(r'[^零〇一二三四五六七八九十百千萬億兆]', '', hanja_str)
    total = 0
    parts = re.split('([兆億萬])', hanja_str)
    parts.append('')  # 마지막 단위 처리용
    i = 0
    while i < len(parts):
        section = parts[i]
        if i + 1 < len(parts) and parts[i + 1] in large_units:
            unit = large_units[parts[i + 1]]
            section_value = parse_section(section)
            total += section_value * unit
            i += 2
        else:
            total += parse_section(section)
            i += 1
    return total


# ── 2단계: CSV 파일 불러오기 ─────────────────────────────────
gu_data = []
with open(input_csv, mode="r", encoding="utf-8-sig") as file:
    reader = csv.reader(file)
    header = next(reader)  # 헤더 저장
    for row in reader:
        gu_data.append(row)

print(f"{len(gu_data)}개의 데이터를 불러왔습니다.")

# ── 3단계: 한문 숫자 변환 ────────────────────────────────────
converted_data = []
for row in gu_data:
    han_number = row[0]  # 1열(첫 번째 열)에 한문 숫자가 있다고 가정
    arabic_number = hanja_to_number(han_number)
    converted_data.append([han_number, arabic_number])
    print(f"  {han_number}  ->  {arabic_number}")

# ── 4단계: 변환된 데이터 다시 CSV로 저장 ─────────────────────
with open(output_csv, mode="w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["구(口) 데이터 (한문)", "구(口) 데이터 (아라비아 숫자)"])
    for row in converted_data:
        writer.writerow(row)

print(f"한문 숫자가 변환되어 {output_csv} 파일로 저장되었습니다!")
