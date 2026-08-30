# -*- coding: utf-8 -*-
"""
운영체제에 맞는 한글 폰트를 자동으로 찾아 주는 도우미 모듈.

기존 코드는 font_path="malgun.ttf" (맑은 고딕) 로 고정되어 있어
맥에서는 폰트를 찾지 못해 오류가 납니다.
이 모듈을 쓰면 Windows / macOS / Linux 어디서나 한글이 깨지지 않습니다.
"""

from pathlib import Path

# 운영체제별 대표 한글 폰트 후보 (위에서부터 순서대로 탐색)
FONT_CANDIDATES = [
    # Windows — 맑은 고딕
    r"C:\Windows\Fonts\malgun.ttf",
    # macOS — 애플고딕 / 애플 SD 산돌고딕 Neo
    "/System/Library/Fonts/Supplemental/AppleGothic.ttf",
    "/Library/Fonts/AppleGothic.ttf",
    "/System/Library/Fonts/AppleSDGothicNeo.ttc",
    # Linux / Google Colab — 나눔고딕
    "/usr/share/fonts/truetype/nanum/NanumGothic.ttf",
    "/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf",
]


def find_korean_font() -> str:
    """사용 가능한 한글 폰트 경로를 반환한다. 없으면 안내와 함께 오류를 낸다."""
    for path in FONT_CANDIDATES:
        if Path(path).exists():
            return path

    raise FileNotFoundError(
        "한글 폰트를 찾지 못했습니다.\n"
        "  · Windows : 맑은 고딕(malgun.ttf)이 기본 설치되어 있어야 합니다.\n"
        "  · macOS   : 시스템에 AppleGothic이 있어야 합니다.\n"
        "  · Linux   : sudo apt-get install -y fonts-nanum 으로 설치하세요.\n"
        "그래도 안 되면 원하는 .ttf 파일 경로를 FONT_CANDIDATES 맨 위에 추가하세요."
    )


if __name__ == "__main__":
    print("찾은 한글 폰트:", find_korean_font())
