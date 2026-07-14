# 라이브러리: [matplotlib](https://matplotlib.org/)(3.11.0)

그래프, 차트 등을 그릴 수 있는 라이브러리다. 눈에 들어오는 시각적 자료를 그려보고 싶어서 해당 라이브러리를 선택했다.

버전은 특정 버전을 지정한 것은 아니고 설치했을 때 최신 stable 버전인 듯하다.

---
## matplotlib 사용 방법

우선 matplotlib을 import 해준다.

numpy를 보편적으로 as np를 붙이는 것처럼 matplotlib.pyplot을 plt로 줄여서 사용하는 것 같다.
```python
import matplotlib.pyplot as plt
```

<img width="717" height="716" alt="image" src="https://github.com/user-attachments/assets/8f305a42-7f70-4a49-b40b-1ef82c61b773" />



---

설치:
```
pip install matplotlib
```
(numpy랑 자주 쓰는 것 같아서 같이 설치하면 좋을 것 같다)

---
예제 (다항 함수 4분할 출력)

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

```

실행 결과

<img width="635" height="526" alt="image" src="https://github.com/user-attachments/assets/4fe084b9-9ba3-4f26-8d5e-43d80ba5e132" />
