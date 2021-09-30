fruits_tuples=("Banana","Orange","Grapes","Apple","starwberry","Orange")
#fruits_tuples[0]="Water-melon" #tuples value can't change
print(fruits_tuples)

#tuples methods

# count methods - return number of times specified value appears in tupels.
count_tuples=fruits_tuples.count("Orange")
print(count_tuples) #2 times orange in the tuples

#index methods - find first occurence of specified value. return position. raise exception if not found.
index_tuples=fruits_tuples.index("Apple")
print(index_tuples) #index position of apple is 3 