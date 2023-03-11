from fastapi import APIRouter
from fastapi import Depends, status, HTTPException
from sqlmodel import Session, select
from database import get_db
from mall.models import ShowUser, User, CreateUpdateUser, Login
from mall.auth import AuthHandler

router = APIRouter()
auth_handler = AuthHandler()


# Create user
@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=ShowUser)
async def create_user(request: CreateUpdateUser, session: Session = Depends(get_db)):
    hashed_password = auth_handler.get_password_hash(request.password)
    new_user = User(
        name=request.name,
        username=request.username,
        email=request.email,
        password=hashed_password
    )
    with session:
        statement = select(User).where(User.username == new_user.username)
        results = session.exec(statement)
        one_user = results.first()
        if not one_user:
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
            return new_user
        else:
            raise HTTPException(status_code=400, detail=f'Username: {one_user.username} is taken')



#Kullanıcı adı ve password alarak giriş yapıyor
@router.post('/login')
def login(request: Login, session: Session = Depends(get_db)):
    with session:
        statement = select(User).where(User.username == request.username)
        results = session.exec(statement)
        one_user = results.first()
        if (one_user is None) or (not auth_handler.verify_password(request.password, one_user.password)):
            raise HTTPException(status_code=401, detail='Invalid username and/or password')
        token = auth_handler.encode_token(one_user.username)
        return {'token': token}



#Sadece belirli autocation sahip kullanıcalar girme tanımlaması
@router.get('/protected')
def protected(username=Depends(auth_handler.auth_wrapper)):
    return {'name': username}