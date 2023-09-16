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
    states = session.query(State)
    for stat in states:
        if 'a' in stat.name:
            session.delete(stat)
    session.commit()
    session.close()
