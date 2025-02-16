"""Fusionando migraciones

Revision ID: e99232d402c7
Revises: 00578bc00af1, 68b390f66e25, c22e43b73872, e3e193d5f849
Create Date: 2025-02-16 13:07:18.443650

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e99232d402c7'
down_revision = ('00578bc00af1', '68b390f66e25', 'c22e43b73872', 'e3e193d5f849')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
