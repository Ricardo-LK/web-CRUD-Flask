from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(25))
    email = Column(String(50))

    purchases = relationship("Compra", back_populates="client")


class Flor(Base):
    __tablename__ = "flores"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    sci_name = Column(String(30))

    family_id = Column(Integer, ForeignKey('familias.id'))

    purchases = relationship("Compra", back_populates="flower")
    family = relationship("Familia", back_populates="flowers")  


class Familia(Base):
    __tablename__ = "familias"

    id = Column("id", Integer, primary_key = True, autoincrement = True)
    name = Column("name", String(30))

    flowers = relationship("Flor", back_populates="family")

    def __init__(self, name):
        self.name = name
    

class Compra(Base):
    __tablename__ = "compras"

    id = Column(Integer, primary_key=True, autoincrement=True)
    payment_method = Column(String(15))
    price = Column(Integer)

    client_id = Column(Integer, ForeignKey('clientes.id'))
    flower_id = Column(Integer, ForeignKey('flores.id'))

    client = relationship("Cliente", back_populates="purchases")
    flower = relationship("Flor", back_populates="purchases")