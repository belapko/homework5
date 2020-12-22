import json
with open(file="task7.txt", encoding="UTF-8", mode="r+") as my_file:
    my_list = my_file.readlines()
    profit = {}
    end_avg_profit = 0
    last_list = []
    for el in my_list:
        name, firm, prof, costs = el.split()
        costs = int(costs)
        prof = int(prof)
        profit[name] = int(prof) - int(costs)
        avg_profit = prof - costs
        if avg_profit > 0:
            end_avg_profit += avg_profit
    last_list.append(profit)
    print(profit)
    end_avg_profit ={"average profit": round(end_avg_profit / len(my_list))}
    last_list.append(end_avg_profit)
    print(end_avg_profit)

with open(file="task7.json", mode="w") as file:
    new_json = json.dump(last_list, file)

