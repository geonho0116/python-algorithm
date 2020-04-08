#주어진 n개의 동전 중에 가짜 동전을 찾아내는 알고리즘
#입력 : 전체 동전의 시작과 끝(0,n-1)
#출력 : 가짜 동전의 인덱스

#무게 재기 함수
#a에서 b까지에 놓인 동전과 c에서 d까지에 놓인 동전의 무게를 비교
#a에서 b까지에 놓인 동전이 가벼우면 -1리턴 c에서 d까지에 놓인 동전이 가벼우면 1 리턴
#무게가 같으면 0리턴
def weigh(a,b,c,d):
    fake=29 #가짜동전 위치의 인덱스 -> weigh함수를 사용하여 맞춘다
    if a<=fake and b>=fake:
        return -1
    if c<=fake and d>=fake:
        return 1
    return 0

#1. 두 개씩 비교하여 찾는 함수
def find_fakecoin(left,right):
    for i in range(left+1,right+1):
        #가장 왼쪽 동전과 나머지 동전을 하나씩 비교
        result=weigh(left,left,i,i)
        if result == -1:
            return left
        elif result == 1:
            return i

    return -1 #가짜가 없는 경우
    
n=30
print(find_fakecoin(0,n-1))