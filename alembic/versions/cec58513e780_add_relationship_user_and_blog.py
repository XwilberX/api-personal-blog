"""Add relationship user and blog

Revision ID: cec58513e780
Revises: 5ad78344e0c5
Create Date: 2024-12-22 02:18:08.093101

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "cec58513e780"
down_revision: Union[str, None] = "5ad78344e0c5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("blogs", schema=None) as batch_op:
        batch_op.alter_column(
            "content",
            existing_type=sa.VARCHAR(),
            type_=sa.TEXT(),
            existing_nullable=False,
        )

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("blogs", schema=None) as batch_op:
        batch_op.alter_column(
            "content",
            existing_type=sa.TEXT(),
            type_=sa.VARCHAR(),
            existing_nullable=False,
        )

    # ### end Alembic commands ###
