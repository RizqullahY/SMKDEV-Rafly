# basic challenge - smkdev
# data 1

massa_udin = 78
tinggi_udin = 1.69

massa_nanang = 92
tinggi_nanang = 1.95

bmi_udin =round(massa_udin/tinggi_udin**2 , 2)  # round untuk membatasi jumlah angka dibelakang koma pada tipe float
bmi_nanang = round(massa_nanang/tinggi_nanang** 2, 2)

bmi_udin_lebih_tinggi = bmi_udin > bmi_nanang 

if bmi_udin_lebih_tinggi == True:
   print (f"BMI Udin ({bmi_udin}) lebih tinggi dari Nanang ({bmi_nanang})!")
else:
   print (f"BMI Udin ({bmi_udin}) tidak lebih tinggi dari Nanang ({bmi_nanang})!")


# data 2

massa_udin2 = 95
tinggi_udin2 = 1.88

massa_nanang2 = 85
tinggi_nanang2 = 1.76

bmi_udin2 =round(massa_udin2/tinggi_udin2**2 , 2)  
bmi_nanang2 = round(massa_nanang2/tinggi_nanang2** 2, 2)

bmi_udin_lebih_tinggi2 = bmi_udin2 > bmi_nanang2 

if bmi_udin_lebih_tinggi2 == True:
   print (f"BMI Udin ({bmi_udin2}) lebih tinggi dari Nanang ({bmi_nanang2})!")
else:
   print (f"BMI Udin ({bmi_udin2}) tidak lebih tinggi dari Nanang ({bmi_nanang2})!")
