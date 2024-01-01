from itertools import permutations

def calculate_distance(city1, city2):
   return abs(city1[0] - city2[0]) + abs(city1[1] - city2[1])

def total_distance(route, cities):
   distance = 0
   for i in range(len(route) - 1):
      distance += calculate_distance(cities[route[i]], cities[route[i+1]])
   distance += calculate_distance(cities[route[-1]], cities[route[0]])  # Kembali ke kota awal
   return distance

# Input
N = int(input())  # Jumlah kota
cities = [tuple(map(int, input().split())) for _ in range(N)]  # Koordinat setiap kota

# Membuat semua kemungkinan rute
all_routes = permutations(range(N))

# Inisialisasi variabel untuk menyimpan hasil terbaik
best_route = None
min_distance = float('inf')

# Pencarian rute optimal
for route in all_routes:
   distance = total_distance(route, cities)
   if distance < min_distance:
      min_distance = distance
      best_route = route

# Output
print("Rute optimal:")
for city in best_route:
   print("City", city + 1, end=" -> ")
print("City 1")
print("Total jarak tempuh minimal:", min_distance)
