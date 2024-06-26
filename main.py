calls = 0


def count_calls(func):
    def wrapper(*args, **kwargs):
        global calls
        calls += 1
        count_calls(func)
        return func(*args, **kwargs)

    return wrapper


@count_calls
def string_info(string):
    result = (len(string), string.upper(), string.lower())
    return result


@count_calls
def is_contains(string, list_strings):
    for string_in_list in list_strings:
        if string.lower() == string_in_list.lower():
            return True
    return False


if __name__ == '__main__':
    print(string_info('Capybara'))
    print(string_info('Armageddon'))
    print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
    print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
    print(calls)
