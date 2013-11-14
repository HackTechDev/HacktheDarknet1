import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tableDatabase import *

engine = create_engine('sqlite:///darknet.db', echo = True)

Session = sessionmaker(bind=engine)
session = Session()

new_user = User("Samuel", "Geeker", "samuel.geeker@hackthedarknet.com", "p@55w0rd", 1000)
new_user.hacker = [Hacker("9EEK", "geek@htd.com", "password")]

more_hackers = [Hacker("SolomonKane", "solomonkane@htd.com", "password1"),
        Hacker("LeSanglier", "lesanglier@htd.com", "password2")]

new_user.hacker.extend(more_hackers)

session.add(new_user)

session.commit()

session.add_all([
    User("Test", "Test1", "test.test1@hackthedarknet.com", "p@55w0rd", 1500),
    User("azerty", "qwerty", "azerty.qwerty@hackthedarknet.com", "p@55w0rd",2000)
    ])
session.commit()


server1 = Server("server1", "666", "12.0.0.1")
server2 = Server("server2", "777", "192.168.1.1")

new_user.server = [
        server1,
        server2
        ]

session.add(new_user)
session.commit()


session.add_all([
    Softwaretype("Virus"),
    Softwaretype("Antivirus"),
    Softwaretype("Firewall"),
    Softwaretype("Secure shell"),
    Softwaretype("No-secure shell"),
    Softwaretype("Load balancer"),
    Softwaretype("Mail"),
    Softwaretype("Password Cracker"),
    Softwaretype("Ping"),
    Softwaretype("Database")
    ])
session.commit()        


session.add_all([
    Software("Tcherno", "0.0.1", 100, "Against DDOS", "Virus: Harddisk destruction", "None"),
    Software("Panda", "0.3.1", 100, "No security hole", "Antivirus", "None")
    ])

session.commit()                

