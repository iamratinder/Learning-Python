# With break statement we can stop the loop before it has looped through all the items
## In short loop toh use time baahr aaju
### will skip the loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)
print()

# With the continue statement we can stop the current iteration of the loop, and continue the next iteration
## In short continue ton baad likhya code skip hoju te next iteration ton loop fr shuru hou
### will skip the iteration
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
