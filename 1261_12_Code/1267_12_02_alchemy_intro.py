import sqlalchemy as sqa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Pet(Base):
    __tablename__ = "pet"
    id = sqa.Column(sqa.Integer, primary_key=True)
    type = sqa.Column(sqa.String(16))
    breed = sqa.Column(sqa.String(32))
    gender = sqa.Column(sqa.Enum("male", "female"))
    name = sqa.Column(sqa.String(64))

engine = sqa.create_engine('sqlite:///mydata.db')
Base.metadata.create_all(engine)

pet = Pet()
pet.id = 1
pet.type = "dog"
pet.breed = "spaniel"
pet.gender = "female"
pet.name = "Esme"

Session = sqa.orm.sessionmaker(bind=engine)
session = Session()

session.add(pet)
session.commit()

session.query(Pet).filter_by(name="Esme").one()
session.query(Pet).filter(Pet.name=="Esme")
