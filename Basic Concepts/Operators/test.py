from PySDDTest import Tests

T = Tests()

try:
    print("****** CODE OUTPUT ******")
    from task import *
except SyntaxError:
    print("ERROR: Your code 'data_types.py' won't execute.\n"
          "It probably has a syntax errors.\n"
          "Run and debug the code by carefully reading the information in the output window\n"
          "The location of syntax errors is usually indicated by a caret symbol '^'")
    exit()


if __name__ == '__main__':
    print("\n\n****** TEST RESULTS ******")

    #test each of the variables for type
    T.testVarType("varInt", varInt, int)
    T.testVarType("varFloat", varFloat, float)
    T.testVarType("varString", varString, str)
    T.testVarType("varBool", varBool, bool)

    #print the ovwerall result
    T.printResults()



