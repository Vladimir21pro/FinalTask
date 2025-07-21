from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    phone: str
    fam: str
    name: str
    otc: str


class PerevalBase(BaseModel):
    beauty_title: str
    title: str
    other_titles: str


class PerevalCreate(PerevalBase):
    user: UserBase


class PerevalOut(PerevalBase):
    id: int
    status: str
    user: UserBase

    class Config:
        orm_mode = True
