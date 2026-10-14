# AI가 읽어낸 조선왕조실록의 패턴들(서울대, 2026.08.31.)

<!-- english:start -->
<details markdown="1">
<summary markdown="span"><strong>🌐 English</strong> — click to open the English version</summary>

## Patterns in the Annals of the Joseon Dynasty as Read by AI (Seoul National University, 2026.08.31.)

**Centered on research cases from the Geography Section of the *Sejong Sillok***

Slides from a workshop at Seoul National University. For graduate students in history and the humanities, the talk shows through actual research cases how AI can be used in historical research. The slides are in Korean.

> #### ▶ **[Open the slides](https://littlekg87.github.io/lecture/2026_SeoulUnivWorkshop/)**
> They open directly in the browser without downloading.

- **Speaker** Kunha Kim (Institute for Maritime Humanities, Pukyong National University)
- **Length** 45 minutes · 27 slides

### The claim of this talk

> **Using AI does not change the essence of what historians do.**

Historians still read sources, select information, classify it, find relations and patterns, interpret, and present the results. AI does not replace this; it expands the **scale, the ways of comparing, and the forms of presentation** we can handle.

> **We do not ask AI about history; we have it compute what we are historically curious about.**

### Structure

| Part | Content |
|---|---|
| **Problem** | The methods of history and of digital history are the same |
| **Pattern 1 — patterns in the source** | Find the repeated sentence forms of the *Sejong Sillok* geography and turn them into data for 334 counties (source → data) |
| **Pattern 2 — patterns in the data** | Combine a “distance to Hanyang”, which the geography does not contain, using HGIS to see the spatial distribution of rotating capital-duty soldiers (data → interpretation) |
| **Pattern 3 — patterns between source and data** | Why was the *bobeop* system implemented first in the three southern provinces? Test a question from the sources with data and return to the sources |
| **Conclusion · epilogue** | Summary of the three levels, and Ask Sillok |

### Controls

| Action | How |
|---|---|
| Next / previous | `→` `←` `Space` `PageUp/Down`, or the arrows at the top right |
| Open contents | Click the page number, or `G` |
| Close contents | `ESC` `G`, or click outside |
| First / last | `Home` `End` |

Some slides have elements that respond to hovering or clicking.

- Donut charts and cards — hovering highlights the item
- Map on slide 16 — **click to enlarge**
- Original regulation text on slide 18 — the `기존 연구가 주목한 것` (what earlier research focused on) / `이 발표가 주목한 것` (what this talk focuses on) buttons change the highlight

### Files

**Slides**

| File | Description |
|---|---|
| `SeoulUniv_Presentation.html` | The slides: a single HTML file including the images |
| `index.html` | Redirects the folder address to the file above |

Any browser opens it; no other program or internet connection is needed. The body font is loaded from Google Fonts, so offline it falls back to the system font.

**Printing / saving as PDF** — print from the browser in landscape and each slide fills one page.

**Exercise data**

Materials for following the three demonstrations in the talk.

| File | Content | Used in |
|---|---|---|
| `2nd_wda_400.xml` | XML text of the *Sejong Sillok* geography (2.8 MB). Structure: `level2` (geography) → `level3` (11 provinces) → `level4` (44 principal towns) → `level5` (291 subordinate towns) | **Demo 1** — extracting 戶·口·軍丁 from the repeated sentence forms |
| `counties_334.csv` | Data for 334 counties extracted and cleaned from the text above (49 columns) | **Demos 2 · 3** — distribution of service branches, analysis of 口/戶 |

**Columns of `counties_334.csv`** (the column names are in Korean or Classical Chinese)

| Group | Columns |
|---|---|
| Identification · administration | `아이디` (ID) `고을` (county) `한자` (Chinese characters) `도` (province) `계수관` (regional seat) `레벨` (level) |
| Households · soldiers | `호` (households) `구` (persons) `군정` (adult males for service) `번상군` (rotating capital duty) `유방군` (local garrison) `수군` (navy) |
| Service branches | 23 columns such as `侍衛軍` `守城軍` `船軍` `翼軍` `鎭軍` `甲士` |
| Space | `lon` `lat` `면적km2` (area) `한양거리km` (distance to Hanyang) |

> **The `아이디` (ID) column is the key for joining.** Values such as `wda_40009001` match the article IDs of the National Institute of Korean History’s Annals XML exactly. This is where one article of the source connects to one row of spatial data; slide 15 covers this join.

`한양거리km` is not in the geography. It is a column computed with HGIS as the distance between each county seat and Hanyang — **a variable the researcher created that the source does not contain** (slides 14–16).

Caution — the figures in the geography are not actual households, population or troop strength but **figures recorded under the central government’s compilation system**. They must be interpreted with that premise.

### See also

- **[Ask Sillok](https://beta.asksillok.com/)** — an AI question-answering service based on the Annals of the Joseon Dynasty
- **[kunslab.com](https://kunslab.com/)** — the speaker’s research site (publications, talks, teaching materials)
- **[Sejong_Sillok_Jiriji](https://github.com/littlekg87/Sejong_Sillok_Jiriji)** — the related research dataset

### Sources

The historical material in the talk is based on databases published by the National Institute of Korean History. Please cite the original source.

- Annals of the Joseon Dynasty database · Geography Section of the *Sejong Sillok* — National Institute of Korean History

The maps and statistics on the slides are the speaker’s research results. Please cite them when you use them.

---

</details>
<!-- english:end -->

**세종실록지리지 연구 사례를 중심으로**

서울대학교 워크숍 발표 슬라이드입니다. 역사학·인문학 대학원생을 대상으로, 실제 연구 사례를 통해 AI를 역사 연구에 어떻게 활용하는지 보여줍니다.

> ### ▶ **[슬라이드 바로 보기](https://littlekg87.github.io/lecture/2026_SeoulUnivWorkshop/)**
> 내려받지 않아도 브라우저에서 바로 열립니다.

- **발표** 김근하 (국립부경대학교 해양인문학연구소)
- **분량** 45분 · 27장

---

## 이 발표의 명제

> **AI를 사용해도 역사학자가 하는 일의 본질은 바뀌지 않는다.**

역사학자는 여전히 사료를 읽고, 정보를 선택하고, 분류하고, 관계와 패턴을 찾고, 해석하고, 결과로 표현합니다.
AI는 이를 대체하는 것이 아니라 다룰 수 있는 **규모·비교 방식·표현 형식**을 확장합니다.

> **AI에게 역사를 물어보는 것이 아니라, 내가 역사적으로 궁금한 것을 계산시키는 것이다.**

---

## 구성

| 장 | 내용 |
|---|---|
| **문제 제기** | 역사학의 방법과 디지털역사학의 방법은 같다 |
| **패턴 1 — 사료의 패턴** | 『세종실록지리지』의 반복 문형을 찾아 334개 군현 데이터로 만든다 (사료 → 데이터) |
| **패턴 2 — 데이터의 패턴** | 지리지에 없는 '한양거리'를 HGIS로 결합해 번상군의 공간 분포를 본다 (데이터 → 해석) |
| **패턴 3 — 사료와 데이터 사이의 패턴** | 보법은 왜 삼남에서 먼저 시행되었나 — 사료의 질문을 데이터로 검증하고 다시 사료로 돌아간다 |
| **결론 · 에필로그** | 세 층위의 정리, 그리고 Ask Sillok |

---

## 조작법

| 동작 | 방법 |
|---|---|
| 다음 / 이전 | `→` `←` `Space` `PageUp/Down`, 또는 우측 상단 화살표 |
| 목차 열기 | 페이지 번호 클릭, 또는 `G` |
| 목차 닫기 | `ESC` `G`, 또는 바깥 클릭 |
| 처음 / 끝 | `Home` `End` |

일부 슬라이드에는 마우스를 올리거나 눌러야 반응하는 요소가 있습니다.

- 도넛 그래프 · 카드 — 마우스를 올리면 해당 항목이 강조됩니다
- 16장 지도 — **클릭하면 크게 확대**됩니다
- 18장 사목 원문 — `기존 연구가 주목한 것` / `이 발표가 주목한 것` 버튼으로 강조 지점이 바뀝니다

---

## 파일

### 슬라이드

| 파일 | 설명 |
|---|---|
| `SeoulUniv_Presentation.html` | 발표 슬라이드 본체. 이미지까지 포함된 단일 HTML 파일입니다 |
| `index.html` | 폴더 주소로 접속했을 때 위 파일로 이동시키는 문서 |

브라우저만 있으면 열립니다. 별도 프로그램이나 인터넷 연결이 필요하지 않습니다.
다만 본문 글꼴은 Google Fonts에서 불러오므로, 오프라인에서는 시스템 기본 글꼴로 표시됩니다.

**인쇄 · PDF 저장** — 브라우저 인쇄에서 용지를 가로로 두면 슬라이드 한 장이 한 쪽으로 출력됩니다.

### 실습 데이터

발표의 세 시연을 직접 따라 해 볼 수 있는 자료입니다.

| 파일 | 내용 | 쓰이는 곳 |
|---|---|---|
| `2nd_wda_400.xml` | 『세종실록』 지리지 원문 XML (2.8MB). `level2`(지리지) → `level3`(도 11) → `level4`(주읍 44) → `level5`(속읍 291) 구조 | **시연 1** — 반복 문형에서 戶·口·軍丁 추출 |
| `counties_334.csv` | 위 원문에서 추출·정제한 334개 군현 데이터 (49개 열) | **시연 2 · 3** — 병종 분포, 口/戶 분석 |

**`counties_334.csv` 열 구성**

| 묶음 | 열 |
|---|---|
| 식별 · 행정 | `아이디` `고을` `한자` `도` `계수관` `레벨` |
| 호구 · 군정 | `호` `구` `군정` `번상군` `유방군` `수군` |
| 병종 세부 | `侍衛軍` `守城軍` `船軍` `翼軍` `鎭軍` `甲士` 등 23개 |
| 공간 | `lon` `lat` `면적km2` `한양거리km` |

> **`아이디` 열이 결합의 열쇠입니다.**
> `wda_40009001` 같은 값은 국사편찬위원회 실록 XML의 기사 ID와 그대로 일치합니다.
> 사료 기사 하나가 공간 데이터 한 행과 이어지는 지점이며, 발표 15장에서 이 결합을 다룹니다.

`한양거리km`는 지리지에 없는 값입니다. HGIS로 군현 치소와 한양 사이 거리를 계산해 붙인 열로, **사료에 없는 변수를 연구자가 만들어 넣은 사례**입니다 (14~16장).

주의 — 지리지의 수치는 실제 가구·인구·군액이 아니라 **중앙의 편찬 체계 아래 등재된 기록상 수치**입니다. 해석할 때 이 전제를 두고 다뤄야 합니다.

---

## 함께 보기

- **[Ask Sillok](https://beta.asksillok.com/)** — 조선왕조실록 기반 AI 질의 서비스
- **[kunslab.com](https://kunslab.com/)** — 발표자 연구 홈페이지 (연구성과 · 학술발표 · 강의 자료)
- **[Sejong_Sillok_Jiriji](https://github.com/littlekg87/Sejong_Sillok_Jiriji)** — 관련 연구 데이터셋

---

## 자료 출처

발표에 사용한 역사 자료는 국사편찬위원회가 공개한 데이터베이스에 기반합니다.
인용하실 때에는 원 출처를 함께 밝혀 주시기 바랍니다.

- 조선왕조실록 DB · 『세종실록지리지』 — 국사편찬위원회

슬라이드에 실린 지도와 통계는 발표자의 연구 결과입니다. 인용 시 출처를 밝혀 주세요.
