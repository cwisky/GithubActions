# Docker, Django Image 생성
* WSL, Docker 통합 설정된 상태에서 진행

## 1단계: Django 프로젝트 생성 (WSL2 내 Ubuntu 터미널)
```bash
# 필요한 패키지 설치
sudo apt update && sudo apt install python3-pip python3-venv

# 새 디렉토리 생성 후 진입
mkdir django_docker_project && cd django_docker_project

# 가상환경 생성 및 활성화
python3 -m venv venv
source venv/bin/activate

# Django 설치
pip install django

# Django 프로젝트 생성
django-admin startproject mysite .

# 서버 실행 확인
python manage.py runserver
```

## 위의 명령어 분석
* sudo
  + “superuser do”의 줄임말로, 관리자 권한으로 명령어를 실행할 때 사용
* apt
  + Ubuntu에서 사용하는 패키지 관리 명령어 (APT: Advanced Package Tool)
* update
  + /etc/apt/sources.list에 정의된 저장소 목록에서 최신 버전의 정보를 가져와 갱신
  + 설치되는 프로그램을 최신 상태로 유지하기 위해 반드시 먼저 실행해야 하는 단계
* &&
  + 앞의 명령어가 성공한 경우에만 뒤의 명령어를 실행
* apt install
  + apt install [패키지명1] [패키지명2] ...
* python3-pip
  + Python 3용 pip(패키지 설치 도구)
* python3-venv

## 2단계: requirements.txt 파일 생성
```bash
pip freeze > requirements.txt
```

## 3단계: Dockerfile 생성
* WSL2의 django_docker_project 폴더에 Dockerfile 생성:
```Dockerfile
# 베이스 이미지 선택
FROM python:3.10-slim

# 환경 변수 설정
ENV PYTHONDONTWRITEBYTECODE 1      # docker에 불필요한 파이썬 캐시 파일 생성 방지, 이미지 용량을 줄임
ENV PYTHONUNBUFFERED 1

# 작업 디렉토리 설정
WORKDIR /app

# 필요 파일 복사
COPY requirements.txt /app/

# 라이브러리 설치
RUN pip install --upgrade pip && pip install -r requirements.txt

# 전체 프로젝트 복사
COPY . /app/

# 포트 노출
EXPOSE 8000

# 서버 실행 명령어
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

## 위의 명령어 해석
* ENV PYTHONDONTWRITEBYTECODE 1           # docker에 불필요한 파이썬 캐시 파일 생성 방지, 이미지 용량을 줄임
* ENV PYTHONUNBUFFERED 1                  # Python의 출력 버퍼링을 비활성화, Docker 컨테이너에서 Python 로그를 실시간으로 확인
* WORKDIR /app                            # 이후 모든 경로는 /app 기준
* COPY . .                                # 현재 디렉토리의 모든 파일을 /app으로 복사
* RUN pip install -r requirements.txt     # /app 디렉토리 내에서 실행
* EXPOSE 8000                             # 애플리케이션의 서비스 포트임을 명시적으로 표시함 (문서화 목적)
  + EXPOSE만으로는 외부 접속 불가
  + 외부 접속을 원하면 docker run 시 -p 옵션 필요
  + docker run -p 8000:8000 my-django-app
  + 이 설정이면 브라우저에서 http://localhost:8000으로 접속 가능
  + 만약 -p 옵션 없이 실행하면, 포트는 열려 있지만 외부에 노출되지 않으므로 접속 불가
* CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
  + 컨테이너가 실행될 때 기본적으로 수행할 명령어
  + 컨테이너가 실행될 때 가장 마지막에 실행되는 기본 명령어를 정의
  + "0.0.0.0": 모든 IP 인터페이스에서 접속 허용
  + -p 8000:8000 my-django-app  : port forwarding, port mapping

## 4단계: .dockerignore 생성 (선택 권장)
* .dockerignore 파일에 명시된 항목들은 Docker 이미지 빌드 시 컨테이너에 포함되지 않음
```text
venv/
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
db.sqlite3
```

## 5단계: Docker 이미지 빌드
* 같은 이름의 이미지라도 태그를 다르게 해서 버전 구분할 수 있음
* latest 외에 명확한 버전을 붙이는 습관이 좋음
* Docker Desktop이 실행 중인지 확인한 후, WSL2 터미널에서:
```bash
docker build -t django-test-app .    # docker build -t [이름]:[태그] [경로], [태그]가 생략되면 자동으로 ":latest" 가 붙음
```

## 6단계: Docker 컨테이너 실행
```bash
docker run -d -p 8000:8000 django-test-app   # -d는 --detach의 줄임말로, 컨테이너를 백그라운드(Detached mode)에서 실행하라는 의미
```

## 브라우저에서 http://localhost:8000로 접속하여 Django 웹 실행 확인
* 브라우저에서 http://localhost:8000로 접속하여 Django 웹 실행 확인

## (선택) 7단계: GitHub 연동 및 DockerHub 배포
* git init, .gitignore, git remote add
* docker tag 및 docker push 명령으로 DockerHub 배포

## 도커 이미지의 파일 시스템과 내부 구조를 확인
* 이미지로부터 컨테이너 생성 후 bash로 진입, 가장 일반적이고 권장되는 방식
```bash
# 1. 이미지로부터 임시 컨테이너 생성 및 bash 실행
docker run -it --rm --entrypoint /bin/bash django-test-app
```
* -it : interactive + tty(가상 터미널) 연결
* --rm :	컨테이너가 종료되면 자동 삭제
* --entrypoint /bin/bash	기본 시작 명령(CMD)을 무시하고 /bin/bash 실행,  "echo $SHELL" 으로 셸 종류 확인 가능
* 셸 진입 후 확인 가능:
```bash
# 컨테이너 내에서
ls /
cat /app/requirements.txt
```
* cat : concatenate(연결하다, 이어붙이다), cat file1.txt file2.txt처럼 여러 파일을 한꺼번에 출력하여 이어붙임
* cat a.txt b.txt > merged.txt → 두 파일을 합쳐 새 파일로 저장

## 컨테이너 셸에서 빠져 나오려면
* exit
* Ctrl + D

