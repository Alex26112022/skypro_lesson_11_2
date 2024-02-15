def str_upper(input_str: str = '') -> str:
    """
    Принимает на вход строку и возвращает ее со всеми заглавными буквами.
    """
    return input_str.upper()


def str_title(input_str: str = '') -> str:
    """
    Делает заглавными первые буквы каждого слова в строке, поступившей на вход.
    """
    return input_str.title()


if __name__ == '__main__':
    str_upper()
    str_title()
