"""adding benefits table

Revision ID: bb8ad29a9ac5
Revises: baf6b24c9348
Create Date: 2017-05-23 17:13:07.590320

"""

# revision identifiers, used by Alembic.
revision = 'bb8ad29a9ac5'
down_revision = 'baf6b24c9348'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('benefits',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('cost_per_employee', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employee_benefits',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.Column('benefit_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['benefit_id'], ['benefits.id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employee_benefits')
    op.drop_table('benefits')
    ### end Alembic commands ###