print("hello welcome to ansh coffee shop!")
name = input("what's your name\n").lower()
menu = "black coffee: " + "$15\n" "normal coffee: " + "$3\n" + "normal coffee with sugar: " "$5\n" + "our coffee: " + "$7\n"
price = 10
if name == "ansh":
    print("what will you have today")
    print(menu)
    answer = input("what's your answer\n").lower()
    howmany = input("how many do you want\n")
    if answer == "black coffee":
     price = 0
    elif answer == "normal coffee":
     price = 0
    elif answer == "normal coffee with sugar":
     price = 0
    elif answer == "our coffee":
     price = 0
    else:
     print("sorry,we don't have that try something else")
    print("i repeat your order: " + howmany + " times " + 
    answer)
    total = int(howmany)*int(price)
    print("your total will be: $" + str(total))
    print("sounds good " + name + " you order will be ready in moments!")
    anotherother = input("do you want to place another order y/n\n").lower()
print("what will you have today")
print(menu)
answer = input("what's your answer\n").lower()
if answer == "black coffee":
     price = 15
elif answer == "normal coffee":
     price = 3
elif answer == "normal coffee with sugar":
     price = 5
elif answer == "our coffee":
     price = 7
else:
     print("sorry,we don't have that try something else")
howmany = input("how many do you want\n")
yesno = input("anything else\n").lower()
total = int(howmany)*int(price)
if yesno == "yes":
    print(menu)
    anyanswer = input("what's your answer\n").lower()
    anyhowmany = input("how many do you want\n")
    anyprice = 10
    if anyanswer == "black coffee":
     anyprice = 15
    elif anyanswer == "normal coffee":
     anyprice = 3
    elif anyanswer == "normal coffee with sugar":
     anyprice = 5
    elif anyanswer == "our coffee":
     anyprice = 7
    else:
     print("sorry,we don't have that try something else")
    anyresult = int(anyhowmany)*int(anyprice)
    anytotal = anyresult + total
    print("i repeat your order: " + howmany + " times " + answer + " and " + anyhowmany + " " + anyanswer)
    print("your total will be: $" + str(anytotal))
    print("sounds good your order will be ready in the moments")
    anotherother = input("do you want to place another order y/n\n").lower()
elif yesno == "no":
    if answer == "black coffee":
     price = 15
    elif answer == "normal coffee":
     price = 3
    elif answer == "normal coffee with sugar":
     price = 5
    elif answer == "our coffee":
     price = 7
    else:
     print("sorry,we don't have that try something else")
    total = int(howmany)*int(price)
    print("i repeat your order: " + howmany + " times " + answer)
    print("your total will be: $" + str(total))
    print("sounds good " + name + " you order will be ready in moments!")
    anotherother = input("do you want to place another order y/n\n").lower()
else:
    print("not a option")
if anotherother == "y":
    menu = "black coffee: " + "$15\n" "normal coffee: " + "$3\n" + "normal coffee with sugar: " "$5\n" + "our coffee: " + "$7\n"
    price = 10
    print("hello " + name + " welcome to my coffee shop!")
    print("what will you have today")
    print(menu)
    answer = input("what's your answer\n").lower()
    howmany = input("how many do you want\n")
    if answer == "black coffee":
     price = 15
    elif answer == "normal coffee":
     price = 3
    elif answer == "normal coffee with sugar":
     price = 5
    elif answer == "our coffee":
     price = 7
    else:
     print("sorry,we don't have that try something else")
    print("i repeat your order: " + howmany + " times " + answer)
    total = int(howmany)*int(price)
    print("your total will be: $" + str(total))
    print("sounds good " + name + " you order will be ready in moments!")
    anotherother = input("do you want to place another order y/n\n").lower()
else:
    print("thank you for coming")