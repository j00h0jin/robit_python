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
    # if 원본이 짧다면 원본 return            
    if len(text) > len(temp):
        return temp
    else:
        return text

def decompress(code):
    if is_valid_code(code):
        # is_valid_code을 통해 code[0] = 알파벳임을 신뢰한 상태로 코드 진행
        current = code[0]
        count = ''
        temp = ''
        i = 1
        
        while i < len(code):
            # 현재 인덱스가 알파벳인 경우 current를 temp에 추가
            if is_alphabet(code[i]): 
                if count != '':
                    temp = temp + current*int(count)
                else:
                    temp = temp + current
                current = code[i]
                count = ''
                i = i + 1
            # 숫자인 경우 count에 대입
            else:
                    count = count + code[i]
                    i = i + 1 
                    
            # 마지막 인덱스 예외처리
            if i == len(code) - 1:
                # 알파벳일 경우 temp에 추가
                if is_alphabet(code[i]):
                    if count != '':
                        temp = temp + current*int(count)
                    else:
                        temp = temp + current
                # 알파벳 아닐 경우
                else:
                    j = i - 1
                    while j > 1:
                        # 뒤에서 가장 가까운 알파벳 인덱스 찾아 temp 추가
                        if is_alphabet(code[j]):
                            count = ''
                            current = code[j]
                            k = j + 1
                            while k < len(code):
                                count = count + code[k]
                                k = k + 1

                            temp = temp + current*int(count)
                            break
                        j = j - 1
            
        return temp

    else:
        return "ERROR"

print(compress("aaabbccccd"))
print(decompress("a3b2c4d1"))
print(decompress("a12b3"))
print(decompress("a0"))
print(decompress("3a"))
print(compress("abcde"))

