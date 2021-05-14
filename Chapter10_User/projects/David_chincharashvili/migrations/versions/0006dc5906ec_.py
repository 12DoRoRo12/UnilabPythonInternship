"""empty message

Revision ID: 0006dc5906ec
Revises: 852ab04e1165
Create Date: 2021-05-06 20:59:24.459534

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0006dc5906ec'
down_revision = '852ab04e1165'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('test')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('age', sa.DATETIME(), nullable=True),
    sa.Column('company', sa.VARCHAR(), nullable=True),
    sa.Column('surname', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
