# Test Task 2

🚀 This project implements a client-server program to load data into the database using encryption. The client sends data in encrypted form to the server, which decrypts it and adds it to the database.

## Installation

### Without Docker

1. **Clone the repository:**
    ```bash
    git clone https://github.com/kostomeister/socket-encrypt.git
    ```

2. **SetUp Project(In terminal):**
   * For Windows: 
    ```bash
    .\run_app_windows.bat
    ```
   * For Linux:
   ```bash
   .\run_app_linux.sh
   ```

### With Docker(Recommended)

1. **Clone the repository:**
    ```bash
    git clone https://github.com/kostomeister/socket-encrypt.git
    ```

2. **Build and run the container:**
    ```bash
    docker-compose up --build
    ```

## Features

- Encrypted data transmission 🔒
- Secure server-client communication 🛡️
- Django admin panel for data management 🖥️

## Configuration

To configure the project, copy the `.env.sample` file to `.env` and adjust the values as needed(You can use default values)


## Credentials

- Admin Panel:
  - Username: admin
  - Password: 123321

## API Endpoint

You can access the API endpoint to view cars data at `/api/cars/`.

## Usage

1. **Run the server:**
    - In Docker: Execute `docker exec -it socket_encrypt bash` to open a bash shell in the Docker container, then run `python manage.py server`.
    - Without Docker: Run `python manage.py server`.
    
2. **Run the client:**
    - In Docker: Execute `docker exec -it socket_encrypt bash` to open a bash shell in the Docker container, then run `python manage.py client`.
    - Without Docker: Run `python manage.py client`.

3. Follow the on-screen instructions to enter data.
4. Check the data in your database through the Django admin interface.

## Contributions

If you want to contribute to the project, please create a pull request in the repository.
