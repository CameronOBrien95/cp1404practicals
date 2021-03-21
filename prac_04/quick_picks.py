
import random
quick_picks = []
quick_pick_lines = int(input("How many quick pick lines would you like"))
for i in range(0, quick_pick_lines):
    quick_picks.clear()
    for num in range(0, 6):
        quick_pick = random.randint(1, 46)
        if quick_pick not in quick_picks:
            quick_picks.append(quick_pick)
    print(quick_picks)






