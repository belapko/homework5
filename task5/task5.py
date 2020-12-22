with open(file="task5.txt", encoding="UTF-8", mode="w+") as my_file:
 my_list = input("Введите числа: ").split(' ')
 my_file.writelines(my_list)
 print(f"Сумма всех чисел = {(sum((int(my_list[i]) for i in range(0, int(len(my_list))))))}")
