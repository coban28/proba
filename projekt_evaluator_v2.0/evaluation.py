from subprocess import Popen, PIPE
from reader import *
from ispis import *
from os import listdir
import os
ime = "proba.py" #ime programa koji se treba evaluirati
vrijeme = 5  #vremenski limit za izvodjenje programa

file_input = Reader()
L = file_input.read_in()
Provjera = file_input.read_out()

def evaluacija(L, ime = "proba.py"):  # funkcija koja evaluira program i vraca output skripte koju je pokrenula
    izlaz = []
    flag = 0
    for i in (L):
        if i != "---\n" and i != "---" and flag == 0:
            a = i
            p = Popen(['python', ime],
                    stdin = PIPE, stdout = PIPE, stderr = PIPE, shell = False)
            p.stdin.write(bytes(a , "ascii"))
            p.stdin.flush()
            flag = 1
        elif i != "---\n" and i != "---" and flag == 1:
            a = i
            p.stdin.write(bytes(a, "ascii"))
            p.stdin.flush()
        else:
            output = p.communicate(timeout=5)
            izlaz += [[output]]
            flag = 0
            continue
    return izlaz

def provjeri(dobiveno,tocno): #provjera dobivenih rezultata evaluacijom i ockivanih iz txt datoteke
    br = 0
    for i in range(len(dobiveno)):
        if dobiveno[i] == tocno[i]:
            br += 1
    #print(dobiveno)
    return br

def prolaz(): #funkcija koja prolazi kroz sve foldere i trazi python filove sa odredenim imenom
    global ime, L
    
    prezimena = listdir('prezimena')
    fajlovi = []
    rezultati = [0]* len(prezimena)
    
    for i in prezimena:
        fajlovi += [[]]
        fajlovi[-1] = listdir('prezimena\\'+i)

    for i in range(len(prezimena)):
        for j in fajlovi[i]:
            if j == ime:
                skripta = os.path.join(os.getcwd(), ('prezimena//'+ str(prezimena[i]) + "//" + ime))
                izlaz = evaluacija(L, skripta)
                ispis = Ispis(izlaz, file_input.read_out())
                exit, exit_provjera = ispis.shorten()
                br = provjeri(exit, exit_provjera)
                rezultati[i] += br


    return rezultati, prezimena

    
     
izlaz, fajl = prolaz()

#ispis svih mogucih gresaka i konacnih rezultata
for i in range(len(fajl)):
    print(fajl[i], "\t", izlaz[i])


'''ispis = Ispis(izlaz, Provjera)
exit, exit_provjera = ispis.shorten()'''

