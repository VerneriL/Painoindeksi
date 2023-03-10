# BASIC USER INFORMATION
import kuntoilija
import questions


# def get_input(input_msg, is_name=False, loop=True):
#     while loop:
#         if is_name:
#             input_value = input(input_msg)
#             result = (input_value, 'OK', 0, 'Conversion successful')
#             return result
#         try:
#             input_value = float(input(input_msg))
#             result = (input_value, 'OK', 0, 'Conversion successful')
#             return result
#         except Exception as e:
#             result = (0, 'Error', 1, str(e))
#             print('Virhe arvossa, syötä vain lukuja.', str(e))

# nimi_question = get_input('Anna nimi: ', True)
# nimi = nimi_question[0]
# pituus_question = get_input('Anna pituus: ')
# pituus = pituus_question[0]
# paino_question = get_input('Anna paino: ')
# paino = paino_question[0]
# sukupuoli_question = get_input('Sukupuoli, 1 jos mies, 0 jos nainen: ')
# sukupuoli = sukupuoli_question[0]
# ika_question = get_input('Anna ika: ')
# ika = ika_question[0]

name = input('Nimi: ')

question = questions.Question('Paino? ')
weight = question.get_input_float()[0]
question = questions.Question('Pituus? ')
height = question.get_input_float()[0]
question = questions.Question('Ikä? ')
age = question.get_input_integer()[0]
question = questions.Question('Sukupuoli, 1 mies, 2 nainen: ')
gender = question.get_input_integer()[0]
question = questions.Question('Kaulanympärys (cm): ')
neck = question.get_input_float()[0]
question = questions.Question('Vyötärönympärys (cm): ')
waist = question.get_input_float()[0]

if gender == 0:
    question = questions.Question('Mikä on lantionympäryksesi: ')
    hips = question.get_input_float()[0]

athlete = kuntoilija.Kuntoilija(name, height, weight, age, gender)

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


# if __name__ == '__main__':
#     kuntoilija1 = kuntoilija.Kuntoilija(nimi, pituus, paino, ika, sukupuoli)
#     print(kuntoilija1.nimi.title(), 'Painoindeksi:', kuntoilija1.bmi)
#     kuntoilija2 = kuntoilija.Kuntoilija(nimi, pituus, paino, ika, sukupuoli)
#     print(kuntoilija2.nimi.title(), 'ja', kuntoilija2.bmi, nimi_question)