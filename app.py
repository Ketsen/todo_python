tasks = []
print("Hello,\n"+
      "Welcome on Todoapp!!!")

option_input = ''
while option_input != 'q':

    print('(q = quit, l = list, n = new, c = complete, r = reset)')
    option_input = input("What do you want to do ?").lower()

    if option_input == 'q':
        print("Thank you for using Todoapp! See you next time")

    elif option_input == 'l':
        print('your open tasks are:')
        for task in tasks:
            print('-'+task)

    elif option_input == 'n':
        tasks.append(input('Write your new task:'))

    elif option_input == 'c':
        to_delete =input('Which task do you want to delete ?')

        if to_delete in tasks:
            tasks.remove(to_delete)
        else:
            print("Task  unknow. Back to the menu.")

    elif option_input == 'r':
        pass

    else:
        pass