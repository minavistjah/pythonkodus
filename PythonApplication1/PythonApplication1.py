1#
from datetime import *

tana = date.today()

print("Tere!")
print("Täna on:", tana)

print(tana.strftime("%d/%m/%Y"))
print(tana.strftime("%B %d, %Y"))
print(tana.strftime("%m/%d/%y"))
print(tana.strftime("%b-%d-%Y"))

print("Päev:", tana.day)
print("Kuu:", tana.month)
print("Aasta:", tana.year)

kuu_lopp = date(tana.year, tana.month + 1, 1) if tana.month < 12 else date(tana.year + 1, 1, 1)
aasta_lopp = date(tana.year + 1, 1, 1)

print("Päevi kuu lõpuni:", (kuu_lopp - tana).days - 1)
print("Päevi aasta lõpuni:", (aasta_lopp - tana).days - 1)

sunnipaev = date(2009, 5, 10)  # Muuda enda sünnikuupäevaks

vanus = tana.year - sunnipaev.year
if (tana.month, tana.day) < (sunnipaev.month, sunnipaev.day):
    vanus -= 1

print("Vanus aastates:", vanus)
2#
vastus = 3 + 8 / (4 - 2) * 4

print("Tehte 3 + 8 / (4 - 2) * 4 vastus on:", vastus)

print("Ilma sulgudeta:", 3 + 8 / 4 - 2 * 4)
print("Sulgudega:", 3 + 8 / (4 - 2) * 4)
print("Teistsuguste sulgudega:", (3 + 8) / (4 - 2) * 4)
3#
import math

R = float(input("Sisesta ringi raadius: "))

ruudu_kulg = R * 2

ruudu_pindala = ruudu_kulg ** 2
ruudu_umbermoot = ruudu_kulg * 4

ringi_pindala = math.pi * R ** 2
ringi_umbermoot = 2 * math.pi * R

print("Ruudu pindala:", ruudu_pindala)
print("Ruudu ümbermõõt:", ruudu_umbermoot)
print("Ringi pindala:", ringi_pindala)
print("Ringi ümbermõõt:", ringi_umbermoot)
4#
import math

maa_raadius = 6378
mundi_labimoot = 0.02575
pi = 3.14159

maa_umbermoot = 2 * pi * maa_raadius
mundi_labimoot_km = mundi_labimoot / 1000

muntide_arv = maa_umbermoot / mundi_labimoot_km

print("Maa ümbermõõt:", maa_umbermoot, "km")
print("Vajalike 2-euroste müntide arv:", round(muntide_arv))
5#
sona1 = "kill-koll"
sona2 = "killadi-koll"

print((sona1 + " ") * 2 + sona2 + " " +
      (sona1 + " ") * 2 + sona2 + " " +
      (sona1 + " ") * 3)

print(sona1.upper())
6#
laul = """
Rong see sõitis tsuhh tsuhh tsuhh,
piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?

Rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll kill.
"""

print(laul.upper())
7#
a = float(input("Sisesta esimese külje pikkus: "))
b = float(input("Sisesta teise külje pikkus: "))

umbermoot = 2 * (a + b)
pindala = a * b

print("Ristküliku ümbermõõt:", umbermoot)
print("Ristküliku pindala:", pindala)
8#
liitrid = float(input("Sisesta tangitud kütuse kogus liitrites: "))
kilomeetrid = float(input("Sisesta läbitud kilomeetrid: "))

kulu = liitrid / kilomeetrid * 100

print("Keskmine kütusekulu 100 km kohta:", round(kulu, 2), "l/100km")
9#
kiirus = 29.9

minutid = float(input("Sisesta aeg minutites: "))

kaugus = kiirus * minutid / 60

print("Läbitud vahemaa:", round(kaugus, 2), "km")
10#
aeg = int(input("Sisesta aeg minutites: "))

tunnid = aeg // 60
minutid = aeg % 60

print("Aeg:", str(tunnid) + ":" + str(minutid).zfill(2))