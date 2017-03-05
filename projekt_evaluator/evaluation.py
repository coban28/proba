from subprocess import Popen, PIPE
from reader import *
from ispis import *
ime = "proba.py"

file_input = Reader()
L = file_input.read_in()
Provjera = file_input.read_out()

def evaluacija(L, ime = "proba.py"):
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
            output = p.communicate(timeout=15)
            izlaz += [[output]]
            flag = 0
            continue
    return izlaz
evaluacija(L, ime)
ispis = Ispis(izlaz, Provjera)
exit, exit_provjera = ispis.shorten()
print(exit)
print(exit_provjera)