from asyncio.windows_events import INFINITE
from contextlib import nullcontext
from operator import truediv
from xmlrpc.client import MAXINT



class Grana:
    def __init__(self, cvor1, cvor2, tezina):
        self.cvor1 = cvor1
        self.cvor2 = cvor2
        self.tezina = tezina
    def prvi_cvor(self):
        return self.cvor1
    def drugi_cvor(self):
        return self.cvor2
    def tezina(self):
        return self.tezina
    def compare_to(self, druga):
        if(self.tezina() < druga.tezina()):
            return -1
        elif(self.tezina()>druga.tezina()):
            return 1
        else:
            return 0
    
class TezinskiGraf:
    def __init__(self):
        self.susedstva = {}
        self.brGrana = 0
    
    def dodaj_granu(self, grana):
        if grana.prvi_cvor() not in self.susedstva:
            self.susedstva[grana.prvi_cvor()] = []
        if grana.drugi_cvor() not in self.susedstva:
            self.susedstva[grana.drugi_cvor()] = []

        cvor1 = grana.prvi_cvor()
        self.susedstva[cvor1].append(grana)
        self.brGrana += 1

    def susedi(self, cvor1, cvor2):
        for g in self.susedstva[cvor1]:
            if(g.drugi_cvor(cvor1) == cvor2):
                return 1
            return 0
    
    def ispisi_susedstva(self):
        print('Niz listi susedstva')
        for i in self.susedstva:
            for grana in self.susedstva[i]:
                print("("+ i + "-> " + grana.drugi_cvor() + ")")
    
    def get_broj_cvorova(self):
        return self.susedstva.__sizeof__()
    
    def get_susedstva(self):
        return self.susedstva
    
    def print_gr(self):
        for i in self.susedstva:
            print(i)
        
    

    
    def floyd_warshall(self):
        udaljenost = None
        for i in self.susedstva:
            for j in self.susedstva:
                if(i==j):
                    udaljenost[i][i] = 0
                elif(self.susedi(i, j)):
                    grana = None
                    for g in self.get_susedstva()[i]:
                        if(g.drugi(i) == j):
                            grana = g
                    
                    if(grana != None):
                        udaljenost[i][j] = grana.tezina()
                    else:
                        udaljenost[i][j] = INFINITE
                else:
                    udaljenost[i][j] = INFINITE
        
        for k in self.get_broj_cvorova():
            for i in self.get_broj_cvorova():
                for j in self.get_broj_cvorova():
                    if(self.susedi(i, k) and self.susedi(k, j)):
                        if(udaljenost[i][k] + udaljenost[k][j] < udaljenost[i][j]):
                            udaljenost[i][j] = udaljenost[i][k] + udaljenost[k][j]
        
        return udaljenost

   

def ispisi(graf, udaljenost):
    for i in graf.get_broj_cvorova():
        for j in graf.get_broj_cvorova():
            print("udaljenost["+ i + "]["+ j + "]= " + (udaljenost[i][j]))

if __name__ == '__main__':

    g = TezinskiGraf()
    grana1 = Grana("London", "Pariz", 16)
    grana2 = Grana("London", "New York", 15)
    grana3 = Grana("New York", "Pariz", 12)
    grana4 = Grana("Pariz", "Istanbul", 17)
    g.dodaj_granu(grana1)
    g.dodaj_granu(grana2)
    g.dodaj_granu(grana3)
    g.dodaj_granu(grana4)
    udaljenost = g.floyd_warshall()
    g.ispisi(udaljenost)


    
    