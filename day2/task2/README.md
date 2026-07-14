# 라이브러리: [matplotlib](https://matplotlib.org/)(3.11.0)

그래프, 차트 등을 그릴 수 있는 라이브러리다. 눈에 들어오는 시각적 자료를 그려보고 싶어서 해당 라이브러리를 선택했다.

버전은 특정 버전을 지정한 것은 아니고 설치했을 때 최신 stable 버전인 듯하다.

---
## matplotlib 사용 방법

설치:
```
pip install matplotlib
```
(numpy랑 자주 쓰는 것 같아서 같이 설치하면 좋을 것 같다)

우선 matplotlib을 import 해준다.

numpy를 보편적으로 as np를 붙이는 것처럼 matplotlib.pyplot을 plt로 줄여서 사용하는 것 같다.
```python
import matplotlib.pyplot as plt
```

<img width="717" height="716" alt="image" src="https://github.com/user-attachments/assets/8f305a42-7f70-4a49-b40b-1ef82c61b773" />

뭘 그릴건지에 따라 다르지만 그래프를 그린다면 위 사진의 요소들을 조합하여 사용하면 된다.

ex)

선형 -> plot

점 -> catter 사용 등

그래프 색상이나 굵기, 모양 등도 지정 가능하다.

원하는 그래프는 [예제](https://matplotlib.org/stable/plot_types/index.html)에서 찾아 입맛에 맞게 수정해주면 된다.



---
예제

다항 함수 4분할 출력

```python

import matplotlib.pyplot as plt
import numpy as np


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

plt.show()

```

결과

<img width="635" height="526" alt="image" src="https://github.com/user-attachments/assets/4fe084b9-9ba3-4f26-8d5e-43d80ba5e132" />


sin함수

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 500)
y = np.sin(x)
plt.plot(x,y)

plt.show()
```
결과

<img width="626" height="510" alt="image" src="https://github.com/user-attachments/assets/1d9c2cbd-a57d-4f27-99a1-995af08a583e" />

3차원

```python
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(2)
ax = fig.add_subplot(111, projection='3d')

# ramdom값 n개 뽑기 (standard_normal(표준정규분포) 기준)
x = np.random.standard_normal(50)
y = np.random.standard_normal(50)
z = np.random.standard_normal(50)

# scatter = markers(점)
ax.scatter(x, y, z)

plt.show()
```

결과(마우스로 축 돌리기 가능)

<img width="623" height="465" alt="image" src="https://github.com/user-attachments/assets/cea1fed7-8a5d-46ca-8330-e2b554726849" />
<img width="627" height="464" alt="image" src="https://github.com/user-attachments/assets/bf1d6c03-6196-4ce1-9787-368628e04039" />


