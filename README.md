# Train Application

![GitHub last commit](https://img.shields.io/github/last-commit/Substance-live/Train_application)

A train schedule management application built using **PySide6**. It allows users to view, add, and modify train schedules with a user-friendly graphical interface. The app interacts with a database to store and retrieve train data.

## Features
- View and manage train schedules
- Add, edit, or delete train information
- Search for train departures and arrivals
- User-friendly graphical interface created with PySide6
- Database-backed for storing train schedule information

## Libraries Used
The following libraries were used in the development of this project:
- PySide6
- PyMySQL

## Installation

To set up the project locally, you have two installation options:

### Option 1: Automatic Installation via `install.py`

Run the `install.py` script to automatically create a virtual environment, install the necessary dependencies, and set up the **.env** file:

1. Clone the repository:
    ```bash
    git clone https://github.com/Substance-live/Train_application.git
    cd Train_application
    ```

2. Run the `install.py` script:
    ```bash
    python install.py
    ```

This will:
- Create a virtual environment
- Install the dependencies from `requirements.txt`
- Set up a `.env` file (if it doesn't exist)

### Option 2: Manual Installation

Alternatively, you can manually set up the environment:

1. Clone the repository:
    ```bash
    git clone https://github.com/Substance-live/Train_application.git
    cd Train_application
    ```

2. Create and activate a virtual environment:

    - On **Windows**:
      ```bash
      python -m venv venv
      venv\Scripts\activate
      ```

    - On **macOS/Linux**:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Create **.env** file with Database configuration:
   ```
   DB_NAME=...
   DB_USER=...
   DB_PASSWORD=...
   DB_HOST=...
   ```

6. Set up the database:
   If you don't have an existing database, you can use the `dump_bd.sql` file to create one. Simply execute the SQL script in your SQL database management tool.

### Starting the Application

Once the setup is complete, run the application:

```bash
python main.py
```

## Contributing
Have ideas or want to help? Fork the repo and make it better — whether it's new features, improvements, or bug fixes!

Issues and pull requests are welcome. ✨
