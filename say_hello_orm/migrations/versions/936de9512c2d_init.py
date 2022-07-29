"""`init`

Revision ID: 936de9512c2d
Revises: 
Create Date: 2022-07-15 20:34:44.871222

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '936de9512c2d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('body', sa.String(length=200), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_message_timestamp'), 'message', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_message_timestamp'), table_name='message')
    op.drop_table('message')
    # ### end Alembic commands ###
