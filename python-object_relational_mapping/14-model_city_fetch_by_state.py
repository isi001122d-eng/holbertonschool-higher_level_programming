#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Verilənlər bazasına qoşulma mühərriki yaradılır
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Sessiya yaradılır
    Session = sessionmaker(bind=engine)
    session = Session()

    # State və City cədvəllərini id-yə görə birləşdirib (Join) çəkirik
    results = session.query(State, City).filter(State.id == City.state_id)\
                     .order_by(City.id.asc()).all()

    # Nəticələri tələb olunan formatda çap edirik
    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
