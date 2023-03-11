from fastapi import FastAPI
from database import create_db_and_tables
from mall.routers import customer,user


app = FastAPI()

app.include_router(customer.router)
app.include_router(user.router)


create_db_and_tables()