def max_subarray_sum(arr):
   max_sum = float('-inf')
   current_sum = 0
   for num in arr:
      current_sum = max(num, current_sum + num)
      max_sum = max(max_sum, current_sum)

   return max_sum

# Input
n = int(input("Masukkan jumlah elemen dalam larik: "))
arr = list(map(int, input("Masukkan elemen-elemen larik (pisahkan dengan spasi): ").split()))

# Output
result = max_subarray_sum(arr)
print("Jumlah maksimum dari suatu subarray berurutan adalah:", result)
