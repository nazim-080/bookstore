from sqlmodel import Field, Relationship, SQLModel


class CountryBase(SQLModel):
    name: str

    def __str__(self):
        return self.name


class Country(CountryBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    authors: list["Author"] = Relationship(back_populates="country", sa_relationship_kwargs={"lazy": "selectin"})
    publishers: list["Publisher"] = Relationship(back_populates="country", sa_relationship_kwargs={"lazy": "selectin"})


class CountryRead(CountryBase):
    id: int


class CountryUpdate(CountryBase):
    pass


class CountryCreate(CountryBase):
    pass
