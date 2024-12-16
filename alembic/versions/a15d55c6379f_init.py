"""init

Revision ID: a15d55c6379f
Revises: 
Create Date: 2024-12-16 09:35:15.784892

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'a15d55c6379f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('hashed_password', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('disabled', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_table('wishlists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_wishlists_name'), 'wishlists', ['name'], unique=True)
    op.create_table('wishlist_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('wishlist_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['wishlist_id'], ['wishlists.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_wishlist_items_name'), 'wishlist_items', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_wishlist_items_name'), table_name='wishlist_items')
    op.drop_table('wishlist_items')
    op.drop_index(op.f('ix_wishlists_name'), table_name='wishlists')
    op.drop_table('wishlists')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
