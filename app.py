tasks = []
print("Hello,\n"+
      "Welcome on Todoapp!!!")

option_input = ''
while option_input != 'q':

    print('(q = quit, l = list, n = new, c = complete, r = reset)')
    option_input = input("What do you want to do ?").lower()

    if option_input == 'q':
        print("Thank you for using Todoapp! See you next time")

   
