#Write a Python program to get the largest number from a list.
l1=[1,2,3,4,5,6]
print(max(l1))

#remove the even numbers from the lost
l1=range(1,10)
l2=[]
for i in l1:
    if i%2!=0:
        l2.append(i)
print(l2)

#multiply the items in the list

l1=[1,2,3,4,5,6]
l2=1
for i in l1:
    l2*=i
print(l2)
