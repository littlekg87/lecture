# Ask Sillok 단독 발표

행사별 폴더: [KOSSDA](../2026_KOSSDA/) · [율곡국학진흥원](../2026_Yulgok/). 이 폴더는 기존 주소와 발표 목록을 유지하는 안내 페이지입니다.

Event folders: [KOSSDA](../2026_KOSSDA/) · [Yulgok](../2026_Yulgok/). Legacy slide URLs redirect to the event folders.

<!-- english:start -->
<details markdown="1">
<summary markdown="span"><strong>🌐 English</strong> — click to open the English version</summary>

## Ask Sillok — standalone talk

**Kunha Kim (Research Professor, Institute for Maritime Humanities, Pukyong National University) · an interactive HTML presentation of about 30 minutes**

The talk explains how [Ask Sillok](https://beta.asksillok.com), which answers questions about the Annals of the Joseon Dynasty together with its evidence, actually works. Following a single article of the Annals, it shows how sources become data that can be asked (building the DB) and how a question becomes a grounded answer (retrieval).

This folder collects editions adapted for each event. The Yulgok edition includes everyday-language access to local archives and a closing message on their use with AI.

### Talks

| Date | Event | Title | Open |
|---|---|---|---|
| 23 October 2026 | The 21st KOSSDA Data Fair | Can Historical Data and AI Converge? — Designing an AI Chatbot for the Annals of the Joseon Dynasty | **[2026_KOSSDA.html ↗](https://littlekg87.github.io/lecture/2026_KOSSDA/)** |
| 30 October 2026 | Yulgok Institute of Korean Studies (율곡국학진흥원) · Regional Data and Digital Archives in the Age of AI | Searchable to Askable Archive: RAG-based Annals of the Joseon Dynasty AI chat-bot Architecture | **[2026_Yulgok.html ↗](https://littlekg87.github.io/lecture/2026_Yulgok/)** |

Listing page: **[littlekg87.github.io/lecture/Asksillok_presentation/](https://littlekg87.github.io/lecture/Asksillok_presentation/)**

### Structure

KOSSDA: 18 main slides and 5 appendix slides. Yulgok: 19 main slides and 5 appendix slides.

Printable Yulgok PDFs (27 pages each, with expanded diagrams and intermediate source-processing steps): [Korean](../2026_Yulgok/2026_Yulgok.pdf) · [English](../2026_Yulgok/2026_Yulgok_en.pdf).

| Part | Content |
|---|---|
| **Introduction** | QR codes for these slides and for Ask Sillok, with their addresses · from sources you search to sources you ask · the two phases of RAG |
| **1 · Building the DB** | An article of the Annals → XML → body and metadata archives · fine-tuning on Korean title–Classical Chinese body pairs · the LoRA adapter · the vectors as actually stored |
| **2 · Retrieval** | Splitting the question into a vector and metadata conditions · comparing similarity and conditions · selecting candidates and adding a bonus · linking the answer to the actual article |
| **Closing** | The technology that runs the service · the Ask Sillok research team · the historian’s role in the age of AI |
| **Appendix** | Comparison of six models · blind evaluation by historians · findings · related work |

### Korean / English

Each file contains both languages. Press **ENG** at the top right to switch to English on the slide you are viewing, and press it again to return to Korean. Parts that are data in themselves, such as the Korean titles of Annals articles and the original XML, stay as they are on the English screens.

### How to use

- **Moving:** arrow keys, Page Up / Page Down, the previous/next buttons at the bottom, or scrolling. Some scenes continue in steps within one slide.
- **Contents:** “Contents” at the top right, or the `M` key.
- **Interaction:** press the training buttons, retrieval routes and citation numbers to see changes and explanations.
- **More:** “More” at the bottom left opens notes on terms and the evaluation procedure.
- **Screen:** slides use a fixed 1920×1080 canvas scaled to the device. “Full screen” and “Zoom ＋” are at the top.

### Offline use

Open a file from the list above and save it, or choose a file in this folder and press **Download raw file**, then open it in a browser. Images, fonts, scripts and data are all inside the one HTML file. Each file is about 10 MB. Visiting Ask Sillok and the original-text links needs an internet connection.

### Research material and demonstration

The deck contains actual material (stored embedding vectors, Annals articles) alongside conceptual diagrams of training, retrieval and evaluation. Weight changes, the matrix sizes and values of the LoRA adapter, retrieval scores and metadata bonuses, and the scores clicked on the expert-evaluation screen are illustrative examples, labelled as such on each screen. The deck does not itself run live AI retrieval or answering.

### Files

| File | Description |
|---|---|
| [`index.html`](index.html) | Listing page for this folder |
| [`2026_KOSSDA.html`](2026_KOSSDA.html) | Deck for the 21st KOSSDA Data Fair (2026.10.23.) |
| [`2026_Yulgok.html`](2026_Yulgok.html) | Deck for “Regional Data and Digital Archives in the Age of AI”, Yulgok Institute of Korean Studies (2026.10.30.) |
| [`FONT-NOTICE.txt`](FONT-NOTICE.txt) | License notice for the embedded font |
| [`README.md`](README.md) | This guide |

### Related

- [Ask Sillok](https://beta.asksillok.com): a research interface for asking questions of the Annals of the Joseon Dynasty and exploring the evidence
- [Historical Research in the Age of AI](../2026_AI_History/): the integrated 4-chapter deck that includes Ask Sillok as one chapter (in Korean)
- [From Searchable Archives to Askable Archives](../2026_HanyeonForum/): slides from the 24th Hanyeon Forum
- [Annals of the Joseon Dynasty, National Institute of Korean History](https://sillok.history.go.kr/): original texts and translations
- [Speaker’s portfolio](https://kunslab.com)
- [All teaching and presentation materials](../README.md)

For related papers and patent applications, see the “Related work” slide in the appendix. When citing, please give the original source and the presentation details. Use of the embedded font follows `FONT-NOTICE.txt`.

---

</details>
<!-- english:end -->

**김근하 (국립부경대학교 해양인문학연구소 전임연구원) · 약 30분 분량의 인터랙티브 HTML 발표자료**

조선왕조실록에 질문하면 근거와 함께 답하는 [Ask Sillok](https://beta.asksillok.com)이 어떻게 작동하는지를 설명합니다. 사료가 질문할 수 있는 데이터가 되는 과정(DB 구축)과, 질문이 근거 있는 답변이 되는 과정(검색)을 하나의 실록 기사를 따라가며 보여 줍니다.

행사에 맞춰 구성한 발표자료를 이 폴더에 모아 둡니다. Yulgok판에는 일상 언어로 접근하는 지역 아카이브 장면과 지역 아카이브의 AI 활용에 관한 마무리를 담았습니다.

## 발표 목록

| 일자 | 행사 | 제목 | 바로 보기 |
|---|---|---|---|
| 2026년 10월 23일 | 제21회 KOSSDA 데이터 페어 | 역사데이터와 AI의 융합은 가능한가? — 조선왕조실록 AI챗봇 설계 사례 | **[2026_KOSSDA.html ↗](https://littlekg87.github.io/lecture/2026_KOSSDA/)** |
| 2026년 10월 30일 | 율곡국학진흥원 · AI 시대의 지역 데이터와 디지털 아카이브 | 검색하는 아카이브에서 질문하는 아카이브로: RAG기반 조선왕조실록 AI챗봇 설계 연구 사례 | **[2026_Yulgok.html ↗](https://littlekg87.github.io/lecture/2026_Yulgok/)** |

전체 목록 페이지: **[littlekg87.github.io/lecture/Asksillok_presentation/](https://littlekg87.github.io/lecture/Asksillok_presentation/)**

## 구성

KOSSDA판은 본편 18슬라이드와 부록 5슬라이드, Yulgok판은 본편 19슬라이드와 부록 5슬라이드입니다.

Yulgok 인쇄용 PDF: [국문](../2026_Yulgok/2026_Yulgok.pdf) · [영문](../2026_Yulgok/2026_Yulgok_en.pdf). 펼친 도식과 사료 처리의 중간 단계를 포함해 각각 27페이지입니다.

| 부 | 내용 |
|---|---|
| **도입** | 발표자료 · Ask Sillok 접속 QR(주소 함께 표기) · 검색하는 사료에서 질문하는 사료로 · RAG의 두 국면 |
| **1 · DB 구축** | 실록 기사 → XML → 본문·메타데이터 아카이브 · 한글 제목–한문 본문 대응을 이용한 파인튜닝 · LoRA 어댑터 · 실제로 저장된 벡터 |
| **2 · 검색** | 질문을 벡터와 메타데이터 조건으로 분리 · 유사도와 조건 비교 · 후보 선정과 가점 · 답변의 근거를 실제 기사로 연결 |
| **마무리** | 서비스를 작동시키는 기술 · Ask Sillok 연구팀 · AI 시대 역사학자의 역할 |
| **부록** | 여섯 모델의 비교 · 역사연구자의 블라인드 평가 · 연구 결과 · 관련 연구 |

## 한국어 / English

각 파일에 한국어와 영어가 함께 들어 있습니다. 우측 상단의 **ENG** 버튼을 누르면 보던 슬라이드 그대로 영어로 바뀌고, 다시 누르면 한국어로 돌아옵니다. 실록 기사의 한글 제목과 XML 원문처럼 자료 자체인 부분은 영어 화면에서도 그대로 둡니다.

Each file contains both Korean and English. Press **ENG** in the top-right corner to switch languages on the slide you are viewing.

## 이용 방법

- **이동:** 방향키, Page Up / Page Down, 화면 하단의 이전·다음 버튼 또는 스크롤을 사용합니다. 일부 화면은 같은 슬라이드 안에서 단계가 이어집니다.
- **전체 목차:** 우측 상단의 ‘전체 목차’ 또는 `M` 키로 원하는 슬라이드를 선택합니다.
- **상호작용:** 학습 버튼, 검색 경로, 인용 번호 등을 눌러 변화와 설명을 확인합니다.
- **추가 설명:** 좌측 하단의 ‘더보기’에서 용어와 평가 절차 설명을 확인합니다.
- **화면:** 슬라이드는 1920×1080 고정 캔버스이며 기기 화면에 맞춰 같은 비율로 축소됩니다. 상단의 ‘전체 화면’과 ‘확대 ＋’를 쓸 수 있습니다.

## 내려받아 오프라인으로 보기

위 목록의 파일을 열어 저장하거나, 이 폴더에서 파일을 골라 **Download raw file**을 누른 뒤 브라우저에서 엽니다. 이미지·폰트·스크립트·데이터가 HTML 하나에 포함되어 있어 별도 설치가 필요하지 않습니다. 파일 하나의 크기는 약 10MB입니다. Ask Sillok과 실록 원문 링크 방문에는 인터넷 연결이 필요합니다.

## 실제 연구 자료와 시연의 구분

저장된 임베딩 벡터와 실록 기사 등 실제 자료와, 학습·검색·평가 절차를 설명하는 개념 도식이 함께 포함되어 있습니다. 가중치 변화, LoRA 어댑터의 행렬 크기와 수치, 검색 점수와 메타데이터 가점, 전문가 평가 화면의 클릭 점수 등은 각 화면에 표시된 설명용 예시입니다. 발표자료 자체가 실시간 AI 검색·답변을 수행하지는 않습니다.

## 파일 구성

| 파일 | 설명 |
|---|---|
| [`index.html`](index.html) | 이 폴더의 발표 목록 페이지 |
| [`2026_KOSSDA.html`](2026_KOSSDA.html) | 제21회 KOSSDA 데이터 페어 발표자료 (2026.10.23.) |
| [`2026_Yulgok.html`](2026_Yulgok.html) | 율곡국학진흥원 「AI 시대의 지역 데이터와 디지털 아카이브」 발표자료 (2026.10.30.) |
| [`FONT-NOTICE.txt`](FONT-NOTICE.txt) | 포함된 폰트의 라이선스 고지 |
| [`README.md`](README.md) | 발표 내용과 이용 안내 |

## 관련 자료

- [Ask Sillok](https://beta.asksillok.com): 조선왕조실록에 질문하고 근거를 탐색하는 연구 인터페이스
- [AI 시대의 역사 연구](../2026_AI_History/): Ask Sillok을 한 챕터로 포함한 4챕터 통합 발표자료
- [검색하는 사료에서 질문하는 사료로](../2026_HanyeonForum/): 제24회 한연포럼 발표 슬라이드
- [국사편찬위원회 조선왕조실록](https://sillok.history.go.kr/): 실록 원문과 번역문
- [발표자 포트폴리오](https://kunslab.com)
- [강의·발표 자료 전체 목록](../README.md)

관련 논문과 특허출원은 부록의 ‘관련 연구’ 슬라이드를 참고해 주세요. 자료를 인용할 때에는 원 출처와 발표 정보를 함께 밝혀 주세요. 포함된 폰트의 이용 조건은 `FONT-NOTICE.txt`를 따릅니다.
