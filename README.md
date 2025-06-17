# Pizza Restaurant API

## Overview

This is a RESTful API for a Pizza Restaurant application built with Flask. It allows management and querying of restaurants, pizzas, and their associated prices.

## Project Structure

The project follows a basic MVC-like structure:
- `server/models/`: Database models (SQLAlchemy).
- `server/controllers/`: Route logic and data processing.
- `server/`: Contains main app setup (`app.py`, `config.py`, `__init__.py`) and database seed script (`seed.py`).
- `migrations/`: Database migration scripts.

## Setup

1. Clone the repository.
2. Navigate into the project directory.
3. Install dependencies using Pipenv: `pipenv install`.
4. Activate the virtual environment: `pipenv shell`.

## Database Setup & Seeding

1. Ensure the virtual environment is active (`pipenv shell`).
2. Set the `FLASK_APP` environment variable:
    - Linux/macOS: `export FLASK_APP=server/app.py`
    - Windows (Cmd): `set FLASK_APP=server\app.py`
    - Windows (PowerShell): `$env:FLASK_APP="server/app.py"`
3. Initialize migrations: `flask db init` (run only once).
4. Create initial migration: `flask db migrate -m "Initial migration"` (run whenever models change).
5. Apply migration: `flask db upgrade` (creates/updates tables in `server/app.db`).
6. Seed the database with initial data: `python -m server.seed`.

## Running the API

1. Ensure the virtual environment is active and `FLASK_APP` is set.
2. Start the Flask server: `python server/app.py`.
The API will run on `http://localhost:5555`.

## API Endpoints

Base URL: `http://localhost:5555`

*   `GET /` - Welcome message.
*   `GET /restaurants` - List all restaurants.
*   `GET /restaurants/<int:id>` - Get a specific restaurant (includes pizzas) or 404 error.
*   `DELETE /restaurants/<int:id>` - Delete a restaurant (cascades to RestaurantPizzas) or 404 error. Returns 204 on success.
*   `GET /pizzas` - List all pizzas.
*   `POST /restaurant_pizzas` - Create a new RestaurantPizza association. Requires JSON body `{"price": <int>, "pizza_id": <int>, "restaurant_id": <int>}`. Price must be between 1 and 30. Returns 201 on success, 400 on validation error.

## Validation

*   `Restaurant`: Name unique, name/address not null.
*   `Pizza`: Name/ingredients not null.
*   `RestaurantPizza`: `price` is an integer between 1 and 30 (inclusive). `pizza_id` and `restaurant_id` refer to existing records.

## Testing

A Postman collection is provided for testing.

1.  Download and import the `challenge-1-pizzas.postman_collection.json` file into Postman.
2.  Ensure the Flask application is running (`python server/app.py`).
3.  Run the requests in the Postman collection to test each endpoint. You may need to re-seed the database (`python -m server.seed`) between test runs, especially after DELETE requests.

---