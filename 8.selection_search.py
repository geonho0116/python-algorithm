#쉽게 설명한 선택정렬
#입력:리스트a
#출력:정렬된 새 리스트

def find_min_idx(a):
    n=len(a)
    min_idx=0
    for i in range(1,n):
        if a[i]<a[min_idx]:
            min_idx=i
    return min_idx

def sel_sort(a):
    result=[]
    while a:
        min_idx=find_min_idx(a)
        value=a.pop(min_idx)
        result.append(value)
    return result

d=[2,4,5,1,3]
print(sel_sort(d))

#선택정렬
#입력:리스트a
#출력:없음(입력으로 주어진 a를 정렬만 함)

def sel_sort1(a):
    n=len(a)
    for i in range(0,n-1):
        min_idx=i
        for j in range(i+1,n):
            if a[j]<a[min_idx]:
                min_idx=j
        a[i],a[min_idx]=a[min_idx],a[i]

d=[2,4,5,1,3]
sel_sort1(d)
print(d)
#O(n^2)

#reverse
def sel_sort2(a):
    n=len(a)
    for i in range(0,n-1):
        max_idx=i
        for j in range(i+1,n):
            if a[j]>a[max_idx]:
                max_idx=j
        a[i],a[max_idx]=a[max_idx],a[i]

d=[2,4,5,1,3]
sel_sort2(d)
print(d)

