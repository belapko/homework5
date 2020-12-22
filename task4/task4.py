new_file = []
translated = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open(file= 'task4.txt', encoding='UTF-8', mode='r+') as my_file:
    my_list = my_file.read().split('\n')

    for i in my_list:
        i = i.split(" ", 1)
        new_file.append(translated[i[0]] +  i[1])
    print(new_file)
with open(file='task4_2.txt', encoding='UTF-8', mode='w') as newest_file:
    newest_file.writelines("%s\n" % line for line in new_file)