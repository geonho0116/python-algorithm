#거품정렬(버블소트)

def bubble_sort(a):
    n=len(a)
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a

d=[2,5,4,1,3]
print(bubble_sort(d))#O(n^2)
