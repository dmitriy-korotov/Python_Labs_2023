import random
import socket
from smtplib import SMTP
from smtplib import SMTPException
from utility import load_settings
from threading import Thread
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


APPLICATION_IS_RUNNING = True


def is_valid_email(_email: str) -> bool:
    return True


def build_mail_packet(_sender: str, _receiver: str, _subject: str, _message: str) -> MIMEMultipart:
    packet = MIMEMultipart()
    packet["From"] = _sender
    packet["To"] = _receiver
    packet["Subject"] = _subject
    packet.attach(MIMEText(_message, "plain"))
    return packet


def send_email_message_to(_dst_email: str, _message: str, _sender_data: tuple, _smtp_host_data: tuple) -> tuple:
    try:
        with SMTP(_smtp_host_data[0], _smtp_host_data[1]) as smtp_connect:
            smtp_connect.starttls()
            smtp_connect.login(_sender_data[0], _sender_data[1])

            subject = f"<[Ticket #{random.randint(1, int(1e6))}] Mailer>"

            client_mail_paket = build_mail_packet(_sender_data[0], _dst_email, subject, _message)
            smtp_connect.send_message(client_mail_paket)

            admin_mail_packet = build_mail_packet(_sender_data[0], _sender_data[0], subject, _message)
            smtp_connect.send_message(admin_mail_packet)

            smtp_connect.quit()

    except SMTPException as _ex:
        print(f"ERROR: {_ex.strerror}")
        return False, _ex.strerror

    return True, "OK"


def closing_handler(_close_command: str) -> None:
    global APPLICATION_IS_RUNNING
    while True:
        command = input()
        if command == _close_command:
            APPLICATION_IS_RUNNING = False
            break
        else:
            print("=> ERROR: Unknowing command")


def clients_handler(_address: str, _port: int, _settings: dict) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((_address, _port))
        server.listen()

        try:
            while True:
                connection, address = server.accept()
                print(f"=> Accept address: {address[0]}:{address[1]}")
                data = repr(connection.recv(1024))
                data = data[2: len(data) - 1]
                print(f"=> Received message")

                email, message = data.split(':')
                if not is_valid_email(email):
                    connection.send(b"This email is not exists")

                is_sent = send_email_message_to(email, message,
                                                (_settings["EMAIL_LOGIN"], _settings["EMAIL_PASSWORD"]),
                                                (_settings["SMTP_HOST"], _settings["SMTP_PORT"]))
                if is_sent[0]:
                    print("=> Successfully sent message")
                else:
                    print("=> Failed sending message")
                connection.send(bytearray(is_sent[1], "utf-8"))

        except IOError as _ex:
            print(f"ERROR: {_ex.strerror}")


def main() -> None:

    global APPLICATION_IS_RUNNING
    SETTINGS_FILE = "settings.env"

    settings = load_settings(SETTINGS_FILE)

    print("\t\t\tMailer server running...")
    print(f"=> email host: {settings['SMTP_HOST']}:{settings['SMTP_PORT']}")

    closing_handler_thread = Thread(target=closing_handler, args=("close",), daemon=True)
    clients_handler_thread = Thread(target=clients_handler,
                                    args=(settings["SERVER_ADDRESS"], int(settings["SERVER_PORT"]), settings), daemon=True)

    closing_handler_thread.start()
    clients_handler_thread.start()

    while True:
        if not APPLICATION_IS_RUNNING:
            break

    print("\t\t\tMailer server is closed")


if __name__ == "__main__":
    main()
