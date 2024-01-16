from typing import Optional
from pydantic import BaseModal

class Item(BaseModal):
  id:Optional[int]
  name:str
  lastname:str
  age:int

  class Config:
    orm_mode = True


class Itemupdate(BaseModal):
  name:str

  class Config:
    orm_mode = True
    