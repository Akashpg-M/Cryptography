import hmac

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
    return raw_hash % 26


def generate_mac(ciphertext: str, password: str) -> str:
    combined_data = password + "|" + ciphertext
    raw_hash = cascade_hash(combined_data)
    return format(raw_hash, '08x')


def verify_mac(received_ciphertext: str, received_mac: str, password: str) -> bool:
    calculated_mac = generate_mac(received_ciphertext, password)
    return hmac.compare_digest(calculated_mac, received_mac)


def decrypt_caesar(ciphertext: str, shift: int) -> str:
    plaintext = ""

    for char in ciphertext:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            shifted_ascii = (ord(char) - ascii_offset - shift) % 26
            plaintext += chr(shifted_ascii + ascii_offset)
        else:
            plaintext += char

    return plaintext


def receive_secure_payload(payload: dict, password: str) -> str:
    if "ciphertext" not in payload or "mac" not in payload:
        raise ValueError("Invalid payload format")

    ciphertext = payload["ciphertext"]
    received_mac = payload["mac"]

    print("System: Verifying message integrity...")
    is_authentic = verify_mac(ciphertext, received_mac, password)

    if not is_authentic:
        raise ValueError("SECURITY ALERT: MAC verification failed! The message was tampered with or the password is wrong.")

    print("System: Integrity verified. Message is authentic.")

    shift_key = generate_shift_key(password)

    print("System: Decrypting payload...")
    plaintext = decrypt_caesar(ciphertext, shift_key)

    return plaintext


incoming_payload = {
    'ciphertext': 'Rjjy rj fy ymj xjhzwj qthfynts fy rnisnlmy!',
    'mac': 'f33ac44e'
}

receiver_password = "SuperSecretPassword123"

try:
    revealed_message = receive_secure_payload(incoming_payload, receiver_password)
    print("\nINCOMING MESSAGE")
    print(revealed_message)
except ValueError as e:
    print(f"\n{e}")
