import os
import gui, db
from random import randint

# Generates a list of exercises to turn into exam depending on the Lessons entered and the number of exercises
# wanted
#
# @param {list} L : list of lessons selected by user
# @param {int} num : number of exercises wanted
# @returns {list} Generated : list of exercises generated
def GetDS(L, num):
    T = []
    for i in L :
        if(i[1].get() == 1):
            T.append(i[0])
    Exos = []
    for i in T:
        Exos.append(db.GetExoFromLesson(i))
    Generated = []
    cnt = 0
    while cnt < int(num.get()):
        buffer = Exos[randint(0,int(num.get())-1)]
        if(buffer not in Generated):
            Generated.append(buffer)
            cnt += 1

    return Generated

# Generated the tex file of the exam
# @param {list} L : list of exercise paths to put into exam tex
# @param {string} binary : value of radio button of whether to generate a "DS" or "TD"
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
