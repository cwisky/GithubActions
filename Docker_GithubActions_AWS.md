# CI/CD (Docker, Github Actions, AWS)
* Windows → WSL2 + Docker → Python 앱 개발 → GitHub 업로드 → GitHub Actions로 EC2에 배포 → 실행 로그 기록

## 개발 시스템에 git 클라이언트 설치
* https://github.com/cwisky/Git_Github

## [1단계] Windows에 WSL + Docker 환경 구축  
📌 필요한 도구 설치  
* WSL2 설치 (Ubuntu 권장) https://learn.microsoft.com/ko-kr/windows/wsl/install
* 공식 가이드 또는 PowerShell에서:
```powershell
wsl --install  # WSL2가 기본으로 설치되며 Ubuntu가 디폴트임
wsl --set-default-version 2
```
* 설치 후에 시스템을 다시 부팅하면 디폴트로 Ubuntu 가 설치된다
* WSL이 실행되고 있는지 확인
```powershell
PS C:\WINDOWS\system32> wsl --list --verbose
  NAME      STATE           VERSION
* Ubuntu    Stopped         2
```
* WSL 삭제 : wsl --unregister Ubuntu


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

## Docker Desktop - Unexpected WSL error
* Window 검색창에서 "Windows 기능 켜기 또는 끄기" 입력
* Hyper -V 체크
* Linux용 Windows 하위 시스템 체크
* Windows 하이퍼바이저 플랫폼
* BIOS 셋업 : 부팅시 ESC, F2, F10, DELETE 키를 눌러서 BIOS셋업 > AMD-V, Intel VT-x, Virtualization 등의 속성을 찾아서 Enabled 설정

## 오류 해결 참조
* https://velog.io/@rondido/window-docker-%EC%8B%A4%ED%96%89-%EA%B4%80%EB%A0%A8-Error-%ED%95%B4%EA%B2%B0
* https://jih0.medium.com/amd-cpu-%EA%B0%80%EC%83%81%ED%99%94-%EB%B0%8F-windows-10-wsl-2-docker-desktop-%EC%84%A4%EC%B9%98-beb2b7a09397
* bcdedit /set hypervisorlaunchtype auto

## Docker Desktop 처음 실행
* Docker Subscription Service Agreement : Accept
* WSL 자동 실행창 표시,닫아도 됨
* work/Person 선택 > Google 로그인
* Survey...
* docker desktop 초기화면 표시됨
* docker 명령어 사용시에는 항상 Docker Desktop 실행되어 있어야 함

## WSL, Docker Desktop 통합
* WSL 기반 개발환경과 Docker가 완벽하게 통합되어 VSCode + WSL 개발에서 매우 중요
* Docker Desktop 실행 → 오른쪽 상단 톱니바퀴(⚙️) 클릭 → Settings 열기
* 좌측 메뉴에서 → "Resources" → "WSL Integration" 클릭
* 설치된 WSL 배포판 목록(Ubuntu 등)이 표시됨, 디폴트로 선택되어 있음
→ 여기서 Ubuntu 옆에 있는 스위치(✔️) 를 켜면 통합 활성화됨
* 설정 저장 후 Docker Desktop 재시작 권장

## WSL에 디폴트 내장된 Ubuntu 에서 Docker 명령어 테스트
* 위의 설정으로 WSL에 포함된 Ubuntu에서도 Docker 명령어를 실행할 수 있다
* 윈도우 검색창에 "Ubuntu" 입력
* 이용자 아이디 : dmin<엔터>
* New password : mbcaca
* Retype new password : mbcaca
* docker --version

## WSL에 포함된 Ubuntu의 활용
* docker를 사용할 때는 거의 필요없음(CMD, Powershell을 사용하면 충분함)
* Linux를 학습해야 할 때는 유용함
* Linux에서 docker를 경험해야 하는 상황이라면 좋은 환경이됨
* Linux에 docker 이미지를 배포할 때 동일한 환경을 제공함
* Linux를 기반으로 개발해야 할 때도 유용함
* WSL의 Ubuntu에서 docker 이미지 개발 및 git배포 가능
* WSL의 Ubuntu에서 docker 이미지를 개발할 때 파이썬 프로젝트를 위해 Window에 설치된 MS Code 연동 가능
* WSL에서 만든 Docker 이미지/컨테이너는 Windows에서도 동일하게 docker 명령어로 접근 가능

## 도커 Image, Container
* Image : Dockerfile로 만든 실행 환경(코드, 라이브러리, 설정 등)을 하나의 패키지처럼 만든 것
* 도커 이미지 배포 : 이미지를 Docker Hub 또는 GitHub Container Registry(GHCR)에 올리는 것
* Container : 이미지를 실행해서 실제로 작동 중인 인스턴스(컨테이너), docker run으로 컨테이너를 생성
* 비유로 설명하면?
  + 이미지 배포 = “앱 설치파일(.apk, .exe)을 다른 사람에게 배포하는 것”
  + 컨테이너 배포 = “그 앱을 실제로 핸드폰이나 서버에 설치하고 실행시켜서 서비스하는 것”

## 도커 설치 후, CMD에서 최초로 Docker 명령어 실행
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

# 로컬 리파지토리에서 github의 코드 리파지토리(MyCode)에 push하고 actions확인하기
* 로컬 push명령에 의해 github actions에 정의된 워크플로우가 실행되는지 확인하는 절차
  1. mycode 리파지토리 생성(보안상 private 설정)
  2. mycode/.github/workflows/log_only.yml 생성 : echo "????" 이용하여 로그를 남기는 내용
  3. 로컬에서 임의의 디렉토리에 가상환경을 생성한다
  4. 가상환경 디렉토리로 이동
  5. 가상환경 활성화
  6. 필요한 모듈 설치(예, pip install django )
  7. git init : 현재 디렉토리를 로컬 리파지토리로 초기화
  8. git clone [mycode 리파지토리 주소]
  9. cd mycode
  10. mycode 안에 app.py 생성(현재 내용은 중요하지 않음)
  11. 현재 가상환경에 설치된 모듈의 목록 추출 : pip freeze > requirements.txt
  12. git add .     # 현재 2개의 파일 존재(app.py, requirements.txt)
  13. git status
  14. git commit -m "github actions 작동 테스트"
  15. git push origin main
  16. Github.com의 mycode/Actions/에서 로그 확인 : log_only.yml 이 실행되었는지 확인

## Github에서 private 코드 저장소 생성
* mycode (임의의 저장소 이름) 지정
* README.md 파일 생성도 임의로 결정
* mycode/.github/workflows/log_only.yml 파일 생성(push origin main을 감지하고 로그를 출력한다)
```yml
name: Log only when pushed

on:
  push:
    branches:
      - main  # 또는 'master' 등 사용 중인 브랜치 이름

jobs:
  log-job:
    runs-on: ubuntu-latest

    steps:
      - name: Show simple log
        run: |
          echo "✅ GitHub Actions workflow triggered!"
          echo "🕒 Timestamp: $(date)"
          echo "📦 Repository: ${{ github.repository }}"
          echo "👤 Triggered by: ${{ github.actor }}"
```

## github.com 리파지토리에서 로컬 리파지토리에 프로젝트 복제하기
* C:/Users/Admin/docker_projects/ 안에서 파이썬 가상환경 생성 : python -m venv venv
* venv 디렉토리 안에서, scripts\\activate : 가상환경 활성화
* git config --global user.email "cwiskykim@gmail.com"
* git config --global user.name "cwisky"
* git init  # 로컬 리파지토리 초기화
* git clone https://github.com/cwisky/MyCode.git
* cd mycode
* 복제된 리파지토리 안에서 아래의 파일들을 새로 생성

## [2단계] WSL 또는 VSCode에서 Python + Docker 프로젝트 작성  
* 필요한 모듈 설치
* 도커 이미지에 포함될 모듈 목록인 requirements.txt 파일 생성
* pip freeze > requirements.txt
* app.py 생성, 임의의 코드 추가 및 저장

## Docker와 무관하게 로컬 리파지토리의 app.py 파일을 업로드하여 github actions 반응 테스트
* 아래처럼 push 하면 github actions의 워크플로우가 실행되고 그 결과 yml에 정의된 로그가 확인되어야 함
* git add app.py
* git status
* git commit -m "github actions 워크플로우 작동 테스트"
* git push -u origin main   # 이때 로그인을 요구하면 따른다

## github actions 에서 위의 push명령에 반응하여 워크플로우가 실행되었는지 확인
* github에서 mycode 리파지토리 Actions 누르고 log_only.yml에 정의된 로그가 기록되었는지 확인


# 로컬 리파지토리에서 push 명령으로 github actions의 워크플로우에 따라 도커 이미지가 생성되지 확인
1. 로컬 리파지토리에서 도커 이미지를 생성하고 실행하여 문제가 없는 경우에 코드를 push하여 yml에 의해 도커 이미지가 생성되는지 확인
2. 로컬 리파지토리에서 도커 이미지를 생성하려면 Dockerfile 이 필요함
3. github actions에서도 도커 이미지를 생성하려면 Dockerfile이 필요하므로 git add 할 때 포함되어야 함
4. github actions에서 도커 이미지를 생성할 수 있도록 워크플로우를 yml 에 정의해야 함

## 작성된 프로그램을 도커 이미지로 생성하여 로컬 도커에서 실행 테스트
📁 예시 프로젝트 구조  
```text
MyCode/
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
* Dockerfile (실행할 코드, 모듈, 환경 및 실행 방법 정의)
```docker
FROM python:3.10-slim

WORKDIR /app
COPY . .
#COPY app.py .
#COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt   # --no-cache-dir:설치 후 바로 삭제함, -r : requirement의 약자

CMD ["python", "app.py"]
```
* 로컬에서 도커 이미지 생성 및 컨테이너에서 이미지 실행 테스트
```docker
docker build -t python-test-app .  # 현재 디렉토리에 있는 Makefile를 사용하여 이미지 생성
docker images   # image 생성 확인

# 1. 컨테이너를 실행하면서 컨테이너 이름 지정
docker run --name mylogtest python-test-app

# 2. 컨테이너에서 호스트로 파일 복사
docker cp mylogtest:/app/log.txt ./log.txt   # mylogtest컨테이너의 app/log.txt 파일을 현재 디렉토리의 log.txt에 복사

cat log.txt    # 현재 디렉토리에 복사된 log.txt 파일 내용 표시
```

## [3단계] GitHub 리파지토리에 프로젝트 업로드 및 github actions에 의해 도커 이미지 생성 테스트
* 로컬 도커에서 이미지로 생성된 프로그램을 실행했을 때 문제가 없다면 코드를 push하여 github actions가 이미지를 생성(빌드)하도록 한다
* .github/workflows/image_build.yml
```yml
name: Build and Push Docker Image

on:
  push:
    branches:
      - main  # main 브랜치에 push될 때 실행

permissions:
  contents: read
  packages: write

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v3

      - name: Log in to GitHub Container Registry
        uses: docker/login-action@v2
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Build and Push Docker Image
        run: |
          IMAGE_NAME=ghcr.io/${{ github.repository }}:latest
          docker build -t $IMAGE_NAME .
          docker push $IMAGE_NAME
```
* 아래와 같이 로컬 리파지토리에서 push 하여 위의 워크플로우에서 의해 도커 이미지가 생성되는지 확인
```docker
git init
git remote add origin https://github.com/cwisky/MyCode.git   # 이미 등록되었다면 오류발생
git remote -v   # 현재 설정된 remote origin의 주소를 확인
#git add .    # 다수개의 파일 선택시, git add 파일1.py 파일2.html 파일3.txt
git add app.py Dockerfile requirements.txt
git commit -m "Commit to test the build"
git push -u origin main
```

## Github Actions에 의해 GHCR에 생성된 도커 이미지 확인
* 해당 코드 리파지토리 선택 / 화면 오른쪽 컬럼에서 아래쪽 Packages 섹션 확인

## 처음 push 할 때 표시되는 인증창 처리(GitHub Sign in)
* git push -u origin main 처음 명령에 아래의 로그인 창이 표시됨
* Browser/Device 선택 vs Token
* [Sign in with your browser]클릭 vs [Sign in with a code]
* Username or email address :
* Password :
* [Sign in]
* Two factor Authetication Send Message
* 폰에 받은 인증 코드를 브라우저에 입력
* Authentication Succeeded
* You may now close this tab and return to the application.
* github.com 해당 리파지토리에 프로젝트가 로드되어 있는지 확인
* 이 때 이용자의 아이디, 암호를 입력하여 인증을 통과하면 "윈도우 자격증명"에는 아이디와 github에서 발급한 인증토큰이 저장되어 이후의 git 명령에 자동으로 사용됨

## [4단계] AWS EC2 서버 준비
* 설정요약

| 항목        | 설명                                    |
| --------- | ------------------------------------- |
| OS        | Ubuntu 22.04 추천                       |
| 공개키 등록    | GitHub Actions에서 접속할 수 있도록 SSH 공개키 등록 |
| 보안그룹      | 포트 22 (SSH), 80, 443 열기               |
| Docker 설치 | 아래 명령 실행                              |
```bash
sudo apt update
sudo apt install -y docker.io
sudo usermod -aG docker ubuntu
newgrp docker
```
* 설치된 Docker 테스트
```docker
docker run hello-world
```

## [5단계] GitHub Actions 워크플로우 설정  
* .github/workflows/log_only.yml
```yml
name: Log only when pushed

on:
  push:
    branches:
      - main  # 또는 'master' 등 사용 중인 브랜치 이름

jobs:
  log-job:
    runs-on: ubuntu-latest

    steps:
      - name: Show simple log
        run: |
          echo "✅ GitHub Actions workflow triggered!"
          echo "🕒 Timestamp: $(date)"
          echo "📦 Repository: ${{ github.repository }}"
          echo "👤 Triggered by: ${{ github.actor }}"
```

📁 .github/workflows/deploy.yml  
```yml
name: Deploy to EC2

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Copy files to EC2 via SCP
        uses: appleboy/scp-action@v0.1.4
        with:
          host: ${{ secrets.EC2_HOST }}
          username: ubuntu
          key: ${{ secrets.EC2_SSH_KEY }}
          source: "."
          target: "~/python-app"

      - name: Run Docker on EC2 via SSH
        uses: appleboy/ssh-action@v1.0.0
        with:
          host: ${{ secrets.EC2_HOST }}
          username: ubuntu
          key: ${{ secrets.EC2_SSH_KEY }}
          script: |
            cd ~/python-app
            docker build -t python-test-app .
            docker run --rm python-test-app
            cat log.txt
```
📌 GitHub Secrets 설정  
* GitHub 저장소 > Settings > Secrets and variables > Actions > New Repository secret

| 이름            | 값                                     |
| ------------- | ------------------------------------- |
| `EC2_HOST`    | EC2 퍼블릭 IP                            |
| `EC2_SSH_KEY` | EC2에 등록된 개인키 (ex: `~/.ssh/id_rsa` 내용) |

## [6단계] 테스트 및 확인  
▶️ 코드 푸시  
```bash
git add .
git commit -m "배포 테스트"
git push
```
▶️ GitHub → Actions → 워크플로우 > yml 파일명(deploy) > 실행 확인  
* 로그에 다음이 나오면 성공:  ✅ 프로그램 실행됨: 2025-05-17 08:10:00

# 각 팀원의 push내역을 파일에 기록하고 리파지토리에 반영하는 yml 예
```yml
name: Log Commits

on:
  push:
    branches:
      - main

permissions:
  contents: write   # write는 읽고 쓰기 포함
  packages: write

jobs:
  log-commit-info:
    if: "!contains(github.event.head_commit.message, '[bot]')"  # 반복 방지 조건
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Git user
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions@github.com"

      - name: Extract commit info
        run: |
          echo "==== New Push ====" >> commit-log.txt
          echo "Time: $(date '+%Y-%m-%d %H:%M:%S')" >> commit-log.txt
          git log -1 --pretty=format:"Author: %an%nMessage: %s%nCommit: %H%n" >> commit-log.txt
          echo "" >> commit-log.txt

      - name: Commit and push log file
        run: |
          git add commit-log.txt
          git commit -m "Update commit-log.txt [bot]" || echo "No changes to commit"
          git push
```

## 셸 스크립트의 || 연산자의 작동 방식
* '||' 왼쪽의 명령이 실패하면 오른쪽 명령이 실행된다
* git commit 명령은 아무런 변경이 없는 내용을 commit 하려고 하면 exit(1)으로 종료하면서 실패를 나타낸다
```yml
git commit -m "message" || echo "No changes to commit"
```

## 위의 코드에서 사용된 서식 문자열 속의 변환 문자 해석 (포맷 코드)
| 포맷 코드       | 의미                                |
| ----------- | --------------------------------- |
| `Author: `  | 문자열 (출력에 그대로 나타남)                 |
| `%an`       | Author Name – 커밋 작성자의 이름          |
| `%n`        | 줄바꿈 (new line)                    |
| `Message: ` | 문자열 (커밋 메시지 앞에 붙이는 라벨)            |
| `%s`        | Subject – 커밋 메시지 제목 (첫 줄)         |
| `Commit: `  | 문자열 (커밋 해시 앞에 붙이는 라벨)             |
| `%H`        | Commit Hash – 전체 40자리 SHA-1 커밋 ID |

## 리파지토리 안에 있는 README.md 파일의 한단에 각 개발자의 push 이력을 추가하는 예
```yml
name: Append Push Info to README

on:
  push:
    branches:
      - main  # 또는 dev 등 원하는 브랜치

permissions:
  contents: write

jobs:
  update-readme-log:
    if: "!contains(github.event.head_commit.message, '[bot]')"  # 반복 방지
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Configure Git identity
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions@github.com"

      - name: Append commit info to README.md
        run: |
          echo -e "\n### 📝 Commit Log\n" >> README.md   # escape 문자 해석 요청
          echo "**Author:** $(git log -1 --pretty=format:'%an')" >> README.md    # git log --> 문자열 출력
          echo "**Message:** $(git log -1 --pretty=format:'%s')" >> README.md
          echo "**Commit:** $(git log -1 --pretty=format:'%H')" >> README.md
          echo "**Date:** $(date '+%Y-%m-%d %H:%M:%S')" >> README.md      # +는 기본 출력 대신 내가 지정한 형식을 사용해 출력하라는 의미
          echo "" >> README.md

      - name: Commit and push changes
        run: |
          git add README.md
          git commit -m "Update README with commit info [bot]" || echo "No changes"
          git push
```
