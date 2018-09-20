from PySDDTest import Tests

#T = Tests("data_types")


if __name__ == '__main__':
    T = Tests("data_types")

    #test each of the variables for type
    T.testVarType("varInt", int)
    T.testVarType("varFloat", float)
    T.testVarType("varString", str)
    T.testVarType("varBool", bool)

    #print the overall result
    T.printResults()


