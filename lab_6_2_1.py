from threading import Thread
from multiprocessing import Semaphore


counter = 0
locker = None


def increment() -> None:
    global counter
    global locker
    if locker is None:
        counter += 1
    else:
        with locker:
            counter += 1


def increment_n(_n: int) -> None:
    for _ in range(_n):
        increment()


def error_callback(_error) -> None:
    print(_error, flush=True)


def main() -> None:
    global counter

    thread1 = Thread(target=increment_n, args=(1000000,))
    thread2 = Thread(target=increment_n, args=(1000000,))
    thread3 = Thread(target=increment_n, args=(1000000,))

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

    print(f"Counter = {counter}")
    assert counter == 3000000


if __name__ == "__main__":
    main()
