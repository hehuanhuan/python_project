a = 'abca'
b='a1234'
c=a+b
print(c.find('4'))
list1=c.split('c')
list2=[1,2,1,1,1]
list1.extend(list2)
print(list1)
i=1
try:
    if i==1:
        for i in range(10):
            print(i)
    elif i==2:
            print(i+1)
except:
    print('sorry,input error')

list1=[1,2,3,45]
list2=list1
print(list2)