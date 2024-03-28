import pickle
import socket


from django.core.management import BaseCommand
from cryptography.fernet import Fernet

from config.settings import HOST, PORT, ENCRYPTION_KEY

cipher = Fernet(ENCRYPTION_KEY.encode())


def validate_car_data(data):
    value_list = [value for key, value in data.items()]

    if not all([isinstance(value, str) for value in value_list]):
        raise ValueError("Car data should be strings")

    if not all([value for value in value_list]):
        raise ValueError("Car data shouldn't be empty")


def encrypt_car_data(data):
    return cipher.encrypt(data)


def send_car_data(name: str, color: str, brand: str):
    data = {"name": name, "color": color, "brand": brand}

    validate_car_data(data)

    pickled_data = pickle.dumps(data)
    encrypted_data = encrypt_car_data(pickled_data)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        client_socket.sendall(encrypted_data)
        print("Data sent to server successfully")


class Command(BaseCommand):

    def handle(self, *args, **options):
        name = input("Enter car name: ")
        color = input("Enter car color: ")
        brand = input("Enter car brand: ")

        send_car_data(name, color, brand)
