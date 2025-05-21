# WSL에 포함된 Ubuntu 와 VS Code 연동하기
* Windows에 WSL(Ubuntu)과 Docker Desktop 설치된 상태
* Windows의 CMD나 Powershell을 사용하지 않고 Ubuntu를 실행하고 VS Code를 연동하여 사용하려고 한다
* Microsoft가 공식 제공하는 "WSL 통합 기능"을 사용하는 것이 가장 편리
* Docker Desktop을 실행하고 상단 메뉴에서 톱니바귀 아이콘 > Resources > WSL Integration > Ubuntu 클릭하여 활성화
* 위의 설정은 Docker명령을 WSL의 Ubuntu에서 실행될 수 있도록 통합한다

## 1단계: WSL2와 Docker Desktop이 이미 설치되어 있어야 함
* WSL2: Ubuntu 등 배포판 설치됨
* Docker Desktop: 설치 및 실행 중 (WSL2 기반 통합 활성화)
* Windows용 VS Code 설치 완료

## 2단계: VS Code에 WSL 확장(Extension) 설치
* VS Code 실행
* 왼쪽 사이드바 Extensions 클릭 (또는 Ctrl+Shift+X)
* "Remote - WSL" 검색
🔵 "Remote - WSL" by Microsoft 설치

## 
