from sqlalchemy import (
    MetaData,
    Column,
    Integer,
    String,
    DateTime,
    PrimaryKeyConstraint,
    ForeignKey,
    ForeignKeyConstraint,
    CheckConstraint,
    func,
    Table,
)

import re
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, validates

metadata = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_`%(constraint_name)s`",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
)

Base = declarative_base(metadata=metadata)

pet_owner = Table(
    "pet_owner",
    Base.metadata,
    # Column("id", Integer, primary_key=True), # would remove primary key constraint on pet_id and owner_id
    Column("pet_id", Integer, ForeignKey("pets.id"), primary_key=True),
    Column("owner_id", Integer, ForeignKey("owners.id"), primary_key=True),
)


class Owner(Base):
    __tablename__ = "owners"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    phone = Column(Integer, unique=True)
    address = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    pets = relationship("Pet", secondary=pet_owner, back_populates="owners")

    def __repr__(self):
        return (
            f"<Owner #{self.id} \n"
            + f"name: {self.name}\n"
            + f"email: {self.email}\n"
            + f"phone: {self.phone}\n"
            + f"address: {self.address} >\n"
        )


class Pet(Base):
    __tablename__ = "pets"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="owner_pk"),
        CheckConstraint("length(name) > 0", name="owner_name_length"),
    )

    id = Column(Integer)
    name = Column(String, nullable=False)
    species = Column(String)
    breed = Column(String)
    temperament = Column(String)
    owner_id = Column(Integer, ForeignKey("owners.id"))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    owners = relationship("Owner", secondary=pet_owner, back_populates="pets")

    def __repr__(self):
        return (
            f"<Pet #{self.id} \n"
            + f"name: {self.name}\n"
            + f"species: {self.species}\n"
            + f"breed: {self.breed}\n"
            + f"temperament: {self.temperament}\n"
            + f"owner_id: {self.owner_id} >\n"
        )
