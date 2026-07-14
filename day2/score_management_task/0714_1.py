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
import json
import numpy as np
from pathlib import Path

students_path = Path('.\day2\score_management_task\students.csv')
clean_students_path = Path('.\day2\score_management_task\clean_students.csv')
summary_path = Path('.\day2\score_management_task\summary.json')


def readerWriter():
    rows = []
    scores = []
    dict = {}
    
    if students_path.exists():
        with open(students_path, newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader)

            for row in reader:
                name = row[0]
                if row[1].isdecimal():
                    score = int(row[1])
                    if score >= 0 and score <=100:
                        valid_score = score
                        print(name, valid_score)
                        rows.append([name, valid_score])
                    else:
                        error = "허용 범위 초과"
                        print(error)
                else:
                    error = "숫자 변환 실패"
                    print(error)
    else:
        print("ERROR")
    
    if clean_students_path.exists():
        with open(clean_students_path, "w", newline="", encoding="utf-8")as file:
            writer = csv.writer(file)

            writer.writerow(["name", "score"])
            writer.writerows(rows)
    
    else:
        print("ERROR")
    
    for row in rows:
        scores.append(int(row[1]))
    
    mean = np.mean(scores)
    max = int(np.max(scores))

    for i in rows:
        dict = {"count": len(rows), "mean": mean, "max": max}
        
    if summary_path.exists():
        with open(summary_path, "w", encoding="utf-8") as file:
            json.dump(dict, file, indent = 2)
    
    else:
        print("ERROR")


def dictReaderWriter():
    rows = []
    scores = []
    dict = {}
    
    if students_path.exists():
        with open(students_path, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file) #

            for row in reader:
                name = row["name"]
                if row["score"].isdecimal():
                    score = int(row["score"]) #
                    if score >= 0 and score <=100:
                        valid_score = score
                        print(name, valid_score)
                        rows.append({"name": name, "score": valid_score})
                    else:
                        error = "허용 범위 초과"
                        print(error)
                else:
                    error = "숫자 변환 실패"
                    print(error)
    else:
        print("ERROR")

    if clean_students_path.exists():
        with open(clean_students_path, "w", newline="", encoding="utf-8")as file:
            writer = csv.DictWriter(file, fieldnames=["name", "score"])

            writer.writeheader
            writer.writerows(rows)
    
    else:
        print("ERROR")
    
    for row in rows:
        scores.append(int(row["score"]))
    
    mean = np.mean(scores)
    max = int(np.max(scores))
    
    for i in rows:
        dict = {"count": len(rows), "mean": mean, "max": max}
        
    if summary_path.exists():
        with open(summary_path, "w", encoding="utf-8") as file:
            json.dump(dict, file, indent = 2)
    
    else:
        print("ERROR")

readerWriter()
#dictReaderWriter()