# Version 0.2
def string_filtering(standard_info):
    
def data_processing(standard_info):
    import itertools
    file = open("pwlist-created-wordlist.txt", "w")
    file.write("")
    file.close()
    file = open("pwlist-created-wordlist.txt", "a")
    list1 = []
    list2 = []
    for key in standard_info:
        if standard_info[key] == "none":
            pass
        if standard_info[key] ==
        else:
            list1.append(standard_info[key])
    for i in range(1,len(list1)+1):
        drip = [list(x) for x in itertools.permutations(list1, i)]
        list2.extend(drip)
    for element in list2:
        string = ''.join(element)
        file.write(string + "\n")
