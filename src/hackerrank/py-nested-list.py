if __name__ == '__main__':
    names = []
    scores = []
    arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, score])
        if score not in scores:
            scores.append(score)
    scores.sort()
    for student in arr:
        if student[1] == scores[1]:
            names.append(student[0])
    names.sort()
    for name in names:
        print(name)
