# Simple Cipher

A small Python command-line tool that encrypts and decrypts text using a custom reversible formula and two randomly generated keys.

⚠️ **This is a learning project, not a real security tool.** The cipher is easy to break and should never be used to protect sensitive information.

## How it works

1. The message is reversed.
2. Each character's Unicode code point is transformed using two random keys:
   ```
   encrypted_value = ((ord(char) / 2) + key1 - key2) / 2
   ```
3. To decrypt, the same keys are used to reverse the formula and rebuild the original message.

Because the keys are generated randomly each time you encrypt, **you must save key1 and key2** — without them, the message cannot be decrypted.

## Requirements

- Python 3.9 or later (no external libraries needed)

## Usage

Clone the repo and run the script:

```bash
git clone https://github.com/4hmed-kr/simple-cipher.git
cd simple-cipher
python3 encryption.py
```

You'll be prompted to choose an action:

```
Encrypt [1] | Decrypt [2]:
```

### Encrypting a message

```
Encrypt [1] | Decrypt [2]: 1
Enter your message to encrypt: hello world

Encrypted message: 2788.0 2790.0 2791.5 2790.75 2792.75 2771.0 2790.75 2790.0 2790.0 2788.25 2789.0
Keys — key1: 7405 | key2: 1879
Keep these keys safe, you'll need them to decrypt!
```

### Decrypting a message

```
Encrypt [1] | Decrypt [2]: 2
Enter the encrypted message: 2788.0 2790.0 2791.5 2790.75 2792.75 2771.0 2790.75 2790.0 2790.0 2788.25 2789.0
key 1: 7405
key 2: 1879

Decrypted message: hello world
```

After each operation, you'll be asked if you want to encrypt or decrypt another message.

## Example (Python)

You can also import the functions directly:

```python
from encryption import encrypt, decrypt, generate_keys

key1, key2 = generate_keys()
cipher = encrypt("hello world", key1, key2)
message = decrypt(cipher, key1, key2)

print(cipher)
print(message)
```

## License

This project is open source and available under the [MIT License](LICENSE).
