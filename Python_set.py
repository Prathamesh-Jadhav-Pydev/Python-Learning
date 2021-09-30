a={1,2,3,4,5,6,7,7,8,8,9,9} #define set
print(type(a))

#define empty set
b={}
print(type(b)) #it's dictionary

c=set()
print(type(c)) #it's set



#set methods
#add() methods
c.add(1)
c.add(2)
c.add(2)
c.add(3)
c.add(3)
c.add(4)
print(c)

#copy method -return copy of a set
c1=c.copy()
print(c1)
#clear methods - remove all elements in set
c.clear()
print(c)

s1={1,2,3,4,5,6,7,8}
s2={6,7,8,9,10,11,12,13}
s3={1,2,3}

#union methods
s3=s1.union(s2)
print(s3)

#intersection methods
s3=s1.intersection(s2)
print(s3)

#issubset method
s4=s3.issubset(s1)
print(s4) #true

#issuperset method
s4=s1.issuperset(s3)
print(s4)

#intersection_update method
#print(s1.intersection_update(s3))


#isdisjoint method 
d1={2,3,4,5}
d2={6,7,8,9}
print(d1.isdisjoint(d2))

#difference method 
s4=s1.difference(s2)
print(s4)