"""
Netti Welsh
Fall 2020 CS5001
Problem 1: Scores
"""

def average(scores):
    length = len(scores)
    total = 0
    for i in scores:
        total += i
    return total / length


def median(scores):
    scores.sort()
    length = len(scores)
    if length ==0:
        return "no values"
    elif  length%2==1:
         return scores[length //2]
    else:
        i = length //2
        return (scores[i -1] + scores[i]) /2



def lowest_score(scores):
    scores.sort()
    return scores[0]

def highest_score(scores):
    scores.sort()
    return scores[-1]


def main():
    scores = [1, 2, 2, 4]
    print("The average score is: ", average(scores))
    print("The median score is: ", median(scores))
    print("The lowest score is: ", lowest_score(scores))
    print("The highest score is: ", highest_score(scores))


if __name__ == "__main__":
    main()