from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import BaseModel

# Predicton information of data example
class hepsiburada(BaseModel):
    memory: float
    ram: float
    screen_size: float
    power:float
    front_camera:float
    rc1:float
    rc3:float
    rc5:float
    rc7:float

    class Config:
        schema_extra = {
            "example": {
                "memory": 128.0,
                "ram": 8.0,
                "screen_size": 6.40,
                "power": 4310.0,
                "front_camera": 32.0,
                "rc1": 48.0,
                "rc3": 8.0 ,
                "rc5": 2.0,
                "rc7": 2.0,

            }
        }

#Tabloların tanımının yapıldığı yer
#Table true komutu ile yarat tanımı vermiş olduk
#Ancak asıl yaratma komutu main.py da vermiş olacağız
class create_data(SQLModel, table=True):
    dataID: Optional[int] = Field(default=None, primary_key=True)
    memory: float
    ram: float
    screen_size: float
    power:float
    front_camera:float
    rc1:float
    rc3:float
    rc5:float
    rc7:float

#Bu class tanımıyla update yapıyoruz.
#Yani True komutu vermediğimizden yeni bir table yaratmayacak.
#Sadece güncelleyecek.
class CreateUpdateData(SQLModel):
    dataID: Optional[int] = Field(default=None, primary_key=True)
    memory: float
    ram: float
    screen_size: float
    power:float
    front_camera:float
    rc1:float
    rc3:float
    rc5:float
    rc7:float

#Kısıtlı sayıda bilgi göstermek istiyorsam
class limited_information(SQLModel):
    memory: float
    ram: float
    screen_size: float


#Giriş bilgileri için bilgi tanımlama
class Login(SQLModel):
    username: str
    password: str


#Yeni tablo yaratacak 
#Bu tabloda kulanıcıların adı yazacak
class User(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    username: str
    email: str
    password: str    
        
#Girilen usersı update yapmak için
class CreateUpdateUser(SQLModel):
    name: str
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "Mesut KOCAMAN",
                "username": "mlops1",
                "email": "mlops1@vbo.local",
                "password": "strongPassword"
            }
        }


#Giriş yaplan kullanıcıları görüntüleme
class ShowUser(SQLModel):
    name: str
    email: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "Mesut KOCAMAN",
                "email": "mlops1@vbo.local"
            }
        }        
        