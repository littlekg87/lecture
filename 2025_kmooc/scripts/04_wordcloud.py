# -*- coding: utf-8 -*-
"""
[단어 분석 2] 김상헌 상소문 워드클라우드

단어 빈도를 그림으로 그립니다.

필요한 준비물
  pip install konlpy wordcloud matplotlib
  ※ KoNLPy는 자바(JDK)가 설치되어 있어야 동작합니다.
    설치가 번거로우면 Google Colab 노트북을 쓰세요 (notebooks/04_wordcloud.ipynb).
"""

import re
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
from konlpy.tag import Okt
from wordcloud import WordCloud

from korean_font import find_korean_font

# ── 경로 설정 ────────────────────────────────────────────────
BASE = Path(__file__).resolve().parent.parent
file_path = BASE / "data" / "word-analysis" / "kim-sangheon-sangso.txt"
output_png = BASE / "data" / "word-analysis" / "wordcloud-output.png"

# ── 텍스트 파일 읽기 ─────────────────────────────────────────
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# ── 한글 이외의 문자 제거 ────────────────────────────────────
text = re.sub(r"[^가-힣\s]", "", text)

# ── 형태소 분석 (명사 추출) ──────────────────────────────────
okt = Okt()
tokens = okt.nouns(text)

# ── 불용어 제거 ──────────────────────────────────────────────
stopwords = ["것", "저", "그", "이", "수", "있다", "하다"]
tokens = [word for word in tokens if word not in stopwords and len(word) > 1]

# ── 단어 빈도수 계산 ─────────────────────────────────────────
word_counts = Counter(tokens)

# ── 워드클라우드 생성 ────────────────────────────────────────
# 폰트는 운영체제에 맞춰 자동으로 찾습니다 (Windows 맑은고딕 / macOS 애플고딕 / Linux 나눔고딕).
font_path = find_korean_font()
print("사용할 한글 폰트:", font_path)

wordcloud = WordCloud(
    font_path=font_path,
    background_color="white",
    width=800,
    height=600,
).generate_from_frequencies(word_counts)

# ── 워드클라우드 출력 및 저장 ────────────────────────────────
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")  # 축 제거
plt.tight_layout(pad=0)
plt.savefig(output_png, dpi=150, bbox_inches="tight")
print(f"워드클라우드를 {output_png} 에 저장했습니다.")
plt.show()
