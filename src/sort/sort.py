# coding : UTF-8

def main():
    

    numbers1 = [3, 2, 4, 1, 5]
    # sorted_numbers = sorted(numbers1)
    sorted_numbers = sorted(numbers1, reverse = True)
    print(sorted_numbers)

    numbers2 = [3, 2, 4, 1, 5]
    # numbers2.sort()
    numbers2.sort(reverse = True)
    print(numbers2)

    words = ['apple', 'banana', 'cherry', 'date']
    sorted_by_length = sorted(words, key=len)
    print(sorted_by_length)  # ['date', 'apple', 'banana', 'cherry']

    # 元のリストを長さでソート（破壊的）
    words.sort(key=len)
    print(words)  # ['date', 'apple', 'banana', 'cherry']

    students = [
        {'name': 'Alice', 'score': 85},
        {'name': 'Bob',   'score': 92},
        {'name': 'Carol', 'score': 78},
        {'name': 'Dave',  'score': 92},
    ]

    # score（点数）で昇順にソート
    sorted_by_score = sorted(students, key=lambda x: x['score'])
    print(sorted_by_score)

    # scoreで降順にソート
    students.sort(key=lambda x: x['score'], reverse=True)
    print(students)

    students = [
        {'name': 'Alice', 'score': 85},
        {'name': 'Bob',   'score': 92},
        {'name': 'Carol', 'score': 78},
        {'name': 'Dave',  'score': 92},
    ]

    # 複数キーでソート（点数の降順、名前の昇順）
    sorted_students = sorted(students, key=lambda x: (-x['score'], x['name']))
    print(sorted_students)

    # ===
    def custom_key(student):
        # 点数が低いほど優先（昇順）、名前は長さの昇順
        return (student['score'], len(student['name']))

    sorted_students = sorted(students, key=custom_key)
    print(sorted_students)

if __name__ == "__main__":
    main()
