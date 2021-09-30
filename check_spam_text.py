text=input("Enter your comment:\n")
if "make a lot of money" in text:
    spam=True
elif "subscrine now" in text:
    spam=True
elif "watch now" in text:
    spam=True
elif "pay now" in text:
    spam=True
else:
    spam=False
if(spam):
    print("spam comment")
else:
    print("Not spam comment")
