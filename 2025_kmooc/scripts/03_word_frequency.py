# -*- coding: utf-8 -*-
"""
[4-4차시 텍스트분석 ①] 김상헌 상소문 단어 빈도수 분석

교안의 1~4단계를 그대로 옮긴 코드입니다.

필요한 준비물
  pip install konlpy
  ※ KoNLPy는 자바(JDK)가 설치되어 있어야 동작합니다.
    설치가 번거로우면 구글 코랩 노트북을 쓰세요 (notebooks/03_word_frequency.ipynb).
"""

import re
from collections import Counter
from pathlib import Path

from konlpy.tag import Okt

# ── 1단계: 텍스트 가져오기 ───────────────────────────────────
# 이 스크립트 위치를 기준으로 경로를 잡으므로, 경로를 직접 고칠 필요가 없습니다.
BASE = Path(__file__).resolve().parent.parent
file_path = BASE / "data" / "word-analysis" / "kim-sangheon-sangso.txt"

with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# ── 2단계: 텍스트 전처리 (불용어 제거, 형태소 분석) ──────────
# 한글 이외의 문자 제거
text = re.sub(r"[^가-힣\s]", "", text)

# 형태소 분석기 사용 (명사 추출)
okt = Okt()
tokens = okt.nouns(text)

# ── 3단계: 단어빈도수 계산 ───────────────────────────────────
word_counts = Counter(tokens)

# 빈도수 기준 정렬
sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# ── 4단계: 결과 출력 ─────────────────────────────────────────
for word, freq in sorted_words:
    print(f"{word}, {freq}회")

# ── (교안 밖) 불용어를 걸러내고 싶다면 ───────────────────────
# '것', '수', '그' 처럼 어느 글에나 나오는 말을 빼면
# 이 글이 무엇에 관한 글인지 훨씬 잘 드러납니다.
# 아래 주석을 풀어서 실행해 보세요.
#
# stopwords = ["것", "저", "그", "이", "수", "때", "등", "바", "더"]
# filtered = [w for w in tokens if w not in stopwords and len(w) > 1]
# print("\n--- 불용어를 걸러낸 결과 (상위 20개) ---")
# for word, freq in Counter(filtered).most_common(20):
#     print(f"{word}, {freq}회")
