# def display(to_do_lst):
#     if not to_do_lst:
#         print("List is empty")
#     else:
#         for index, item in enumerate(to_do_lst, start=1):
#             print(f"{index}. {item}")

# def add(to_do_lst, new_task):
#     to_do_lst.append(new_task)

def remove(to_do_lst, serial_no_to_remove):
    if serial_no_to_remove<1 or serial_no_to_remove>len(to_do_lst):
        print("INVALID serial number")
    else:
        removed_task = to_do_lst.pop(serial_no_to_remove)
        print("New to-do list : ")
        print(f"Task {removed_task} removed from the list")


to_do_lst = []
print("Choose Your Action :-")
print("1. Display to-do list")
print("2. Add Task")
print("3. Remove Task")
print("4. Quit")
choice = int(input("\nEnter Your Choice : "))

if choice == 1:
    
    print("─"*70)
    file = open("my_tasks.txt", 'r')      # By default its 'rt' no need to mention t
    contents = file.read()
    print(contents)  
    file.close()                          ;print("─"*70)

elif choice == 2:
    print("enter 'quit' when you are finished")
    i = 1
    while(1):
        new_task = input("Enter task you want to add : ")
        if new_task.lower() == 'quit':
            break
        with open("my_task_no.txt", 'a') as f:
            f.write(f"{i}")
        f =  open('my_tasks.txt', 'a')
        f.write(f"{i}. {new_task}\n")
        # add(to_do_lst, new_task)
        i += 1
    
    
        
    # print("Added Tasks : ")
    # for index, item in enumerate(to_do_lst, start = 1):
    #     print(f"{index}. {item}")
    
elif choice == 3:
    rem = input("Enter the Serial no. of task you want to remove : ")
    remove(to_do_lst, rem+1)
elif choice == 4:
    print("Alright You are free !!")
else: 
    print("Invalid choice, Kindly enter choice 1-4")


