import imaplib
import email
from utility import load_settings
import time
import threading
import re


APPLICATION_IS_RUNNING = True


def log_message(_msg: str, _file: str) -> None:
    with open(_file, "a", encoding="utf-8") as log:
        log.write(f"=> {_msg}")


def is_valid_subject(_subject: str) -> bool:
    #pattern = r"^<[Ticket #[1-9]*] Mailer>"
    #re.match(pattern, _subject)
    return False


def get_id_from_subject(_subject: str) -> str:
    ID = ""
    start = _subject.find('#') + 1
    while _subject[start].isdigit():
        ID += _subject[start]
    return ID


def letters_handler(_settings: dict) -> None:
    imap_host = _settings["IMAP_HOST"]
    imap_port = _settings["IMAP_PORT"]

    admin_login = _settings["EMAIL_LOGIN"]
    admin_password = _settings["EMAIL_PASSWORD"]

    period_check = int(_settings["PERIOD_CHECK"])

    with imaplib.IMAP4_SSL(imap_host) as connection:
        connection.login(admin_login, admin_password)
        connection.select("inbox")

        while True:
            print("=> Email checked")

            status, uid_list_str = connection.uid("search", "ALL")
            print(uid_list_str)
            if status != "OK":
                print("=> ERROR: Can't get access to letters uid")
                continue

            uid_list = tuple(map(int, uid_list_str[0][2: len(uid_list_str[0]) - 1].split()))
            for uid in uid_list:
                res, message = connection.uid("fetch", str(uid), "(RFC822)")
                message = email.message_from_bytes(message[0][1])
                subject = message["Subject"]
                print(subject)
                if is_valid_subject(subject):
                    log_message(f"[SUCCESS] ID: {get_id_from_subject(subject)} => message: \n", _settings["SUCCESS_LOG"])
                else:
                    log_message(f"[ERROR] Message: \n", _settings["ERROR_LOG"])

            time.sleep(period_check)
        connection.close()
        connection.logout()


def closing_handler(_close_command: str) -> None:
    global APPLICATION_IS_RUNNING
    while True:
        command = input()
        if command == _close_command:
            APPLICATION_IS_RUNNING = False
            break
        else:
            print("=> ERROR: Unknowing command")


def main() -> None:

    print("\t\t\tMailer collector running...")

    SETTINGS_FILE = "settings.env"
    settings = load_settings(SETTINGS_FILE)

    closing_handler_thread = threading.Thread(target=closing_handler, args=("close",), daemon=True)
    letters_handler_thread = threading.Thread(target=letters_handler, args=(settings,), daemon=True)

    letters_handler_thread.start()
    closing_handler_thread.start()

    while True:
        if not APPLICATION_IS_RUNNING:
            break

    print("\t\t\tMailer collector closed")


if __name__ == "__main__":
    main()
