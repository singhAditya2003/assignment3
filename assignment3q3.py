# assignment3print("\nQuestion 3")

#input list
list1=list(map(int,input("enter the numbers separated by space:").split()))
#blank list
list2=[]
for e in list1:
    t=(e,e*e)
    list2.append(t)
#printing the final result
print("\nList containing(n,n^2) is shown below:")
print(list2)
