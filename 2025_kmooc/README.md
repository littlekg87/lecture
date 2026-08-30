# 디지털 인문학 실습 자료 (K-MOOC)

『세종실록』 지리지와 조선왕조실록을 재료로, **역사 자료를 데이터로 다루는 다섯 가지 방법**을 실습합니다.

> ## 📌 실습은 이 페이지의 자료로 하세요
>
> 강의 영상과 교안은 **촬영 당시 기준**입니다. 그 뒤로
> 프로그램이 새 버전으로 바뀌었고, 파일 이름과 실행 방식도 정리되었습니다.
>
> **영상과 이 페이지의 내용이 다르면, 이 페이지가 맞습니다.**
> 무엇이 왜 다른지는 아래 각 항목에 전부 적어 두었습니다.
>
> | 영상·교안에서는 | 지금은 |
> |---|---|
> | 파이썬을 컴퓨터에 설치해서 실행 | **구글 코랩** — 설치 없이 브라우저에서 실행 |
> | 코드에 긴 파일 경로를 직접 입력 | **경로 입력 불필요** — 파일을 자동으로 내려받음 |
> | `실습예제_○○○.csv` 같은 한글 파일명 | **영문 파일명** ([대조표](#강의-영상에-나오는-파일-이름과-다릅니다)) |
> | Gephi 0.10.1 / QGIS 3.x 화면 | **최신 버전** ([Gephi](guides/gephi.md) · [QGIS](guides/qgis.md) 가이드) |
> | QGIS에서 인코딩을 `Korean` 으로 지정 | **`UTF-8` 로 지정** — 안 그러면 한글이 깨집니다 |

## 차시별 바로가기

| 차시 | 실습 | 여기로 |
|---|---|---|
| **2-4** | 텍스트마이닝 실습 | [① 구(口) 추출](notebooks/01_gu_extract.ipynb) · [② 숫자 변환](notebooks/02_gu_convert.ipynb) |
| **4-4** | 텍스트분석 실습 | [③ 단어 빈도](notebooks/03_word_frequency.ipynb) · [④ 워드클라우드](notebooks/04_wordcloud.ipynb) |
| **3-2** | 통계 분석 실습 | [데이터·분석 안내](data/statistics/) (jamovi) |
| **3-4** | HGIS 실습 | [QGIS 가이드](guides/qgis.md) |
| **4-2** | 네트워크 분석 실습 | [Gephi 가이드](guides/gephi.md) |

## 실습 구성

| 분야 | 무엇을 하나 | 쓰는 도구 |
|---|---|---|
| 텍스트 마이닝 | 한문 원문에서 인구 수치 뽑아내기 | Python (구글 코랩) |
| 텍스트 분석 | 상소문의 단어 빈도·워드클라우드 | Python (구글 코랩) |
| 통계 분석 | 호구 수와 군사 수의 상관관계 | jamovi |
| HGIS | 팔도별 통계를 지도로 그리기 | QGIS |
| 네트워크 분석 | 비변사 관원들의 인적 관계망 | Gephi |

---

## 🚀 빠른 시작

### 파이썬 실습 — **설치할 것이 없습니다**

아래 버튼을 누르면 구글 코랩(Colab)이 열립니다.
**구글 계정으로 로그인한 뒤, 왼쪽의 ▶ 버튼을 위에서부터 차례로 누르기만 하면 됩니다.**

| 차시 | 실습 | 열기 |
|---|---|---|
| **2-4** | ① 구(口) 데이터 추출하기 | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/littlekg87/lecture/blob/main/2025_kmooc/notebooks/01_gu_extract.ipynb) |
| **2-4** | ② 한문 숫자 → 아라비아 숫자 변환 | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/littlekg87/lecture/blob/main/2025_kmooc/notebooks/02_gu_convert.ipynb) |
| **4-4** | ③ 단어 빈도 분석 | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/littlekg87/lecture/blob/main/2025_kmooc/notebooks/03_word_frequency.ipynb) |
| **4-4** | ④ 워드클라우드 | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/littlekg87/lecture/blob/main/2025_kmooc/notebooks/04_wordcloud.ipynb) |

> 노트북의 **단계 번호는 강의 교안과 똑같이** 맞추어 두었습니다.
> 영상에서 "2-1단계" 라고 하면 노트북에서도 "2-1단계" 를 찾으면 됩니다.

> 💡 **코랩(Colab)이 뭔가요?**
> 구글이 무료로 제공하는 **웹브라우저 안의 파이썬**입니다.
> 내 컴퓨터에 아무것도 설치하지 않고, **윈도우든 맥이든 똑같이** 실행됩니다.
> 특히 **맥 사용자**는 파이썬·자바 설치로 애먹는 과정을 통째로 건너뛸 수 있습니다.

### 프로그램 실습 — 설치 가이드를 먼저 읽으세요

| 차시 | 실습 | 프로그램 | 가이드 |
|---|---|---|---|
| **3-2** | 통계 분석 | jamovi | [데이터 설명](data/statistics/) · 사용법은 강의 영상 |
| **3-4** | HGIS | QGIS | **[QGIS 설치·사용 가이드](guides/qgis.md)** |
| **4-2** | 네트워크 분석 | Gephi | **[Gephi 설치·사용 가이드](guides/gephi.md)** |

> ⚠️ **두 가이드를 꼭 먼저 읽어 주세요.**
> Gephi와 QGIS 모두 강의 촬영 이후 새 버전이 나와 **화면이 달라졌습니다.**
> 어떤 버전을 받아야 하는지, 무엇이 달라졌는지 정리해 두었습니다.

---

## 📥 실습 자료 내려받기

**깃허브(GitHub)를 몰라도 됩니다. 아래대로만 하세요.**

1. 이 페이지 위쪽의 초록색 **`< > Code`** 버튼을 누릅니다.
2. 맨 아래 **`Download ZIP`** 을 누릅니다.
   (지도 파일이 들어 있어 **약 17MB**입니다. 잠시 걸릴 수 있습니다.)
3. 내려받은 압축 파일을 풉니다.

   - **Windows** — 파일 우클릭 → **압축 풀기**
   - **macOS** — 파일을 **더블클릭**하면 바로 풀립니다.

4. 압축을 푼 폴더에서 **`2025_kmooc`** 폴더를 찾아 들어갑니다.

> 🔴 **압축을 꼭 풀고 쓰세요.**
> 압축 파일 안에서 바로 열면 QGIS나 Gephi가 파일을 찾지 못합니다.
>
> 🔴 **폴더 이름에 한글이나 띄어쓰기가 없는 곳에 두세요.**
> 예) `C:\실습 자료\` 보다는 `C:\kmooc\` 가 안전합니다.

---

## 📁 폴더 구성

```
2025_kmooc/
├── notebooks/     구글 코랩 실습 파일 4종 (①~④)
├── scripts/       내 컴퓨터에서 돌리는 파이썬 코드 (코랩 대신 쓰고 싶을 때)
├── guides/        Gephi · QGIS 설치 및 사용 가이드
└── data/          실습 데이터
    ├── text-mining/     『세종실록』 지리지 충청도 조 원문
    ├── word-analysis/   김상헌 상소문
    ├── statistics/      팔도 333개 군현 호구·군사 통계 (설명 파일 있음)
    ├── gis/             조선 팔도 지도(셰이프파일) + 팔도별 통계
    └── network/         비변사 관원 네트워크
```

### 강의 영상에 나오는 파일 이름과 다릅니다

파일 이름을 **영문으로 바꾸었습니다.** 한글·띄어쓰기가 들어간 이름이
맥과 일부 프로그램에서 오류를 일으키기 때문입니다.
**영상에서 부르는 이름**과 **실제 파일**을 아래 표로 대조하세요. **내용은 똑같습니다.**

| 영상·교안에서 부르는 이름 | 실제 파일 |
|---|---|
| `Practice_1.txt` | `data/text-mining/practice_1.txt` |
| `실습예제_김상헌상소문.txt` | `data/word-analysis/kim-sangheon-sangso.txt` |
| `실습예제데이터_인구군사.xlsx` | `data/statistics/population-military.xlsx` |
| `실습예제_GIS데이터.CSV` | `data/gis/provinces-data.csv` |
| `실습예제_비변사 네트워크.csv` | `data/network/bibyeonsa-network.csv` |

---

## 🖥️ 맥 사용자를 위한 안내

이 강의의 실습은 **맥에서도 모두 가능합니다.** 다만 몇 가지 다른 점이 있습니다.

| | Windows | macOS |
|---|---|---|
| 파이썬 실습 | 코랩 사용 (동일) | **코랩 사용 (동일)** |
| QGIS | 정상 설치 | 정상 설치 (애플 공증 완료) |
| Gephi | 정상 설치 | **칩 종류 확인 후 받아야 함** ([가이드](guides/gephi.md#macos--내-맥이-어떤-종류인지-먼저-확인하세요)) |
| 한글 글꼴 | 맑은 고딕 | **맑은 고딕이 없음** → 파이썬은 코랩이 해결, Gephi·QGIS는 직접 지정 |
| 상소문 원문 | `.txt` 제공 | `.txt` 제공 (맥에서 열리지 않는 `.hwp` 는 넣지 않았습니다) |

### 맥에서 특히 주의할 것

1. **`malgun.ttf` 오류**
   강의 코드의 `font_path="malgun.ttf"` 는 **윈도우 전용 글꼴**입니다.
   맥에서 그대로 실행하면 오류가 납니다.
   → **코랩 노트북을 쓰면 이 문제가 없습니다.**
   → 내 컴퓨터에서 돌리고 싶다면 `scripts/` 폴더의 코드를 쓰세요. 글꼴을 자동으로 찾아 줍니다.

2. **Gephi 이름표가 `□□□` 네모로 나오는 문제**
   강의 영상은 글꼴을 **`HY중고딕`** 으로 지정하는데, 이 글꼴은 **맥에 없습니다.**
   → Gephi 글꼴 목록에서 **`AppleGothic`** 을 고르세요. 결과는 똑같습니다.
   자세한 내용은 [Gephi 가이드](guides/gephi.md#3-이름-보이게-하기--맥-사용자-필독) 참고.

3. **"확인되지 않은 개발자" 경고**
   프로그램 아이콘을 **`control` 키를 누른 채 클릭** → **열기** 를 고르면 실행됩니다.

4. **자바(JDK) 설치**
   형태소 분석기(KoNLPy)는 자바가 필요해 맥에서 설치가 까다롭습니다.
   → **코랩을 쓰면 설치할 필요가 없습니다.**

---

## 📋 파일 경로 복사하는 법

파이썬 코드에 `"C:\Users\..."` 같은 **파일 위치(경로)** 를 적어야 할 때가 있습니다.
직접 타이핑하면 거의 틀립니다. **복사해서 붙여 넣으세요.**

### Windows

1. 파일 탐색기에서 원하는 파일을 찾습니다.
2. 파일을 **`Shift` 키를 누른 채 오른쪽 클릭** 합니다.
3. 메뉴에서 **"경로로 복사"** 를 누릅니다.
4. 코드에 붙여 넣습니다. (Windows 11에서는 `Shift` 없이 우클릭해도 나옵니다.)

붙여 넣으면 이런 모양입니다 — **따옴표까지 함께 복사됩니다.**
```
"C:\Users\hong\Desktop\kmooc\data\text-mining\practice_1.txt"
```

### macOS

1. Finder에서 원하는 파일을 찾습니다.
2. 파일을 **오른쪽 클릭** 한 뒤, 메뉴가 뜬 상태에서 **`option` 키를 누릅니다.**
   → "복사"가 **"…을(를) 경로 이름으로 복사"** 로 바뀝니다. 그걸 누르세요.
3. 단축키로는 파일 선택 후 **`option` + `command` + `C`** 입니다.

붙여 넣으면 이런 모양입니다.
```
/Users/hong/Desktop/kmooc/data/text-mining/practice_1.txt
```

### 붙여 넣은 뒤 꼭 확인할 것

경로 앞에 **`r`** 을 붙이고 **따옴표로 감싸야** 합니다.

```python
# ✅ 올바른 예 (Windows)
file_path = r"C:\Users\hong\Desktop\kmooc\data\text-mining\practice_1.txt"

# ✅ 올바른 예 (macOS)
file_path = r"/Users/hong/Desktop/kmooc/data/text-mining/practice_1.txt"

# ❌ 틀린 예 — r 이 없으면 \U, \t 등이 특수 기호로 해석돼 오류가 납니다
file_path = "C:\Users\hong\Desktop\kmooc\data\text-mining\practice_1.txt"
```

> 💡 **`r`은 "있는 그대로 읽어라"(raw)** 라는 뜻입니다.
> 윈도우 경로의 역슬래시(`\`)가 엉뚱하게 해석되는 것을 막아 줍니다.
> 맥 경로에는 역슬래시가 없어 없어도 되지만, **습관적으로 붙여도 아무 문제 없습니다.**
>
> 💡 **코랩을 쓰면 이 과정 자체가 없습니다.** 파일을 자동으로 내려받습니다.

---

## 💻 내 컴퓨터에서 파이썬 코드 돌리기 (선택)

코랩 대신 내 컴퓨터에서 돌리고 싶다면 `scripts/` 폴더를 쓰세요.
**경로를 직접 고칠 필요가 없도록** 만들어 두었습니다.

```bash
pip install konlpy wordcloud matplotlib
```

```bash
python scripts/01_gu_extract.py
python scripts/02_gu_convert.py
python scripts/03_word_frequency.py
python scripts/04_wordcloud.py
```

> ⚠️ `03`, `04` 번은 **자바(JDK)가 설치되어 있어야** 합니다.
> 설치가 번거로우면 코랩을 쓰세요.

---

## 📚 데이터 출처

- **『세종실록』 지리지 원문** — 국사편찬위원회 조선왕조실록 DB
  실습에는 충청도 조 발췌본(`practice_1.txt`)을 사용합니다.
  전체 원문 XML과 군현별 정리 데이터는 별도 저장소에서 볼 수 있습니다.
  → https://github.com/littlekg87/Sejong_Sillok_Jiriji
- **조선 팔도 경계 지도** — 국사편찬위원회 역사지리정보DB (2024년판)
- **김상헌 상소문** — 『인조실록』

---

## 🙋 자주 묻는 질문

**Q. 코랩을 쓰려면 돈을 내야 하나요?**
아니요. 구글 계정만 있으면 무료입니다. 이 실습은 무료 사용량으로 충분합니다.

**Q. 코랩에서 만든 파일은 어디에 저장되나요?**
코랩 서버에 임시로 저장되며, 창을 닫으면 사라집니다.
각 노트북의 **"내려받기"** 칸을 실행해 내 컴퓨터로 저장하세요.

**Q. 파이썬을 전혀 몰라도 되나요?**
네. 노트북의 ▶ 버튼을 위에서부터 차례로 누르기만 하면 됩니다.
각 칸이 무엇을 하는지 설명이 함께 적혀 있습니다.

**Q. 실습 중 오류가 났어요.**
각 가이드 맨 아래 **"문제가 생겼을 때"** 항목을 먼저 확인해 주세요.
그래도 해결되지 않으면 강의 게시판에 **오류 메시지 전체를 복사해서** 올려 주세요.
