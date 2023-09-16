#!/usr/bin/python3
"""
lists all State objects from the database
"""

if __name__ == '__main__':
    from sys import argv
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for _c, _s in session.query(City, State).join(
            State).order_by(City.id).all():
        print("{}: ({}) {}".format(_s.name, _c.id, _c.name))
    session.close()
