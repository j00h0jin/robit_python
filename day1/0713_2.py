'''
1. 실행 시 발생하는 오류를 수정할 것
2. 배터리 값이 문자열과 정상적으로 합쳐지도록 수정할 것
3. 함수 호출마다 로그가 의도치 않게 누적되는 문제를 해결할 것
4. 수정한 이유를 설명할 것

평가 기준
- TypeError를 이해하고 수정할 수 있는가
- f-string 또는 str() 형변환을 사용할 수 있는가
- 함수의 기본값 매개변수 함정을 이해했는가
- 리스트가 mutable 자료형이라는 것을 이해했는가
- 단순히 코드를 고치는 것이 아니라 이유를 설명할 수 있는가
'''

# TypeError: can only concatenate str (not "int") to str

# 1. 실행 시 오류를 수정하는 것이므로 입력값 수정 X
# 2. battery가 int형으로 들어오는 것을 string으로 변경
# 2. add_log의 battery 값을 log라는 변수에 지정할 때 str로 강제 변형
# 3. i) 리스트 출력값에 전체 로그가 뜨는 게 문제인 건지,
# 3. ii) add_log를 새로 입력받았을 때 기존의 로그가 사라져야 하는 건지

# 3. i의 경우 return값을 logs[-1]로 변경(마지막 index만 보여주기)

# 3. ii의 경우 값 삭제 후 추가
# 3. 맨 처음 pop 시 index out of range 발생 방지를 위해 조건문 추가


def add_log(robot_name, battery, logs=[]):
    log = robot_name + " battery: " + str(battery)
    if len(logs) != 0:
        logs.pop(0)
    logs.append(log)
    return logs

print(add_log("frontbot", 80))
print(add_log("rearbot", 50))
print(add_log("armbot", 20))
