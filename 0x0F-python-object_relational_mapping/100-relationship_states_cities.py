#!/usr/bin/python3
"""lists all State objects from database """
from sys import argv
from relationship_city import Base, City
from relationship_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == '__main__':
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]} \
        @localhost/{argv[3]}', pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    row = State(name="California")
    session.add(row)
    row2 = City(name="San Francisco", state=row)
    session.add(row2)
    session.commit()
    session.close()
