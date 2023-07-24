"""add_timestamps_to_allocations

Revision ID: a49d3e62bda9
Revises: 7509cfc0824d
Create Date: 2023-06-28 12:42:07.968118

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a49d3e62bda9"
down_revision = "7509cfc0824d"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("allocations", schema=None) as batch_op:
        batch_op.add_column(sa.Column("deleted_at", sa.TIMESTAMP(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("allocations", schema=None) as batch_op:
        batch_op.drop_column("deleted_at")

    # ### end Alembic commands ###