
import time
import bcrypt


def benchmark_password(password: str):
    password_bytes = password.encode("utf-8")

    print("\n===== bcrypt Benchmark =====\n")

    for cost in range(10, 15):
        start = time.perf_counter()

        bcrypt.hashpw(
            password_bytes,
            bcrypt.gensalt(rounds=cost)
        )

        end = time.perf_counter()

        elapsed_ms = (end - start) * 1000

        print(f"Cost {cost}: {elapsed_ms:.2f} ms")