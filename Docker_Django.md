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
ENV PYTHONDONTWRITEBYTECODE 1
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

## 4단계: .dockerignore 생성 (선택 권장)
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
* Docker Desktop이 실행 중인지 확인한 후, WSL2 터미널에서:
```bash
docker build -t django-test-app .
```

## 6단계: Docker 컨테이너 실행
```bash
docker run -d -p 8000:8000 django-test-app
```

## 브라우저에서 http://localhost:8000로 접속하여 Django 웹 실행 확인
* 브라우저에서 http://localhost:8000로 접속하여 Django 웹 실행 확인

## (선택) 7단계: GitHub 연동 및 DockerHub 배포
* git init, .gitignore, git remote add
* docker tag 및 docker push 명령으로 DockerHub 배포

