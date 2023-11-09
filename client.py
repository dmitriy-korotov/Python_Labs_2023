from utility import load_settings
import re
import socket


def input_email(_label: str) -> str:
    email_regex = r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$"
    while True:
        email = input(_label)
        if re.match(email_regex, email):
            return email
        print("=> ERROR: Invalid email format, try something like this (example@gmail.com)")


def input_message(_label: str) -> str:
    return input(_label)


def main() -> None:

    SETTINGS_FILE = "settings.env"

    print("\t\t\tMailer client running...")

    settings = load_settings(SETTINGS_FILE)

    while True:
        email = input_email("=> Input email address:\t")
        message = input("=> Input your message:\t")

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((settings["SERVER_ADDRESS"], int(settings["SERVER_PORT"])))
            client.send(bytearray(f"{email}:{message}", "utf-8"))

            reply = repr(client.recv(1024))
            reply = reply[2: len(reply) - 1]
            if reply == "OK":
                print("=> Message successfully sent")
                break
            print(f"=> ERROR: {reply}")

    print("\t\t\tMailer client closed")


if __name__ == "__main__":
    main()
