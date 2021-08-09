#!/usr/bin/python3
"""Start link class to table in database
"""


import sys
from model_state import State
from sqlalchemy import create_engine -
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == "__main__":
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

        Session = sessionmaker(engine)
        session = Session()

        for city, city_id, state in session.query(
                City.name, City.id, State.name).order_by(City.id).join(City):
            print("{}: ({}) {}".format(state, city_id, city))
