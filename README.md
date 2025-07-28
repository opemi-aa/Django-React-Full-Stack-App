# Django-React-Full-Stack-App

This is a full-stack note-taking application built with a focus on features essential for enterprise and regulated environments.

*   **Backend:** A Django-based API that allows users to create, view, and delete notes. It uses Django REST Framework to expose the API endpoints and Simple JWT for token-based authentication. It's configured to use a PostgreSQL database.
*   **Frontend:** A React application built with Vite that provides the user interface for the note-taking app. It allows users to register, log in, and then create, view, and delete their notes. It uses `axios` to communicate with the backend API and `react-router-dom` for navigation.

## Key Enterprise Features

This project has been enhanced with several features that are critical for applications in a professional, regulated industry like financial services:

*   **Immutable Audit Trail:** Every key action (note creation, deletion) is recorded in a permanent, unchangeable `ActionLog`. This provides a complete history of activities for compliance and security reviews.
*   **Professional Admin Interface:** A secure, built-in Django Admin panel is configured for administrators. It provides a user-friendly web interface to review the audit trail, with appropriate permissions to ensure the log cannot be altered.
*   **Soft Delete for Data Preservation:** Notes are never permanently deleted from the database. Instead, they are marked as "inactive" (soft-deleted), preserving data history for potential audits while hiding it from the user's primary view.
*   **Automated User Communication:** New users automatically receive a welcome email upon registration, demonstrating integration with external services and a focus on the complete user lifecycle.

## How to run it locally:

### Backend (Django):

1.  **Navigate to the backend directory:**
    ```bash
    cd Django-React-Full-Stack-App/backend
    ```
2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```
3.  **Activate the virtual environment:**
    *   On Windows:
        ```bash
        venv\Scripts\activate
        ```
    *   On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```
4.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Set up the database:** Since it's configured for PostgreSQL, you'll need to have PostgreSQL installed and running. You'll also need to create a database and configure the connection in `backend/settings.py`.
6.  **Run the database migrations:**
    ```bash
    python manage.py migrate
    ```
7.  **Create a superuser to access the Admin panel:**
    ```bash
    python manage.py createsuperuser
    ```
8.  **Start the Django development server:**
    ```bash
    python manage.py runserver
    ```
    *The Admin panel is available at `http://127.0.0.1:8000/admin/`*

### Frontend (React):

1.  **Navigate to the frontend directory:**
    ```bash
    cd Django-React-Full-Stack-App/frontend
    ```
2.  **Install the dependencies:**
    ```bash
    npm install
    ```
3.  **Start the Vite development server:**
    ```bash
    npm run dev
    ```

After completing these steps, you should be able to access the application in your browser at the address provided by Vite (usually `http://localhost:5173`).
