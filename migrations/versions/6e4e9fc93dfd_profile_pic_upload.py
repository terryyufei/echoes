"""profile pic upload

Revision ID: 6e4e9fc93dfd
Revises: b422a635d625
Create Date: 2023-10-24 13:19:13.549962

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e4e9fc93dfd'
down_revision = 'b422a635d625'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_file', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('date_created', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('date_created')
        batch_op.drop_column('image_file')

    # ### end Alembic commands ###