import uuid

from sqlmodel import SQLModel, Field


class PostgresModel(SQLModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)


class SqliteModel(SQLModel):
    id: int = Field(primary_key=True, default=None)


class SqlBaseModel(SqliteModel):
    pass


PrimaryKeyType = int
