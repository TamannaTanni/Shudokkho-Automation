class EnglishToBangla:
    def __init__(self):
        # Define a dictionary to map English digits to Bangla digits
        self.number_map = {
            '0': "০", '1': "১", '2': "২", '3': "৩",
            '4': "৪", '5': "৫", '6': "৬", '7': "৭",
            '8': "৮", '9': "৯"
        }

    def translate_number(self, num):
        """
        Translates an English number into its Bangla numeral representation.
        :param num: int or str - A number to translate
        :return: str - The Bangla numeral representation
        """
        # Convert to string if the input is an integer
        num_str = str(num)

        # Validate input
        if not num_str.isdigit():
            raise ValueError("Input must be a numeric value.")

        # Translate each digit to Bangla
        bangla_number = "".join(self.number_map[digit] for digit in num_str)
        return bangla_number


    def translate_ampm(self, hour_value, ampm_value):

        """
        Translates the AM/PM into its Bangla representation.
        :param ampm_value: str; should only input AM or PM
        :return: str - The Bangla representation
        """
        ampm_value = ampm_value.upper()
        hour_value = int(hour_value)

        #validate the input and convert
        if 6 <= hour_value < 12 and ampm_value == 'AM':
            return 'সকাল'
        elif (1 <= hour_value < 4 and ampm_value == 'PM') or ( hour_value == 12 and ampm_value == 'PM'):
            return 'দুপুর'
        elif 4 <= hour_value < 6 and ampm_value == 'PM':
            return 'বিকাল'
        elif 6 <= hour_value < 8 and ampm_value == 'PM':
            return 'সন্ধ্যা'
        elif (8 <= hour_value < 12 and ampm_value == 'PM') or ( hour_value == 12 and ampm_value == 'AM') or (1 <= hour_value < 4 and ampm_value == 'AM'):
            return 'রাত'
        elif 4 <= hour_value < 6 and ampm_value == 'AM':
            return 'ভোর'
        else:
            raise ValueError("invalid time, couldn't translate")

