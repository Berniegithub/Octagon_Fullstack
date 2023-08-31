
**Fullstack Login, Register, View Profile Project**
This is a **fullstack** project built using Vue.js and Django Rest Framework (DRF) for handling user authentication, registration, and profile viewing. This README provides an overview of the project and guidelines for running it.

**Project Overview**
This project is designed to demonstrate the implementation of user authentication, registration, and profile viewing in a fullstack application. It uses Vue.js for the frontend and Django Rest Framework (DRF) for the backend. Users can:

**Register**: Create a new account by providing a First Name, Last Name, Phone Number and password.
**Login**: Authenticate themselves with their registered credentials.
**View Profile**: Access their user profile information after logging in.

**Getting Started**
Follow these instructions to set up and run the project on your local machine.

**Prerequisites**
Python: Make sure you have Python 3.x installed. You can download it from Python's official website.

Node.js: Ensure you have Node.js and npm (Node Package Manager) installed. You can download them from Node.js official website.

Setting up the Backend (Django Rest Framework)
Clone the repository:
git clone <Backend_vuiAPI>
cd <Backend_vuiAPI>

Create a virtual environment and activate it (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows, use "venv\Scripts\activate"

python manage.py migrate

Create a superuser to access the Django admin panel:
python manage.py createsuperuser
Start the Django development server:
python manage.py runserver
The backend should now be running at http://localhost:8000/.

**Setting up the Frontend (Vue.js)**
Navigate to the frontend directory:
cd vue-project
Install the Node.js dependencies:
npm install
Create a .env file in the frontend directory with the following content:
Vue-project=http://localhost:8000/api/
This tells the Vue.js app where to find the backend API.

Start the Vue.js development server:
npm run serve
The frontend should now be running at http://localhost:8080/.

**Accessing the Application**
Open your web browser and navigate to http://localhost:8080/ to access the application. You can register a new account, log in, and view your profile.

**Project Structure**
Here's an overview of the project structure:

backend/: Contains the Django backend code.
frontend/: Contains the Vue.js frontend code.
frontend/src/components/: Vue.js components for login, registration, and profile viewing.
frontend/src/router/: Vue Router configuration.
frontend/src/axios-api/: API service for making requests to the backend.
**Additional Notes**
Make sure to customize and style the frontend as needed to match your project's design.
Ensure that the backend and frontend run concurrently during development.
Implement proper error handling and validation to enhance the user experience.
Review and adhere to security best practices for user authentication and data protection.
**Acknowledgments**
Octagon Africa Financial Services Limited System for Technical test interview.
