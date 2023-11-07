import os
import time
from multiprocessing import Pool
from threading import Thread


def search_files(search_dir: str, key_word: str, extension: str = "txt", with_threads: True = False) -> None:

    for directory in os.listdir(search_dir):

        if os.path.isfile(search_dir + "/" + directory):
            if directory.split('.')[-1] == extension:
                if directory.find(key_word) != -1:
                    print(search_dir + "/" + directory)
            continue

        if os.path.isdir(search_dir + "/" + directory):
            if with_threads:
                thread = Thread(target=search_files,
                                args=(search_dir + "/" + directory, key_word, extension, with_threads))
                thread.run()
            else:
                search_files(search_dir + "/" + directory, key_word, extension, with_threads)


def main() -> None:

    key = "Task"
    extension = "cpp"
    search_directory = "C:/Users/User/MyProjects"

    before = time.time()
    search_files(search_directory, key, extension)
    after = time.time()

    print(f"Search files without threads: {after - before}s")

    before = time.time()
    search_files(search_directory, key, extension, True)
    after = time.time()

    print(f"Search files with threads: {after - before}s")


if __name__ == "__main__":
    main()
