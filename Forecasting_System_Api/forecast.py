from typing import final

import numpy as np

import pandas as pd

import warnings

import pickle

from pathlib import Path

from sklearn.preprocessing import LabelEncoder

import json

warnings.filterwarnings('ignore')


def forecast(product_name, area, promotion, month, week, day):

    result = {}

    result['forecast'] = []

    product_name = str(product_name)

    HERE = str(Path(__file__).parent) + '\products\{}'.format(product_name)

    xgmodel = pickle.load(open(HERE + '\{}XG.sav'.format(product_name), "rb"))

    # print(HERE + '\{}XG.sav'.format(product_name))

    model = pickle.load(
        open(HERE + '\{}Linear.sav'.format(product_name), "rb"))

    # print(HERE + '\{}Linear.sav'.format(product_name))

    encoder = LabelEncoder()

    encoder.classes_ = np.load(HERE + "\classes.npy", allow_pickle=True)

    file = open(HERE + '\datacolumns.txt', 'r')

    items = file.read().split('\n')

    file.close()

    items = items[:-1]

    Areas = {'ShomalGharb': ['Ardebil H', 'Ramsar H', 'Rasht S'], 'ShomalMarkaz': ['Amol 1 H', 'Amol 2 H', 'Babol H', 'Chalus H', 'Sari H'],

             'Jonoob': ['Ahvaz H', 'Esfahan S', 'Shiraz S', 'Yazd S'], 'Gharb': ['Ghazvin H', 'Hamedan H', 'Kermanshah H', 'Lorestan 2 H', 'Tabriz S'],

             'Markaz': ['Karaj S', 'Tehran S'], 'Shargh': ['Gorgan H', 'Mashhad H']}

    persian_centers = {'Ardebil H': 'اردبیل هیبرید', 'Ramsar H': 'رامسر هیبرید', 'Rasht S': 'رشت سایت', 'Amol 1 H': 'آمل 1 هیبرید', 'Amol 2 H': 'آمل 2 هیبرید', 'Babol H': 'بابل هیبرید', 'Chalus H': 'چالوس هیبرید', 'Sari H': 'ساری هیبرید',
                       'Ahvaz H': 'اهواز هیبرید', 'Esfahan S': 'اصفهان سایت', 'Shiraz S': 'شیراز سایت', 'Yazd S': 'یزد سایت', 'Ghazvin H': 'قزوین هیبرید', 'Hamedan H': 'همدان هیبرید', 'Kermanshah H': 'کرمانشاه هیبرید', 'Lorestan 2 H': 'لرستان 2 هیبرید', 'Tabriz S': 'تبریز سایت',
                       'Karaj S': 'کرج سایت', 'Tehran S': 'تهران سایت', 'Gorgan H': 'گرگان هیبرید', 'Mashhad H': 'مشهد هیبرید'
                       }

    stats_df = pd.read_excel(HERE + '\stats.xlsx', index_col=0)

    stats_dict = {}

    for i in stats_df['CenterName'].unique():

        stats_dict[i] = stats_df[stats_df['CenterName']
                                 == i]['MajorUnitQuantity'].describe()

    Centers = pd.read_excel(HERE + '\information2.xlsx')

    # j=0

    # for i in Areas.keys():

    #     print(i,'\t',j,'\n')

    #     j=j+1

    Area_code = area

    # print('')

    # low_xg = []

    # avg_xg = []

    # up_xg = []

    # low_linear = []

    # avg_linear = []

    # up_linear = []

    # print(Areas[list(Areas)[Area_code]],'\n')

    new_discount = promotion

    # print('')

    new_shamsimonth = month

    # print('')

    new_weekofmonth = week

    # print('')

    new_dayofweek = day

    # print('')

    # print('#######################################################################################')

    for i in Areas[list(Areas)[Area_code]]:

        new_centername = i
        
        persian_centername = persian_centers[new_centername]

        # result[new_centername] = {}

        # print('Your Center is :\t' , i)

        # print('')

        # print(stats_dict[new_centername])

        # result[new_centername]['statics'] = stats_dict[new_centername]

        # print('')

        new_test = pd.DataFrame(data={'Discount': [new_discount], 'ShamsiMonth': [new_shamsimonth], 'weekofmonth': [
                                new_weekofmonth], 'dayofweek': [new_dayofweek], 'Center': [new_centername]})

        # print('Your Test Item Is : \n')

        # print(new_test,'\n\n')

        new_test['Center'] = encoder.transform(new_test['Center'])

        result['forecast'].append(
            {'center': persian_centername, 'xgboost': {}, 'linear': {}})

        xgpredict = xgmodel.predict(new_test)

        # print('\t\tXGBoost Model Results : \n\n')

        # print('Average Value In Each Invoice Is : \t',xgpredict,'\n\n')

        result['forecast'][-1]['xgboost']['unit'] = round(float(xgpredict))

        # print('Lower Limit In Target Center Is : \t',(xgpredict - 2.40) * Centers[Centers['Center']==new_centername]['count'].iloc[0],'\n\n')

        result['forecast'][-1]['xgboost']['low'] = round(float(
            (xgpredict - 2.40) * Centers[Centers['Center'] == new_centername]['count'].iloc[0]))

        # low_xg.append((xgpredict - 2.40) * Centers[Centers['Center']==new_centername]['count'].iloc[0])

        # print('Average Limit In Target Center Is : \t',(xgpredict) * Centers[Centers['Center']==new_centername]['count'].iloc[0],'\n\n')

        result['forecast'][-1]['xgboost']['mid'] = round(float(
            (xgpredict) * Centers[Centers['Center'] == new_centername]['count'].iloc[0]))

        # avg_xg.append((xgpredict) * Centers[Centers['Center']==new_centername]['count'].iloc[0])

        # print('Upper Limit In Target Center Is : \t',(xgpredict + 2.40) * Centers[Centers['Center']==new_centername]['count'].iloc[0],'\n\n')

        result['forecast'][-1]['xgboost']['up'] = round(float(
            (xgpredict + 2.40) * Centers[Centers['Center'] == new_centername]['count'].iloc[0]))

        # up_xg.append((xgpredict + 2.40) * Centers[Centers['Center']==new_centername]['count'].iloc[0])

        new_test_2 = pd.DataFrame(data={'Discount': [new_discount], 'ShamsiMonth': [new_shamsimonth], 'weekofmonth': [
                                  new_weekofmonth], 'dayofweek': [new_dayofweek], 'Center': [new_centername]})

        test = pd.get_dummies(new_test_2, prefix='Center')

        for i in (items[4:]):

            test[i] = 0

        test.columns = items

        col = 'Center_' + new_centername

        test[col] = 1

        # print('Your Test Item Is : \n')

        # print(test,'\n\n')

        predict = model.predict(test)

        # print('\t\tLinear Model Results : \n\n')

        # print('Average Value In Each Invoice Is : \t',predict,'\n\n')

        result['forecast'][-1]['linear']['unit'] = round(float(predict))

        # print('Lower Limit In Target Center Is : \t',(predict - 2.87) * Centers[Centers['Center']==new_centername]['count'].iloc[0],'\n\n')

        result['forecast'][-1]['linear']['low'] = round(float(
            (predict - 2.87) * Centers[Centers['Center'] == new_centername]['count'].iloc[0]))

        # low_linear.append((predict - 2.87) * Centers[Centers['Center']==new_centername]['count'].iloc[0])

        # print('Average Limit In Target Center Is : \t',(predict) * Centers[Centers['Center']==new_centername]['count'].iloc[0],'\n\n')

        result['forecast'][-1]['linear']['mid'] = round(
            float((predict) * Centers[Centers['Center'] == new_centername]['count'].iloc[0]))

        # avg_linear.append((predict) * Centers[Centers['Center']==new_centername]['count'].iloc[0])

        # print('Upper Limit In Target Center Is : \t',(predict + 2.87) * Centers[Centers['Center']==new_centername]['count'].iloc[0],'\n\n')

        result['forecast'][-1]['linear']['up'] = round(float(
            (predict + 2.87) * Centers[Centers['Center'] == new_centername]['count'].iloc[0]))

        # up_linear.append((predict + 2.87) * Centers[Centers['Center']==new_centername]['count'].iloc[0])

        # print('#######################################################################################')

    # return json.dumps(result)

    return result

    # print('')

    # print('Our Lower and Average and Upper limits for Area')

    # print('')

    # print('Lower XG  : ',list(low_xg))

    # print('')

    # print('Average XG  : ',list(avg_xg))

    # print('')

    # print('Upper XG  : ',list(up_xg))

    # print('')

    # print('Lower Linear  : ',list(low_linear))

    # print('')

    # print('Average Linear  : ',list(avg_linear))

    # print('')

    # print('Upper Linear  : ',list(up_linear))

    # print('')


# forecast('mast-saboo-por-1800',3,0.12,3,4,5)
