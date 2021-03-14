from hashlib import sha256


def encrypt_string(hash_string):
    """SHA256 Encrypting"""
    return sha256(hash_string.encode()).hexdigest()


s = "This is a string"
sha_signature = encrypt_string(s)
print(sha_signature)
