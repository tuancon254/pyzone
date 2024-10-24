"""change password length

Revision ID: f15715123f9d
Revises: 8727a9c28a8d
Create Date: 2024-09-30 23:46:56.821381

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f15715123f9d'
down_revision: Union[str, None] = '8727a9c28a8d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('users', 'password', type_=sa.String(255))


def downgrade() -> None:
    op.alter_column('users', 'password', type_=sa.String(16))
