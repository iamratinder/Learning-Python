def cal_gmean(x, y):         # rules for naming a function is same as that for variables
    ans = (x*y)/(x+y)
    return ans
a = int(input("\aEnter 1st number : "))
b = int(input("Enter 2nd number : "))
result = cal_gmean(a, b)
print("The geometric mean of {} and {} is : ".format(a,b),result)

def khali_function():  # je manle hje ni body likhni tn pass krde (error ni dau)
    pass

'''NOTE : You can send any data types of arguments to a function (string, number, list,
dict etc..), and it will be treated as the same data type inside the function.
eg. if you send a list as an argument, it will still be a list when it reaches the function:-'''
def func(food):
    for i in food:
        print(i)

fruits = ["apple", "banana", "cherry"]
func(fruits)