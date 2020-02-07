#최댓값 구하기
#입력 : 숫자가 n개 들어있는 리스트
#출력 : 숫자 n개 중 최댓값

def find_max(a):
    n=len(a)
    max_v=a[0]
    for i in range(1,n):
        if max_v<a[i]:
            max_v=a[i]
    return max_v

v=[1,2,3,4,5,6,7,8,9]
print(find_max(v))
#O(n)이다. 비교는 n-1회 실행하지만 n이 굉장히 커질 때는 차이가 무의미하기 때문이다.

def find_maxidx(a):
    n=len(a)
    max_idx=0
    for i in range(1,n):
        if a[max_idx]<a[i]:
            max_idx=i
    return max_idx

v=[1,2,3,4,5,6,7,8,9]
print(find_maxidx(v))

#최솟값 구하기
def find_min(a):
    n=len(a)
    min_v=a[0]
    for i in range(1,n):
        if min_v>a[i]:
            min_v=a[i]
    return min_v

v=[1,2,3,4,5,6,7,8,9]
print(find_min(v))