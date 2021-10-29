# Emily Catanzariti
# CS151, Dr. Rajeev
# 10/28/2021
# Programming Assignment 3
# Program Inputs: choice of sport, rates in sports
# Program Outputs: calculations for the scores of each sport

# quarterback function
def qb_score(a, c, py, tp, i):
    rating = float((100 * (5*(c/a) + 0.25*(py/a - 3) + 20*(tp/a) + 2.375 - (25 * (i/a))) / 6))
    return rating


# quidditch function
def quidditch_score(goal, snitch):
    goal = int(goal)
    snitch = int(snitch)
    rating = (goal * 10) + snitch
    return rating


# gymnast function
def gymnast_score(score1, score2, score3, score4, score5, difficulty):
    score1 = float(score1)
    score2 = float(score2)
    score3 = float(score3)
    score4 = float(score4)
    score5 = float(score5)
    difficulty = float(difficulty)
    rating = ((score1 + score2 + score3 + score4 + score5) / 5) + difficulty
    return rating


# main function
def main():
    print("This program will ask for a choice of which sport you would like to determine the score of")
    print("The choices for the sports are a quarterback, quidditch, and gymnast")
    choice = input("Please enter which sport you would like to choose:")
    choice = choice.strip().lower()
    if choice == "quarterback":
        attempts = float(input("Please enter the number of passing attempts of your quarterback:"))
        if attempts == 0:
            print("Sorry, your quarterbacks score is 0")
        else:
            completions = float(input("Please enter the number of completions"))
            passing_yards = float(input("Please enter the number of passing yards:"))
            touchdown_passes = float(input("Please enter the number of touchdown passes:"))
            interceptions = float(input("Please enter the number of interceptions:"))
            qb_rating = qb_score(attempts, completions, passing_yards, touchdown_passes, interceptions)
            print("The rating of your quarterback is:", qb_rating)
            if qb_rating == 158.3:
                print("The quarterback you chose has a perfect passing score")
    elif choice == "quidditch":
        goal = input("Please enter how many goals your team scored:")
        choice2 = str(input("Did your team catch the snitch? Please enter yes or no:"))
        choice2 = choice2.strip().lower()
        if choice2 == "yes":
            snitch = 30
        elif choice2 == "no":
            snitch = 0
        else:
            print("Sorry, your input is invalid. The rating will be calculated without points for the snitch.")
            snitch = 0
        quidditch_rating = quidditch_score(goal, snitch)
        print("The rating of your quidditch team is:", quidditch_rating)
    elif choice == "gymnast":
        difficulty = input("Please enter the difficulty score:")
        score1 = input("Please enter the first score:")
        score2 = input("Please enter the second score:")
        score3 = input("Please enter the third score:")
        score4 = input("Please enter the fourth score:")
        score5 = input("Please enter the fifth score:")
        gymnast_rating = gymnast_score(score1, score2, score3, score4, score5, difficulty)
        print("The rating of your gymnast is:", gymnast_rating)
    else:
        print("Sorry, the choice you gave was not valid")
    print("Thank you for using this program!")


main()
