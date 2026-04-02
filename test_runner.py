from ceaser_cipher import build_secure_payload, receive_secure_payload

def run_tests():
    print("SECURE TRANSMISSION TEST RUNNER\n\n")

    print("EXAMPLE 1\n")
    original_message_1 = "Meet me at the secure location at midnight!"
    password_1 = "SuperSecretPassword123"
    
    print(f"Original Plaintext: '{original_message_1}'")
    print(f"Using Password:     '{password_1}'\n")

    payload_1 = build_secure_payload(original_message_1, password_1)
    print("Sender Transmitting Payload")
    print(f"Ciphertext: {payload_1['ciphertext']}")
    print(f"MAC:        {payload_1['mac']}\n")

    try:
        revealed_message_1 = receive_secure_payload(payload_1, password_1)
        print(f"SUCCESS! Decrypted Message: '{revealed_message_1}'\n")
    except ValueError as e:
        print(f"ERROR: {e}\n")


    print("\n\n")


    print("EXAMPLE 2\n")
    original_message_2 = "The eagle has landed. Initiate phase two."
    password_2 = "AlphaBravoCharlie456"
    
    print(f"Original Plaintext: '{original_message_2}'")
    print(f"Using Password:     '{password_2}'\n")

    payload_2 = build_secure_payload(original_message_2, password_2)
    print("Sender Transmitting Payload")
    print(f"Ciphertext: {payload_2['ciphertext']}")
    print(f"MAC:        {payload_2['mac']}\n")

    try:
        revealed_message_2 = receive_secure_payload(payload_2, password_2)
        print(f"SUCCESS! Decrypted Message: '{revealed_message_2}'\n")
    except ValueError as e:
        print(f"ERROR: {e}\n")


run_tests()