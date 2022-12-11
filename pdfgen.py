import os
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
    for i in range(int(num.get())):
        Generated.append(Exos[i])
    return Generated

def GeneratePDF(L, binary):
    if('result.tex' in os.listdir()):
        os.remove('result.tex')
    DSr = open('result.tex', 'a')
    if(binary.get()=='ds'):
        DS = open('examples/DS.tex', 'r')
        lines = DS.readlines()
        i = 0
        while(lines[i]!= '\end{document}\n'):
            DSr.write(lines[i])
            i+=1
    if(binary.get()=='td'):
        TD = open('examples/TD.tex', r)
        lines = TD.readlines()
        while(lines[i]!= '\end{document}\n'):
            DSr.write(lines[i])
            i+=1

    for i in range(len(L)):
        flag = False
        exo = open(L[i], 'r')
        j = 0
        LineList = exo.readlines()
        DSr.write("\section{Exercice "+ str(i+1)+ ": }\n")
        while(LineList[j]!= '\end{document}\n'):
            if(LineList[j]== '\\begin{questions}\n'):
                flag = True
            if(LineList[j]=='\end{document}\n'):
                flag = False
            if(flag):
                DSr.write(LineList[j])
            j+=1
    DSr.write("\end{document}\n")
