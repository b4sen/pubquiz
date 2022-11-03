from sqlalchemy import Column, Integer
from sqlalchemy.orm import as_declarative


@as_declarative()
class Base:

    id = Column(Integer, primary_key=True)

    def _asdict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
