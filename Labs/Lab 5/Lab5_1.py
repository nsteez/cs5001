"""
Netti Welsh
Fall 2020 CS5001
Problem 1: Scores
"""

#def empty_list(scores):
#    if len(scores) == 0:
#        return "No Values"

def average(scores,length):
    if length == 0:
        return "No values"

    else:
        length = len(scores)
        total = 0
        for i in scores:
            total += i
        return total / length


def median(scores,length):
    if length == 0:
        return "No values"
    else:
        scores.sort()
        #length = len(scores)
        if  length%2==1:
            return scores[length //2] #floor division
        else:
            i = length //2
            return (scores[i -1] + scores[i]) /2


def lowest_score(scores,length):
    if length ==0:
        return "No values"
    else:
        scores.sort()
        return scores[0]


def highest_score(scores,length):
    if length ==0:
        return "No values"
    else:
        scores.sort()
        return scores[-1]


def main():
    scores = []


    while True:
        user_input= input("Enter a score: ")
        if user_input == "quit":

            break
        else:
            scores.append(int(user_input))
    print(scores)
    length = len(scores)

    print("The average score is: ", average(scores,length))
    print("The median score is: ", median(scores,length))
    print("The lowest score is: ", lowest_score(scores,length))
    print("The highest score is: ", highest_score(scores,length))


if __name__ == "__main__":
    main()