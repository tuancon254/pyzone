"""add phone number to users table

Revision ID: 8727a9c28a8d
Revises: 
Create Date: 2024-09-30 23:27:49.249715

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8727a9c28a8d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(15), nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'phone_number')
