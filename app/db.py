from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
import config
import os

def get_engine() -> Engine:
    """Create a SQLAlchemy engine for PostgreSQL."""
    db_url = (
        f"postgresql+psycopg2://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}"
        f"@{config.POSTGRES_HOST}:{config.POSTGRES_PORT}/{config.POSTGRES_DB}"
    )
    return create_engine(db_url)
