l1=["Hello",12,2.3,False] #list store any datatype
l2=[2,56,23,4,12,43,7,8]
print(l2) #print list using print() function
print(l2[3]) #print list element at index 3
l2[0]=20 #update list element at index 0 position
print(l2)

#list slicing
fruits=["Apple","Orange","Banana","Grapes","Avacado","Mango","Water-melon","Orange"]
print(fruits[0:4]) #print list start from index 0 to 3
print(fruits[:6]) #print list from index 5
print(fruits[0:4:2]) #skipping list

#list methods

#index methods
list_fruits=fruits.index("Apple") #return list element index position "apple"
print(list_fruits)
 
fruits.index[0:4]
fruits.index[:5]  

#append methods -add single element to end of list
fruits.append("Onion")
print(fruits)

#count methods - return count of an element in list
count_orange=fruits.count("Orange")
print(count_orange)

#extend methods - adds iterable elements to end of list.
fruits.extend(("Potato","Honey"))
print(fruits)

#insert methods -insert element to list at given index.
fruits.insert(1,"Kiwi")
print(fruits)

#pop elements - remove element to list at given index.
fruits.pop(1)
print(fruits)

#remove methods- remove first item from list that has given value
fruits.remove("Potato")
print(fruits)

#reverse methods -reverse the list
fruits.reverse()
print(fruits)

#sort methods -sort elements of a list
fruits.sort()
print(fruits)