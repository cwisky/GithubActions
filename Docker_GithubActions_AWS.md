# CI/CD (Docker, Github Actions, AWS)
* Windows → WSL2 + Docker → Python 앱 개발 → GitHub 업로드 → GitHub Actions로 EC2에 배포 → 실행 로그 기록

## 개발 시스템에 git 클라이언트 설치
* https://github.com/cwisky/Git_Github

## [1단계] Windows에 WSL + Docker 환경 구축  
📌 필요한 도구 설치  
* WSL2 설치 (Ubuntu 권장)
* 공식 가이드 또는 PowerShell에서:
```powershell
wsl --install
wsl --set-default-version 2
```

## 위의 방법으로 안되면...
* 수동으로 가상환경 활성화 :
```powershell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```
* 재부팅
```powershell
shutdown /r /t 0
```
* Ubuntu 배포판 설치
```powershell
wsl --install -d Ubuntu
```

## 추가로 확인할 BIOS 설정 (필요시)
* 제조사 로고 화면에서 F2, Del, 또는 Esc 눌러 BIOS 진입
* Virtualization 또는 Intel VT-x, AMD-V 같은 설정을 Enabled로 변경

## 위의 방법이 모두 안되면 Ubuntu 수동 설치 (WSL Store 우회)
* 만약 wsl --install이 계속 실패한다면,
* Microsoft Store 대신 수동으로 Ubuntu 패키지를 설치
* https://aka.ms/wslubuntu2204
* C:\\Windows\\System32\\> Add-AppxPackage .\Ubuntu2204-221101.AppxBundle
* wsl -d Ubuntu
* wsl.exe --install --no-distribution
* wsl 기반으로 리눅스가 실행되는지 확인 > 창 닫기

## Docker Desktop 설치
* https://www.docker.com/products/docker-desktop/
* 관리자 권한으로 설치
* 설치 중 “WSL2 기반 백엔드” 옵션 선택 필수
* 설치 후 Docker Desktop 실행(Docker 명령을 사용할 때는 항상 실행된 상태여야 함)

## Docker Desktop 처음 실행
* Accept
* WSL 자동 실행창 표시,닫아도 됨
* work/Person 선택 > Google 로그인

## WSL, Docker Desktop 통합
* WSL 기반 개발환경과 Docker가 완벽하게 통합되어 VSCode + WSL 개발에서 매우 중요
* Docker Desktop 실행 → 오른쪽 상단 톱니바퀴(⚙️) 클릭 → Settings 열기
* 좌측 메뉴에서 → "Resources" → "WSL Integration" 클릭
* 설치된 WSL 배포판 목록(Ubuntu 등)이 표시됨, 디폴트로 선택되어 있음
→ 여기서 Ubuntu 옆에 있는 스위치(✔️) 를 켜면 통합 활성화됨
* 설정 저장 후 Docker Desktop 재시작 권장

## CMD에서 Docker 명령어 실행
* docker --version
* docker run hello-world
```cmd
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
e6590344b1a5: Pull complete
Digest: sha256:dd01f97f252193ae3210da231b1dca0cffab4aadb3566692d6730bf93f123a48
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.
```

## VS Code와 WSL 통합
* VS Code의 콘솔에서 Docker 명령어를 수행할 수 있음
* wsl extentension 설치(아래의 목록 참조)

| 목적        | 확장             |
| --------- | -------------- |
| WSL 통합    | ✅ Remote - WSL |
| Python 개발 | ✅ Python       |
| Docker 연동 | ✅ Docker       |
| Git 추적    | ✅ GitLens      |
| 원격 서버     | ✅ Remote - SSH |
| YAML 편집   | ✅ YAML         |

## [2단계] WSL 또는 VSCode에서 Python + Docker 프로젝트 작성  
📁 예시 프로젝트 구조  
```text
python-app/
├── app.py
├── Dockerfile
└── requirements.txt
```
* app.py
```python
from datetime import datetime

with open("log.txt", "a") as f:
    f.write(f"✅ 프로그램 실행됨: {datetime.now()}\n")
print("작업 완료")
```
* requirements.txt
```text
```
* Dockerfile
```docker
FROM python:3.10-slim

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
```
* 로컬에서 테스트
```docker
docker build -t python-test-app .  # 현재 디렉토리에 있는 Makefile를 사용하여 이미지 생성
docker images   # image 생성 확인

# 1. 컨테이너를 실행하면서 컨테이너 이름 지정
docker run --name mylogtest python-test-app

# 2. 컨테이너에서 호스트로 파일 복사
docker cp mylogtest:/app/log.txt ./log.txt   # mylogtest컨테이너의 app/log.txt 파일을 현재 디렉토리의 log.txt에 복사

cat log.txt    # 현재 디렉토리에 복사된 log.txt 파일 내용 표시
```

## [3단계] GitHub에 프로젝트 업로드
```docker
git init
git remote add origin https://github.com/cwisky/GithubActions.git
git add .
git commit -m "Initial commit"
git push -u origin main
```

