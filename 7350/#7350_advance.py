
#* FYI : angka prima adalah angka yang hanya dapat dibagi oleh 1 dan angka itu sendiri
#  2 3 5 7 


def angka_prima(angka):
   if angka <= 1 :      
      return False   # angka 1 dan dibawah bukan termasuk angka prima  
   if angka <= 3 :
      return True    # angka 2 salah satu angka genap prima, 3 juga angka prima
   
   if angka % 2 == 0 or angka % 3 == 0:
      return False   # angka yang bisa dibagi habis oleh 2 dan 3 juga bukan angka prima
   
   
   i = 5                   # sebagai divisor / pembagi                       
   
   while i * i <= angka:   # jika angkanya lebih besar dari kuadrat dari "i" maka :
      
      if angka % i == 0 or angka % (i + 2) == 0:   # jika angka bisa dibagi habis oleh "i" maupun (i + 2) maka angka itu bukan angka prima
            return False
      i += 6               # menggeser "i" ke faktor berikutnya
   return True             # jika tidak bisa dibagi habis oleh "i" maka ia adalah bilangan prima




start = 25
end = 50

print(f"Prime numbers between {start} and {end} are:")
for angkaPrima in range(start, end, +1):
   if angka_prima(angkaPrima):
      print(angkaPrima)
   









