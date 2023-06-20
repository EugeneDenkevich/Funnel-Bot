from collections import Counter

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import DeclarativeBase, sessionmaker


def db_connect():
    base_url = "sqlite:///db_lite.db"
    engine = create_engine(base_url, connect_args={"check_same_thread": False})

    class Base(DeclarativeBase):
        pass

    class Client(Base):
        __tablename__ = "person"

        id = Column(Integer, primary_key=True, index=True)
        hw1 = Column(String)
        hw2 = Column(String)
        hw3 = Column(String)
        username = Column(String)
        tg_id = Column(Integer)
        sys_id = Column(String)

    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(autoflush=False, bind=engine)
    db = Session()
    return db, Client


def set_user(user_id, username):
    db, Client = db_connect()
    if not db.query(Client).filter(Client.tg_id == user_id).first():
        db.add(Client(hw1='disactive',
                      hw2='disactive',
                      hw3='disactive',
                      tg_id=user_id,
                      username=username))
        db.commit()
    else:
        return


def check_hw1(user_id):
    db, Client = db_connect()
    client = db.query(Client).filter(Client.tg_id == user_id).first()
    return client.hw1


def activate_hw1(user_id):
    db, Client = db_connect()
    client = db.query(Client).filter(Client.tg_id == user_id).first()
    client.hw1 = 'active'
    db.commit()


def get_homeworks_from_db():
    db, Client = db_connect()
    res = db.query(Client).all()
    return res


def get_system_id(user_id):
    db, Client = db_connect()
    client = db.query(Client).filter(Client.tg_id == user_id).first()
    sys_id = f"{str(client.tg_id)[:4]}-{client.id}"
    if client.sys_id != None:
        return client.sys_id
    else:
        client.sys_id = sys_id
        db.commit()
        return sys_id
    

def get_hw_number(user_id):
    db, Client = db_connect()
    client = db.query(Client).filter(Client.tg_id == user_id).first()
    hws = [client.hw1, client.hw2, client.hw3]
    if Counter(hws)['active'] > 1:
        raise Exception("More than 1 homeworks in 'active' status!")
    for hw in hws:
        if hw == 'active':
            return f"ДЗ{hws.index('active')+1}"
