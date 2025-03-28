from datetime import datetime
import sys
import random
import csv

def main():
    print("WELCOME!!!\nTEST YOUR TYPING SPEED HERE")
    while True:
        name = input("Enter your name: ").title().strip()
        if len(name)!=0:
            break
        else:
            print("Invalid Name")
    print("Select the number of words you want to type")

    a = word_length()
    while True:
        b = word_generator(a)
        words = " ".join(b)
        print(f"Text: {words}")
        start = input("Do you want to start your typing speed test (yes/no): ").strip()
        if start.lower()=="yes":
            t1 = str(datetime.now())
            time1= t1.split(" ")[1]
        else:
            sys.exit("You have exited the typing speed test")
        typing = input("Type here: ").split()
        typed_words = " ".join(typing)
        acc = accuracy(words,typed_words)
        if float(acc)<50:
            print("Your accuracy is less than 50")
            again = input("Do you want to restart test (yes/no): ")
            if again.lower() == "yes":
                continue
            else:
                break
        else:
            break

    t2 = str(datetime.now())
    time2 = t2.split(" ")[1]
    timedifference = time_difference(time1,time2)
    wpm = f"{float(a)/timedifference:.2f}"
    print(f"Your WPM is {wpm}")
    print(f"Your accuracy is {acc}")
    with open("score.csv","a") as file:
        writer = csv.DictWriter(file, fieldnames=["Name" , "WPM" , "Accuracy"])
        writer.writerow({"Name": name, "WPM" : wpm , "Accuracy" : acc})


def word_generator(n):
    with open("words.txt","r") as file:
        content = file.read()
    words = content.split()
    l = []
    for i in range(int(n)):
        l.append(random.choice(words))
    return l
def word_length():

    length = [10,25,50,100]
    val = 65
    for i in length:
        print(f"{chr(val)}.{i}")
        val += 1
    while True:
        try:
            selection = input("Select one of the follwing options: ").upper()
            if selection in ["A","B","C","D"]:
                break
            raise ValueError
        except ValueError:
            print("Invalid selection")
    match selection:
        case "A":
            print("You have selected 10 words")
            length = 10
        case "B":
            print("You have selected 25 words")
            length = 25
        case "C":
            print("You have selected 50 words")
            length = 50
        case "D":
            print("You have selected 100 words")
            length = 100
    return f"{length}"

def accuracy(a,b):
    count = 0
    a_list = a.split()
    b_list = b.split()
    atotal = len("".join(a_list))
    btotal = len("".join(b_list))
    if len(a_list)>=len(b_list):
        for i in range(len(a_list)):
            try:
                if len(a_list[i])>=len(b_list[i]):
                    for j in range(len(a_list[i])):
                        try:
                            if a_list[i][j]==b_list[i][j]:
                                count += 1
                        except IndexError:
                            continue
                else:
                    for j in range(len(b_list[i])):
                        try:
                            if b_list[i][j]==a_list[i][j]:
                                count += 1
                        except IndexError:
                            continue
            except IndexError:
                continue
    else:
        for i in range(len(b_list)):
            try:
                if len(a_list[i])>=len(b_list[i]):
                    for j in range(len(a_list[i])):
                        try:
                            if a_list[i][j]==b_list[i][j]:
                                count += 1
                        except IndexError:
                            continue
                else:
                    for j in range(len(b_list[i])):
                        try:
                            if b_list[i][j]==a_list[i][j]:
                                count += 1
                        except IndexError:
                            continue
            except IndexError:
                continue
    if atotal>btotal:
        maximum = atotal
    else:
        maximum = btotal
    accuracy = (count/maximum)*100
    return f"{accuracy:.2f}"


def time_difference(t1,t2):
    h1,m1,s1 = t1.split(":")
    h2,m2,s2 = t2.split(":")
    difference = (float(h2)*60 + float(m2) + float(s2)/60)-(float(h1)*60 + float(m1) + float(s1)/60)
    return difference

if __name__=="__main__":
    main()

    