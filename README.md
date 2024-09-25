# README.md

# Greywolfx Company Website

## Description
Greywolfx is a dynamic web application designed to facilitate a marketplace for students, allowing them to buy and sell products. The platform includes features such as blog addition, blog , reviews, and a user-friendly dashboard.

## Features
- User authentication (sign up, login, logout)
- Product management (add, edit, delete products)
- Category management
- User profiles with personal information
- Comment and review system for products
- Responsive design for mobile and desktop

## Installation
To set up the project locally, follow these steps:

1. Clone the repository
    ```
   git clone https://github.com/Trent130/greywolfx-site.git
   cd greywolfx-site
    ```
3. Install dependencies
    ```
   pip install -r requirements.txt
    ```
5. Apply migrations
    ```
   python manage.py migrate
    ```
7. Create a superuser (optional)
    ```
   python manage.py createsuperuser
    ```
9. Run the development server
    ```
   python manage.py runserver
    ```


## Usage
After setting up the project, you can access it at 
```
http://127.0.0.1:8000/admin
```.
Use the following credentials to log in as an admin (if you created a superuser):

- Username: admin
- Password: your_password

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any inquiries, please reach out to [warsamegift@gmail.com](mailto:warsamegift@gmail.com).
