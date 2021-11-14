## 21-2학기 Big Data Programming 프로젝트

---

### 문제 정의

---

- 문제 정의
  - 컴퓨터 관련 학과에 재학 중인 3,4학년 학생들이 취업을 준비함에 있어서 자신의 준비상태를 명확하게 알기가 어려움.
- 해결 방법
  - 채용 공고 속 IT직무 신입의 자격 조건과 우대 조건을 자연어 처리를 통해 키워드를 분석
  - 이를 자신의 상태와 비교하여 준비 상태를 점검하고자 함.
- 제한 사항
  - 기술스택 등에 준비 상태의 질적인 측면(같은 기술 스택을 사용하더라도 지식과 이해, 경험의 깊이 차이 등)을 명확하게 평가할 수 없으므로 단순 키워드를 통한 대학생의 준비상태 확인을 목표로 한다.

### 실행 계획

---

- 데이터 수집 방법
  1. 채용공고 사이트 API 활용
     Saramin 채용정보 API([https://oapi.saramin.co.kr/](https://oapi.saramin.co.kr/))
  2. 채용공고 사이트 크롤링

     JobKorea, 원티드 등 채용 공고 사이트들을 크롤링
- 데이터 분석 방법
  - raw데이터들을 확인하고 이를 적절한 table형태로 변형 저장한다.
  - 이렇게 된 데이터들에 대해서 koNLPy를 이용하여 회사,직무, 자격조건, 우대조건 등에 대한 키워드를 노출 빈도로 정리한다.
  - 정리된 데이터를 활용하여 원하는 직무 혹은 회사의 규모에 따른 자격 조건과 우대 조건에 대한 정보를 확인하고 자신의 현재 상태와 비교한다.
- 시스템 아키텍쳐
  ![Untitled](https://www.notion.so/dojinyou/bb1e61e5e84c4782bb0bb61d624f122f#0916f311833146188e62c96d0f74047a)
  1. 데이터 수집은 api와 크롤링을 이용해서 local에서 진행하고 Cyberduck을 이용해 업로드 한다.
  2. 이후 해당 데이터를 hadoop fs로 copy하여 저장한다.
  3. 이렇게 저장된 데이터를 hbase에 통해서 접근한다.
  4. hive는 hbase의 데이터들을 table로 만들고 이를 zeppelin을 이용하여 분석한다.
