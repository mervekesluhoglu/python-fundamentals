import math

# ---------------------------------------------------------
# Proje: Öklid Mesafesi Hesaplayıcı (Algorithms)
# Amaç: İki boyutlu uzaydaki noktalar arasındaki mesafeyi hesaplama.
# ---------------------------------------------------------

def euclidean_distance(point1, point2):
    """
    İki nokta arasındaki Öklid mesafesini hesaplar.
    Noktalar (x, y) formatında demet (tuple) olmalıdır.
    """
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Örnek Veri Seti (Noktalar)
points = [(1, 2), (4, 6), (7, 8), (3, 5)]

# Tüm Nokta Çiftleri Arasındaki Mesafeleri Hesaplama
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclidean_distance(points[i], points[j])
        distances.append(dist)

# Minimum Mesafeyi Belirleme
min_dist = min(distances)

print(f"Tanımlı Noktalar: {points}")
print(f"Hesaplanan Tüm Mesafeler: {[round(d, 2) for d in distances]}")
print(f"Noktalar Arasındaki Minimum Mesafe: {min_dist:.2f}")
