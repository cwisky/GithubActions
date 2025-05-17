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
