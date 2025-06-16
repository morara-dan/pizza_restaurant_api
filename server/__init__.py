from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()      # Handles database interactions (defining models, querying)
migrate = Migrate()    # Handles database schema migrations (e.g., creating tables)