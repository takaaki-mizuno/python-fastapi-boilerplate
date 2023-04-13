"""create users table

Revision ID: 7a1cbf774557
Revises: 
Create Date: 2023-04-12 21:13:39.478384

"""
from alembic import op
import sqlalchemy
from app.models.types.uuid import UUID
from sqlalchemy.sql import func, text

# revision identifiers, used by Alembic.
revision = '7a1cbf774557'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sqlalchemy.Column('id', UUID, primary_key=True, server_default=text('gen_random_uuid()')),
        sqlalchemy.Column('name', sqlalchemy.Text, nullable=False),
        sqlalchemy.Column('email', sqlalchemy.Text, nullable=False),
        sqlalchemy.Column('password', sqlalchemy.Text, nullable=False),
        sqlalchemy.Column('updated_at', sqlalchemy.TIMESTAMP(timezone=True), nullable=False,
                          server_default=func.now(),
                          onupdate=func.now()),
        sqlalchemy.Column('created_at', sqlalchemy.TIMESTAMP(timezone=True), nullable=False,
                          server_default=func.now()),
    )

    op.create_index('users_email', 'users', ['email'])


def downgrade() -> None:
    op.drop_table('users')
