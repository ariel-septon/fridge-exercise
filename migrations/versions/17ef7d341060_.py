"""empty message

Revision ID: 17ef7d341060
Revises: ae10100c1f29
Create Date: 2020-04-30 18:41:54.655862

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17ef7d341060'
down_revision = 'ae10100c1f29'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('shelf_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'items', 'shelves', ['shelf_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'items', type_='foreignkey')
    op.drop_column('items', 'shelf_id')
    # ### end Alembic commands ###