# WSL에 포함된 Ubuntu 와 VS Code 연동하기
* Windows에 WSL(Ubuntu)과 Docker Desktop 설치된 상태
* Windows의 CMD나 Powershell을 사용하지 않고 Ubuntu를 실행하고 VS Code를 연동하여 사용하려고 한다
* Microsoft가 공식 제공하는 "WSL 통합 기능"을 사용하는 것이 가장 편리
* Docker Desktop을 실행하고 상단 메뉴에서 톱니바귀 아이콘 > Resources > WSL Integration > Ubuntu 클릭하여 활성화
* 위의 설정은 Docker명령을 WSL의 Ubuntu에서 실행될 수 있도록 통합한다

## Docker Desktop에서 WSL의 Ubuntu 와 통합 설정
* 참고: Docker Desktop 설정 확인
* Docker Desktop 실행
* Settings > Resources > WSL Integration
* 사용 중인 Ubuntu 배포판 옆에 ✅ 체크되어 있어야 함

## 1단계: WSL2와 Docker Desktop이 이미 설치되어 있어야 함
* WSL2: Ubuntu 등 배포판 설치됨
* Docker Desktop: 설치 및 실행 중 (WSL2 기반 통합 활성화)
* Windows용 VS Code 설치 완료

## 2단계: VS Code에 WSL 확장(Extension) 설치
* VS Code 실행
* 왼쪽 사이드바 Extensions 클릭 (또는 Ctrl+Shift+X)
* "Remote - WSL" 검색  
🔵 "Remote - WSL" by Microsoft 설치

## 3단계: WSL2의 Ubuntu 경로를 VS Code에서 열기
* 방법 1: WSL 터미널에서 바로 VS Code 실행
```bash
cd ~/django_docker_project
code .
```
* 방법 2: VS Code 내에서 직접 열기
  + VS Code 실행
  + 왼쪽 아래 초록색 버튼 클릭 (WSL 로고 표시)
  + WSL: Ubuntu 클릭
  + WSL 내 디렉토리를 탐색하여 열기

## 4단계: 열 수 있는 파일들
* WSL2에 있는 모든 파일을 VS Code로 열고 자유롭게 수정할 수 있음:
  + Dockerfile
  + .dockerignore
  + manage.py
  + settings.py
  + .env 파일 등
* 변경 후 저장하면 자동으로 WSL2 내 파일로 저장됨

## 5단계: Docker와의 연동
 * Docker Desktop이 WSL2 연동 기능이 활성화되어 있다면, Docker 관련 명령어도 VS Code 내 터미널(WLS Ubuntu 쉘)에서 자유롭게 실행할 수 있음
```bash
docker build -t django-test-app .
docker run -d -p 8000:8000 django-test-app
```

