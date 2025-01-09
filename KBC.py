questions = [
    ["What is my Name ?", "Simran", "Ratan", "Ratinder", "Jaspreet", "c"],
    ["What is my birth year ?", "2003", "2004", "2005", "2006", "c"],
    ["What does CSS stand for in the context of web development?", "Counter Style Sheets", "Computer Style Sheets", "Cascading Style Sheets", "Centralized Style Sheets", "c"],
    ["How many seconds make one hour ?", "3700", "3600", "4800", "2800", "b"],
    ["What is the pH value of the human body ?", "9.2 to 9.8", "7.0 to 7.8", "6.1 to 6.3", "5.4 to 5.6", "b"],
    ["What is my Father's name ?", "Jaspreet Singh", "Sarbjeet Singh", "Manjeet Singh", "Manmohan Singh", "b"],
    ["What is my Mother's name ?", "Jaspreet Kaur", "Simranjeet Kaur", "Inderpreet Kaur", "Gurjeet Kaur", "a"],
    ["Which of the following Himalayan regions is called \"Shivalik\'s\" ?", "Upper Himalayas", "Lower Himalayas", "Outer Himalayas", "Inner Himalayas", "c"],
    ["What is my Grandpa's name ?", "Jagtar Singh", "Harmanpreet Singh", "Gurjeet Singh", "Manmohan Singh", "d"],
    ["What is my Grandma's name ?", "Harleen Kaur", "Jasleen Kaur", "Gurjeet Kaur", "Manpreet Kaur", "c"],
    ["How am I ?", "tenu pta hou", "Theek Thak", "Soch ke dsu", "shi ans eh hai", "d"],
]
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000]
money = 0
x = input("Press enter to continue")
for i in range(len(questions)) :
    ques = questions[i]
    print(f"Question for ₹ {levels[i]} :-")     ; print()
    print("👉",ques[0])
    print(f"a. {ques[1]}")
    print(f"b. {ques[2]}")
    print(f"c. {ques[3]}")
    print(f"d. {ques[4]}")                       ; print()
    a = (input("Enter your answer : "))
    if a.lower()==ques[-1]:
        print("\aWoho!!! CORRECT ANSWER 🤩🥳🥳")
        money = levels[i]
    else :
        print("WRONG ANSWER !!! 😭😭😭😭")
        break
    print()
    print('─'*80)

print('─'*80)
print(f"You have won 👀 :\n₹ {money} 🫡\n\n😲😊🤩😁\n(pr Pta ni kon dau 🙄!!! 😉😂🤣 )")

print('─'*80)

    

    
