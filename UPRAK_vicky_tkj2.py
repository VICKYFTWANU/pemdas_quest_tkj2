print("1.balok")

panjang = int(input("masukan nilai panjang:"))
lebar = int(input("masukan nilai lebar:"))
tinggi = int(input("masukan nilai tinggi:"))

volume_balok = panjang * lebar * tinggi
print ("nilai volume balok adalah",volume_balok)

print("2.tabung")
import math
r=float (input("masukan jari jari:"))
t=float (input("masukan tinggi:"))
pi = math . pi
V=round(pi*(r*r)*t,2)
print("volume tabung adalah",V)
 
print("3.limas")
luas_alas_persegi =int (input("masukan nilai luas alas persegi"))
tinggi =int (input("masukan nilai tinggi"))
volume_limas = (1/3 *luas_alas_persegi) * tinggi
print("nilai volume limas adalah",volume_limas)

kursdolar =14000
rupiah =float(input("masukan uang rupiah="))
ruptodol =rupiah/ kursdolar