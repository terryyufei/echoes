"""uploaded profile pic

Revision ID: f72b17ebae73
Revises: f4cf47d8fc2b
Create Date: 2023-10-26 16:12:12.532988

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f72b17ebae73'
down_revision = 'f4cf47d8fc2b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('picture', sa.String(length=120), nullable=True))
        batch_op.drop_column('image_file')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_file', sa.VARCHAR(length=120), nullable=True))
        batch_op.drop_column('picture')

    # ### end Alembic commands ###