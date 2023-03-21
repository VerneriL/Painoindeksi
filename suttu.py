import datetime
import json

# year = 2023
# month = 3
# day = 17
# date = datetime.datetime(year, month, day)
# print(date)

# current = datetime.datetime.now()
# print(current)



# kesto = time_diff('10:00:00', '14:30:00')
# print(kesto)

jumppari_lista = []

jumppari = {'nimi': 'Erkki', 'Pituus': 171, 'Paino': 75.5}
jumppari_2 = {'nimi': 'Essi', 'Pituus': 165, 'Paino': 61.2}
jumppari_lista.append(jumppari)
jumppari_lista.append(jumppari_2)
print(jumppari_lista)

# json_jumppari = json.dumps(jumppari)

# print(json_jumppari)

# # file_to_use = open('kuntoilijat.json', 'x')
# # file_to_use.close()

# file_to_use = open('kuntoilijat.json', 'w')
# json.dump(jumppari, file_to_use)
# file_to_use.close()

# with open('kuntoilijat.json', 'r') as file_to_use:
#     data = json.load(file_to_use)
#     print(data)

# with open('kuntoilijat.json', 'a') as file_to_use:
#     json.dump(jumppari_2, file_to_use)

with open('kuntoilijat.json', 'w') as file_to_use:
    json.dump(jumppari_lista, file_to_use, indent=4)

with open('kuntoilijat.json', 'r') as file_to_use:
    read_data = json.load(file_to_use)
    last_data = read_data.pop()
    print(last_data)