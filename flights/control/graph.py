from asyncio.windows_events import INFINITE
from contextlib import nullcontext
from email.policy import default
from operator import truediv
from xmlrpc.client import MAXINT
from collections import defaultdict



class Grana:
    def __init__(self, cvor1, cvor2, tezina):
        self.cvor1 = cvor1
        self.cvor2 = cvor2
        self.tezina = tezina
    def prvi_cvor(self):
        return self.cvor1
    def drugi_cvor(self):
        return self.cvor2
    def get_tezina(self):
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
            if(g.drugi_cvor() == cvor2):
                return 1
            return 0
    
    def ispisi_susedstva(self):
        print('Niz listi susedstva')
        for i in self.susedstva:
            
            for grana in self.susedstva[i]:
                print("("+ i + "-> " + grana.drugi_cvor() + "), " + str(grana.get_tezina()))
    
    def get_broj_cvorova(self):
        return self.susedstva.__sizeof__()
    
    def get_susedstva(self):
        return self.susedstva
    
    def print_gr(self):
        for i in self.susedstva:
            print(i)
        
    def min_distance(self, dist, sptSet):
        
        min = 1e7
        min_index = -1

        for i in self.susedstva:
            if(sptSet[i] == 0 and dist[i]<=min):
                min = dist[i]
                min_index = i
        
        return min_index
    
    def dijkstra(self, src, dest):
        dist = defaultdict()
        sptSet = defaultdict()
        parent = defaultdict()
      
        parent[src] = -1
        


        for i in self.susedstva:
            dist[i] = 1e7
            sptSet[i] = 0
            

        
               
        dist[src] = 0
        
        for count in self.susedstva:
            u = self.min_distance(dist, sptSet)
            sptSet[u] = 1
            for grana in self.susedstva[u]:
                if(sptSet[grana.drugi_cvor()] == 0 and grana.get_tezina()!=0 and dist[u]!=1e7 and dist[u]+grana.get_tezina()<dist[grana.drugi_cvor()]):
                    dist[grana.drugi_cvor()] = dist[u]+grana.get_tezina()

                    parent[grana.drugi_cvor()] = u

        return self.SolutionforVertex(parent, src, dest)
        
    def print_path(self, parent, j, htmlText):
        if(parent[j] == -1):
            return htmlText
        
        htmlText = self.print_path(parent, parent[j], htmlText)
        htmlText += j + ' -> '
        return htmlText

    def SolutionforVertex(self, parent, src, dest):
        htmlText="<h1>" + src + " -> "  
        htmlText = self.print_path(parent, dest, htmlText)
        htmlText= htmlText[:-4]
        htmlText+="</h1>"
        return htmlText

    
    