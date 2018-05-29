from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)

    def __repr__(self):
        return self.name

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    street = Column(String(200), nullable=False)
    neighborhood = Column(String(200))
    postal_code = Column(String(20))
    person_id = Column(Integer, ForeignKey('people.id'))
    person = relationship(Person)

    def __repr__(self):
        print('{}, {} - {}'.format(self.street, self.neighborhood, self.postal_code))

engine = create_engine('sqlite:///people.sqlite3')

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    p = Person(name="Severo")

    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(p)
    session.commit()