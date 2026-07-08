import bcrypt
from src.hasher import hash_password, verify_password


def test_hash_password_returns_string():
    password = "CyberSpec@123"

    hashed = hash_password(password)

    assert isinstance(hashed, str)


def test_hash_starts_with_bcrypt_identifier():
    password = "CyberSpec@123"

    hashed = hash_password(password)

    assert hashed.startswith("$2")


def test_same_password_produces_different_hashes():
    password = "CyberSpec@123"

    hash1 = hash_password(password)
    hash2 = hash_password(password)

    assert hash1 != hash2


def test_correct_password_verification():
    password = "CyberSpec@123"

    hashed = hash_password(password)

    assert verify_password(password, hashed)


def test_wrong_password_verification():
    password = "CyberSpec@123"

    hashed = hash_password(password)

    assert not verify_password("WrongPassword", hashed)


def test_hash_can_be_verified_multiple_times():
    password = "CyberSpec@123"

    hashed = hash_password(password)

    assert verify_password(password, hashed)
    assert verify_password(password, hashed)
    assert verify_password(password, hashed)


def test_bcrypt_generates_unique_salts():
    password = "CyberSpec@123"

    hashes = {hash_password(password) for _ in range(5)}

    assert len(hashes) == 5