# src/comparison.py

import hashlib
import bcrypt
import time


def compare_algorithms(password: str):
    password_bytes = password.encode("utf-8")

    print("\n===== SHA-256 vs bcrypt =====\n")

    # SHA-256
    start = time.perf_counter()

    sha_hash = hashlib.sha256(password_bytes).hexdigest()

    end = time.perf_counter()

    sha_time = (end - start) * 1000

    print("SHA-256")
    print("-" * 30)
    print(f"Hash : {sha_hash}")
    print(f"Time : {sha_time:.4f} ms\n")

    # bcrypt
    start = time.perf_counter()

    bcrypt_hash = bcrypt.hashpw(
        password_bytes,
        bcrypt.gensalt(rounds=12)
    )

    end = time.perf_counter()

    bcrypt_time = (end - start) * 1000

    print("bcrypt")
    print("-" * 30)
    print(f"Hash : {bcrypt_hash.decode()}")
    print(f"Time : {bcrypt_time:.2f} ms")