#리스트에서 특정 숫자의 위치 찾기
#입력 : 리스트 a, 찾는 값 x
#출력 : 찾으면 그 값의 위치, 찾지 못하면 -1

def search_list(a,x):
    n = len(a)
    for i in range(0,n):
        if x == a[i]:
            return i,a[i]
        
    return -1

v=[18,97,5,46,84,21,5948,491,545]
print(search_list(v,21))
print(search_list(v,10))
print(search_list(v,18))
