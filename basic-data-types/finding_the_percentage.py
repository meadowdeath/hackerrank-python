if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    chosen_student = student_marks[query_name]

    average = sum(chosen_student) /len(chosen_student)

    print(average)
