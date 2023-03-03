# MODULE FOR ASKING QUESTIONS FROM CONSOLE AND CONVERTING ANSWERS

# LIBRARIES AND MODULES
import kuntoilija
# CLASS DEFINITIONS
class Question:
    """A class containing methods to ask questions on console and convert answers to various datatypes.
    """
    def __init__(self, input_msg):
        self.input_msg = input_msg

    

    def get_input_float(self, loop=True) -> tuple:
        """Convert input to float
        Args:
            is_name (bool, optional): Is input a name. Defaults to False.
            loop (bool, optional): Loop until proper input. Defaults to True.
        Returns:
            tuple: (converted_value(float), error_msg(str), error_code(int), detailed_message(str))
        """
        while True:
            input_value = input(self.input_msg)
            try:
                input_float = float(input_value)
                result = (input_float, 'OK', 0, 'Conversion successful')
                return result
            except Exception as e:
                result = (0, 'Error', 1, str(e))
                print('Virhe arvossa, syötä vain lukuja.', str(e))
                if loop:
                    continue
                else:
                    return result

    def get_input_integer(self, loop=True) -> tuple:
            """Convert input to integer
            Args:
                is_name (bool, optional): Is input a name. Defaults to False.
                loop (bool, optional): Loop until proper input. Defaults to True.
            Returns:
                tuple: (converted_value(int), error_msg(str), error_code(int), detailed_message(str))
            """
            while True:
                input_value = input(self.input_msg)
                try:
                    input_float = int(input_value)
                    result = (input_float, 'OK', 0, 'Conversion successful')
                    return result
                except Exception as e:
                    result = (0, 'Error', 1, str(e))
                    print('Virhe arvossa, syötä vain lukuja.', str(e))
                    if loop:
                        continue
                    else:
                        return result

    def get_input_boolean(self, true_value, false_value, loop=True) -> tuple:
        """_summary_
        Args:
            true_value (bool): value to use as True
            false_value (bool): value to use as False
            loop (bool, optional): Defaults to True.
        Returns:
            tuple: (converted_value(bool), error_msg(str), error_code(int), detailed_message(str))
        """
        prompt = f'{self.input_msg}, vastaa {true_value}/{false_value}: '
        while True:
            input_value = input(prompt).lower()
            if input_value == true_value.lower():
                input_bool = True
                result = (input_bool, 'OK', 0, 'Conversion successful')
                return result
            elif input_value == false_value.lower():
                input_bool = False
                result = (input_bool, 'OK', 0, 'Conversion successful')
                return result
            else:
                print('Virhe arvossa, tarkista syöte.')
                result = ('N/A,', 'Error', 1, 'Unable to convert to boolean')
                if loop:
                    continue
                else:
                    return result


if __name__ == '__main__':
    # nimi_question = Question('Anna nimi').get_input_float('Anna nimi: ', True)
    # nimi = nimi_question[0]
    # nimi = input('Anna nimi: ')
    # pituus_question = Question('Anna pituus: ').get_input_float()
    # pituus = pituus_question[0]
    # paino_question = Question('Anna paino: ').get_input_float()
    # paino = paino_question[0]
    # sukupuoli_question = Question('Sukupuoli, 1 jos mies, 0 jos nainen: ').get_input_float()
    # sukupuoli = sukupuoli_question[0]
    # ika_question = Question('Anna ika: ').get_input_float()
    # ika = ika_question[0]

    # kuntoilija1 = kuntoilija.Kuntoilija(nimi, pituus, paino, ika, sukupuoli)
    # print(kuntoilija1.nimi.title(), 'Painoindeksi:', kuntoilija1.bmi)
    # kuntoilija2 = kuntoilija.Kuntoilija(nimi, pituus, paino, ika, sukupuoli)
    # print(kuntoilija2.nimi.title(), 'ja', kuntoilija2.bmi)
    # print(pituus_question)

    question = Question('Kuinka paljon painat? (kg) ')
    answer_and_error = question.get_input_float(False)
    print(answer_and_error)
    question2 = Question('Kuinka vanha olet? ')
    answer_and_error2 = question2.get_input_integer(True)
    print(answer_and_error2)
    question3 = Question('Haluatko lähteä viikonlopun viettoon? ')
    answer_and_error3 = question3.get_input_boolean('Y', 'N')
    print(answer_and_error3)