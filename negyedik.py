# függvény
def beolvas():
    szam = float(input("Kérem adjon meg egy számot!"))
    return szam
# return átadja a szam értékét
#4.	Készíts egy programot, amely beolvas 3 valós számot, majd kiírja őket, mindegyiket egy sorba szóközzel elválasztva!

#eljárás (adatelrejtés)
def negyedikFeladat():
    szam1 = beolvas()
    szam2 = beolvas()
    szam3 = beolvas()
    #int(input típuskényszerítés, hogy egész számot várok)
    #float(input
    print(str(szam1)+" "+str(szam2)+" "+str(szam3))
    #kérdezzük meg, hogy milyen típusú ez a szám
    print(type(szam1))