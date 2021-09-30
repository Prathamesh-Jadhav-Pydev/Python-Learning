marks1=int(input("Enter total markes of student:\n"))
marks2=int(input("Enter total markes of student:\n"))
marks3=int(input("Enter total markes of student:\n"))
if(marks1<33 or marks2<33 or marks3<33):
    print("You fail in one of the subject\n")
total=((marks1+marks2+marks3)/3)
print(total)
if(total>=90):
    print("Your grade are Ex")
elif(total>=80):
    print("Your grade are A ")
elif(total>=70):
    print("Your grade are B")
elif(total>=60):
    print("Your grade are C ")
elif(total>=50):
    print("Your grade are D ")
else:
    print("You are fail")