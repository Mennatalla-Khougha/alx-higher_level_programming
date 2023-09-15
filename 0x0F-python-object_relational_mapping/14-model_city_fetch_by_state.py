#!/usr/bin/python3
"""lists all State objects from database """
from sys import argv
from model_city import Base, City
from model_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == '__main__':
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]} \
        @localhost/{argv[3]}', pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(City, State).join(State)
    for city, state in rows:
        print(f'{state.name}: ({city.id}) {city.name}')
    session.close()
