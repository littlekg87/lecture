# 냉전기 부산항 구호물자 유통 H-GIS 구축 실무

<!-- english:start -->
<details markdown="1">
<summary markdown="span"><strong>🌐 English</strong> — click to open the English version</summary>

## Building an H-GIS of Relief Goods Distribution at Busan Port in the Cold War Era

**Kunha Kim (Institute of Marine Humanities, Pukyong National University) · an interactive HTML presentation of 62 slides with two hands-on sessions** (the slides themselves are in Korean)

To draw a good map you first need a good table. The lecture starts from the basics of data and normalization (first, second and third normal forms), moves on to the rules for writing location data (points, lines and polygons, coordinates, georeferencing basis) and ends with layers — why overlaying separate tables shows what no single table can. Each part is followed by a hands-on session done together with the lecturer.

**[Open the presentation ↗](https://littlekg87.github.io/lecture/2026_Pukyong_GIS/)** · [Download the HTML](https://raw.githubusercontent.com/littlekg87/lecture/main/2026_Pukyong_GIS/index.html)

### Talk given with this deck

| Date | Event |
|---|---|
| 22 October 2026, 13:00–15:00 | Pukyong National University, the 1st Expert Invited Lecture — Humanities, Social Sciences and Business Building (C25), Room 509 |

### Structure

| Part | Slides | Topic |
|---|---|---|
| Introduction | 01–02 | Cover · today's order |
| Ⅰ Data basics | 03–26 | Anatomy of a table · schema · rules for a good table · first, second and third normal forms · how 2NF and 3NF differ · joining split tables by ID |
| Practice 1 | 27 | Normalizing data |
| Ⅱ H-GIS | 28–60 | Historical GIS cases · vector and raster · maps are tables · writing location as numbers · point, line and polygon schemas · rules for GIS data · layers, with the four-layer map of the Fushun carbon energy regime |
| Practice 2 | 61 | Cleaning, normalizing, adding coordinates, mapping points, lines and polygons, and overlaying layers in kepler.gl |
| Q & A | 62 | |

### Practice data

All three files are **fictional examples made for the practice sessions**. Ships, warehouses, distribution sites and quantities are invented, and the addresses are present-day Busan addresses attached only for practising geocoding; they do not mean that those places were actually used as warehouses or distribution sites.

| File | Used in | Content |
|---|---|---|
| [`data/p1_arrivals_raw.csv`](data/p1_arrivals_raw.csv) | Practice 1 | 8 arrivals of relief ships at Busan Port, not yet normalized (several goods in one cell) |
| [`data/p2_distribution_raw.csv`](data/p2_distribution_raw.csv) | Practice 2 | 15 records of goods sent from warehouses to distribution sites, with inconsistent spellings left in for data cleaning |
| [`data/p2_polygon_template.csv`](data/p2_polygon_template.csv) | Practice 2 | Template for a polygon drawn in kepler.gl |

The CSV files are UTF-8 (with BOM). Tools: Google Sheets and [kepler.gl](https://kepler.gl/demo) (no installation or sign-in).

### How to use the presentation

- **Moving:** → / Space / ‹ › buttons at the top right for the next and previous slide. Swipe left or right on a phone.
- **Jumping:** click the page number (or press `G`) to open the slide list.
- Many slides respond to clicks (tables, layer toggles, buttons).

The deck is one HTML file of about 1 MB. Fonts and the link to the live map on slide 57 need an internet connection; everything else works offline.

### Files

| File | Description |
|---|---|
| [`index.html`](index.html) | The web/offline presentation of 62 slides |
| [`data/`](data/) | Three practice CSV files |
| [`README.md`](README.md) | This guide |

---

</details>
<!-- english:end -->

**국립부경대학교 해양인문학연구소 김근하 · 이론 두 파트와 실습 두 번으로 된 62장 웹 발표자료**

지도를 잘 그리려면 표를 먼저 잘 만들어야 합니다. 데이터의 기초와 정규화(제1·2·3정규형)에서 시작해, 위치를 적는 규칙(점·선·면, 좌표, 위치기준)을 거쳐, 따로 만든 표를 겹쳐야 보이는 것 — 레이어 — 까지 갑니다. 파트마다 강사와 함께 한 단계씩 따라 하는 실습이 이어집니다.

**[발표자료 바로 보기 ↗](https://littlekg87.github.io/lecture/2026_Pukyong_GIS/)** · [HTML 내려받기](https://raw.githubusercontent.com/littlekg87/lecture/main/2026_Pukyong_GIS/index.html)

## 이 자료로 진행한 강연

| 날짜 | 강연 |
|---|---|
| 2026.10.22.(목) 13:00–15:00 | 국립부경대학교 제1회 전문가초청강연 · 인문사회경영관(C25) 경영동 509호 |

## 구성

| 부분 | 장면 | 내용 |
|---|---|---|
| 들어가며 | 01–02 | 표지 · 오늘의 순서 |
| Ⅰ 데이터의 기초 | 03–26 | 데이터베이스 구축 핵심 · 스키마 · 좋은 표를 만드는 규칙 · 제1·2·3정규형 · 2정규형과 3정규형의 차이 · 쪼갠 표는 아이디로 잇는다 |
| 실습 1 | 27 | 데이터 정규화 실습 |
| Ⅱ H-GIS | 28–60 | 역사 GIS 뜯어보기 · 벡터와 래스터 · 지도도 표다 · 위치를 숫자로 · 점·선·면 스키마 · GIS 데이터를 다루는 규칙 · 레이어(무순 탄소 에너지 레짐 4레이어 지도) |
| 실습 2 | 61 | 정제 → 정규화 → 위도·경도 → 점·선·면 → 레이어 겹치기 (kepler.gl) |
| 질문과 토론 | 62 | |

## 실습 자료

세 파일 모두 **실습을 위해 만든 가상의 예**입니다. 선박·창고·배급소·수량은 지어낸 것이고, 주소는 위도·경도 변환을 연습하기 위해 부산의 현재 주소를 임의로 붙였습니다. **그 자리가 실제 창고나 배급소였다는 뜻이 아닙니다.**

| 파일 | 쓰는 곳 | 내용 |
|---|---|---|
| [`data/p1_arrivals_raw.csv`](data/p1_arrivals_raw.csv) | 실습 1 | 부산항 구호물자 선박 입항 기록 8건. 정규화하기 전의 표(한 칸에 물자 여러 개) |
| [`data/p2_distribution_raw.csv`](data/p2_distribution_raw.csv) | 실습 2 | 창고에서 배급소로 물자를 내보낸 기록 15건. 정제 실습을 위해 흔들린 표기를 남겨 둠 |
| [`data/p2_polygon_template.csv`](data/p2_polygon_template.csv) | 실습 2 | kepler.gl에서 그린 면을 옮겨 적는 양식 |

CSV는 UTF-8(BOM 포함)입니다. 도구는 구글 시트와 [kepler.gl](https://kepler.gl/demo)(설치·로그인 없음)입니다.

> 파일 이름은 macOS와 Windows에서 깨지지 않도록 영어로 두었습니다. 실습 중에 만드는 스프레드시트와 시트 이름도 영어로 두기를 권합니다.

## 사용법

- **이동:** → · Space · 오른쪽 위 ‹ › 단추로 다음·이전 장면. 휴대폰에서는 좌우로 밀어 넘깁니다.
- **장면 바로 가기:** 페이지 번호를 누르거나 `G` 키를 누르면 장면 목록이 열립니다.
- 표, 레이어 켜고 끄기, 단추 등 눌러서 움직이는 장면이 많습니다.

HTML 파일 하나(약 1MB)입니다. 글꼴과 57장 무순 지도의 실제 화면 링크는 인터넷 연결이 필요하고, 나머지는 오프라인에서도 열립니다.

## 파일

| 파일 | 설명 |
|---|---|
| [`index.html`](index.html) | 62장면 웹/오프라인 발표자료 |
| [`data/`](data/) | 실습용 CSV 세 개 |
| [`README.md`](README.md) | 이 안내 |
