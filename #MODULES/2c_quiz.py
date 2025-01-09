import requests, json, random, html

url = "https://opentdb.com/api.php?amount=1"
endGame = ""

score_correct = 0
score_incorrect = 0

while endGame.lower() != 'quit':
    r = requests.get(url)

    if(r.status_code != 200):
        endGame = input("***Sorry, there was a problem retrieving the question. Press enter to try again or type 'quit' to quit the game.***")  # if the user press enter than also endgame is an empty string

    else:
        valid_ans = False
        ans_number = 1 # to chek the correct ans option
        info = json.loads(r.text)
        question = info['results'][0]['question']
        answers = info['results'][0]['incorrect_answers']
        correct_ans = info['results'][0]['correct_answer']

        answers.append(correct_ans)

        random.shuffle(answers)   # so that the correct answer is not always the last option

        print(html.unescape(question) + "\n")  # to avoid html code for quotation marks and special characters

        for answer in answers:
            print(str(ans_number) + "- " + html.unescape(answer))
            ans_number += 1

        while not valid_ans:
            user_ans = input("\nType the number of the correct answer : ")
            if int(user_ans) > len(answers) or int(user_ans) < 1:
                print("Invalid Answer!")
            else:
                valid_ans = True
            try:
                user_ans = int(user_ans)
            except:
                print("Invalid answer. Use only numbers!")

        user_ans = answers[int(user_ans)-1]
        if user_ans == correct_ans:
            print("\nCongratulations! You answered correctly! The correct answer was " + html.unescape(correct_ans))
            score_correct += 1
        else:
            print("Sorry! " + html.unescape(user_ans) + " is incorrect. The correct answer is : " + html.unescape(correct_ans))
            score_incorrect += 1

        print("####################################################")
        print("Your Score is :")
        print("Correct answers : ", score_correct)
        print("Incorrect answers : ", score_incorrect)
        print("####################################################")
        endGame = input("\nPress enter to play again or type 'quit' to quit the game.")

print("\nThanks for playing!")