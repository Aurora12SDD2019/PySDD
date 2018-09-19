from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()

    try:
        placeholders = [eval(p) for p in placeholders] #placeholders are strings
        passed('eval')
    except ValueError:
        failed('one or both variables are not numbers')


    try:
        if sum(placeholders) == 42:       # TODO: your condition here
            passed('sum')
        else:
            failed('the two variables to not add up to 42')

    except TypeError:
        failed('One or both of your variables is a string or bool')


if __name__ == '__main__':
    test_answer_placeholders()       
    run_common_tests()
    # test_answer_placeholders()



