from datetime import datetime

with open("log.txt", "a") as f:
    f.write(f"✅ 프로그램 실행됨: {datetime.now()}\n")
print("작업 완료")
