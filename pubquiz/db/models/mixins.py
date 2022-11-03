from functools import partial
from sqlalchemy import Column

NotNull = partial(Column, nullable=False)
