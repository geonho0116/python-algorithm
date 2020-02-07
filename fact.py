#연속한 숫자의 곱을 구하는 알고리즘
#입력 : n
#출력 : 1부터 n까지 연속한 숫자를 곱한 값

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

print(fact(1))
print(fact(3))
print(fact(5))


def fact1(n):
    if n<=1:
        return 1
    else:
        return n*fact1(n-1)
print(fact1(1))
print(fact1(3))
print(fact1(10))
#O(n)

#재귀호출을 이용한 1부터 n까지의 합
#입력 : n
#출력 : 1부터 n까지의 합

def sum_recursive(n):
    if n<=0:
        return 0
    else:
        return n+sum_recursive(n-1)
    
print(sum_recursive(10))

#재귀호출을 이용한 최댓값 찾기
#입력 : 숫자 n개를 포함한 리스트
#출력 : 최댓값

def find_max_recursive(a,n):
    if n==1:
        return a[0]
    max_n_1 = find_max_recursive(a,n-1)
    if max_n_1 > a[n-1]:
        return max_n_1
    else:
        return a[n-1]

lista=[1,2,3,4,5,6,7,8,9]
print(find_max_recursive(lista,len(lista)))
