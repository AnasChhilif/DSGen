import gui, db

def GetDS(L, num):
    T = []
    for i in L :
        if(i[1].get() == 1):
            T.append(i[0])
    Exos = []
    for i in T:
        Exos.append(db.GetExoFromLesson(i))
    Generated = []
    for i in range(num):
        Generated.append(Exos[i])
    print(Generated)
    return Generated
