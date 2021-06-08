list = [3,2,1,4]
inf = 0
ins = 1
find = 1
finish = False
while find <= len(list)-1:
    if list[inf] > list[ins]:
        fv = list[ins]
        sv = list[inf]
        list[inf] = fv
        list[ins] = sv
        inf = inf + 1
        ins = ins + 1
    else:
        inf = inf + 1
        ins = ins + 1
