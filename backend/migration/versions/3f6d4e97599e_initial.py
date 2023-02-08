"""initial

Revision ID: 3f6d4e97599e
Revises: 
Create Date: 2023-01-19 02:18:25.957529

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '3f6d4e97599e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), primary_key=True, index=True),
                    sa.Column('email', sa.String(length=255), unique=True, index=True),
                    sa.Column('hashed_password', sa.String(length=255)),
                    sa.Column('is_active', sa.Boolean(), default=True)
                    )
    op.create_table('items',
                    sa.Column('id', sa.Integer(), primary_key=True, index=True),
                    sa.Column('title', sa.String(length=255), index=True),
                    sa.Column('description', sa.Text(), index=True),
                    sa.Column('owner_id', sa.Integer()),
                    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], )
                    )


def downgrade() -> None:
    op.drop_table('users')
    op.drop_table('items')
