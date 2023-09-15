#!/usr/bin/python3
"""makes new state and city"""
from sys import argv
from relationship_state import State
from relationship_city import City, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]} \
        @localhost/{argv[3]}', pool_pre_ping=True)
    Base.metadata.create_all(engine)
    start_Session = sessionmaker(bind=engine)
    session = start_Session()
    state = State(name="California")
    session.add(state)
    city = City(name="San Francisco", state=state)
    session.add(city)
    session.commit()
    session.close()
