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
def sxlocation(latitude: float = Query(default=None, title='Latitude', description='the lat of the location'), longitude: float = Query(default=None, title='Longitude', description='the lng of the location')):

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
            location_stores_base_dict = json.loads(
                (requests.get(location_stores_base_url)).text)
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


def extract_type(x):

    if('پنیر' in x.split(' ')):
        return 'پنیر'
    elif('شیر' in x.split(' ')):
        return 'شیر'
    elif('ماست' in x.split(' ')):
        return 'ماست'
    elif('دوغ' in x.split(' ')):
        return 'دوغ'
    elif('کره' in x.split(' ')):
        return 'کره'
    elif('خامه' in x.split(' ')):
        return 'خامه'
    elif('کشک' in x.split(' ')):
        return 'کشک'
    elif('بستنی' in x.split(' ')):
        return 'بستنی'
    else:
        return 'سایر'


@app.get('/sxstoreproducts')
def sxstoreproducts(storecode: str = Query(default=None, title='StoreCode', description='the code of stores')):

    # products_base_url = 'https://api.snapp.express/product-list/{}/vendor/{}?lat={}&long={}&page=0&size=10'.format(
    #     1032, storecode, latitude, longitude)

    products_base_url = 'https://api.snapp.express/product-list/{}/vendor/{}?page=0&size=10'.format(
        1032, storecode)

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

        products_url = 'https://api.snapp.express/product-list/{}/vendor/{}?page={}&size={}'.format(
            1032, storecode, page, size)

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
                product_dict['product_rating'] = round(
                    product['data']['rating'], 2)*100
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
            try:
                product_dict['product_category'] = extract_type(
                    product['data']['title'])
            except:
                product_dict['product_category'] = '---'

            products.append(product_dict)

    return({'products': products})


@app.get('/smlocation')
def smlocation(latitude: float = Query(default=None, title='Latitude', description='the lat of the location'), longitude: float = Query(default=None, title='Longitude', description='the lng of the location')):

    location = '---'
    while (location == '---'):
        try:
            location = json.loads(requests.get(
                'https://reverse.snappmaps.ir/maps/api/place/reverse?lat={}&lon={}&display=true'.format(latitude, longitude)).text)['result']['displayName']
        except:
            time.sleep(1)

    return {'location': str(location)}


@app.get('/smlocationstores')
def smlocationstores(latitude: float = Query(default=None, title='Latitude', description='the lat of the location'), longitude: float = Query(default=None, title='Longitude', description='the lng of the location')):

    location_stores_dict = '---'
    while (location_stores_dict == '---'):
        try:
            location_stores_dict = json.loads(requests.get(
                'https://core.snapp.market/api/v1/vendors/availables?lat={}&lon={}'.format(latitude, longitude)).text)
        except:
            time.sleep(1)

    location_stores = []

    for store in location_stores_dict['items']:

        if(store['type'] != 'MYLI'):

            store_information = {}

            try:
                store_information['store_type'] = store['type']
            except:
                store_information['store_type'] = '---'
            try:
                store_information['store_persian_type'] = store['title']
            except:
                store_information['store_persian_type'] = '---'
            try:
                store_information['store_id'] = store['vendors'][0]['id']
            except:
                store_information['store_id'] = '---'
            try:
                store_information['store_code'] = store['vendors'][0]['code']
            except:
                store_information['store_code'] = '---'
            try:
                store_information['store_title'] = store['vendors'][0]['title']
            except:
                store_information['store_title'] = '---'
            try:
                store_information['store_long_address'] = store['vendors'][0]['address']
            except:
                store_information['store_long_address'] = '---'
            try:
                store_information['store_short_address'] = store['vendors'][0]['display_address']
            except:
                store_information['store_short_address'] = '---'
            try:
                store_information['store_phone'] = store['vendors'][0]['customer_phone']
            except:
                store_information['store_phone'] = '---'
            try:
                store_information['store_min_price_free_delivery'] = store['vendors'][0]['min_price_for_free_delivery']
            except:
                store_information['store_min_price_free_delivery'] = '---'
            try:
                store_information['store_min_basket_price'] = store['vendors'][0]['min_basket_price']
            except:
                store_information['store_min_basket_price'] = '---'
            try:
                store_information['store_delivery_fee'] = store['vendors'][0]['delivery_fee']
            except:
                store_information['store_delivery_fee'] = '---'
            try:
                store_information['store_delivery_fee_before_discount'] = store[
                    'vendors'][0]['default_time_slot']['delivery_fee_before_discount']
            except:
                store_information['store_delivery_fee_before_discount'] = '---'
            try:
                store_information['store_maximum_discount'] = store['vendors'][0]['maximum_discount']
            except:
                store_information['store_maximum_discount'] = '---'
            try:
                store_information['store_city'] = store['vendors'][0]['city']
            except:
                store_information['store_city'] = '---'
            try:
                store_information['store_status'] = store['vendors'][0]['default_time_slot']['status']
            except:
                store_information['store_status'] = '---'

            location_stores.append(store_information)

        else:
            pass

    return({'location_stores': location_stores})


@app.get('/smstoreproducts')
def smstoreproducts(storecode: str = Query(default=None, title='StoreCode', description='the code of stores')):

    products = []

    products_base_url = 'https://core.snapp.market/api/v2/vendors/{}/products?categories%5B%5D={}'.format(
        storecode, 278345)

    number_of_products = '---'

    while (number_of_products == '---'):
        try:
            number_of_products = json.loads(requests.get(products_base_url).text)[
                'metadata']['pagination']['total']
        except:
            time.sleep(1)

    limit = 50

    for off in range(0, number_of_products, limit):

        products_url = 'https://core.snapp.market/api/v2/vendors/{}/products?categories%5B%5D={}&limit={}&offset={}'.format(
            storecode, 278345, limit, off)

        products_list = '---'

        while (products_list == '---'):
            try:
                products_list = json.loads(
                    requests.get(products_url).text)['results']
            except:
                time.sleep(1)

        for product in products_list:

            product_dict = {}

            try:
                product_dict['product_id'] = product['id']
            except:
                product_dict['product_id'] = '---'
            try:
                product_dict['product_name'] = product['title']
            except:
                product_dict['product_name'] = '---'
            try:
                product_dict['product_max_order'] = product['max_order_cap']
            except:
                product_dict['product_max_order'] = '---'
            try:
                product_dict['product_selling_price'] = product['discounted_price']
            except:
                product_dict['product_selling_price'] = '---'
            try:
                product_dict['product_main_price'] = product['price']
            except:
                product_dict['product_main_price'] = '---'
            try:
                product_dict['product_discount_percent'] = product['discount_percent']
            except:
                product_dict['product_discount_percent'] = '---'
            try:
                product_dict['product_brand_name'] = product['brand']['title']
            except:
                product_dict['product_brand_name'] = '---'
            try:
                product_dict['product_category'] = extract_type(
                    product['title'])
            except:
                product_dict['product_category'] = '---'

            products.append(product_dict)

    return({'products': products})


def status_translate(x):
    if(x == 'marketable'):
        return 'قابل فروش'
    if(x == 'coming_soon'):
        return 'به زودی'
    if(x == 'in_supply'):
        return 'در حال تامین'
    if(x == 'stop_production'):
        return 'توقف تولید'

def offer_translate(x):
    if(x == 'none'):
        return 'معمولی'
    if(x == 'special-offer'):
        return 'فروش ویژه'
    if(x == 'incredible'):
        return 'پیشنهاد شگفت انگیز'

def rial_be_toman(x):
    try:
        return int(x/10)
    except:
        return '---'

@app.get('/dkproducts')
def dkproducts():

    group_translate = {
    'khame': 'خامه',
    'shir': 'شیر',
    'mast': 'ماست',
    'doogh': 'دوغ',
    'panir': 'پنیر',
    'kashk': 'کشک',
    'deser': 'دسر',
    'kareh': 'کره',
}

    application_products = []

    application_information = {'khame': {}, 'shir': {}, 'mast': {}, 'doogh': {}, 'panir': {}, 'kashk': {}, 'deser': {}, 'kareh': {}}


    casting = {'khame': 'https://api.digikala.com/v1/categories/cream/search/?page=1', 'shir': 'https://api.digikala.com/v1/categories/milk/search/?page=1', 'mast': 'https://api.digikala.com/v1/categories/yogurt/search/?page=1', 'doogh': 'https://api.digikala.com/v1/categories/doogh/search/?page=1',
            'panir': 'https://api.digikala.com/v1/categories/cheese/search/?page=1', 'kashk': 'https://api.digikala.com/v1/categories/whey/search/?page=1', 'deser': 'https://api.digikala.com/v1/categories/ready-dessert/search/?page=1', 'kareh': 'https://api.digikala.com/v1/categories/butter/search/?page=1'}

    for categ in list(application_information.keys()):

        base_dict = '---'

        while (base_dict == '---'):
            try:
                base_dict = json.loads(requests.get(casting[categ], timeout=5).text)
            except:
                time.sleep(0.1)

        base_data = base_dict['data']

        application_information[categ]['number_of_products'] = base_data['pager']['total_items']
        application_information[categ]['number_of_pages'] = base_data['pager']['total_pages']
        application_information[categ]['category_id'] = base_data['category']['id']
        application_information[categ]['category_persian_title'] = base_data['category']['title_fa']
        application_information[categ]['category_english_title'] = base_data['category']['code']
        application_information[categ]['brands'] = [{'brand_id': brand['id'], 'brand_persian_title':brand['title_fa'],'brand_english_title':brand['code']} for brand in base_data['filters']['brands']['options']]


        for product in base_data['products']:
        
            product_dict = {}

            try:
                product_dict['product_id'] = product['id']
            except:
                product_dict['product_id'] = '---'
            try:
                product_dict['product_persian_title'] = product['title_fa']
            except:
                product_dict['product_persian_title'] = '---'
            try:
                product_dict['product_english_title'] = product['title_en']
            except:
                product_dict['product_english_title'] = '---'
            try:
                product_dict['product_star_rate'] = product['rating']['rate']
            except:
                product_dict['product_star_rate'] = '---'
            try:
                product_dict['product_star_number_of_scorer'] = product['rating']['count']
            except:
                product_dict['product_star_number_of_scorer'] = '---'
            try:
                product_dict['product_status'] = status_translate(product['status'])
            except:
                product_dict['product_status'] = '---'
            try:
                product_dict['product_brand'] = product['data_layer']['brand']
            except:
                product_dict['product_brand'] = '---'
            try:
                product_dict['product_offer'] = offer_translate(product['data_layer']['dimension7'])
            except:
                product_dict['product_offer'] = '---'
            try:
                product_dict['product_min_price_last_month'] = rial_be_toman(product['properties']['min_price_in_last_month'])
            except:
                product_dict['product_min_price_last_month'] = '---'
            try:
                product_dict['product_satisfy_rate'] = product['default_variant']['statistics']['total_rate']
            except:
                product_dict['product_satisfy_rate'] = '---'
            try:
                product_dict['product_satisfy_number_of_scorer'] = product['default_variant']['statistics']['total_count']
            except:
                product_dict['product_satisfy_number_of_scorer'] = '---'
            try:
                product_dict['product_digiplus_cashback'] = rial_be_toman(product['default_variant']['digiplus']['cash_back'])
            except:
                product_dict['product_digiplus_cashback'] = '---'
            try:
                product_dict['product_digiclub_point'] = product['default_variant']['digiclub']['point']
            except:
                product_dict['product_digiclub_point'] = '---'
            try:
                product_dict['product_selling_price'] = rial_be_toman(product['default_variant']['price']['selling_price'])
            except:
                product_dict['product_selling_price'] = '---'
            try:
                product_dict['product_rrp_price'] = rial_be_toman(product['default_variant']['price']['rrp_price'])
            except:
                product_dict['product_rrp_price'] = '---'
            try:
                product_dict['product_order_limit'] = product['default_variant']['price']['order_limit']
            except:
                product_dict['product_order_limit'] = '---'
            try:
                product_dict['product_discount_percent'] = product['default_variant']['price']['discount_percent']
            except:
                product_dict['product_discount_percent'] = '---'
            try:
                product_dict['product_group'] = group_translate[categ]
            except:
                product_dict['product_group'] = '---'

            application_products.append(product_dict)

        # /////////////////////////////////////////////////////////////////////////////////////////////////////////////

    for category in list(application_information.keys()):
        category_title = application_information[category]['category_english_title']
        for page_number in range(2, (application_information[category]['number_of_pages'])+1):
            url = 'https://api.digikala.com/v1/categories/{}/search/?page={}'.format(
                category_title, page_number)
            products_dict = '---'
            while (products_dict == '---'):
                try:
                    products_dict = json.loads(requests.get(url, timeout=5).text)
                except:
                    time.sleep(0.1)

            products_data = products_dict['data']

            for product in products_data['products']:

                product_dict = {}

                try:
                    product_dict['product_id'] = product['id']
                except:
                    product_dict['product_id'] = '---'
                try:
                    product_dict['product_persian_title'] = product['title_fa']
                except:
                    product_dict['product_persian_title'] = '---'
                try:
                    product_dict['product_english_title'] = product['title_en']
                except:
                    product_dict['product_english_title'] = '---'
                try:
                    product_dict['product_star_rate'] = product['rating']['rate']
                except:
                    product_dict['product_star_rate'] = '---'
                try:
                    product_dict['product_star_number_of_scorer'] = product['rating']['count']
                except:
                    product_dict['product_star_number_of_scorer'] = '---'
                try:
                    product_dict['product_status'] = status_translate(product['status'])
                except:
                    product_dict['product_status'] = '---'
                try:
                    product_dict['product_brand'] = product['data_layer']['brand']
                except:
                    product_dict['product_brand'] = '---'
                try:
                    product_dict['product_offer'] = offer_translate(product['data_layer']['dimension7'])
                except:
                    product_dict['product_offer'] = '---'
                try:
                    product_dict['product_min_price_last_month'] = rial_be_toman(product['properties']['min_price_in_last_month'])
                except:
                    product_dict['product_min_price_last_month'] = '---'
                try:
                    product_dict['product_satisfy_rate'] = product['default_variant']['statistics']['total_rate']
                except:
                    product_dict['product_satisfy_rate'] = '---'
                try:
                    product_dict['product_satisfy_number_of_scorer'] = product['default_variant']['statistics']['total_count']
                except:
                    product_dict['product_satisfy_number_of_scorer'] = '---'
                try:
                    product_dict['product_digiplus_cashback'] = rial_be_toman(product['default_variant']['digiplus']['cash_back'])
                except:
                    product_dict['product_digiplus_cashback'] = '---'
                try:
                    product_dict['product_digiclub_point'] = product['default_variant']['digiclub']['point']
                except:
                    product_dict['product_digiclub_point'] = '---'
                try:
                    product_dict['product_selling_price'] = rial_be_toman(product['default_variant']['price']['selling_price'])
                except:
                    product_dict['product_selling_price'] = '---'
                try:
                    product_dict['product_rrp_price'] = rial_be_toman(product['default_variant']['price']['rrp_price'])
                except:
                    product_dict['product_rrp_price'] = '---'
                try:
                    product_dict['product_order_limit'] = product['default_variant']['price']['order_limit']
                except:
                    product_dict['product_order_limit'] = '---'
                try:
                    product_dict['product_discount_percent'] = product['default_variant']['price']['discount_percent']
                except:
                    product_dict['product_discount_percent'] = '---'
                try:
                    product_dict['product_group'] = group_translate[category]
                except:
                    product_dict['product_group'] = '---'

                application_products.append(product_dict)

    return({'products':application_products})





