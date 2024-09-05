for x in range(15):
    score: int = int(input(" Enter your score: "))
    if 0 <= score <= 40:
        print("try harder next time…")
    elif 41 <= score <= 60:
        print("you're getting there, need some more work")
    elif 61 <= score <= 80:
        print("pretty good")
    elif 81 <= score <= 95:
        print("awesome!")
    elif 96 <= score <= 100:
        print("excellent!!! You're a Star!")
    elif 100 < score or score < 0:
        print("illegal grade")