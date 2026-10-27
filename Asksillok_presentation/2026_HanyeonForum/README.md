# 검색하는 사료에서 질문하는 사료로 (제24회 한연포럼, 2026.09.15.)

<!-- english:start -->
<details markdown="1">
<summary markdown="span"><strong>🌐 English</strong> — click to open the English version</summary>

## From Searchable Sources to Askable Sources (The 24th Hanyeon Forum, 2026.09.15.)

**Designing a RAG-based research interface for the Annals of the Joseon Dynasty**

Slides from the 24th Hanyeon Forum of the Institute of Hanmun Education, Dankook University. To turn the Annals of the Joseon Dynasty from “sources you search” into “sources you ask”, the talk explains how Ask Sillok was designed, in three layers: archive construction, the retrieval pipeline, and expert-grounded validation.

> #### ▶ **[Open the slides](https://littlekg87.github.io/lecture/Asksillok_presentation/2026_HanyeonForum/)**
> They open directly in the browser without downloading. The slides can be switched between Korean and English.

- **Speaker** Kunha Kim (Research Professor, Institute for Maritime Humanities, Pukyong National University)
- **Date · venue** Tuesday 15 September 2026, 4 p.m. · Room 403, College of Education, Dankook University & Zoom
- **Hosts** Institute of Hanmun Education and Department of Hanmun Education, Dankook University
- **Demonstrated system** [Ask Sillok (public beta)](https://beta.asksillok.com)

### The claim of this talk

> **An askable archive is not built by attaching an LLM.**

The quality of RAG is decided across the whole pipeline, before generation. You have to build an archive-native database, design retrieval around historical questions, and keep the historian inside the validation loop.

### Structure

| Part | Content |
|---|---|
| **Problem** | The Annals are searchable but not yet askable · RAG quality is decided in the pipeline · the three layers of Ask Sillok |
| **01 Archive construction** | Source structure before vectors · metadata and text · two languages in one article (Korean title / Classical Chinese body) · domain-adapted embeddings |
| **02 Retrieval pipeline** | Four decisions from question to evidence · query reformulation · dual retrieval · historical weighting · provenance and a real answer example |
| **03 Expert-grounded validation** | Similarity ≠ historical relevance · human in the loop |
| **Closing** | Overall architecture · live infrastructure (NPU · AWS) · key message |

### Controls

| Action | How |
|---|---|
| Next / previous | `→` `←` or the arrows at the top right |
| Contents | `G` or click the page number at the bottom left |
| Language (Korean / English) | `L` or the button at the top right |
| Light / dark | `T` or the button at the top right |

Step cards, XML notes and citation marks `[1]` on the slides highlight the related element when clicked.

### Files

| File | Content |
|---|---|
| `HanyeonForum24_AskableArchives_presentation.html` | The slides (a single HTML file with no external files) |
| `index.html` | Redirects to the slides |

Because a patent application is pending and a related paper is under review, some implementation details and unpublished experimental results are not disclosed.

---

</details>
<!-- english:end -->

**조선왕조실록 RAG 기반 연구 인터페이스 설계**

단국대학교 한문교육연구소 제24회 한연포럼 발표 슬라이드입니다. 조선왕조실록을 "검색하는 사료"에서 "질문하는 사료"로 바꾸기 위해 Ask Sillok을 어떻게 설계했는지, 아카이브 구축 · 검색 파이프라인 · 전문가 기반 검증의 세 계층으로 설명합니다.

> ### ▶ **[슬라이드 바로 보기](https://littlekg87.github.io/lecture/Asksillok_presentation/2026_HanyeonForum/)**
> 내려받지 않아도 브라우저에서 바로 열립니다.

- **발표** 김근하 (국립부경대학교 해양인문학연구소 연구교수)
- **일시 · 장소** 2026년 9월 15일(화) 오후 4시 · 단국대학교 사범관 403호 & Zoom
- **주최** 단국대학교 한문교육연구소 · 한문교육과
- **시연 시스템** [Ask Sillok (공개 베타)](https://beta.asksillok.com)

---

## 이 발표의 명제

> **질문 가능한 아카이브는 LLM을 붙인다고 만들어지지 않는다.**

RAG의 품질은 생성 이전, 파이프라인 전체에서 결정됩니다. 아카이브 고유의 데이터베이스를 구축하고, 역사적 질문을 중심으로 검색을 설계하며, 역사학자를 검증의 고리 안에 두어야 합니다.

---

## 구성

| 장 | 내용 |
|---|---|
| **문제 제기** | 실록은 검색할 수 있지만 아직 질문할 수는 없다 · RAG 품질은 파이프라인에서 결정된다 · Ask Sillok의 세 계층 |
| **01 아카이브 구축** | 벡터보다 먼저 사료 구조 · 메타데이터와 텍스트 · 한 기사 속 두 언어(한국어 제목 / 한문 본문) · 도메인 적응 임베딩 |
| **02 검색 파이프라인** | 질문에서 증거까지 네 번의 판단 · 질의 재정의 · 이중 검색 · 역사적 가중치 · 출처 추적과 실제 답변 예시 |
| **03 전문가 기반 검증** | 유사도 ≠ 역사적 관련성 · Human in the Loop |
| **마무리** | 전체 구조 · 실제 운영 인프라(NPU · AWS) · 핵심 메시지 |

---

## 조작법

| 동작 | 방법 |
|---|---|
| 다음 / 이전 | `→` `←` 또는 화면 우측 상단 화살표 |
| 목차 | `G` 또는 왼쪽 아래 페이지 번호 클릭 |
| 언어 전환 (한국어 / English) | `L` 또는 우측 상단 버튼 |
| 밝게 / 어둡게 | `T` 또는 우측 상단 버튼 |

슬라이드 안의 단계 카드, XML 설명, 인용 표시 `[1]` 등은 클릭하면 해당 요소가 강조됩니다.

---

## 파일

| 파일 | 내용 |
|---|---|
| `HanyeonForum24_AskableArchives_presentation.html` | 발표 슬라이드 (단일 HTML, 외부 파일 없음) |
| `index.html` | 슬라이드로 자동 이동 |

특허 출원 중 · 관련 논문 심사 중이므로 일부 구현 세부사항과 미발표 실험 결과는 공개하지 않습니다.


통합 관리 위치: `Asksillok_presentation/2026_HanyeonForum/`. 상위의 [Ask Sillok 발표 목록](../README.md)에서 다른 행사판을 볼 수 있습니다. 기존 발표 주소와 QR은 새 위치로 연결됩니다.
