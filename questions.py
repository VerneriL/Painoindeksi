# MODULE FOR ASKING QUESTIONS FROM CONSOLE AND CONVERTING ANSWERS

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

    def test_fail(self):
        inp = int(input(self.input_msg))
        return inp + 1
    
if __name__ == '__main__':

    question = Question('Kuinka paljon painat? (kg) ')
    answer_and_error = question.get_input_float(False)
    print(answer_and_error)
    question2 = Question('Kuinka vanha olet? ')
    answer_and_error2 = question2.get_input_integer(True)
    print(answer_and_error2)
    question3 = Question('Haluatko lähteä viikonlopun viettoon? ')
    answer_and_error3 = question3.get_input_boolean('Y', 'N')
    print(answer_and_error3)