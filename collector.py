import base64
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
    pattern = r"<\[Ticket #\d+\] Mailer>"
    return bool(re.fullmatch(pattern, _subject))


def get_id_from_subject(_subject: str) -> str:
    ID = ""
    start = _subject.find('#') + 1
    while _subject[start].isdigit():
        ID += _subject[start]
        start += 1
    return ID


def letters_handler(_settings: dict) -> None:
    imap_host = _settings["IMAP_HOST"]
    imap_port = _settings["IMAP_PORT"]

    admin_login = _settings["EMAIL_LOGIN"]
    admin_password = _settings["EMAIL_PASSWORD"]

    period_check = int(_settings["PERIOD_CHECK"])

    with imaplib.IMAP4_SSL(imap_host) as connection:
        connection.login(admin_login, admin_password)
        connection.select("INBOX/ToMyself")

        while True:
            print("=> Email checked")

            status, uid_list_str = connection.uid("search", "UNSEEN")
            if status != "OK":
                print("=> ERROR: Can't get access to letters uid")
                continue

            str_uid_list = str(uid_list_str)
            str_uid_list = str_uid_list[str_uid_list.find("\'") + 1: str_uid_list.rfind("\'")]
            uid_list = [uid_str for uid_str in str_uid_list.split() if uid_str.isdigit()]

            print(f"=> Messages count: {len(uid_list)}")

            for uid in uid_list:
                res, message = connection.uid("fetch", uid, "(RFC822)")

                if message[0] is None:
                    continue

                message = email.message_from_bytes(message[0][1])
                subject = message["Subject"]

                content = ""

                if is_valid_subject(subject):
                    if message.is_multipart():
                        for part in message.walk():
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))
                            try:
                                body = part.get_payload(decode=True).decode()
                            except:
                                pass
                            if content_type == "text/plain" and "attachment" not in content_disposition:
                                content += body

                    log_message(f"[SUCCESS] ID: {get_id_from_subject(subject)} => message: {content}\n", _settings["SUCCESS_LOG"])
                else:
                    log_message(f"[ERROR] Invalid subject: {subject} => message: {content}\n", _settings["ERROR_LOG"])

                print("=> Message checked")

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
