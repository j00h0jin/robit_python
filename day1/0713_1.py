'''
평가 기준
- 리스트 안의 딕셔너리 구조를 이해했는가
- 튜플 언패킹을 사용할 수 있는가
- 조건문으로 상태를 분류할 수 있는가
- 반복문으로 여러 데이터를 처리할 수 있는가
- 함수를 이용해 코드를 기능별로 나눌 수 있는가
'''

def battery(battery):
    if battery >= 60:
        return "배터리 충분"
    elif battery >=20:
        return "배터리 주의"
    elif battery>=0:
        return "충전 필요"

def status(distance):
    if distance >= 0.5:
        return "전진 가능"
    else:
        return "장애물 감지"

robot_status = [
{"name": "mobilebot", "battery": 82, "position": (1.2, 0.5), "distance": 0.8},
{"name": "drone", "battery": 18, "position": (0.3, 1.5), "distance": 0.4},
{"name": "manipulator", "battery": 45, "position": (2.0, 1.0), "distance": 1.2},
]

for i in robot_status:
    print(i["name"])
    print(f"배터리: {battery(i["battery"])}")
    print(f"위치: x={i["position"][0]},y={i["position"][1]}")
    print(f"상태: {status(i["distance"])}")
    print("\n")