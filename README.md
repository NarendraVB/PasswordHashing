# Password Hashing Demo

## Overview

Password Hashing Demo is a Python-based cybersecurity project that demonstrates how modern applications securely store and verify user passwords.

The project explains why passwords should never be stored in plaintext and showcases industry-standard password hashing using **bcrypt**. It also compares bcrypt with SHA-256, benchmarks different bcrypt cost factors, and visualizes how random salts protect against rainbow table attacks.

This project focuses on cybersecurity concepts first and implementation second.

---

## Cybersecurity Concepts

- Authentication
- Password Hashing
- Cryptographic Hash Functions
- bcrypt
- Salting
- Cost Factor (Work Factor)
- Adaptive Hashing
- Password Verification
- Rainbow Tables
- Offline Password Cracking
- Dictionary Attacks
- SHA-256 vs bcrypt
- Security vs Performance Trade-offs

---

## Attacker Perspective

If an attacker gains access to a leaked password database:

- Plaintext passwords are immediately compromised.
- Fast hash algorithms such as SHA-256 allow attackers to test millions or billions of password guesses quickly.
- Without salts, identical passwords produce identical hashes, making rainbow table attacks practical.

---

## Defender Perspective

Modern authentication systems protect passwords by:

- Never storing plaintext passwords.
- Hashing passwords using bcrypt.
- Automatically generating a unique random salt for every password.
- Choosing an appropriate bcrypt cost factor to slow offline attacks.
- Verifying passwords using bcrypt without ever decrypting stored hashes.

---

## Features

- Password Hashing using bcrypt
- Password Verification
- bcrypt Cost Factor Benchmark
- SHA-256 vs bcrypt Performance Comparison
- Salt Visualization Demo
- Professional CLI Interface

---

## Project Structure

```
PasswordHashingDemo/

├── src/
│   ├── __init__.py
│   ├── hasher.py
│   ├── benchmark.py
│   ├── comparison.py
│   ├── salt_demo.py
│   └── utils.py
│
├── tests/
│   └── test_hasher.py
│
├── README.md
├── requirements.txt
├── .gitignore
└── main.py
```

---

## Installation

Clone the repository

```bash
git clone <repository-url>
cd PasswordHashingDemo
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python main.py
```

---

## Example Output

```
===== Password Hashing Demo =====

1. Hash Password
2. Verify Password
3. Benchmark Cost Factor
4. Compare SHA-256 vs bcrypt
5. Salt Demonstration
6. Exit
```

---

## What I Learned

- Why passwords should never be stored in plaintext.
- Difference between hashing and encryption.
- Why bcrypt is preferred for password storage.
- How salts prevent rainbow table attacks.
- Why bcrypt hashes differ even for identical passwords.
- How bcrypt verifies passwords using embedded salts.
- Why slow hashing protects against offline attacks.
- Security vs usability trade-offs when selecting a cost factor.

---

## Future Improvements

- Support Argon2 password hashing.
- Add password pepper demonstration.
- Store user credentials in SQLite.
- Build a complete authentication system.
- Add user registration and login.
- Implement JWT authentication.
- Build a web interface using FastAPI.
- Add unit test coverage for all modules.