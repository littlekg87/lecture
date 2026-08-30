# -*- coding: utf-8 -*-
"""
[단어 분석 1] 김상헌 상소문 단어 빈도 분석

한글 텍스트에서 명사만 뽑아 빈도수를 세고, 많이 쓰인 순서대로 출력합니다.

필요한 준비물
  pip install konlpy
  ※ KoNLPy는 자바(JDK)가 설치되어 있어야 동작합니다.
    설치가 번거로우면 Google Colab 노트북을 쓰세요 (notebooks/03_word_frequency.ipynb).
"""

import re
from collections import Counter
from pathlib import Path

from konlpy.tag import Okt

# ── 경로 설정 ────────────────────────────────────────────────
BASE = Path(__file__).resolve().parent.parent
file_path = BASE / "data" / "word-analysis" / "kim-sangheon-sangso.txt"

# ── 텍스트 파일 읽기 ─────────────────────────────────────────
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# ── 한글 이외의 문자 제거 ────────────────────────────────────
text = re.sub(r"[^가-힣\s]", "", text)

# ── 형태소 분석기 사용 (명사 추출) ───────────────────────────
okt = Okt()
tokens = okt.nouns(text)

# ── 불용어 제거 ──────────────────────────────────────────────
stopwords = ["것", "저", "그", "이", "수", "있다", "하다"]
tokens = [word for word in tokens if word not in stopwords]

# ── 한 글자 단어 제외 (선택) ─────────────────────────────────
# 한 글자 명사는 의미가 모호한 경우가 많습니다. 필요 없으면 이 줄을 지우세요.
tokens = [word for word in tokens if len(word) > 1]

# ── 단어 빈도수 계산 ─────────────────────────────────────────
word_counts = Counter(tokens)

# ── 빈도수 기준 정렬 ─────────────────────────────────────────
sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# ── 결과 출력 ────────────────────────────────────────────────
print(f"총 {len(word_counts)}종류의 단어가 추출되었습니다.\n")
for word, freq in sorted_words[:50]:  # 상위 50개만
    print(f"{word}, {freq}회")
