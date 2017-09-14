def inputtest(variable):
    foundString = False
    foundInt = False
    sum = 0
    if type(variable) is list:
        for i in variable:
            print i
            if type(i) is str:
                string = "String:" + str(i)
                print string
                foundString = True

            if type(i) is int:
                sum =+ i
                foundInt = True

        if not foundString and foundInt:
            print "This is list contains num"

        elif foundString and foundInt:
            print "This is mixed"

        elif not foundInt and foundString:
            print "This is list contains String"

    print "YO:" + str(sum)

l = ['magical unicorns',19,'hello',98.98,'world']
inputtest(l)
