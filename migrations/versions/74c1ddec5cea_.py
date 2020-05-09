"""empty message

Revision ID: 74c1ddec5cea
Revises: b2d0784160cf
Create Date: 2020-05-09 13:30:48.557793

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74c1ddec5cea'
down_revision = 'b2d0784160cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('refrigerators', sa.Column('shelf_amount', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('refrigerators', 'shelf_amount')
    # ### end Alembic commands ###
