#!/usr/bin/python3
"""lists first State objects from database """
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == '__main__':
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]} \
        @localhost/{argv[3]}', pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    row = session.query(State).filter(State.id==2).first()
    row.name = 'New Mexico'
    session.commit()
    session.close()
