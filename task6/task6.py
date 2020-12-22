with open(file="task6.txt", encoding="UTF-8", mode="r+") as my_file:
    subjects = {}
    for line in my_file:
        subject, hours = line.split(":")
        subject_sum = sum(map(int, "".join([i for i in hours if i == ' ' or (i >= '0' and i <= '9')]).split()))
        subjects[subject] = subject_sum
    print(subjects)
