## f-string

```python
my_name = '광현이'
my_age = 27
message = f'{my_name}는 {my_age}'
print(message)
##광현이는 27##
```

## \n 의 정확한 사용법

문자열 내부에서 줄바꿈

```python
print('안녕하세요.\n반갑습니다.')
#안녕하세요.
#반갑습니다.
```

,로 구분시 맨 뒤에 sep =’\n’

```python
my_name = '광현이'
my_age = 27
print(my_age, my_name, sep='\n')
#27
#광현이
```

## Python에서 문자열 거꾸로 인덱싱 하는 법

```python
letter = 'It is nice day to study.'
forward = letter[:]
backward_1 = letter[::-1]
backward_2 = letter[:][::-1]
print(forward)
print(backward_1)
print(backward_2)
# It is nice day to study.
# .yduts ot yad ecin si tI
# .yduts ot yad ecin si tI
```

## 형 변환

```python
my_age = 27
print(type(my_age))
#<class 'int'>
print(type(str(my_age)))
#<class 'str'>
```

## list 암기

list는 변경 가능, 시퀀스, 대괄호([])로 표기

→ 대괄호를 보면 리스트라고 생각해보자

→ 인덱싱도 대괄호를 사용, list에서 찾을 때는 [숫자], 딕셔너리에서 찾을 때는 [’key’]