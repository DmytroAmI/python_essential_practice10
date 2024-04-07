import re


def is_correct_date(date):
    """Check the date format is correct"""
    if re.match(r"\d{4}[-|\s]\d{1,2}[-|\s]\d{1,2}", date):
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_correct_date('2024-04-07'))
    print(is_correct_date('2024 04 07'))
    print(is_correct_date('2024 4 7'))
    print(is_correct_date('2024-4-7'))
    print(is_correct_date('20240704'))
