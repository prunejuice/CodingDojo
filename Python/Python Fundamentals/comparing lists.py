def inputtest(list1, list2):
    for i in range(0, len(list1)):
        if list1[i] != list2[i]:
            same = False
        else:
            same = True

    if same:
        print "Lists are same"
    else:
        print "Lists are different"


list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

inputtest(list_one, list_two)
