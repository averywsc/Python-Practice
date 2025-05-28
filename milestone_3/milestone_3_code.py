print("Welcome to my Radiohead 2025 quiz")
print("Ready to see if you are a true Radiohead fan?")
name = input("What is your name? - (will not be saved) ")
ready = input("Welcome {}, ready to begin? (yes/no): ".format(name))
ready = ready.strip().lower()

score = 0

if ready == "yes":
    print("Awesome! Let's begin.\n")

    # Question 1
    q1 = input("1. What year was *OK Computer* released? ")
    if q1.strip() == "1997":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong! It was released in 1997.\n")

    # Question 2
    q2 = input("2. How many members are in Radiohead? ")
    if q2.strip() == "5":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong! There are 5 members.\n")

    # Question 3
    q3 = input("3. What is Radiohead's most streamed song? ")
    if q3.strip().lower() == "creep":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong! Their most streamed song is 'Creep'.\n")

    # Question 4
    q4 = input("4. How many studio albums do they have? ")
    if q4.strip() == "9":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong! They have 9 studio albums.\n")

    print("Quiz complete, {}! You got {}/4 correct.".format(name, score))

else:
    print("Maybe next time, {}!".format(name))
