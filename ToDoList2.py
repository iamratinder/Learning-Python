def remove(serial_no):
    to_do_lst = []
    
    with open("my_task_no.txt", 'r') as file:
        lines = file.read().splitlines()
        n = int(lines[-1])
        file.close()

    index = 0
    with open('my_tasks.txt', 'r') as tasks:
        line = tasks.read().splitlines()
        while(index != n):
            task_ = line[index]
            to_do_lst.append(task_)
            index += 1
    to_do_lst.pop(serial_no)
    for index, item in enumerate(to_do_lst, start = 1):
        print(f"{item}")


print("Choose Your Action :-")
print("1. Display to-do list")
print("2. Add Task")
print("3. Remove Task")
print("4. Quit")
choice = int(input("\nEnter Your Choice : "))

if choice == 1:
    
    print("─"*70)
    file = open("my_tasks.txt", 'r')      
    contents = file.read()
    print(contents)  
    file.close()                          ;print("─"*70)

elif choice == 2:
    print("enter 'quit' when you are finished")
    with open("my_task_no.txt", 'r') as file:
        lines = file.read().splitlines()
        i = int(lines[-1]) + 1
        file.close()

    while(1):
        new_task = input("Enter task you want to add : ")
        if new_task.lower() == 'quit':
            break
        with open("my_task_no.txt", 'a') as f:
            f.write(f"{i}\n")
        f =  open('my_tasks.txt', 'a')
        f.write(f"{i}. {new_task}\n")
        i = i + 1
    
    
elif choice == 3:
    rem = int(input("Enter the Serial no. of task you want to remove : "))
    remove(rem-1)


elif choice == 4:
    print("Alright You are free !!")
else: 
    print("Invalid choice, Kindly enter choice 1-4")


