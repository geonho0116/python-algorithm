#동명이인 찾기
#입력:이름이 n개 들어 있는 리스트
#출력:이름 n개 중 반복되는 이름의 집합

def find_same_name(a):
    n=len(a) #리스트의 개수를 n에 저장
    result=set() #결과 저장을 위한 빈 집합
    for i in range(0,n-1): #0부터 n-2까지 반복
        for j in range(i+1,n): #i+1부터 n-1까지 반복
            if a[i]==a[j]:
                result.add(a[i])
    return result

name = ['tom','jerry','mike','tom'] #파이썬은 대소문자구분
print(find_same_name(name))
name2=['tom','jerry','mike','tom','jerry']
print(find_same_name(name2))
#O(n^2)

#n명 중에 두 명을 뽑아 짝을 짓는 조합의 알고리즘
#입력 : n명이 들어있는 리스트
#출력 : 튜플

def find_couple(a):
    n=len(a)
    result=[]
    for i in range(0,n-1):
        for j in range(i+1,n):
            result.append((a[i],a[j]))
    return result

name3 = ['tom','jerry','mike','paul']
print(find_couple(name3))
