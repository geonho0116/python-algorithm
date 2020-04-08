#쉽게 설명한 삽입 정렬
#입력:리스트a
#출력:정렬된 새 리스트

def find_ins_idx(r,v):
    for i in range(0,len(r)):
        if v<r[i]:
            return i
    return len(r)

def ins_sort(a):
    result=[]
    while a:
        value=a.pop(0)
        ins_idx=find_ins_idx(result,value)
        result.insert(ins_idx,value)
    return result

d=[2,4,5,1,3]
print(ins_sort(d))

#삽입정렬
#입력:리스트a
#출력:없음(입력으로 주어진 a를 정렬한다)

def ins_sort1(a):
    n=len(a)
    for i in range(1,n):
        key=a[i]
        j=i-1
        while j>=0 and a[j]>key:
            a[j+1]=a[j]
            j=j-1
        a[j+1]=key

d=[2,4,5,1,3]
ins_sort1(d)
print(d)
#O(n^2)