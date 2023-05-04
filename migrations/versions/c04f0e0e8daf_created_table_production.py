"""Created table Production

Revision ID: c04f0e0e8daf
Revises: 
Create Date: 2023-05-05 01:05:08.154500

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c04f0e0e8daf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('productions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('genre', sa.String(), nullable=True),
    sa.Column('budget', sa.Float(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('director', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('ongoing', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('productions')
    # ### end Alembic commands ###
