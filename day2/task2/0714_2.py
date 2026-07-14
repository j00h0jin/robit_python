'''
임의의 파이썬 라이브러리를 선택해서 설치한 뒤 해당 라이브러리의 기능을 적용한 코드 작성
조건
1 pip install로 외부 라이브러리 설치
2 설치된 라이브러리의 버전 확인 및 명시
3 라이브러리를 활용한 main.py 코드 작성
4 pip freeze를 통한 requirements.txt 작성
5 실행 방법 및 코드 설명, 라이브러리의 이해에 대한 보고서 작성 (README 파일로 작성)

제출 // main.py · requirements.txt · README
추가 구현 // 라이브러리 선택 및 버전 선택에 대한 이유 등 과제의 기본 틀 안에서의 자유로운 확장 가능
'''
import matplotlib.pyplot as plt
import numpy as np

# 다항함수 그리기
def polynomialFunction():
    plt.figure(1)
    # 10 >= x >= -10
    x = np.arange(-10, 10 + 1)

    y1 = x
    y2 = pow(x, 2)
    y3 = pow(x, 3)
    y4 = pow(x, 4)
    # subplot(nrows: int, ncols: int, index: int)
    # 행, 열, index순
    # 한 화면에 여러 그래프를 따로 띄울 수 있음
    plt.subplot(2,2,1)
    plt.plot(x,y1)
    plt.subplot(2,2,2)
    plt.plot(x,y2)
    plt.subplot(2,2,3)
    plt.plot(x,y3)
    plt.subplot(2,2,4)
    plt.plot(x,y4)
    
def threeDimension():
    fig = plt.figure(2)
    ax = fig.add_subplot(111, projection='3d')

    # ramdom값 n개 뽑기 (standard_normal(표준정규분포) 기준)
    x = np.random.standard_normal(50)
    y = np.random.standard_normal(50)
    z = np.random.standard_normal(50)

    # 3차원 산점도 그리기
    ax.scatter(x, y, z)


polynomialFunction()
threeDimension()

plt.show()



