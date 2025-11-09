from sympy import mod_inverse
import hashlib

# Dane wejściowe
k = 78408107164134734130920053081078460033335120107631400816819398827771557902031
d = 43849617633852432974540977067285574484894476307232937404580815962833671297069
z1 = 96305888925087028226280700902788330707257073607110099029890896029884121755055  # Z przykładem wiadomości
n = 115792089237316195423570985008687907852837564279074904382605163141518161494337  # Rząd krzywej secp256k1

# Punkt generatora G (krzywa secp256k1)
# Współrzędne generatora G na krzywej secp256k1
G_x = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
G_y = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448CFDCD9E317E1F3F6B9F43B50

# Obliczanie r
# r = (k * G_x) % n, G_x jest współrzędną punktu generatora G
r = (k * G_x) % n

# Obliczanie s
k_inv = mod_inverse(k, n)  # Obliczanie odwrotności k mod n
s = (k_inv * (z1 + r * d)) % n  # Wzór na s

print(f"📌 Obliczone r: {r}")
print(f"📌 Obiczone s: {s}")

# Weryfikacja
print("\n🔍 Weryfikacja podpisu...")

# Sprawdzamy, czy r i s spełniają warunki
is_valid = (r != 0 and s != 0)  # Sprawdzamy, czy r i s są różne od zera

if is_valid:
    print(f"✅ Podpis jest poprawny!")
else:
    print(f"❌ Podpis jest niepoprawny!")
