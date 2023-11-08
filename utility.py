import os


def load_settings(_filename: str, _sep='=') -> dict:
    if not os.path.isfile(_filename):
        print("ERROR: File with settings not found")
        return dict()

    settings = dict()
    with open(_filename, "r") as file:

        for line in file.readlines():
            key, value = line.split(_sep)
            settings[key.strip()] = value.strip()
    return settings


if __name__ == "__main__":
    pass
