from multiprocessing import Pool
from multiprocessing import Semaphore


def increment(_target: int, _locker: Semaphore = None) -> None:
    if _locker is None:
        _target += 1
    else:
        with _locker:
            _target += 1
            print("add")


def increment_n(_target: int, _n: int, _locker: Semaphore = None) -> None:
    for _ in range(_n):
        increment(_target, _locker)


def error_callback(_error) -> None:
    print(_error, flush=True)


counter = 0
locker = Semaphore(10)


def main() -> None:

    with Pool(5) as pool:
        pool.starmap(increment_n, [(counter, 1000, locker) for _ in range(5)])

    print(f"Counter = {counter}")
    assert counter == 5000


if __name__ == "__main__":
    main()