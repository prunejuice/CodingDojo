def inputtest(list, char):
    newlist = []
    for i in range(len(list)):
        str = list[i]
        findvalue = str.find(char)
        if findvalue != -1:
            newlist.append(str)
    print newlist


word_list = ['hello','world','my','name','is','Anna']
char = 'o'
inputtest(word_list, char)
