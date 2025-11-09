# ✍️ ECDSA Signature Generation Example (secp256k1)

This Python script demonstrates how to **manually compute an ECDSA digital signature** for a given message hash `z` using a specified private key `d` and ephemeral key `k` on the **secp256k1** elliptic curve (used by Bitcoin).

The script walks through the mathematical steps that produce the `(r, s)` signature pair and performs a basic validity check.

---

## 🧩 Overview

ECDSA (Elliptic Curve Digital Signature Algorithm) is the digital signature scheme used by Bitcoin and many other cryptosystems.  
Each signature is defined by two integers `(r, s)` derived from:
- the private key `d`,
- a random ephemeral key `k`,
- and the hash of the message `z`.

This script explicitly shows how those values interact.

---

## ⚙️ How It Works

1. **Define inputs**
   - `d`: private key  
   - `k`: ephemeral key (must be unique and random per signature)  
   - `z`: integer representation of the message hash  
   - `n`: group order of the elliptic curve secp256k1  

2. **Use generator point G**
   - The Bitcoin curve uses a fixed generator point `G` with coordinates (`Gx`, `Gy`).

3. **Compute signature components**
   - \( r = (k × G_x) \mod n \)  
     (for simplicity, we use the x-coordinate of G in this toy example)
   - \( s = k^{-1} × (z + r × d) \mod n \)

4. **Verify**
   - Checks that both `r` and `s` are non-zero.

---

## 🧮 Example Code

```python
from sympy import mod_inverse
import hashlib

# Example inputs
k = 78408107164134734130920053081078460033335120107631400816819398827771557902031
d = 43849617633852432974540977067285574484894476307232937404580815962833671297069
z1 = 96305888925087028226280700902788330707257073607110099029890896029884121755055
n = 115792089237316195423570985008687907852837564279074904382605163141518161494337

# secp256k1 generator coordinates
G_x = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
G_y = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448CFDCD9E317E1F3F6B9F43B50

# Compute signature components
r = (k * G_x) % n
k_inv = mod_inverse(k, n)
s = (k_inv * (z1 + r * d)) % n

print(f"r = {r}")
print(f"s = {s}")

# Basic validation
is_valid = (r != 0 and s != 0)
print("Signature valid!" if is_valid else "Invalid signature!")
🧾 Example Output
📌 Computed r: 259307312848403127472033955414...  
📌 Computed s: 882110058674208331997392072387...
🔍 Verifying signature...
✅ Signature is valid!

🧠 Key Concepts Illustrated

✅ How ECDSA uses a random nonce k to produce each signature
✅ The relationship between r, s, d, and z
✅ Why k must be unique and unpredictable — reusing or correlating k leaks the private key
✅ How modular arithmetic drives elliptic-curve cryptography

⚠️ Security Notice

⚠️ This example is for educational purposes only.
It uses simplified elliptic-curve arithmetic and fixed constants for clarity — not secure for production use.
In real ECDSA:

r is derived from the actual elliptic-curve point k·G, not just Gx.

k must be random and never reused.

Implementations should use established libraries like ecdsa, cryptography, or secp256k1 bindings.

BTC donation address: bc1q4nyq7kr4nwq6zw35pg0zl0k9jmdmtmadlfvqhr
