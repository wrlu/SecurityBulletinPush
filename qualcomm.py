import requests
import re


base_url = 'https://www.qualcomm.com/company/product-security/bulletins'

month_table = {
    1: 'january',
    2: 'february',
    3: 'march',
    4: 'april',
    5: 'may',
    6: 'june',
    7: 'july',
    8: 'august',
    9: 'september',
    10: 'october',
    11: 'november',
    12: 'december'
}

def get_latest_bulletin():
    latest_date = get_latest_bulletin_date()
    return latest_date, base_url + '/' + latest_date + '-bulletin'


def get_latest_bulletin_date():
    response = __send_request__('/')
    if response.status_code == 200:
        result = response.text
        td_list = re.findall('href="/company/product-security/bulletins/(.+?)-bulletin"', result)
        latest_date = td_list[0]
        return latest_date
    return ''


def __send_request__(path: str):
    response = requests.get(base_url + path)
    return response


def do():
    print(get_latest_bulletin())
