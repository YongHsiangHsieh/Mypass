# README for Python-based Password Manager

## Table of Contents

- [Introduction](#introduction)
- [Technologies](#technologies)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project is a simple but powerful Password Manager built with Python. Using SQLite for its database and Tkinter for the graphical interface, the application allows you to store, generate, and manage your passwords securely.

## Technologies

- Python 3.x
- SQLite
- Tkinter

## Features

- **Secure Storage**: Safely stores your passwords in an SQLite database.
- **Random Password Generator**: Generates strong, unique passwords for you.
- **Clipboard Support**: Directly copies passwords to your clipboard.
  
## Setup

1. **Clone the Repository**

    ```bash
    git clone https://github.com/YongHsiangHsieh/Password-Manager.git
    ```

2. **Navigate to the Project Directory**

    ```bash
    cd Password-Manager
    ```

3. **Install Dependencies**

    Since the project uses only Python's standard libraries, there are no additional dependencies to install.

4. **Initialize Database**

    Simply run the application, and it will automatically create a database file if it doesn't exist.

## Usage

1. **Run the Application**

    ```bash
    python main.py
    ```

2. **Add a New Password**
    - Click on the "Add" button.
    - Fill in the website, email, and password fields.
    - Click "Save."

3. **Generate a Random Password**
    - Click on the "Generate" button, and a strong password will be generated and copied to your clipboard.

4. **Search for a Password**
    - Use the search bar to find stored passwords by website name.

## Contributing

Feel free to fork the project, make some changes, and submit pull requests. The project is open for enhancements.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
