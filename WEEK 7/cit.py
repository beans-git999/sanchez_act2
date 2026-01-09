citizenship = "Filipino"
age = 25
registered = True

if citizenship == "Filipino" and age >=18:
    if registered:
        print("you can vote")
    else:
        print("can't vote but you can register")
elif citizenship == "Filipino" and age <18:
    print("you can't vote, wait till 18")
else:
    print("you can't vote nor register")

