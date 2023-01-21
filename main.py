from xml.dom import minidom
FILE_BARBATI="C:\\Users\\Alin\\Downloads\\Prenume Baieti.txt"
FILE_NUME_FAMILIE="C:\\Users\\Alin\\Desktop\\numefamilie.txt"
FILE_FEMEI="C:\\Users\\Alin\\Downloads\\PrenumeFete.txt"
criteriu_lungime=lambda nume:len(nume)

def nrVocale(s):
    s=s.lower()
    KV=0
    vocale=['a','e','i','o','u','ă','î','â',"y"]
    for litera in s:
        if litera in vocale:
            KV=KV+1
    return KV
def nrConsoane(s):
    s = s.lower()
    KV = 0
    consoane = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','ș','t','ț','v','w','x','z']
    for litera in s:
        if litera in consoane:
            KV = KV + 1
    return KV
def nrDiacritrice(s):
    s = s.lower()
    KV=0
    diacritice=["ă","î","â","ș","ț"]
    for litera in s:
        if litera in diacritice:
            KV=KV+1
    return KV
def prenumeXMLGenerator():
    f1=open(FILE_BARBATI,"r",encoding="utf-8-sig")
    f2=open(FILE_FEMEI,"r",encoding="utf-8-sig")
    if f1==None or f2==None:
        raise Exception("Fisierul nu a putut fi deschis!")
    else:
        listaBarbati=[]
        for line in f1:
            listaBarbati.append(line.strip())
        f1.close()
        listaBarbati=sorted(listaBarbati,key=criteriu_lungime)
        print(listaBarbati)
        listaBarbati=sorted(listaBarbati,key=lambda s:nrDiacritrice(s),reverse=True)
        print(listaBarbati)
        listaBarbati=sorted(listaBarbati,key=lambda s:nrVocale(s))
        print(listaBarbati)
        listaBarbati=sorted(listaBarbati,key=lambda s:nrConsoane(s))
        print(listaBarbati)
        listaFemei=[]
        for line in f2:
            listaFemei.append(line.strip())
        f2.close()
        listaFemei = sorted(listaFemei, key=criteriu_lungime)
        print(listaFemei)
        listaFemei = sorted(listaFemei, key=lambda s: nrDiacritrice(s), reverse=True)
        print(listaFemei)
        listaFemei= sorted(listaFemei, key=lambda s: nrVocale(s))
        print(listaFemei)
        listaFemei= sorted(listaFemei, key=lambda s: nrConsoane(s))
        print(listaFemei)
        listaFemei = []
        root=minidom.Document()
        listaPrenume=root.createElement("listaPrenume")
        root.appendChild(listaPrenume)
        for p in listaBarbati:
            e=root.createElement("prenume")
            e.setAttribute("lungime",str(len(p)))
            e.setAttribute("sex","M")
            e.setAttribute("consoane",str(nrConsoane(p)))
            e.setAttribute("vocale",str(nrVocale(p)))
            e.setAttribute("diacritice",str(nrDiacritrice(p)))
            nodtext=root.createTextNode(p)
            e.appendChild(nodtext)
            listaPrenume.appendChild(e)
        for p in listaFemei:
            e = root.createElement("prenume")
            e.setAttribute("lungime", str(len(p)))
            e.setAttribute("sex", "F")
            e.setAttribute("consoane", str(nrConsoane(p)))
            e.setAttribute("vocale", str(nrVocale(p)))
            e.setAttribute("diacrtice", str(nrDiacritrice(p)))
            nodtext = root.createTextNode(p)
            e.appendChild(nodtext)
            listaPrenume.appendChild(e)
        xml_sr=root.toprettyxml(indent="\t")
        file="prenume.xml"
        with open(file,"w",encoding="utf-8-sig") as f:
            f.write(xml_sr)
def numeFamilieXMLgenerator():
    f3 = open(FILE_NUME_FAMILIE, "r", encoding="utf-8-sig")
    if f3 == None:
        raise Exception("Fisierul nu a putut fi deschis!")
    else:
        listanumefamilie=[]
        for line in f3:
            listanumefamilie.append(line.strip())
        f3.close()
        root=minidom.Document()
    listafamilie=root.createElement("listaNumeFamilie")
    root.appendChild(listafamilie)
    for p in listanumefamilie:
        e = root.createElement("numeFamilie")
        e.setAttribute("lungime", str(len(p)))
        e.setAttribute("sex", "M")
        e.setAttribute("consoane", str(nrConsoane(p)))
        e.setAttribute("vocale", str(nrVocale(p)))
        e.setAttribute("diacritice", str(nrDiacritrice(p)))
        nodtext = root.createTextNode(p)
        e.appendChild(nodtext)
        listafamilie.appendChild(e)

    xml_str=root.toprettyxml(indent="\t")
    file="numeFamilie.xml"
    with open(file,"w" ,encoding="utf-8-sig") as f:
         f.write(xml_str)
numeFamilieXMLgenerator()
prenumeXMLGenerator()
n="Mihăiță"
x1=nrVocale(n)
x2=nrConsoane(n)
x3=nrDiacritrice(n)
print(x1,x2,x3)
print((x1+x2)==len(n))