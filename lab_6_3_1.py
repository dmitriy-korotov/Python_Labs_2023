import random
import time
from concurrent.futures import ProcessPoolExecutor


def compute_matrix_elem(p_i: float, q_i: float) -> float:
    return 1 / (1 + abs(q_i - p_i))


def compute_matrix_row(matrix: list, p: tuple, q: list) -> None:
    for i, q_i in enumerate(q):
        matrix[p[0]][i] = compute_matrix_elem(p[1], q_i)


def main() -> None:
    n = 5000

    p = [random.randint(1, 1000) for _ in range(n)]
    q = [random.randint(1, 1000) for _ in range(n)]

    matrix = [[0] * n] * n

    before = time.time()
    for i in range(n):
        for j in range(n):
            matrix[i][j] = compute_matrix_elem(p[i], q[j])
    after = time.time()

    print(f"Time without futures = {after - before}s")

    matrix = [[0] * n] * n
    with ProcessPoolExecutor() as executor:
        before = time.time()
        executor.map(compute_matrix_row, [(matrix, (i, p_i), q) for i, p_i in enumerate(p)])
        after = time.time()

    print(f"Time with futures = {after - before}s")


if __name__ == "__main__":
    main()
