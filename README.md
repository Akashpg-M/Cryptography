Secure Message Transmission System 

demonstrates a simple secure communication system that ensures:

Confidentiality – the message is encrypted before transmission
Integrity – the message cannot be altered without detection
Authentication – the receiver can verify the sender knows the shared password

The system follows the Encrypt-then-MAC approach

Components and Workflow:

1. Hash Function (cascade_hash)

A custom hash function is used to generate deterministic numeric values from input strings.

Takes a string as input
Applies bitwise XOR, multiplication, and shifting operations
Produces a 32-bit integer hash

This hash is used for:
Key generation
Message Authentication Code (MAC) generation

2. Key Generation (generate_shift_key)

A shift key is derived from the user-provided password.

The password is passed through the hash function
The result is reduced using modulo 26
This produces a value between 0–25

This key is used in the Caesar cipher for encryption and decryption.

3. Encryption (encrypt_caesar)

The plaintext message is encrypted using a Caesar cipher.

Each alphabetic character is shifted by the generated key
Uppercase and lowercase letters are handled separately
Non-alphabetic characters remain unchanged

The result is the ciphertext, which hides the original message.

4. Message Authentication Code (MAC) (generate_mac)

A MAC is generated to ensure message integrity and authenticity.
Combines the password and ciphertext
Passes the combined data through the hash function
Converts the result into a fixed-length hexadecimal string

The MAC ensures:
Any modification to the ciphertext will change the MAC
Only someone with the correct password can generate a valid MAC

5. Payload Construction (build_secure_payload)

The sender prepares the data for transmission.
Encrypts the plaintext
Generates a MAC for the ciphertext
Packages both into a payload:
{
  "ciphertext": "...",
  "mac": "..."
}


Receiver Side Processing

6. MAC Verification (verify_mac)

Before decryption, the receiver verifies message integrity.
Recomputes the MAC using the received ciphertext and password
Compares it with the received MAC using a constant-time comparison

If verification fails:
The message is rejected
Decryption is not performed

7. Decryption (decrypt_caesar)

If the MAC is valid, the receiver proceeds to decrypt.
Regenerates the same shift key using the password
Reverses the Caesar cipher shift
Recovers the original plaintext message

8. Secure Processing (receive_secure_payload)

This function coordinates the full receiver workflow:
Validates payload structure
Verifies MAC
Generates shift key
Decrypts ciphertext
Returns the original message
Security Model

This system demonstrates the Encrypt-then-MAC principle:

Encrypt the message
Generate a MAC over the ciphertext
Verify MAC before decryption

This ensures:

Tampered messages are detected early
Unauthorized modifications are rejected