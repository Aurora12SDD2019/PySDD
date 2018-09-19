from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = eval(placeholders[0])
    if type(placeholder) is int:       # TODO: your condition here
        passed('int')
    else:
       failed("the first value is {} not integer".format(type(placeholder)))

    placeholder = eval(placeholders[1])
    if type(placeholder) is float:       # TODO: your condition here
        passed('float')
    else:
       failed("the second value is {} not float".format(type(placeholder)))

    placeholder = eval(placeholders[2])
    if type(placeholder) is str:       # TODO: your condition here
        passed('str')
    else:
       failed("the third value is {} not string".format(type(placeholder)))

    placeholder = eval(placeholders[3])
    if type(placeholder) is bool:       # TODO: your condition here
        passed('bool')
    else:
        failed("the third value is {} not boolean".format(type(placeholder)))


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()       # TODO: uncomment test call


