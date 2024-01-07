"""Add password_column to user table

Revision ID: 5885f7d4590d
Revises: ab072128113b
Create Date: 2023-12-29 09:04:07.724464

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5885f7d4590d"
down_revision: Union[str, None] = "ab072128113b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("password", sa.String, nullable=False))


def downgrade() -> None:
    op.drop_column("users", column_name="password")
