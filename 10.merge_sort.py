#쉽게 설명한 병합정렬
#입력:리스트a
#출력:정렬된 새 리스트

def merge_sort(a):
    n=len(a)
    if n<=1:
        return a
    
    mid=n//2
    print(a)
    g1=merge_sort(a[:mid])
    print(g1)
    g2=merge_sort(a[mid:])
    print(g2)
    result=[]
    while g1 and g2:
        if g1[0]<g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    return result

d=[6,8,3,9,10,1,2,4,7,5]
print(merge_sort(d))

#병합정렬
#입력:리스트a
#출력:없음(입력으로 주어진 a가 정렬된다)

def merge_sort1(a):
    n=len(a)
    if n<=1:
        return
    mid=n//2
    g1=a[:mid]
    g2=a[mid:]
    merge_sort1(g1)
    merge_sort1(g2)
    i1=0
    i2=0
    ia=0
    while i1<len(g1) and i2<len(g2):
        if g1[i1]<g2[i2]:
            a[ia]=g1[i1]
            i1+=1
            ia+=1
        else:
            a[ia]=g2[i2]
            i2+=1
            ia+=1
    while i1<len(g1):
        a[ia]=g1[i1]
        i1+=1
        ia+=1
    while i2<len(g2):
        a[ia]=g2[i2]
        i2+=1
        ia+=1

d=[6,8,3,9,10,1,2,4,7,5]
merge_sort1(d)
print(d)

#O(nlogn)