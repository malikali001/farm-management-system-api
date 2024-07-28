# Goat Farm Management System

The Goat Farm Management System is a comprehensive Django REST framework API designed to streamline the management of goats on a farm. The system supports role-based access control, ensuring that managers can only perform CRUD operations on goats they manage, while administrators have broader access to all goats and can assign managers to goats.

## Key Features

- **Role-Based Access Control**:
  - **Managers** can perform CRUD operations only on the goats they manage.
  - **Admins** have full access to all goats and can assign managers to goats.
- **Custom Validation Logic**: Ensures data integrity by validating user roles and permissions during CRUD operations.
- **RESTful API**: Provides endpoints for managing goats with appropriate permission checks.
- **Docker Support**: Facilitates easy setup and deployment using Docker.

## Installation and Setup

### Prerequisites

- Python 3.x
- Docker (optional, for containerized deployment)

### Local Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/malikali001/farm-management-system-api.git
    cd goat_farm_management
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```sh
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

### Docker Setup

1. **Build the Docker image:**

    ```sh
    docker-compose build
    ```

2. **Run the Docker containers:**

    ```sh
    docker-compose up
    ```

## Usage

### Admin User

- Admin users can perform CRUD operations on all goats.
- Admin users must assign a manager to each goat during creation or update.
- Admin users can view and manage all goats in the system.

### Manager User

- Manager users can perform CRUD operations only on the goats they manage.
- Manager users cannot change the `manager_id` of a goat during updates.
- Manager users can only view the goats they manage.

## Security and Validation

The system includes custom validation logic to ensure data integrity and proper role-based access control:

- **Managers**:
  - Can only assign goats to themselves.
  - Can only perform CRUD operations on goats they manage.
- **Admins**:
  - Must assign a valid manager to each goat.
  - Can perform CRUD operations on all goats.


## Contact

For more information, please contact [malik.alihussain001@gmail.com].

