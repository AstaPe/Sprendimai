class StringUtils:
    @staticmethod
    def to_uppercase(input_string):
        return input_string.upper()

    @staticmethod
    def to_lowercase(input_string):
        return input_string.lower()

    @staticmethod
    def reverse_string(input_string):
        return input_string[::-1]


if __name__ == "__main__":
    sample_string = "Laaabas, kaip Sekasi!"

    print(StringUtils.to_uppercase(sample_string))
    print(StringUtils.to_lowercase(sample_string))
    print(StringUtils.reverse_string(sample_string))