import pickle
import socket

from django.core.management import BaseCommand
from cryptography.fernet import Fernet

from config.settings import HOST, PORT, ENCRYPTION_KEY
from car.models import Car


cipher = Fernet(ENCRYPTION_KEY.encode())


def decrypt_data(data):
    return cipher.decrypt(data)


def server():
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((HOST, PORT))
            server_socket.listen()

            print("Server listening on", HOST, "port", PORT)

            conn, addr = server_socket.accept()
            with conn:
                print("Connected by", addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    decrypted_data = pickle.loads(decrypt_data(data))
                    car = Car(**decrypted_data)
                    car.save()
                    print("Received data:", decrypted_data)


class Command(BaseCommand):

    def handle(self, *args, **options):
        server()
