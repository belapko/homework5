file = open(file= 'podschet.txt', encoding='UTF-8', mode = 'r')
cont = file.readlines()
print(f"Кол-во строк = {len(cont)} ")
for i in range(len(cont)):
    print(f"Кол-во символов в {i+1} строке = {len(cont[i])}")