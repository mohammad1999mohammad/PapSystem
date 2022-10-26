from fastapi import FastAPI, Path, Query, Form
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import false, true
from forecast import forecast

app = FastAPI()

# origins = [
#     'http://192.168.43.54:3000',
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    product: str
    area: int
    promotion: float
    month: int
    week: int
    day: int


class User(BaseModel):
    username: str
    password: str


global items

items = {
    # 1: Item(product='m', area=1, promotion=0.12, month=7, week=2, day=4)
}

global users

users = [{'username': 'sh.dadgar', 'password': '1221'},
         {'username': 'm.nasehi', 'password': '2442'}]


@app.get('/get-items')
def get_items():
    global items
    return items


@app.post('/add-item')
def add_item(item: Item):
    global items
    items = {}
    # if(item_id in items):
    #     return {'Error': 'Item ID already exist'}

    items[1] = item
    return {'Data': 'Success'}


@app.get('/get-result')
def get_result():
    global items
    return (forecast(items[1].product, items[1].area, items[1].promotion, items[1].month, items[1].week, items[1].day))
    # return {"1":'hello'}


@app.post('/login')
def login(user: User):
    global users
    user_name = user.username
    pass_word = user.password
    for item in users:
        if(item['username'] == user_name):
            if(item['password'] == pass_word):
                return ({'message': 'ورود موفق','login':True})
            else:
                return({'message': 'رمز عبور اشتباه است','login':False})
        else:
            return ({'message': 'نام کاربری نامعتبر است','login':False})
