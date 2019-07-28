from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
engine = create_engine('sqlite:///sales.db', echo = True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Customers(Base):
   __tablename__ = 'customers'
   id = Column(Integer, primary_key=True)

   name = Column(String)
   address = Column(String)
   email = Column(String)
Base.metadata.create_all(engine) ##This line was missing from where I copied the code, that's why it was giving an error that table 'customers' not found

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()

c1 = Customers(name = 'Ravi Kumar', address = 'Station Road Nanded', email = 'ravi@gmail.com')

session.add(c1)
session.commit()

session.add_all([
   Customers(name = 'Komal Pande', address = 'Koti, Hyderabad', email = 'komal@gmail.com'),
   Customers(name = 'Rajender Nath', address = 'Sector 40, Gurgaon', email = 'nath@gmail.com'),
   Customers(name = 'S.M.Krishna', address = 'Budhwar Peth, Pune', email = 'smk@gmail.com')]
)

session.commit()
