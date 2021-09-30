# st="Hello You How Are You"
# Index Start from Zero and represent by [X]
# print(st[0]) #Print index zero position letter
# print(len(st)) #Calculate length of string
# print(st[0:4]) #O is included and 4 position exlcluded
# print(st[:4]) #same as above O is included and 4 position exlcluded
# print(st[2:]) #2 is included and run upto end position exlcluded
# print(st[0::2]) #Start from 0 And end at 4 and skip 2
#===========================================#
# st=st.index("e") #Print index position of letter "e"
# print(st)
# rindex_string=st.rindex("You")
# rindex method same as index but searches for last occurences of string
# print(rindex_string) 
#=====================1=======================#
# Capitalize Method
# st_1 = "good morning guys"
# st_2 = "hONEY"
# st_1=st_1.capitalize()
# st_2=st_2.capitalize()
# print(st_1)
# print(st_2)
#=====================2=======================#
# Convert string to lower case .More aggresive than lower
# st_3="GoOd AfTeRnOoN"
# st_3=st_3.casefold()
# print(st_3)
#=================================================#
# Find method return of value if string is found otherwsie -1 when not found 
# st_4="Apple is red and Rose are red"
# st_4=st_4.find("e") #find first "e" position not all
# print(st_4)
#=================================================#
# Count method return no of times values is in string
# st_5="Mumbai Big city in India"
# c=st_5.count("i") #case sensitive "i"
# d=st_5.count("I") #case sensitive "I"
# print(c)
# print(d)
#==================================================#
# Replace method return string where one value is replaced with another
# st_6="Mumbai Pune expreesway"
# st_6=st_6.replace("Pune","Nashik") 
# print(st_6)
#=================================================#
# Title method covert first character of each letter to capital letter
# st_7="maharashtra times"
# st_7=st_7.title()
# print(st_7)
#=================================================#
# isAplha method return true of all string character are in alphabet
# st_8="Google is best search Engine"
# st_9="SMILE"
# st_8=st_8.isalpha()
# st_9=st_9.isalpha()
# print(st_8)
# print(st_9)
#=================================================#
# isspace Method return truep if all character are whitespaces
# sti_1="      "
# sti_2="Hello"
# sti_1=sti_1.isspace()
# print(sti_1)
#=================================================#
# endswith method return true of stirng ends with value
# st_10="America"
# st_10=st_10.endswith("ica")
# print(st_10)
#=================================================#
# demo_string="Mumbai is city of dreams"
# dem_string="Mumbai"
# removeprefix method remove string without specified prefix. Only Python3.9+
# removeprefix_string=demo_string.removeprefix("Mum")
# removesuffix method remove string without specified sufffix. Only Python3.9+
# removesuffix_string=demo_string.removesuffix("ams")
# swapcase method (Lowercase to uppercase and vice versa)
# swapcase_string=demo_string.swapcase()
# rjust method return string right specified
# rjust_str=dem_string.rjust(20,".")
# ljust method return string left specified
# ljust_str=dem_string.ljust(20,".")

# print(removeprefix_string)
# print(removesuffix_string)
# print(swapcase_string)
# print(rjust_str)
# print(ljust_str)

#==============================================#
#Join method iterable elements to end string
# Join_str=("Thane","Dombivali","Karjat")
# Join_str=" > ".join(Join_str)
# print(Join_str)
#=================================================#
# dummy_str="    Smith      "
# #strip method remove leading and trailing chars.
# strip_str=dummy_str.strip()
# #rstrip method same as strip but only trailing chars
# rstrip_str=dummy_str.rstrip()
# print("Hello",strip_str,"!")
# print("Hello",rstrip_str,"!")


