# Alembic
Generic single-database configuration.

## Useful commands
```shell
# Generate new revision file
alembic revision --autogenerate -m "Add some columns"

# Upgrade DB to the latest version
alembic upgrade head

# Downgrade the latest version
alembic downgrade -1
```