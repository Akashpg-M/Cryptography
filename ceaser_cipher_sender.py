def cascade_hash(string_data: str) -> int:
    hash_value = 104729     
    multiplier = 65599  
    for char in string_data:
        hash_value = hash_value ^ ord(char)        
        hash_value = (hash_value * multiplier) % (2**32)        
        hash_value = hash_value ^ (hash_value >> 5)
        
    return hash_value

def generate_shift_key(password: str) -> int:
    raw_hash = cascade_hash(password)
    shift_key = raw_hash % 26
    
    return shift_key

def encrypt_caesar(plaintext: str, shift: int) -> str:
    ciphertext = ""
    
    for char in plaintext:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')            
            shifted_ascii = (ord(char) - ascii_offset + shift) % 26
            ciphertext += chr(shifted_ascii + ascii_offset)
        else:
            ciphertext += char
            
    return ciphertext

def generate_mac(ciphertext: str, password: str) -> str:
    combined_data = password + "|" + ciphertext
    raw_hash = cascade_hash(combined_data)
    return format(raw_hash, '08x')

def build_secure_payload(plaintext: str, password: str) -> dict:
    shift_key = generate_shift_key(password)    
    encrypted_text = encrypt_caesar(plaintext, shift_key)    
    message_mac = generate_mac(encrypted_text, password)
    
    return {
        "ciphertext": encrypted_text,
        "mac": message_mac
    }

secret_message = "Meet me at the secure location at midnight!"
user_password = "SuperSecretPassword123"

payload = build_secure_payload(secret_message, user_password)

print("Payload Ready for Transmission")
print(f"Ciphertext: {payload['ciphertext']}")
print(f"MAC:        {payload['mac']}")