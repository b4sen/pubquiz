import uvicorn

if __name__ == "__main__":
    from pubquiz.db.models import Base
    from pubquiz.db.session import engine
    Base.metadata.create_all(bind=engine)
    uvicorn.run("pubquiz.server:app", host='0.0.0.0', port=5000, reload=True)
