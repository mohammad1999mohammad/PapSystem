from fastapi import FastAPI, Path, Query, Form
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import false, true
from forecast import forecast
import time
import requests
import json

app = FastAPI()


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


class Location(BaseModel):
    lat: float
    lng: float


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
                return ({'message': 'ورود موفق', 'login': True})
            else:
                return({'message': 'رمز عبور اشتباه است', 'login': False})
        else:
            return ({'message': 'نام کاربری نامعتبر است', 'login': False})


@app.get('/sxlocation')
def location(latitude: float = Query(default=None, title='Latitude', description='the lat of the location'), longitude: float = Query(default=None, title='Longitude', description='the lng of the location')):

    selected_location = None

    while (selected_location is None):

        try:
            selected_location = json.loads(requests.get(
                'https://api.snapp.express/map/address/reverse?lat={}&lon={}'.format(latitude, longitude)).text)[0]['data']
        except:
            time.sleep(1)

    try:
        # first solution
        city = next(item['name']
                    for item in selected_location if item["type"] == "city")
    except:
        city = ''

    try:
        neighbourhood = next(
            item['name'] for item in selected_location if item["type"] == "neighbourhood")
    except:
        neighbourhood = ''

    try:
        primary = next(item['name']
                       for item in selected_location if item["type"] == "primary")
    except:
        primary = ''

    try:
        secondary = list(filter(lambda item: item["type"] == 'secondary', selected_location))[
            0]['name']  # second solution
    except:
        secondary = ''

    location = city + ' , ' + neighbourhood + ' , ' + primary + ' , ' + secondary

    return {'location': str(location)}


@app.get('/sxlocationstores')
def sxlocationstores(latitude: float = Query(default=None, title='Latitude', description='the lat of the location'), longitude: float = Query(default=None, title='Longitude', description='the lng of the location')):

    location_stores_base_url = 'https://api.snapp.express/mobile/v3/restaurant/vendors-list?lat={}&long={}'.format(
        latitude, longitude)

    location_stores_base_dict = '---'

    while (location_stores_base_dict == '---'):

        try:
            location_stores_base_dict = json.loads((requests.get(location_stores_base_url)).text)
        except:
            time.sleep(0.5)

    stores_count = location_stores_base_dict['data']['count']

    location_stores = []

    page = 0        # page query

    i = 0           # store counter

    while(i < stores_count):

        location_stores_url = 'https://api.snapp.express/mobile/v3/restaurant/vendors-list?lat={}&long={}&page={}&page_size={}'.format(
            latitude, longitude, page, 20)

        items_list = '---'

        while (items_list == '---'):
            try:
                items_list = (json.loads((requests.get(location_stores_url)).text))[
                    'data']['finalResult']
            except:
                time.sleep(1)

        for item in items_list:

            if(item['type'] == 'VENDOR'):

                i = i+1

                store_dict = {}

                try:
                    store_dict['store_id'] = item['data']['id']
                except:
                    store_dict['store_id'] = '---'
                try:
                    store_dict['store_code'] = item['data']['vendorCode']
                except:
                    store_dict['store_code'] = '---'
                try:
                    store_dict['store_type'] = item['data']['vendorTypeTitle']
                except:
                    store_dict['store_type'] = '---'
                try:
                    store_dict['store_name'] = item['data']['title']
                except:
                    store_dict['store_name'] = '---'
                try:
                    store_dict['store_rate_five'] = item['data']['rate']
                except:
                    store_dict['store_rate_five'] = '---'
                try:
                    store_dict['store_tax'] = item['data']['tax']
                except:
                    store_dict['store_tax'] = '---'
                try:
                    store_dict['store_service_fee'] = item['data']['serviceFee']
                except:
                    store_dict['store_service_fee'] = '---'
                try:
                    store_dict['store_discount'] = item['data']['discount']
                except:
                    store_dict['store_discount'] = '---'
                try:
                    store_dict['store_open'] = item['data']['isOpen']
                except:
                    store_dict['store_open'] = '---'
                try:
                    store_dict['store_min_price_order'] = item['data']['minOrder']
                except:
                    store_dict['store_min_price_order'] = '---'
                try:
                    store_dict['store_address'] = item['data']['address']
                except:
                    store_dict['store_address'] = '---'
                try:
                    store_dict['store_phone'] = item['data']['phone']
                except:
                    store_dict['store_phone'] = '---'
                try:
                    store_dict['store_location_lat'] = item['data']['lat']
                except:
                    store_dict['store_location_lat'] = '---'
                try:
                    store_dict['store_location_lon'] = item['data']['lon']
                except:
                    store_dict['store_location_lon'] = '---'
                try:
                    store_dict['store_priority'] = item['data']['priority']
                except:
                    store_dict['store_priority'] = '---'
                try:
                    store_dict['store_city'] = item['data']['city']
                except:
                    store_dict['store_city'] = '---'
                try:
                    store_dict['store_area'] = item['data']['area']
                except:
                    store_dict['store_area'] = '---'
                try:
                    store_dict['store_comment_count'] = item['data']['commentCount']
                except:
                    store_dict['store_comment_count'] = '---'
                try:
                    store_dict['store_vote_count'] = item['data']['voteCount']
                except:
                    store_dict['store_vote_count'] = '---'
                try:
                    store_dict['store_container_fee'] = item['data']['containerFee']
                except:
                    store_dict['store_container_fee'] = '---'
                try:
                    store_dict['store_discount_for_view'] = item['data']['discountValueForView']
                except:
                    store_dict['store_discount_for_view'] = '---'
                try:
                    store_dict['store_budget_class'] = item['data']['budgetClass']
                except:
                    store_dict['store_budget_class'] = '---'
                try:
                    store_dict['store_delivery_fee'] = item['data']['deliveryFee']
                except:
                    store_dict['store_delivery_fee'] = '---'
                try:
                    store_dict['store_coupon_count'] = item['data']['coupon_count']
                except:
                    store_dict['store_coupon_count'] = '---'
                try:
                    store_dict['store_best_coupon'] = item['data']['best_coupon']
                except:
                    store_dict['store_best_coupon'] = '---'
                try:
                    store_dict['store_delivery_fee_discount'] = item['data']['deliveryFeeDiscount']
                except:
                    store_dict['store_delivery_fee_discount'] = '---'

                location_stores.append(store_dict)

        page = page + 1

    return({'location_stores': location_stores})


@app.get('/sxstoreproducts')
def sxstoreproducts(storecode: str = Query(default=None, title='StoreCode', description='the code of stores'), latitude: float = Query(default=None, title='Latitude', description='the lat of the location'), longitude: float = Query(default=None, title='Longitude', description='the lng of the location')):

    products_base_url = 'https://api.snapp.express/product-list/{}/vendor/{}?lat={}&long={}&page=0&size=10'.format(
        1032, storecode, latitude, longitude)

    products = []

    number_of_products = '---'

    while (number_of_products == '---'):
        try:
            number_of_products = json.loads(requests.get(
                products_base_url).text)["data"]["count"]
        except:
            # time.sleep(0.5)
            pass

    size = 50

    for page in range(0, (number_of_products//size)+1):

        products_url = 'https://api.snapp.express/product-list/{}/vendor/{}?lat={}&long={}&page={}&size={}'.format(
            1032, storecode, latitude, longitude, page, size)

        products_list = '---'

        while (products_list == '---'):
            try:
                products_list = (json.loads(requests.get(products_url).text))[
                    "data"]["finalResult"]
            except:
                # time.sleep(0.5)
                pass


        for product in products_list:

            product_dict = {}

            try:
                product_dict['product_id'] = product['id']
            except:
                product_dict['product_id'] = '---'
            try:
                product_dict['product_name'] = product['data']['title']
            except:
                product_dict['product_name'] = '---'
            try:
                product_dict['product_rating'] = round(product['data']['rating'],2)*100
            except:
                product_dict['product_rating'] = '---'
            try:
                product_dict['product_discount'] = product['data']['discount']
            except:
                product_dict['product_discount'] = '---'
            try:
                product_dict['product_discount_rate'] = product['data']['discount_ratio']
            except:
                product_dict['product_discount_rate'] = '---'
            try:
                product_dict['product_volume'] = product['data']['description']
            except:
                product_dict['product_volume'] = '---'
            try:
                product_dict['product_price'] = product['data']['price']
            except:
                product_dict['product_price'] = '---'
            try:
                product_dict['product_comment_count'] = product['data']['comment_count']
            except:
                product_dict['product_comment_count'] = '---'
            try:
                product_dict['product_brand'] = product['data']['brand']
            except:
                product_dict['product_brand'] = '---'
            try:
                product_dict['product_stock'] = product['data']['stock']
            except:
                product_dict['product_stock'] = '---'

            products.append(product_dict)

    return({'products': products})
