# Github Actions
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

