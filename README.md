# RaspberryPi-HomeAccessoryControl

A Django-based web application for controlling home accessories using a Raspberry Pi. This project includes a user-friendly interface to toggle the status of various accessories and visual feedback for each accessory's state.

## Features

- List all connected home accessories
- Toggle the status of each accessory (On/Off)
- Visual feedback indicating the status of each accessory
- Admin panel for managing accessories

## Requirements

- Raspberry Pi 4 Model B
- Python 3
- Django
- RPi.GPIO

## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/RaspberryPi-HomeAccessoryControl.git
    cd RaspberryPi-HomeAccessoryControl
    ```

2. **Create and Activate a Virtual Environment**
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. **Install the Dependencies**
    ```bash
    pip install django RPi.GPIO
    ```

4. **Run Migrations**
    ```bash
    python manage.py migrate
    ```

5. **Create a Superuser**
    ```bash
    python manage.py createsuperuser
    ```

6. **Start the Development Server**
    ```bash
    python manage.py runserver 0.0.0.0:8000
    ```

7. **Access the Application**
    Open a web browser and go to `http://<your-raspberry-pi-ip>:8000`

## Usage

- **Admin Panel**
    - Go to `http://<your-raspberry-pi-ip>:8000/admin`
    - Log in with the superuser account you created
    - Add and manage accessories

- **Main Application**
    - The main page lists all accessories with their current status
    - Click on an accessory to toggle its status

## Code Structure

- `smart_home/`: Main Django project directory
- `control/`: Django app for handling accessories
    - `models.py`: Defines the `Accessory` model
    - `views.py`: Contains views for listing and toggling accessories
    - `admin.py`: Registers the `Accessory` model in the admin panel
    - `templates/accessory_list.html`: Template for displaying accessories
    - `static/style.css`: CSS styles for the application

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Contact

For any questions or suggestions, please contact [magicbulletsoft@gmail.com](mailto:magicbulletsoft@gmail.com).
