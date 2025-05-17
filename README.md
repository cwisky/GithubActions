# Github Actions
* GitHub Actions는 GitHub 저장소에 업로드된 코드에 연결된 자동화 시스템이며,
* 사용자가 정의한 .yml 파일에 따라 코드의 변경을 감지하고 자동으로 작업을 수행하는 플랫폼.
* 그 핵심은 워크플로우 → 이벤트 → 작업 → 단계 구조이며, 모든 설정은 GitHub UI의 Actions 탭과 .yml 파일로 연결되어 있다.
  
## GitHub Actions란? (개념 정의)
* GitHub Actions는 GitHub 저장소 안에서 코드를 자동으로 빌드, 테스트, 배포할 수 있도록 만들어진 자동화(Automation) 시스템.
* 코드 변경(push, PR, schedule)을 감지하여
* 정의된 **워크플로우(workflow)**에 따라
* CI/CD 파이프라인을 실행함  
👉 쉽게 말해, "GitHub 안에서 내가 설정한 자동화 명령서(yml)를 따라 알아서 작업을 해주는 비서".

## GitHub 웹 UI에서의 메뉴 위치
* GitHub 저장소(Repository) 페이지 상단에서:
* [Code] [Issues] [Pull requests] [Actions] [Projects] ...
* 여기서 [Actions] 탭이 바로 GitHub Actions 대시보드이다.
* 이 탭에서 할 수 있는 일:
  + 저장소에 설정된 워크플로우 목록 확인
  + 실행된 기록(Log) 확인
  + 실패/성공 상태 확인
  + 수동 실행도 가능
 
## GitHub Actions의 구성 체계
* GitHub Actions는 아래와 같은 4단계 구조로 이루어져 있음:
* 구성요소	설명
  + Workflow (워크플로우)	.yml 파일 하나 = 자동화 시나리오 전체
  + Event (이벤트)	언제 실행할지 정함 (예: push, PR, schedule 등)
  + Job (작업)	워크플로우 내에서 병렬/순차적으로 실행되는 작업 단위
  + Step (단계)	각 Job 안에서 순서대로 실행되는 명령어나 Action

## yml에 정의하는 workflow의 예
```yml
# Workflow
on: push             # Event

jobs:
  build:             # Job
    runs-on: ubuntu-latest
    steps:           # Step 목록
      - name: Checkout
        uses: actions/checkout@v3

      - name: Run tests
        run: npm test
```

## YML 핵심 구성요소 설명

|용어	|설명	|예시| 
|-----|-----|-----|
|Workflow|	.github/workflows/*.yml 파일로 저장	|ci.yml, deploy.yml 등|
|Event|	워크플로우를 트리거하는 조건	|push, pull_request, schedule, workflow_dispatch 등|
|Job|	하나 이상의 Step으로 구성된 실행 단위	|build, deploy|
|Step|	단일 명령이나 Action 수행	|run: echo Hello, uses: actions/checkout@v3|
|Action|	재사용 가능한 단위 작업	|actions/checkout, appleboy/ssh-action|
|Runner|	실제로 코드를 실행하는 GitHub 제공 가상머신	|ubuntu-latest, windows-latest 등|

## 내가 GitHub Actions로 하고 싶은 일
|하고 싶은 일	|설정 방법|
|-------------|----------|
|push 할 때마다 자동 테스트|	on: push + npm test 실행|
|하루에 한 번 자동 빌드|	on: schedule + cron 설정|
|PR 만들었을 때 리뷰 알림|	on: pull_request + 슬랙 연동|
|코드 변경 시 서버에 배포|	on: push + SSH 배포 스크립트 실행|

## GitHub Actions를 학습하기 위한 관문 요약
|학습| 순서|	내용|
|----|---------|----------|
|1단계|	"Actions" 탭은 어디 있고, 무엇을 보여주는가?|
|2단계|	.github/workflows/파일.yml 하나가 하나의 워크플로우|
|3단계|	on, jobs, steps, run, uses 같은 키워드 의미|
|4단계|	실제로 간단한 echo 워크플로우를 만들어보기|

## YML안에서 workflow를 사용하여 할 수 있는 테스트 유형
* 단위 테스트 (Unit Tests)
  + 코드의 가장 작은 단위(함수, 메서드 등)를 테스트

|예시 언어|	테스트 도구|  
|---------|------------|
|Python|	pytest, unittest|
|JavaScript|	Jest, Mocha|
|Java|	JUnit, TestNG|
|C#|	xUnit, NUnit|
|Go|	go test|
* 파이썬 단위 테스트의 예
```yml
run: |
  pip install -r requirements.txt
  pytest
```
## 테스트 유형별 GitHub Actions 구조 예시
```yml
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Python 설치
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: 의존성 설치
        run: pip install -r requirements.txt

      - name: 단위 테스트
        run: pytest

      - name: 코드 스타일 검사
        run: flake8 .

      - name: 보안 검사
        run: bandit -r my_project/
```

