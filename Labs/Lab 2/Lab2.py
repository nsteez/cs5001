"""
Netti Welsh
CS 5002 Fall2020 - Lab2
This program
"""
def main():
    SUV = "Ford Explorer"
    sedan = " Toyota Corrolla"
    sports_car = "BMW 53248i" 
    possible_answers = ["A", "B", "C"]
    Suv_options = ["B B B", "B A B", "B A C", "B A A", "B C C", "B B A", "B C A", "B B C", "B C B"]
    sedan_options = ["A A A", "A A B", "A A C", "A B A", "A B B", "A B C", "A C A", "A C B", "A C C"]
    sports_car_options = ["C C C", "C A A", "C A B", "C B B" ,"C C A", "C B A", "C A C", "C B C", "C C B"]

    print("Tell us your favorite hobbies/sports and we'll tell you your future car")


    print("Question 1: Which outdoor activity do you like most? ")
    Question_1 = input("A: Gardening   B: Biking/Hiking  C: Water sports ").upper()
    if Question_1 not in possible_answers:
        Question_1 == "A"
    print("Question 2: Which indoor activity")
    Question_2 = input("A: Cooking/Baking   B: Netflix/Youtube  C: Video Games").upper()
    if Question_2 not in possible_answers:
        Question_2 == "A"
    print("Question 3: Which activity do you like most?")
    Question_3 = input("A: Reading/Writing  B: Exercising/Dancing  C: Studying for Align").upper()
    if Question_3 not in possible_answers:
        Question_3 == "A"

    answer = Question_1 + " " + Question_2 +" " + Question_3

    if answer in Suv_options:
        print("Your future car is " + SUV)
    elif answer in sedan_options:
        print("Your future car is " + sedan)
    else:
        print("Your future car is " + sports_car)    

if __name__ == "__main__":
  main()









