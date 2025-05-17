# CI/CD (Docker, Github Actions, AWS)
* Windows → WSL2 + Docker → Python 앱 개발 → GitHub 업로드 → GitHub Actions로 EC2에 배포 → 실행 로그 기록

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
* 설치된 WSL 배포판 목록(Ubuntu 등)이 표시됨  
→ 여기서 Ubuntu 옆에 있는 스위치(✔️) 를 켜면 통합 활성화됨
* 설정 저장 후 Docker Desktop 재시작 권장

## 
