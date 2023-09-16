#!/usr/bin/python3
"""
lists first State object from the database
"""

if __name__ == '__main__':
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    state = session.query(State).filter(State.id == 2).first()
    if state is not None:
        state.name = 'New Mexico'
        session.commit()
    session.close()
