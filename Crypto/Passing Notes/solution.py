import sys
import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

solution="vyLlwWSY1PCK5ELNTPUVdpl8z0rIXiB2+Ybcu/BeXidR3MEiym852HCkS6wHVCr+CdpP6Moe9VQUeFcyq3vZDpVK/orl+8vREYMRrnQR9O4="
BS = 16
# crackstation can easily crack the hashed secret
secret = b"supersecretpassword"
key = SHA256.new()
key.update(secret)

def decrypt(key, message):
    # IV is included in the base64-encoded string as the first 16 bytes
    iv = base64.b64decode(solution)[:BS]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.decrypt(base64.b64decode(message)[BS:])

print(decrypt(key.digest(),solution))
