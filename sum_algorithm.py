#1부터 n까지 연속한 숫자의 합을 구하는 알고리즘1
#입력 : n
#출력 : 1부터 n까지의 숫자를 더한 값

def sum_n(n):
    s=0 #합을 계산할 변수
    for i in range(1,n+1): #1부터 n까지 반복(n+1은 제외)
        s = s+i
        return s

print(sum_n(10))
print(sum_n(100))

#1부터 n까지 연속한 숫자의 합을 구하는 알고리즘2
#입력 : n
#출력 : 1부터 n까지의 숫자를 더한 값

def sum_n2(n):
    return n*(n+1)/2

print(sum_n2(10))
print(sum_n2(100))

#1부터 n까지 연속한 숫자의 제곱의 합을 구하는 알고리즘
def sum_pow(n):
    s=0
    for i in range(1,n+1):
        s=s+i*i
        return s

print(sum_pow(10))
print(sum_pow(100))

