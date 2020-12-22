with open(file='sotrudniki.txt', encoding='UTF-8', mode='r') as file_read:
    surnames = file_read.readlines()
    for i in range(len(surnames)):
        print(f"{surnames[i].strip()}")

with open(file='sotrudniki.txt', encoding='UTF-8', mode='r') as file_read:
    sal = []
    all = []
    my_list = file_read.read().split('\n')
    for i in my_list:
        line = i.split()
        all.append(line[1])

        if int(line[1]) >20000:
            print(f"У {line[0]}а зарпалата больше 20000")
    # a = 0
    # for i in range(len(all)):
    #     a = all[i]
    print(f"Средняя величина дохода сотрудников = {(sum((int(all[i]) for i in range(0, int(len(all)))))) / len(all)}")







