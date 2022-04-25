from asyncio.windows_events import INFINITE
from contextlib import nullcontext
from email.policy import default
from operator import truediv
from xmlrpc.client import MAXINT
from collections import defaultdict
import copy

class par:
    def __init__(self, cena, stop, putanja):
        self.cena = cena
        self.stop = stop
        self.putanja = putanja
    def __add__(self, p):
        cena = self.cena+ p.cena
        stop = self.stop + p.stop
        putanja = self.putanja + p.putanja
        return par(cena, stop, putanja)
class Grana:
    def __init__(self, cvor1, cvor2, tezina, flight):
        self.cvor1 = cvor1
        self.cvor2 = cvor2
        self.tezina = tezina
        self.flight = copy.copy(flight)

    def prvi_cvor(self):
        return self.cvor1

    def drugi_cvor(self):
        return self.cvor2

    def get_tezina(self):
        return self.tezina

    def get_flight(self):
        return self.flight

    def compare_to(self, druga):
        if(self.tezina() < druga.tezina()):
            return -1
        elif(self.tezina() > druga.tezina()):
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
                print("(" + i + "-> " + grana.drugi_cvor() + "), " +
                      str(grana.get_tezina()))

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
            if(sptSet[i] == 0 and dist[i] <= min):
                min = dist[i]
                min_index = i

        return min_index

    def dijkstraForVertex(self, src, dest):
        dist = defaultdict()
        sptSet = defaultdict()
        parent = defaultdict()

        parent[src] = None

        for i in self.susedstva:
            dist[i] = 1e7
            sptSet[i] = 0
            parent[i] = None

        dist[src] = 0

        for count in self.susedstva:
            u = self.min_distance(dist, sptSet)
            sptSet[u] = 1
            for grana in self.susedstva[u]:
                if(sptSet[grana.drugi_cvor()] == 0 and grana.get_tezina() != 0 and dist[u] != 1e7 and dist[u]+grana.get_tezina() < dist[grana.drugi_cvor()]):
                    if(parent[grana.get_flight().od]!=None):
                        if(parent[grana.get_flight().od].vremeDolaska > grana.get_flight().vremePolaska):
                            continue

                    dist[grana.drugi_cvor()] = dist[u]+grana.get_tezina()
                    parent[grana.drugi_cvor()] = grana.get_flight()
        try:
            return self.SolutionforVertex(parent, src, dest, dist[dest])
        except KeyError:
            return ""
        

    def dijkstra(self, src):
        dist = defaultdict()
        sptSet = defaultdict()
        parent = defaultdict()

        parent[src] = None

        for i in self.susedstva:
            dist[i] = 1e7
            sptSet[i] = 0
            parent[i] = None

        dist[src] = 0

        for count in self.susedstva:
            u = self.min_distance(dist, sptSet)
            sptSet[u] = 1
            for grana in self.susedstva[u]:
                if(sptSet[grana.drugi_cvor()] == 0 and grana.get_tezina() != 0 and dist[u] != 1e7 and dist[u]+grana.get_tezina() < dist[grana.drugi_cvor()]):
                    if(parent[grana.get_flight().od]!=None):
                        if(parent[grana.get_flight().od].vremeDolaska > grana.get_flight().vremePolaska):
                            continue
                    dist[grana.drugi_cvor()] = dist[u]+grana.get_tezina()
                    parent[grana.drugi_cvor()] = grana.get_flight()

        return self.printSolution(dist, parent, src)
        

    def print_path(self, parent, j, number, htmlText):
        if(parent[j] == None):
            return htmlText
        htmlText += j
        self.print_path(parent, parent[j].od, number, htmlText)
        
  


    def odrediParametre(self, parent, j, p):
        if(parent[j] == None):
            return p
        p += self.odrediParametre(parent, parent[j].od, p)
             
        p.cena += parent[j].cenaE
        p.stop+=1
        p.putanja += j
        if(p.stop):
            p.putanja += " -> " 
        return p

    def printSolution(self, dist, parent, src):
        htmlText = ""

        for i in self.susedstva:
            
            if(dist[i] == 0 or dist[i]==1e7):
                continue
            

            htmlText+= "<div class='card'><div class='card-body'>"
            
            pp = par(0, 0, "")
            p = self.odrediParametre(parent, i, pp)
            print(p.putanja)
            htmlText+= "<h1>" + src+"-> " + i + "</h1>" 
            if(p.stop-1 == 0):
              htmlText += "<a href='#'> " + "Direct"
            else:
             htmlText+= "<a class =p path='%s'>" % (p.putanja)  + (str(p.stop-1))+ "stop" 
            htmlText+="</a>"
            htmlText+= "<p> Economy: " + str(round(p.cena, 2)) + "$ Business: " +str(round(p.cena*1.45, 2)) + "$"
            htmlText+="</div></div><br>" 
        return htmlText

    def SolutionforVertex(self, parent, src, dest, dist):
        if(dist == 0 or dist==1e7):
            return ""
        htmlText= "<div class='card'><div class='card-body'>"
            
        pp = par(0, 0, "")
        try:
          p = self.odrediParametre(parent, dest, pp)
        except KeyError:
            return "<div class='card text-danger'>Nema leta/letova za unete datume/lokaciju.</div>"

        print(p.putanja)
        htmlText+= "<h1>" + src+"-> " + dest + "</h1>" 
        if(p.stop-1 == 0):
            htmlText += "<a href='#'> " + "Direct"
        else:
            htmlText+= "<a href='#' onclick='route('" + p.putanja +  "')'>"+ (str(p.stop-1))+ "stop))"
        htmlText+="</a>"
        htmlText+= "<p> Economy: " + str(round(p.cena, 2)) + "$ Business: " +str(round(p.cena*1.45, 2)) + "$"
        htmlText+="</div></div><br>"   
        return htmlText

    def printPathVarsal(self, path,  v,  u):
        if(path[v][u].od == v):
            return
        self.printPathVarsal(path, v, path[v][u].od)
        print(path[v][u].od + ', ')

    def floyd_warshall(self):
        dis = defaultdict(defaultdict)
        path = defaultdict(defaultdict)
        for i in self.susedstva:
            for j in self.susedstva:
                if(i == j):
                    dis[i][i] = 0
                    path[i][i] = None
                elif(self.susedi(i, j) == 1):
                    grana = None
                    for g in self.get_susedstva()[i]:
                        if(g.drugi_cvor() == j):
                            grana = g
                    if(grana != None):
                        dis[i][j] = grana.get_tezina()
                        path[i][j] = grana.get_flight()
                    else:
                        dis[i][j] = 1e7
                        path[i][j] = None
                else:
                    dis[i][j] = 1e7
                    path[i][j] = None
        for k in self.susedstva:
            for i in self.susedstva:
                for j in self.susedstva:
                    if(self.susedi(i, k) == 1 and self.susedi(k, j) == 1):
                        if(dis[i][k] + dis[k][j] < dis[i][j]):
                            if(path[i][k].vremeDolaska > path[k][j].vremePolaska):
                                continue
                            dis[i][j] = dis[i][k]+dis[k][j]
                            path[i][j] = path[k][j]
        return self.ispisiVarsal(path)
        

    def ispisiVarsal(self, path):
        htmlText = ""
        for i in self.susedstva:
            for j in self.susedstva:
                if(j != i and path[i][j] != None):
                    htmlText +="<div class='card'><div class='card-body'>"
                    p = self.odrediParametre(path[i], j, par(0, 0, ""))
                    htmlText+="<h1>"+i+" -> "+j+"</h1>"  
                    if(p.stop-1 == 0):
                        htmlText += "<a href='#'> " + "Direct"
                    else:
                      htmlText+= "<a class =p path='%s'>" % (p.putanja)  + (str(p.stop-1))+ "stop" 
                    htmlText+="</a>"
                    htmlText+= "<p> Economy: " + str(round(p.cena, 2)) + "$ Business: " +str(round(p.cena*1.45, 2)) + "$"
                    htmlText+="</div></div><br>"  
        return htmlText
