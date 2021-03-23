"""empty message

Revision ID: 5cbd00c03b83
Revises: 6661e5acb58d
Create Date: 2021-03-23 13:41:29.753778

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5cbd00c03b83'
down_revision = '6661e5acb58d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('property_profiles', sa.Column('description', sa.String(length=255), nullable=True))
    op.add_column('property_profiles', sa.Column('filename', sa.String(length=255), nullable=True))
    op.add_column('property_profiles', sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('property_profiles', 'price')
    op.drop_column('property_profiles', 'filename')
    op.drop_column('property_profiles', 'description')
    # ### end Alembic commands ###
