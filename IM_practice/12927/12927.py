import sys
sys.stdin = open('input.txt')

arr = list(map(str, input()))  # 전구 상태 입력 ('Y' 또는 'N')

while True:
    switched = False  # 스위치를 눌렀는지 여부 확인용

    for i in range(len(arr)):
        if arr[i] == 'Y':  # 전구가 켜져 있으면
            # i+1번 스위치가 i+1의 배수인 전구들을 반전시킴
            for j in range(i, len(arr), i + 1):
                if arr[j] == 'Y':
                    arr[j] = 'N'
                else:
                    arr[j] = 'Y'
            switched = True  # 스위치를 눌렀음을 표시

    # 전구 상태가 모두 'N'이 되었으면 종료
    if all(light == 'N' for light in arr):
        break

# 결과 출력
print(arr)


