
jumlah_vertikal_horizontal = 5
berhenti = 0  # index 0 = 1
jarak_antar_no = -1

for vertikal in range(jumlah_vertikal_horizontal, berhenti, jarak_antar_no):  # satu baris kebawah
   for horizontal in range( vertikal, berhenti, jarak_antar_no):     # satu baris ke samping | setiap mencapai angka 1, kembali ke setelahnya   (setelah baris 5 ialah baris 4)
      print(horizontal ,end=' ') # end = memberi jarak antar nomer
   print()  # yang awalnya 1 baris akan turun kebawah saat mencapai 1


