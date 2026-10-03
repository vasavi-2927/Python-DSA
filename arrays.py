a=[1,2,3,4,5]
def traversal(b):
    print('[',end="")
    for i in range(len(b)-1):
      print(b[i],end=", ")
    print(b[-1],end="]")

def insert(val,ind,b):
    c=[0 for i in range(len(b)+1)]
    for i in range(0,ind):
        c[i]=b[i]
    for i in range(ind,len(b)):
        c[i+1]=b[i]
    c[ind]=val
    return c
traversal(a)
a=insert(10,2,a)
print()
traversal(a)
a=insert(20,2,a)
print()
traversal(a)




a=[1,2,10,3,4,5]
def delete(ind,a):
    c=[0 for i in range(len(a)-1)]
    for i in range(0,ind):
        c[i]=a[i]
    for i in range(ind,len(a)-1):
        c[i]=a[i+1]
    return c
a=delete(2,a)
print(a)
a=delete(2,a)
print(a)


def delete(a,ind):
    ar=[0 for i in range(len(a)-1)]
    for i in range(ind):
        ar[i]=a[i]
    for i in range(ind+1, len(a)):
        ar[i-1]=a[i]
    return ar
a=delete(a,2)
print(a)





n=int(input())
a=list(map(str,input().split(' ')))[:n]


def palindrome(a):
  l=0
  r=len(a)-1
  for i in range(len(a)//2):
    if a[l]==a[r]:
      l+=1
      r-=1
      return 'it is palindrome'
  return 'it is not a palindrome'
print(palindrome(a))



a=[1,2,3,4,5]
def ls(val,a):
  temp=val
  c=[0 for i in range(len(a))]
  for i in range(0,len(a)-val):
      c[i]=a[val]
      val+=1
  val=temp
  j=0
  for i in range(len(a)-val,len(a)):
      c[i]=a[j]
      j+=1
  print(c)
a=ls(2,a)



a=[1,2,3,4,5]
def rs(val,a):
    temp=val
    c=[0 for i in range(len(a))]
    for i in range(0,len(a)-val):
        c[val]=a[i]
        val+=1
    val=temp
    j=0
    for i in range(len(a)-val,len(a)):
        c[j]=a[i]
        j+=1
    print(c)
a=rs(3,a)

    


a=[1,2,3,4,5]
def search(val,a):
    for i in range(len(a)):
        if a[i]==val:
            print(f"{val} is found at {i} index")
            return
    print(f"{val} is not found")
a=search(2,a)




a=[3,1,4,1,5,9,2,6]
def prefixsumarray(a):
  ar=[]
  sum=0
  for i in a:
    sum+=i
    ar.append(sum)
  return ar
print(prefixsumarray(a))




st="abcabcbb"
sub='ab'

def check(st,sub,i):
    temp=i
    for k in range(len(sub)):
        if st[i]!=st[k]:
            return-1
        i+=1
    return temp
for i in range(len(st)):
    j=0
    if sub[j]==st[i]:
        print(check(st,sub,i))
        j+=1






    a=[1,2,2,3,3,4,4,5]
def appnd(a,el):
    c=[0 for _ in range(len(a)+1)]
    for i in range(len(a)):
        c[i]=a[i]
        i+=1
    c[-1]=el
    return c
def removedup(c):
    ar=[]
    ar=appnd(ar,c[0])
    for i in range(1,len(c)):
        if c[i]!=c[i-1]:
            ar=appnd(ar,c[i])
    return ar
print(removedup(a))





a=[3,1,4,1,5,9,2,6]
def rangesumarray(a):
  ar=[]
  sum=0
  for i in a:
    sum+=i
    ar.append(sum)
  return ar
b=(rangesumarray(a))
print((b[5]-b[2-1]))




a=[-1,5,3,2,1,0,7,6]
def avgsliding(key,a):
    sum=0
    for i in range(0,key):
        sum=sum+a[i]
    maxavg=sum/key
    for i in range(key,len(a)):
        sum+=a[i]
        sum-=a[i-key]
        avg=sum/key 
        if maxavg<avg:
            maxavg=avg
    print(maxavg)
a=avgsliding(4,a)




a=[-1,5,3,2,1,0,7,6]
def avgsliding(key,a):
    sum=0
    for i in range(0,key):
        sum=sum+a[i]
    minavg=sum/key
    for i in range(key,len(a)):
        sum+=a[i]
        sum-=a[i-key]
        avg=sum/key
        if minavg>avg:
            minavg=avg
    print(minavg)
a=avgsliding(2,a)
