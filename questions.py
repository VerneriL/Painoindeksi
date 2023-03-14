# MODULE FOR ASKING QUESTIONS FROM CONSOLE AND CONVERTING ANSWERS

# CLASS DEFINITIONS
class Question:
    """A class containing methods to ask questions on console and convert answers to various datatypes.
    """
    def __init__(self, input_msg):
        self.input_msg = input_msg

    @staticmethod
    def get_input_integer(input_msg, loop) -> tuple:
            """Convert input to integer
            Args:
                loop (bool, optional): Loop until proper input. Defaults to True.
            Returns:
                tuple: (converted_value(int), error_msg(str), error_code(int), detailed_message(str))
            """
            while True:
                input_value = input(input_msg)
                try:
                    input_int = int(input_value)
                    result = (input_int, 'OK', 0, 'Conversion successful')
                    return result
                except Exception as e:
                    result = (0, 'Error', 1, str(e))
                    print('Virhe arvossa, syötä vain lukuja.', str(e))
                    if loop:
                        continue
                    else:
                        return result        

    @staticmethod
    def get_input_float(input_msg, loop=True) -> tuple:
        """Convert input to float
        Args:
            loop (bool, optional): Loop until proper input. Defaults to True.
        Returns:
            tuple: (converted_value(float), error_msg(str), error_code(int), detailed_message(str))
        """
        while True:
            input_value = input(input_msg)
            try:
                input_value = input_value.replace(',', '.')
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


    @staticmethod
    def get_input_boolean(input_msg, true_value, false_value, loop=True) -> tuple:
        """_summary_
        Args:
            true_value (bool): value to use as True
            false_value (bool): value to use as False
            loop (bool, optional): Defaults to True.
        Returns:
            tuple: (converted_value(bool), error_msg(str), error_code(int), detailed_message(str))
        """
        prompt = f'{input_msg}, vastaa {true_value}/{false_value}: '
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
                
    @staticmethod
    def ask_user_dictionary(input_msg: str, dictionary: dict, loop=True) -> tuple:
        """Returns a value based on dictionary
        Args:
            question (str): Ask user question
            dictionary (dict): Possible answers in key-value-pairs
        Returns:
            tuple: (answer as correct type, error_msg(str), error_code(int), detailed_message(str))
        """
        while True:
            input_value = input(input_msg).lower()
            try:
                value = dictionary[input_value]
                result = (value, 'OK', 0,  'Conversion successful')
                return result

            except Exception as e:
                print('Virhe arvossa.', str(e))
                result = ('N/A', 'Error', 1, str(e))    
                print(result)
                if loop:
                    continue
                else:
                    return result
        
if __name__ == '__main__':

    answer_and_error = Question.get_input_float('Kuinka paljon painat? (kg) ', True)
    print(answer_and_error)
    answer_and_error = Question.get_input_integer('Kuinka vanha olet? ', True)
    print(answer_and_error)
    answer_and_error = Question.get_input_boolean('Haluatko lähteä viikonlopun viettoon? ', 'Y', 'N')
    print(answer_and_error)

    gender_dictionary = {'tyttö': 0, 'poika': 1, 'nainen': 0, 'mies': 1}
    answer_and_error = Question.ask_user_dictionary('Sukupuoli: ', gender_dictionary)
    print(answer_and_error)