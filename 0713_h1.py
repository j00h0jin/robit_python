'''
예시) 압축 : aaabbccccd → a3b2c4d1, 복원 : a3b2c4d1 → aaabbccccd

구현 함수
1. compress(text)
2. decompress(code)
3. is_valid_code(code)

is_valid_code
- 압축 문자열이 올바른 형식인지 검사한다.
- decompress 실행 전 검증 역할로 구현하시오
(잘못된 압축문자열 입력 시 ERROR 반환)

조건
1. 반복 횟수는 반드시 1 이상의 정수이다.
2. 반복 횟수는 두 자리 이상일 수 있다. 예: a12
3. 압축 대상 문자는 알파벳이라고 가정한다.
4. 숫자는 반복 횟수로만 사용된다.
5. decompress()는 잘못된 입력을 받으면 ERROR를 반환해야 한다.
6. 압축 결과가 원본보다 길어지면 원본을 반환한다.

출력 예시
a3b2c4d
aaabbccccd
aaaaaaaaaaaabbb
ERROR
ERROR
abcde

'''
# 많이 쓰여서 함수화
def is_alphabet(char):
    return ord('Z') >= ord(char) >= ord('A') or ord('z') >= ord(char) >= ord('a')

# 알파벳 판별 여부를 위해 ASCII코드 활용
def is_valid_code(code):
    if is_alphabet(code[0]):
        for i in range(1, len(code)):
            if code[i] == '0':
                if is_alphabet(code[i-1]):
                    return False
        return True
    else:
        return False

def compress(text):
    current = text[0]
    count = 1
    temp = ''
    for i in range(1,len(text)):
        # 이전 인덱스 문자와 현재 인덱스 문자가 동일하다면 count를 올림
        if current == text[i]:
            count = count + 1
        # 다르다면 count 값을 참고하여 1 이상이면 숫자를 표기, 1이면 그냥 표기
        # 문자가 바뀌었으므로 current를 바꾸어주고 count도 초기화
        else:
            if count > 1:
                temp = temp + current + str(count)
            else:
                temp = temp + current
            current = text[i]
            count = 1
        # 마지막 인덱스 예외처리(다음으로 비교할 인덱스 존재 X)
        if i == len(text)-1:
            if count > 1:
                temp = temp + current + str(count)
            else:
                temp = temp + current
    return temp

def decompress(code):
    if is_valid_code(code):
        current = code[0]
        count = ''
        temp = ''
        i = 1
        while i < len(code):
            current = code[i-1]
            # 문자가 연속 2개인 경우 이전 문자(current)는 숫자가 없으므로 바로 표기
            if is_alphabet(code[i]):
                temp = temp + current
            # 다음 인덱스가 알파벳이 아닌 숫자인 경우
            elif not(is_alphabet(code[i])):
                # 다음 알파벳이 오는 인덱스를 탐색
                for j in range(i, len(code)):
                    # 만약 해당 알파벳 인덱스를 찾았다면
                    if is_alphabet(code[j]):
                        # 알파벳 인덱스 사이의 숫자(형태: str)를 모두 더해줌
                        for k in range(i, j):
                            count = count + code[k]
                            # 중복 방지(숫자가 1자리 이상의 경우 여러번 탐색 방지)
                            i = j
                        temp = temp + current*int(count)
                        break
            # 마지막 인덱스 예외처리(다음으로 비교할 인덱스 존재 X)
            if i == len(code) - 1:
                # 마지막이 알파벳인 경우
                if is_alphabet(code[i]):
                    temp = temp + code[i]
                # 마지막이 숫자인 경우
                else:
                    # 마지막 인덱스부터 가장 가까운 알파벳 인덱스 탐색
                    for j in range(len(code)-1, 1, -1):
                        if is_alphabet(code[j]):
                            current = code[j]
                            # 해당 알파벳 다음 인덱스부터 숫자(형태: str) 더하기
                            for k in range(j+1, len(code)):
                                count = count + code[k]

                            temp = temp + current*int(count)
                            break
            # count 초기화
            count = ''
            i = i + 1
            
        return temp

    else:
        return "ERROR"

print(compress("aaabbccccd"))
print(decompress("a3b2c4d1"))
print(decompress("a12b3"))
print(decompress("a0"))
print(decompress("3a"))
print(compress("abcde"))

