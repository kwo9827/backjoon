import sys
sys.stdin = open('input.txt')


def find_cycle_length(n):
    original_n = n  # 처음 주어진 수를 저장
    count = 0  # 사이클 길이를 저장할 변수

    while True:
        count += 1
        # 10보다 작은 경우 앞에 0을 붙여 두 자리 수로 만든다
        a = n // 10  # 십의 자리
        b = n % 10  # 일의 자리
        sum_digits = a + b  # 두 자리 수의 합
        new_n = (b * 10) + (sum_digits % 10)  # 새로운 수 생성
        if new_n == original_n:  # 원래 수로 돌아오면 종료
            break
        n = new_n  # 새로운 수를 n으로 설정하고 반복

    return count


# 예시 실행
n = int(input("Enter a number: "))  # 입력 받기
cycle_length = find_cycle_length(n)
print(f"Cycle length: {cycle_length}")