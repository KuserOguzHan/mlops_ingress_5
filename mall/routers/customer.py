from typing import Optional
from fastapi import APIRouter, Request, Depends, status, Response, HTTPException
from mall.models import hepsiburada, create_data, CreateUpdateData, limited_information
from pydantic import BaseModel
import joblib
from database import create_db_and_tables, get_db
from sqlmodel import Session, select
from fastapi import status


# Read models saved during train phase
estimator_hepsiburada_loaded = joblib.load("mall/saved_models/randomforest_with_hepsiburada.pkl")

router = APIRouter()

def make_hepsiburada_prediction(model, request):
    # parse input from request
    memory= request["memory"]
    ram= request["ram"]
    screen_size= request["screen_size"]
    power= request["power"]
    front_camera= request["front_camera"]
    rc1= request["rc1"]
    rc3= request["rc3"]
    rc5= request["rc5"]
    rc7= request["rc7"]


    # Make an input vector
    hepsiburada = [[memory, ram, screen_size, power, front_camera, rc1, rc3, rc5, rc7]]

    # Predict
    prediction = model.predict(hepsiburada)

    return prediction[0]

# Hepsiburada Prediction endpoint
@router.post("/prediction/hepsiburada")
def predict_hepsiburada(request: hepsiburada):
    prediction = make_hepsiburada_prediction(estimator_hepsiburada_loaded, request.dict())
    return prediction


#Models içindeki table=True olan sınıflardan küçük harfli bir tablo yaratacak
create_db_and_tables()

#Create New Data
#Bu komutun tamamı models.py deki CreateUpdateData(SQLModel) istekleri gerçekleştiriyor.
#Eğer CreateUpdateData yerine create_data yazsaydık models.py deki create_data classı gelecekti.
#Yani id de görünecekti.
@router.post("/Both_Create_Update", status_code=status.HTTP_201_CREATED)
async def create_new_data(request: CreateUpdateData, session: Session = Depends(get_db)):
    new_data = create_data(
        memory = request.memory,
        ram = request.ram, 
        screen_size= request.screen_size, 
        power= request.power, 
        front_camera= request.front_camera, 
        rc1= request.rc1, 
        rc3= request.rc3, 
        rc5= request.rc5, 
        rc7= request.rc7 

    )
    with session:
        session.add(new_data)
        session.commit()
        session.refresh(new_data)
        return new_data


#Tüm data gösterme komutu. 
#Yani database de 20 kayıt var ise hepsini gösterir
#Get all data
@router.get("/Show_All_Data")
async def get_all(session: Session = Depends(get_db)):
    data = session.exec(
        select(create_data)).all()
    return data


# Get data by id
@router.get("/Show Only By Id/{id}", status_code=status.HTTP_200_OK)
async def get_by_id(id: int, session: Session = Depends(get_db)):
    with session:
        statement = select(create_data).where(create_data.dataID == id)
        results = session.exec(statement)
        try:
            one_data = results.one()
        except:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Product {id} has not found.")
        return one_data    


# Update data
@router.put("/Update/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update(id: int, request: CreateUpdateData, session: Session = Depends(get_db)):
    with session:
        one_data = session.get(create_data, id) # id alarak bakıyoruz
        if not one_data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Product with {id} has not found.")
        update_data = request.dict(exclude_unset=True) #request den geleni güncel Product ile güncelliyoruz
        for key, value in update_data.items():
            setattr(one_data, key, value)
        session.add(one_data) #ekleme
        session.commit()          #commit etme
        session.refresh(one_data) #
        return one_data         


# Delete a data by id
@router.delete("/Delete/{id}", status_code=status.HTTP_200_OK)
async def delete_data(id: int, session: Session = Depends(get_db)): # id ile Product siliyoruz
    with session:
        one_data = session.get(create_data, id)
        if not one_data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,              #yoksa hata versin
                                detail=f"Product with {id} has not found.")
        session.delete(one_data) # varsa silsin
        session.commit()
        return {"ok": True}
                         


# Limited informaiton
@router.get("/data_limited/{id}", status_code=status.HTTP_200_OK, response_model=limited_information)
async def get_by_id(id: int, session: Session = Depends(get_db)):
    with session:
        statement = select(create_data).where(create_data.dataID == id)
        results = session.exec(statement)
        try:
            one_data = results.one()
        except:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Product {id} has not found.")
        return one_data        