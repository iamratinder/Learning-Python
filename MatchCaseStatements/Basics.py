# A match statement will compare a given variable's value to diffrent shapes, also refferred to as the pattern
# The main idea is to keep on comparing the variable with all the present patterns until it fits into one.
# The match case consists of three main elements :-
# 1. The match keyword
# 2. One or more case clauses
# 3. Expression for each case
x = int(input("Enter the value of x : "))
match x:
    case 1:
        print("MONDAY")
    case 2:
        print("TUESDAY")
    case 3 if x!=90:           # can be merged with if..else
        print("WEDNESDAY")
    case _ if x == 4:
        print("This is default case for x = 4")
    case _:
        print("This is the all default case")