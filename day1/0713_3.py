'''
평가 기준
- 리스트의 메서드를 이해했는가
- 리스트의 메서드를 구현할 수 있는가
- 예외상황에 대한 처리를 할 수 있는가

append 값 // 리스트 맨 뒤에 값 추가
insert 인덱스 값 // 특정 위치에 값 추가
remove 값 // 특정 값 삭제
pop 인덱스 // 특정 위치 값 삭제
len // 리스트 길이 출력
print // 리스트 전체 출력
clear // 리스트 초기화

입력값
append apple
append banana
insert 1 orange
remove apple
print
len

고급조건
-리스트가 비어있을 때 pop을 실행하면 오류가 나지 않도록 예외처리할 것
-존재하지 않는 값을 remove하려하면 안내 메시지를 출력
-인덱스 범위를 벗어나면 안내 메시지를 출력
'''

# 인덱스 범위를 검사해야하는 경우가 2가지(insert, pop)이상이므로 함수로 관리
def index_range(index):
    if index >= len(list):
        return True
    else:
        return False

list = []

while True:
    x = input()

    if x.split()[0] == "append":
        list.append(x.split()[1])
        continue
    
    if x.split()[0] == "insert":
        if index_range(int(x.split()[1])):
            print("인덱스 범위를 벗어났음")
            continue
        list.insert(int(x.split()[1]), x.split()[2])
        continue
    
    if x.split()[0] == "remove":
        # 존재하지 않는 값을 remove했을 경우 메세지 출력
        exist = False
        for i in list:
            if str(i) == str(x.split()[1]):
                list.remove(f"{x.split()[1]}")
                exist = True
                break
        if exist == False:
            print("존재하지 않는 값")
            continue
        
    if x.split()[0] == "pop":
        if index_range(int(x.split()[1])):
            print("인덱스 범위를 벗어났음")
            continue
        # 리스트가 비어있을 때 예외처리
        if len(list) == 0:
            print("EMPTY")
            continue       
        list.pop(int(x.split()[1]))
        continue
        
    if x == "len":
        print(len(list))
        continue
    
    if x == "print":
        print(list)
        continue
    
    if x == "clear":
        list = []
        continue