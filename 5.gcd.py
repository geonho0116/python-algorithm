#최대공약수 구하기
#입력 : a, b
#출력 : a와 b의 최대공약수

def gcd(a,b):
    i = min(a,b)
    while True:
        if a%i==0 and b%i==0:
            return i
        i = i-1

print(gcd(1,5))
print(gcd(3,6))
print(gcd(60,24))
print(gcd(81,27))

#유클리드 방식의 최대공약수 구하기

def gcd1(a,b):
    if b==0:
        return a
    return gcd1(b,a%b)  #재귀호출이용

print(gcd1(1,5))
print(gcd1(3,6))
print(gcd1(60,24))
print(gcd1(81,27)) 