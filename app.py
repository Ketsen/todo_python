tasks = []
question = ''
print("Hello,\nWelcome on Todoapp !!!")
num = 1
while question !="q":
    print('(q = quit, l = list, n = new, c = complete, r = reset)')
    question = input("What do you want to do ?\n            ").lower()

    if question =='q':
        print("Thanks to use todoapp !\nSee you soon!!!")

    elif question =="l":
        print("Your tasks are:")
        for task in tasks:
            print("-",num,".",task)
            num +=1
        num = 1

    elif question =='n':
        new = input("Write the new task")
        tasks.append(new)

    elif question =="c":
        for task in tasks:
            print("-", num, ".", task)
            num += 1
        num = 1
        delete = int(input("Which task do you want do delete ? (write the number)"))
        tasks.remove(tasks[delete-1])

    elif question =="r":
        tasks.clear()
        print("tasks are clear")

    else:
        print("Unknow command. Back to menu.")
