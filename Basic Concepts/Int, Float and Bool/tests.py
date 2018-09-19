from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = eval(placeholders[0])
    if type(placeholder) is int:       # TODO: your condition here
        passed()
    else:
       failed("the first value is {} not integer".format(type(placeholder)))

    placeholder = eval(placeholders[1])
    if type(placeholder) is float:       # TODO: your condition here
        passed()
    else:
       failed("the second value is {} not float".format(type(placeholder)))

    placeholder = eval(placeholders[2])
    if type(placeholder) is bool:       # TODO: your condition here
        passed()
    else:
        failed("the third value is {} not boolean".format(str(type(placeholder))))


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()       # TODO: uncomment test call


