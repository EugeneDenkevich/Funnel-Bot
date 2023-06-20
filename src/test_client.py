import unittest

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class TestStringMethods(unittest.TestCase):
    def setUp(self) -> None:
        base_url = "sqlite:///db_lite_test.db"
        self.engine = create_engine(base_url, connect_args={"check_same_thread": False})

        class Base(DeclarativeBase):
            pass

        class Client(Base):
            __tablename__ = "person_test"

            id = Column(Integer, primary_key=True, index=True)
            hw1 = Column(String)
            hw2 = Column(String)
            hw3 = Column(String)
            username = Column(String)
            tg_id = Column(Integer)
            sys_id = Column(String)
        
        self.Client = Client

        Base.metadata.create_all(bind=self.engine)

        Session = sessionmaker(autoflush=False, bind=self.engine)
        self.db = Session()

        client = Client(
            hw1 = 'active',
            hw2 = 'disactive',
            hw3 = 'disactive',
            username = 'Евгений Денкевич',
            tg_id = 5508567586,
            sys_id = None
        )
        self.db.add(client)
        self.db.commit()


    def tearDown(self) -> None:
        self.db.query(self.Client).delete()
        self.db.commit()

    def test_upper(self):
        # data = {
        #     'chat_id': 6196073894,
        #     'text': 'test'
        # }
        # requests.post(f'https://api.telegram.org/bot6156277095:AAGotvCNugBIbBpq9dE0jZgulBpXcW6xKdg/sendMessage', data=data)
        client = self.db.query(self.Client).filter(self.Client.tg_id == 5508567586).first()


        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()