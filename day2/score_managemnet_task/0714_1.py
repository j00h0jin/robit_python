'''
잘못된 행을 건너뛰고 유효한 성적만 CSV와 JSON으로 저장한다

제출 main.py · clean_students.csv · summary.json
완료 reader / writer 사용 · FileNotFoundError / ValueError 처리
추가 구현 같은 기능을 DictReader / DictWriter로 다시 구현

students.csv
name,score
민준,85
서연,92
지우,abc
하늘,105
유진,78
# abc → 숫자 변환 실패
# 105 → 허용 범위 초과

필수 기능
1 첫 행을 header로 건너뛴다
2 score를 int로 바꾸고 0~100 범위를 검사한다
3 오류 행은 이유를 출력하고 다음 행을 계속 처리한다
4 유효 행은 clean_students.csv로 저장한다
5 인원수·평균·최고점을 summary.json으로 저장한다
'''

import csv
from pathlib import Path

path = Path('./students.csv')

if path.exists():
    with open("students.csv", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in header:
            name = row[0]
            score = int(row[1]) # str -> int
            print(name, score)

else:
    print("E")


