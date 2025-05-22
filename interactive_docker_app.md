# 도커 이미지 앱 내부에서 Interaction이 필요한 기능이 있는 경우
* 도커 이미지는 기본적으로 상호작용을 기대하지 않으므로 -it 옵션이 없으면 정상 작동하지 않음

## 이미지 실행시 -it 옵션이 필요한 경우
```python
# 1. 정수 2개를 입력받는다.
n1 = int(input('정수 1: '))
n2 = int(input('정수 2: '))

# 2. 덧셈을 한다.
result = n1 + n2

# 3. 덧셈식을 생성한다.
expression = f'{n1} + {n2} = {result}'

# 4. 덧셈식을 출력한다.
print(expression)
```
* 위의 프로그램이 도커 이미지로 만들어졌을 때 실행하려면 아래의 명령을 사용해야 한다
* docker run -it add-app  # --rm 가능
