def main():
    import random
    score = float(input("Enter score: "))
    score_results = get_score_check(score)
    print(score_results)
    random_score = get_score_check(random.randint(1, 100))
    print(random_score)


def get_score_check(score_check):
    if score_check < 0 or score_check > 100:
        return "Invalid score"
    elif score_check >= 90:
        return "Excellent"
    elif score_check >= 50:
        return "Passable"
    else:
        return "Bad"


main()


