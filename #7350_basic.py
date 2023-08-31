data_uji = [275, 40, 430]


def menghitung_tip(tagihan):
     if 50 <= tagihan <= 300:   # jika tagihannya diantara 50 - 300
        tip = tagihan * 0.15  
     else:
        tip = tagihan * 0.2
     return tip


for tagihan in data_uji:      # loop data di dalam data uji
     tip = menghitung_tip(tagihan)
     total = tagihan + tip
     print(f"Tagihannya {tagihan}, tipnya {tip:.2f}, dan total nilainya {total:.2f}")
