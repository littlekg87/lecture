# AI 시대의 역사 연구

<!-- english:start -->
<details markdown="1">
<summary markdown="span"><strong>🌐 English</strong> — click to open the English version</summary>

## Historical Research in the Age of AI

**Kunha Kim · an interactive HTML presentation of 4 chapters and 49 slides** (the slides themselves are in Korean)

Starting from a historian’s questions, the talk shows how sources are turned into data, how digital analysis leads to a new reading of existing scholarship, and how a service that answers questions from historical sources was designed.

**[Open the presentation ↗](https://littlekg87.github.io/lecture/2026_AI_History/)** · [Download the HTML](https://raw.githubusercontent.com/littlekg87/lecture/main/2026_AI_History/index.html)

### Talks given with this deck

| Date | Event |
|---|---|
| 28 September 2026 | Sogang University, Department of History × Digital History Institute Colloquium |
| 15 October 2026 | Ewha Womans University, Department of History Colloquium |
| 28 October 2026 | Pusan National University, Digital Humanities Center Colloquium |

### Structure

The table of contents is numbered **01–49**, and the bottom of the screen shows a running **1–49 / 49**.

| Chapter | Slides | Topic |
|---|---|---|
| [01 · History in the Age of AI](https://littlekg87.github.io/lecture/2026_AI_History/#/1/cover) | 01–09 | Questions and evidence in historical research; the roles of digital history and AI |
| [02 · A Digital Ontology of the Worldview in the *Huangqing Zhigongtu*](https://littlekg87.github.io/lecture/2026_AI_History/#/2/cover) | 10–16 | A case of building source data with an LLM and a graph database |
| [03 · The Structure of Military Service Mobilization in Early Joseon](https://littlekg87.github.io/lecture/2026_AI_History/#/3/cover) | 17–27 | Turning the Geography Section of the *Sejong Sillok* into data and analyzing every county to reinterpret the long-term context of military service reform |
| [04 · Searchable to Askable: Designing Ask Sillok](https://littlekg87.github.io/lecture/2026_AI_History/#/4/cover) | 28–49 | An end-to-end RAG system design, from data design through embedding, fine-tuning, retrieval, evaluation and service (46–49 are the appendix) |

**A digital ontology of the *Huangqing Zhigongtu*.** The records are transcribed, classified, and structured into an ontology through repeated classification and review. The sources are then read again in a graph database and on a world map, to see what becomes visible once a source is made into data.

**Long-term change in the early Joseon military service system.** The standardization of mobilization units and service costs, treated in the speaker’s doctoral dissertation, is extended to the question of nationwide organization. Records for 334 counties are structured, and household, soldier, service-branch and geographic data are combined to examine differences between counties. You can operate the dataset construction, the code-based joins and the map comparisons yourself.

**Ask Sillok and evaluation by historians.** The chapter covers embedding training on Korean title–Classical Chinese body pairs, the principle of the LoRA adapter, the vectors as actually stored, and hybrid retrieval that combines vector search with metadata. The appendix compares base and fine-tuned models and presents the blind evaluation by historians, distinguishing benchmark gains from usefulness in actual research and arguing for a human in the loop.

| Key scene | Link |
|---|---|
| Reading sources in a graph database | [Slide 14](https://littlekg87.github.io/lecture/2026_AI_History/#/2/network) |
| Joining data with code | [Slide 23](https://littlekg87.github.io/lecture/2026_AI_History/#/3/order) |
| Differences in household ratios between counties | [Slide 24](https://littlekg87.github.io/lecture/2026_AI_History/#/3/inequality) |
| Differences in service-branch ratios between counties | [Slide 25](https://littlekg87.github.io/lecture/2026_AI_History/#/3/service) |
| How a LoRA adapter is trained | [Slide 36](https://littlekg87.github.io/lecture/2026_AI_History/#/4/lora-path) |
| Combining vector search with a metadata bonus | [Slide 40](https://littlekg87.github.io/lecture/2026_AI_History/#/4/query) |
| Blind expert evaluation | [Slide 48](https://littlekg87.github.io/lecture/2026_AI_History/#/4/expert-evaluation) |
| Findings and human-in-the-loop | [Slide 49](https://littlekg87.github.io/lecture/2026_AI_History/#/4/expert-results) |

A standalone talk of about 30 minutes on Ask Sillok alone, available in English, is in [`Asksillok_presentation/`](../Asksillok_presentation/).

### How to use

- **Moving:** arrow keys, Page Up / Page Down, the previous/next buttons at the bottom, or scrolling. Some scenes continue in steps within one slide.
- **Contents:** “전체 목차” at the top right, or the `M` key.
- **Interaction:** select counties on the map, data items, and the model and evaluation buttons to see changes and explanations.
- **More:** “더보기” at the bottom left opens background, evaluation procedure and glossary notes.
- **Screen:** slides are rendered on a **fixed 1920×1080 canvas** and scaled to the device. “전체 화면” is full screen; “확대 ＋” zooms up to 4×; while zoomed, “이동 모드” pans and “조작 모드” lets you operate the slide; “화면 맞춤” returns to the fitted view.

### Offline use

Save the file from the **Download the HTML** link above, or press **Download raw file** on [`index.html`](index.html), then open it in a browser. Images, fonts, scripts and data are all inside the one HTML file, so nothing needs installing. The file is about 23 MB. External links (Ask Sillok, original texts, the GitHub dataset) need an internet connection.

### Research material and demonstration

The deck contains actual research material (maps, datasets, stored embeddings) alongside conceptual diagrams of training, retrieval and evaluation. Weight changes, the matrix sizes and values of the LoRA adapter, retrieval scores and metadata bonuses, and the scores clicked on the expert-evaluation screen are illustrative examples, labelled as such on each screen. The lists and scores on the expert-evaluation screen are not actual retrieval results or expert ratings.

The deck does not itself run live AI retrieval or answering, and it does not submit scores to a server. The actual service is at [Ask Sillok](https://beta.asksillok.com).

### Files

| File | Description |
|---|---|
| [`index.html`](index.html) | The integrated web/offline presentation of 4 chapters and 49 slides |
| [`FONT-NOTICE.txt`](FONT-NOTICE.txt) | License notice for the embedded font |
| [`README.md`](README.md) | This guide |

The talk at Sogang University on 28 September 2026 used a 3-chapter, 41-slide edition. On 14 October 2026 it was replaced by the current 4-chapter edition, which adds the *Huangqing Zhigongtu* chapter. The address is unchanged, and the earlier edition is in the Git history.

### Related

- [*Sejong Sillok* Geography Section dataset](https://github.com/littlekg87/Sejong_Sillok_Jiriji): research data published on the speaker’s GitHub
- [Ask Sillok](https://beta.asksillok.com): a research interface for asking questions of the Annals of the Joseon Dynasty and exploring the evidence
- [Annals of the Joseon Dynasty, National Institute of Korean History](https://sillok.history.go.kr/): original texts and translations
- [Speaker’s portfolio](https://kunslab.com)
- [All teaching and presentation materials](../README.md)

For detailed sources and related papers, see each chapter’s cover and “더보기”. When citing, please give the original source and the presentation details. Use of the embedded font follows `FONT-NOTICE.txt`.

---

</details>
<!-- english:end -->

**김근하 · 4개 챕터, 총 49슬라이드의 인터랙티브 HTML 발표자료**

역사연구자의 질문에서 출발해 사료를 데이터로 만들고, 디지털 분석으로 기존 연구를 다시 해석하고, 역사 자료에 근거해 질문에 답하는 서비스를 설계한 과정을 소개합니다.

**[발표자료 바로 보기 ↗](https://littlekg87.github.io/lecture/2026_AI_History/)** · [HTML 내려받기](https://raw.githubusercontent.com/littlekg87/lecture/main/2026_AI_History/index.html)

## 이 자료를 사용한 발표

| 일자 | 행사 |
|---|---|
| 2026년 9월 28일 | 서강대학교 사학과 × 디지털역사연구소 콜로키움 |
| 2026년 10월 15일 | 이화여자대학교 사학과 콜로키움 |
| 2026년 10월 28일 | 부산대학교 디지털인문학센터 콜로키움 |

## 발표 구성

전체 목차는 **01–49**, 화면 하단은 **1–49 / 49**의 연속 번호를 사용합니다.

| 챕터 | 슬라이드 | 주제 |
|---|---|---|
| [01 · AI 시대의 역사학](https://littlekg87.github.io/lecture/2026_AI_History/#/1/cover) | 01–09 | 역사 연구의 질문과 근거, 디지털역사학과 AI의 역할 |
| [02 · 황청직공도 세계 인식 구조의 디지털 온톨로지 구축 연구](https://littlekg87.github.io/lecture/2026_AI_History/#/2/cover) | 10–16 | LLM과 그래프 DB를 활용해 사료를 데이터로 구축한 사례 |
| [03 · 조선 전기 군역 동원 체계의 구조 연구](https://littlekg87.github.io/lecture/2026_AI_History/#/3/cover) | 17–27 | 『세종실록지리지』의 데이터화와 전국 군현 분석으로 군역 개혁의 장기적 맥락을 재해석 |
| [04 · Searchable to Askable: Ask Sillok 설계 연구](https://littlekg87.github.io/lecture/2026_AI_History/#/4/cover) | 28–49 | 자료 설계부터 임베딩·파인튜닝·검색·평가·서비스 구현까지 이어지는 End-to-End RAG 시스템 설계 연구 사례 (46–49는 부록) |

### 황청직공도 세계 인식 구조의 디지털 온톨로지

『황청직공도』의 기록을 텍스트로 옮기고, 분류를 붙이고, 분류와 검토를 반복해 온톨로지로 구조화하는 과정을 다룹니다. 그래프 DB와 세계 지도 위에서 사료를 다시 읽으며, 사료를 데이터로 만들었을 때 무엇이 새로 보이는지를 살펴봅니다.

### 조선 전기 군역제의 장기적 변화

박사학위논문에서 다룬 군역 동원 단위와 군역 수행 비용의 표준화를, 전국적 편성 구조라는 질문으로 확장합니다. 『세종실록지리지』 334군현의 기록을 구조화하고 호구·군정·병종·지리 데이터를 결합해 군현 간 차이를 살펴봅니다.

사료에서 데이터셋을 만드는 과정, 코드에 의한 데이터 결합, 지도를 통한 호구·병종 비율 비교를 직접 조작할 수 있습니다. 데이터 분석과 문헌연구를 연결해 보법·대립가 상정·군적수포법으로 이어지는 개혁을 표준화라는 틀에서 해석합니다.

### Ask Sillok과 역사연구자의 평가

한글 제목–한문 본문 대응을 활용한 임베딩 모델 학습, LoRA 어댑터의 원리, 실제로 저장된 벡터, 벡터 검색과 메타데이터를 결합하는 Hybrid Retrieval을 소개합니다. 부록에서는 기본 모델과 파인튜닝 모델의 비교, 역사연구자의 블라인드 평가와 연구 결과를 통해 벤치마크 성능 향상과 실제 연구에서의 유용성을 구분하고, Human-in-the-loop의 필요성을 논의합니다.

| 주요 장면 | 바로 가기 |
|---|---|
| 사료를 그래프 DB로 읽기 | [14슬라이드](https://littlekg87.github.io/lecture/2026_AI_History/#/2/network) |
| 데이터와 코드의 결합 | [23슬라이드](https://littlekg87.github.io/lecture/2026_AI_History/#/3/order) |
| 군현 간 호구 비율의 차이 | [24슬라이드](https://littlekg87.github.io/lecture/2026_AI_History/#/3/inequality) |
| 군현 간 병종 비율의 차이 | [25슬라이드](https://littlekg87.github.io/lecture/2026_AI_History/#/3/service) |
| LoRA 어댑터의 학습 원리 | [36슬라이드](https://littlekg87.github.io/lecture/2026_AI_History/#/4/lora-path) |
| 벡터 검색과 메타데이터 가점의 결합 | [40슬라이드](https://littlekg87.github.io/lecture/2026_AI_History/#/4/query) |
| 전문가 블라인드 평가 | [48슬라이드](https://littlekg87.github.io/lecture/2026_AI_History/#/4/expert-evaluation) |
| 연구 결과와 Human-in-the-loop | [49슬라이드](https://littlekg87.github.io/lecture/2026_AI_History/#/4/expert-results) |

Ask Sillok만 다루는 약 30분 분량의 단독 발표는 [`Asksillok_presentation/`](../Asksillok_presentation/)에 있습니다.

## 이용 방법

- **이동:** 방향키, Page Up / Page Down, 화면 하단의 이전·다음 버튼 또는 스크롤을 사용합니다. 일부 화면은 같은 슬라이드 안에서 단계가 이어집니다.
- **전체 목차:** 우측 상단의 ‘전체 목차’ 또는 `M` 키로 원하는 슬라이드를 선택합니다.
- **상호작용:** 지도 위 군현, 데이터 항목, 모델과 평가 버튼을 선택해 변화와 설명을 확인합니다.
- **추가 설명:** 좌측 하단의 ‘더보기’에서 연구 배경·평가 절차·용어 설명 등을 확인합니다.

### 화면 크기와 확대

슬라이드 본문은 **1920×1080 고정 캔버스**로 렌더링하고 기기의 표시 공간에 맞춰 전체를 같은 비율로 확대·축소합니다. 컴퓨터·노트북·모바일에서 글씨, 줄바꿈, 도식과 여백의 상대적 배치가 같습니다. 화면 비율이 다르면 남는 공간은 여백으로 표시합니다.

- **발표장:** 상단의 ‘전체 화면’ 버튼을 사용합니다. 지원하지 않는 환경에서는 브라우저의 전체 화면 기능을 이용합니다.
- **모바일:** 가로로 돌리면 전체 슬라이드를 더 크게 볼 수 있습니다. 세로 화면에서도 전체 슬라이드를 유지합니다.
- **확대:** 상단 ‘확대 ＋’를 누르면 맞춤 크기의 최대 4배까지 확대됩니다.
- **이동 모드:** 확대한 화면을 손가락이나 마우스로 끌어 원하는 영역을 봅니다.
- **조작 모드:** ‘이동 모드’ 버튼을 눌러 전환하면 슬라이드 안의 지도·모델·평가 버튼 등을 조작할 수 있습니다.
- **화면 맞춤:** 확대를 해제하고 전체 슬라이드로 돌아갑니다.

## 내려받아 오프라인으로 보기

1. 위의 **HTML 내려받기** 링크에서 파일을 저장하거나, [`index.html`](index.html)의 **Download raw file**을 누릅니다.
2. 내려받은 `index.html`을 브라우저에서 엽니다.

이미지·폰트·스크립트·데이터가 HTML 하나에 포함되어 있어 별도 설치나 로컬 서버가 필요하지 않습니다. 파일 크기는 약 23MB입니다. Ask Sillok, 원문, GitHub 데이터셋 등 외부 링크 방문에는 인터넷 연결이 필요합니다.

## 실제 연구 자료와 시연의 구분

지도·데이터셋·저장된 임베딩 등 연구 자료와, 학습·검색·평가 절차를 설명하는 개념 도식이 함께 포함되어 있습니다. 가중치 변화, LoRA 어댑터의 행렬 크기와 수치, 검색 점수와 메타데이터 가점, 전문가 평가 화면의 클릭 점수 등은 각 화면에 표시된 설명용 예시입니다. 특히 전문가 평가 화면의 목록과 선택 점수는 실제 검색 결과나 전문가 평정값이 아닙니다.

발표자료 자체가 실시간 AI 검색·답변을 수행하거나 평가 점수를 서버에 제출하지는 않습니다. 실제 서비스는 [Ask Sillok](https://beta.asksillok.com)에서 이용할 수 있습니다.

## 파일 구성

| 파일 | 설명 |
|---|---|
| [`index.html`](index.html) | 4개 챕터·49슬라이드의 웹·오프라인 통합 발표자료 |
| [`FONT-NOTICE.txt`](FONT-NOTICE.txt) | 포함된 폰트의 라이선스 고지 |
| [`README.md`](README.md) | 발표 내용과 이용 안내 |

2026년 9월 28일 서강대학교 발표에서는 3챕터·41슬라이드 판을 사용했습니다. 2026년 10월 14일에 『황청직공도』 챕터를 더한 현재의 4챕터 판으로 교체했습니다. 발표 주소는 유지되며, 이전 판은 Git 커밋 기록에서 확인할 수 있습니다.

## 관련 자료

- [『세종실록지리지』 데이터셋](https://github.com/littlekg87/Sejong_Sillok_Jiriji): 발표자의 GitHub에 공개한 연구 데이터
- [Ask Sillok](https://beta.asksillok.com): 조선왕조실록에 질문하고 근거를 탐색하는 연구 인터페이스
- [국사편찬위원회 조선왕조실록](https://sillok.history.go.kr/): 실록 원문과 번역문
- [발표자 포트폴리오](https://kunslab.com)
- [강의·발표 자료 전체 목록](../README.md)

상세 출처와 관련 논문은 각 챕터의 표지 및 ‘더보기’를 참고해 주세요. 자료를 인용할 때에는 원 출처와 발표 정보를 함께 밝혀 주세요. 포함된 폰트의 이용 조건은 `FONT-NOTICE.txt`를 따릅니다.
