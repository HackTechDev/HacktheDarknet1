# table_def.py
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Table, Text


# http://xsnippet.org/359350/

engine = create_engine('sqlite:///darknet.db', echo = False)
Base = declarative_base()
 

user_server = Table("user_server", Base.metadata,
                        Column('user_id', Integer, ForeignKey('user.id')),
                        Column('server_id', Integer, ForeignKey('server.id'))
                    )

user_workstation = Table("user_workstation", Base.metadata,
                        Column('user_id', Integer, ForeignKey('user.id')),
                        Column('workstation_id', Integer, ForeignKey('workstation.id'))
                    )



"""
A user has several hacker
A user has several server
A user has severak workstation
"""
class User(Base):
    __tablename__ = "user"
 
    id = Column(Integer, primary_key=True)
    firstname = Column(String)  
    lastname = Column(String)
    email = Column(String)
    password = Column(String)
    budget = Column(Integer)

    server = relationship('Server', secondary=user_server, backref='user')
    workstation = relationship('Workstation', secondary=user_workstation, backref='workstation')

    def __init__(self, firstname, lastname, email, password, budget):
        self.firstname = firstname    
        self.lastname = lastname 
        self.email = email
        self.password = password
        self.budget = budget

"""
A hacker has one User
"""
class Hacker(Base):
    __tablename__ = "hacker"
 
    id = Column(Integer, primary_key=True)
    nickname = Column(String)
    email = Column(String)
    password = Column(String)
 
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", backref=backref("hacker", order_by=id))
 
    def __init__(self, nickname, email, password):
        self.nickname = nickname
        self.email= email
        self.password = password

"""
A server can have several user
A server has one operating system
"""
class Server(Base):
    __tablename__ = "server"

    id = Column(Integer, primary_key=True)
    name = Column(String)  
    price = Column(String)
    ipaddress = Column(String)
    
    operatingsystem_id = Column(Integer, ForeignKey("operatingsystem.id"))

    def __init__(self, name, price, ipaddress):
        self.name = name
        self.price = price
        self.ipaddress = ipaddress

"""
"""
class Software(Base):
    __tablename__ = "software"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    version = Column(String)
    price = Column(Integer)
    description = Column(String)
    type = Column(Integer)
    security = Column(String)
    vulnerability = Column(String)

    softwaretype_id = Column(Integer, ForeignKey("softwaretype.id"))

    def __init__(self, name, version, price, description, security, vulnerability):
        self.name = name
        self.version = version
        self.price = price
        self.description = description
        self.security = security
        self.vulnerability = vulnerability

class Softwaretype(Base):
    __tablename__ = "softwaretype"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

"""
"""

class Operatingsystem(Base):
    __tablename__ = "operatingsystem"

    id = Column(Integer, primary_key=True)
    name = Column(String)  
    price = Column(String)
    version = Column(String)
    security = Column(String)
    vulnerability = Column(String)

    def __init__(self, name, price, version, security, vulnerability):
        self.name = name
        self.price = price
        self.version = version
        self.security = security
        self.vulnerability = vulnerability
        
    """
    Client/Serveur:
        Linux: Debian
               Ubuntu
        Windows
        MacOs
    """

"""
A workstation has one user or one hacker
"""
class Workstation(Base):
    __tablename__ = "workstation"

    id = Column(Integer, primary_key=True)
    name = Column(String)  
    price = Column(String)
    ipaddress = Column(String)

    operatingsystem_id = Column(Integer, ForeignKey("operatingsystem.id"))

    def __init__(self, name, price, ipaddress):
        self.name = name
        self.price = price    
        self.ipaddress = ipaddress
        

"""
Create database and all tables
"""
Base.metadata.create_all(engine)
