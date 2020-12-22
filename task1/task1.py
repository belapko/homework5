file = open(file= 'text.txt',encoding='UTF-8', mode= 'w')
while True:
    line = input("Введите текст для добавления его в файл: ")
    file.write(line + '\n')
    if not line:
        break

file.close()