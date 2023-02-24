print("-------------------------------------------Welcome to my Multiplication Timetable--------------------------------------")
continue_m = True
while continue_m:
    ourNum = int(input("Which number do you want the Multiplication timetable for?:"))
    ourRange = range(1, 13)
    for x in ourRange:
        result = ourNum * x
        print(ourNum, " * ", x, "=", result)
    continue_2 = True
    while continue_2:
        proceed = input("Would you like to continue?(y/n)").lower()
        if proceed == "n":
            continue_m = False
            print('------------------------------------------------Thank you for your time-----------------------------------')
            break
        elif proceed == 'y':
            continue_m = True
            break
        else:
            print('try again')
            continue_2= True




