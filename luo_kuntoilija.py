# BASIC USER INFORMATION
import kuntoilija


def get_input(input_msg, is_name=False, loop=True):
    while loop:
        if is_name:
            input_value = input(input_msg)
            result = (input_value, 'OK', 0, 'Conversion successful')
            return result
        try:
            input_value = float(input(input_msg))
            result = (input_value, 'OK', 0, 'Conversion successful')
            return result
        except Exception as e:
            result = (0, 'Error', 1, str(e))
            print('Virhe arvossa, syötä vain lukuja.', str(e))

nimi_question = get_input('Anna nimi: ', True)
nimi = nimi_question[0]
pituus_question = get_input('Anna pituus: ')
pituus = pituus_question[0]
paino_question = get_input('Anna paino: ')
paino = paino_question[0]
sukupuoli_question = get_input('Sukupuoli, 1 jos mies, 0 jos nainen: ')
sukupuoli = sukupuoli_question[0]
ika_question = get_input('Anna ika: ')
ika = ika_question[0]

if __name__ == '__main__':
    kuntoilija1 = kuntoilija.Kuntoilija(nimi, pituus, paino, ika, sukupuoli)
    print(kuntoilija1.nimi.title(), 'Painoindeksi:', kuntoilija1.bmi)
    kuntoilija2 = kuntoilija.Kuntoilija(nimi, pituus, paino, ika, sukupuoli)
    print(kuntoilija2.nimi.title(), 'ja', kuntoilija2.bmi, nimi_question)