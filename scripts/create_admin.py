import sys
sys.path.append("../pubquiz/")

if True:
    from pubquiz.dependencies.auth import hash_password
    from pubquiz.db.session import SessionLocal, engine
    from pubquiz.db.models import Base
    from pubquiz.db.models import Admin


Base.metadata.create_all(bind=engine)
db = SessionLocal()

username = input("Username: ")
password = input("Password: ")

hashed_pw = hash_password(password)

a = Admin(username=username, password=hashed_pw)
db.add(a)
db.commit()
