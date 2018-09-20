import sys

class Tests():
    """Performs common tests and stores test results

    Longer class information....
    Longer class information....

    Attributes:
        fails: An integer count of the number of failed tests.
        passes: An integer count of the number of passed tests.
    """

    def __init__(self, testModule):
        """Inits Tests with passes = 0, fails = 0 and module being tested.

        Args:
            testModule: string - the name of the module being tested
                (don't include the '.py' extension')
        """

        self.fails = 0
        self.passes = 0
        self.failed = None

        # run and enable access to the module being tested
        print("****** CODE OUTPUT ******")

        try:
            __import__(testModule)
            self.M = sys.modules[testModule]
        except SyntaxError:
            print("ERROR: Your code '{}.py' won't execute.\n".format(testModule),
              "It probably has SyntaxErrors.\n"
              "Run the code then debug it carefully, reading the information in the output window\n"
              "The location of syntax errors is usually indicated by a caret symbol '^'")
            exit()

        except NameError:
            print("ERROR: Your code 'data_types.py' won't execute.\n"
              "It probably has NameErrors.\n"
              "Run the code then debug it carefully, reading the information in the output window\n"
              "NameErrors often happen when you forget to use quotes around a string or when you use a variable that hasn't got a value yet")
            exit()

        print("\n****** TEST RESULTS ******")


    def passTest(self, name = "Test", message = "Well done!"):
        """Prints pass message and increments passes counter.

        Args:
            name: optional string - name of the test performed
            message: optional string - message to be displayed
            """

        print("PASSED {}: {}".format(name, message))
        self.passes += 1
        if self.failed is None:
            self.failed = False


    def failTest(self, name = "Test", message = "Please try again"):
        """Prints pass message and increments fails counter.

        Args:
            name: optional string - name of the test performed
            message: optional string - message to be displayed
        """

        print("FAILED {}: {}".format(name, message))
        self.fails += 1
        self.failed = True

    def testVarType(self, name, expectedType):
        """Checks whether a variable confirms to the expected type.

        Args:
            name: string - name of the variable being checked
            expectedType: data type - the expected type of the variable
        """

        for v in dir(self.M):
            if v == name:
                var = eval("self.M." + v)

                if type(var) is expectedType:
                    self.passTest("Type Test", "{} is {} expected {}. Well Done!".format(name, expectedType, type(var)))
                else:
                    self.failTest("Type Test",
                                "{} should be {} not {}. Please try again :(".format(name, expectedType, type(var)))

    def printResults(self):
        """Prints summary of test results"""

        if self.failed is None:
            msg = "THE CODE WAS NOT TESTED"
        elif self.failed:
            msg = "FAILED :( TRY AGAIN"
        else:
            msg = "PASSED :) CONGRATULATIONS"

        total = self.passes + self.fails

        print("\n****** SUMMARY RESULTS ******")
        print("{}: Total {}: Passed {}: Failed {}".format(msg, total, self.passes, self.fails))


