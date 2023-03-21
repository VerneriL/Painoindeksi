# BASIC USER INFORMATION
import json
import kuntoilija
import questions


name = input('Nimi: ')
date_of_weighing = input('Date (vvvv-kk-pp): ')

weight = questions.Question.get_input_float('Paino? ')[0]
height = questions.Question.get_input_float('Pituus? ')[0]
age = questions.Question.get_input_integer('Ikä? ')[0]
gender = questions.Question.get_input_integer('Sukupuoli, 1 mies, 0 nainen: ')[0]
neck = questions.Question.get_input_float('Kaulanympärys (cm): ')[0]
waist = questions.Question.get_input_float('Vyötärönympärys (cm): ')[0]

if gender == 0:
    hips = questions.Question.get_input_float('Mikä on lantionympäryksesi: ')[0]

athlete = kuntoilija.Kuntoilija(name, height, weight, age, gender, date_of_weighing)

text_to_show = f'Terve {athlete.nimi}, painoindeksisi tänään on {athlete.bmi}'
print(text_to_show)
fat_percentage = athlete.rasvaprosentti()

if gender == 1:
    usa_fat_percentage = athlete.usa_rasvaprosentti_mies(height, waist, neck)
else:
    usa_fat_percentage = athlete.usa_rasvaprosentti_nainen(
        height, waist, hips, neck)

text_to_show = f'suomalainen rasva-% on {fat_percentage} ja amerikkalainen on {usa_fat_percentage}'
print(text_to_show)

print('nimi', athlete.nimi, 'paino', athlete.paino)

with open('athlete_data.json', 'r') as file:
    athlete_data = json.load(file)
    for item in athlete_data:
        print('Paino oli:', item['paino'])

athlete_data_row = {
    'nimi': athlete.nimi, 
    'pituus': athlete.pituus, 
    'paino': athlete.paino, 
    'ika': athlete.ika, 
    'sukupuoli': athlete.sukupuoli, 
    'pvm':athlete.punnitus_paiva
}
athlete_data.append(athlete_data_row)

with open('athlete_data.json', 'w') as file:
    json.dump(athlete_data, file, indent=4)