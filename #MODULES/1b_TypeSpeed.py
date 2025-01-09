import time as t, matplotlib.pyplot as plt

times = []
mistakes = 0
lst = ['Hello', 'Resources', 'Making']

print("This program will help you type faster !\nYou have to type 'Programming' as fast as you can for five times")
input("\nPress Enter to continue")

while len(times) < 5:
    start = t.time()               # starting time stamp
    word = input("Type : ")
    end = t.time()                 # end time stamp
    time_elapsed = end - start     # time taken to type a word
    times.append(time_elapsed)

    if word.lower() != 'programming': mistakes+=1

print("You made " + str(mistakes) + " mistake(s)")

print("Now let's see your evoulution chart ! ")

t.sleep(3)   # wait for 3s so that user can read the lines first

x = [1, 2, 3, 4, 5]
plt.plot(x, times)

legends = ['1', '2', '3', '4', '5']  # so that 1.5 2.5 do not appear on the axis
plt.xticks(x,legends)
plt.xlabel("Attempts")
plt.ylabel('Time in seconds')
plt.title('Your typing evolution')
plt.show()

