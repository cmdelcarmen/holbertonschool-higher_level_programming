#!/usr/bin/python3
"""Start link class to table in database
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

        Session = sessionmaker(engine)
        session = Session()
        state_arg = sys.argv[4]

        flag = 0
        for state in session.query(State).order_by(State.id):
            if state_arg == state.name:
                print("{}: {}".format(state.id, state.name))
                flag = 1

        if flag == 0:
            print("Not found")
