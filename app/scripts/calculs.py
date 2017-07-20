
def matriculats(assig, quadri, an, sex):
    """
    retorna el nombre de matriculats per a un aassignatura, quadrimestre, any, si no s'introdueix el sexe,
    retorna els dos
    """
    f1 = open('NouFitxer.csv', 'r')
    c = 0
    for linea in f1:
        linea = linea.strip()
        l = linea.split(';')
        if l[2] == assig:
            if l[3] == an:
                if l[4] == quadri:
                    if sex != "T":
                        if l[8] == sex:
                            c = c + 1
                        else:
                            pass
                    else:
                        c = c + 1
    return c


def aprovats(assig, quadri, an, sex):
    """
    retorna el nombre d'aprovats per assignatura, quadrimestre i any. si no s'introdueix el paràmetre sex retorna
    ambdos sexes
    """
    f1 = open('NouFitxer.csv', 'r')
    c = 0
    for linea in f1:
        linea = linea.strip()
        l = linea.split(';')
        if l[2] == assig:
            if l[3] == an:
                if l[4] == quadri:
                    if l[5] == 'S':
                        if sex != "T":
                            if l[8] == sex:
                                c = c + 1
                            else:
                                pass
                        else:
                            c = c + 1
    return c


def percentatge(assig, quad, an, sex):
    """
    retorna el percentatge d'aprovats per assignatura, quadrimestre, i any
    """
    if matriculats(assig, quad, an, sex) != 0:
        return (aprovats(assig, quad, an, sex) / matriculats(assig, quad, an, sex)) * 100
    else:
        return 0

    # def aprovats1a(assig):
    # f = open('/static/NouFitxer.csv','r')
    # exp = []
    # la = []
    # c = 0
    # ctot = 0
    # for linea in f:
    # l = linea.split(';')
    # if exp != l[1]:
    # exp = l[1]
    # ctot = ctot + 1
    # for e in la:
    # if e == 'N':
    # pass
    # else:
    # c = c+1
    # la = []
    # if l[2] == assig:
    # la.append(l[5])
    # return (c/ctot)*100
    # """
    # def intent(assig,i,sex=0):
    # """
    # reorna el percentatge d'aprovats a la i-essima la assignatura assig
    # """
    # f = open('/NouFitxer.csv','r')
    # exp = []
    # la = []
    # c = 0
    # ctot = 0
    # for linea in f:
    # l = linea.split(';')
    # if exp != l[1]:
    # exp = l[1]
    # if sex != 0:
    # if l[8] == sex:
    # ctot = ctot + 1
    # else:
    # pass
    # else:
    # ctot = ctot + 1
    # if 'S' in la:
    # if len(la) == i:
    # c = c+1
    # la = []
    # if sex != 0:
    # if l[8] == sex:
    # if l[2] == assig:
    # la.append(l[5])
    # else:
    # if l[2] == assig:
    # la.append(l[5])
    # return (c/ctot)*100


def notamitja(assig, quad, an, sex):
    """
    retorna la mitjana per assigm quad i any
    """
    f = open('NouFitxer.csv', 'r')
    n = 0
    c = 0
    for linea in f:
        linea = linea.strip()
        l = linea.split(';')
        if l[2] == assig:
            if l[3] == an:
                if l[4] == quad:
                    if sex != "T":
                        if l[8] == sex:
                            c = c + 1
                            n = n + float(l[6])
                        else:
                            pass
                    else:
                        c = c + 1
                        n = n + float(l[6])
    f.close()
    if c == 0:
        return 0
    return n / c


def llistamitja(any, quad, sex):
    """
    fa una llista amb les mitjanes de totes les assignatures d'un any i un quadri
    """
    l = []
    for assig in range(240011, 240016):
        l.append(notamitja(str(assig), quad, any, sex))
    for assig in range(240021, 240026):
        l.append(notamitja(str(assig), quad, any, sex))
    return l


def llistapercent(any, quad, sex):
    # fa la llista amb els perentatges de la nota
    l = []
    for assig in range(240011, 240016):
        l.append(percentatge(str(assig), quad, any, sex))
    for assig in range(240021, 240026):
        l.append(percentatge(str(assig), quad, any, sex))
    return l
