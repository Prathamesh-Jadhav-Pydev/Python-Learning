mydict={
    "key":"pair",
    "river":"Ganga",
    "food":"Rice",
    "city":"Mumbai",
    "anotherdict":{"place":"Pune"},
    "list":{1,2,3,4}
}
print(mydict)
print(mydict.keys()) #Print keys present inside the dictionary
print(mydict.values()) #Print values present inside the dictionary
print(mydict["river"])

#dictionary methods 
#update method
updatedict={
    "friend":"Abc",
    "hardware":"mouse",
    "software":"msoffice"
}
mydict.update(updatedict)
print(mydict.items())

#copy methods -return copy of dictionary
# mydict_2=mydict.copy()
# print(mydict_2.items())

#get method
print(mydict.get("river")) #return value of key "river"
print(mydict["river"]) #return value of key "river"

print(mydict.get("River1")) #return none
#print(mydict["River"]) #thorws an error because you exact match key before running it.

#items method -return view object containing list of key value pairs
print(mydict.items())

#formkeys method -
print(mydict.fromkeys("river"))

#pop methods -remove element with specified key and retun it.
print(mydict.items())
print(mydict.pop("key"))
print(mydict.items())

#popitem methods - remove last inserted key value pair and return as tuple
print(mydict.popitem())
print(mydict.items())

#setdefault methods
set_default_dict=mydict.setdefault(5,"Five Number")
print(mydict.items())

#clear methods - remove all elements from dictionary
mydict.clear()
print(mydict.items())