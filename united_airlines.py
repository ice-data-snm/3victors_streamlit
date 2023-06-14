#%%

import requests, json, pytz, ast
import pandas as pd
from aux import get_proxy_new as get_proxy
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

from google.cloud import storage
from google.cloud import secretmanager

#%%


def access_secret(secret_id:str, version_id:str ='latest'):
    '''Function for the secrets'''
    
    client = secretmanager.SecretManagerServiceClient()
    name = f'{secret_id}/versions/{version_id}'
    response = client.access_secret_version(name=name)
    return response.payload.data.decode("UTF-8")



#%%
def get_first_search (country_oringin, country_departure, Date_mm_dd_yyyy ):

    headers = {
        'Host': 'mobileapi.united.com',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'User-Agent': 'UnitedCustomerFacingIPhone/4.1.83 (Version 16.5 (Build 20F66))',
        'Accept-Language': 'en-US,en;q=0.9',
        'Content-Type': 'application/json',
    }

    json_data = {
        'travelerTypes': [
            {
                'count': 1,
                'travelerType': 'Adult',
            },
        ],
        'accessCode': 'ACCESSCODE',
        'isReshopChange': False,
        'awardTravel': False,
        'isShareTripSearchAgain': False,
        'isEditSearchEnabledOnBookingFSR': False,
        'trips': [
            {
                'origin': country_oringin,
                'destination': country_departure,
                'useFilters': False,
                'departDate': Date_mm_dd_yyyy,#'07/25/2023',
                'searchNearbyOriginAirports': False,
                'destinationAllAirports': 0,
                'cabin': 'econ',
                'searchNearbyDestinationAirports': False,
                'originAllAirports': 0,
                'changeType': '0',

            },
        ],
        'fareType': 'lf',
        'showMileageDetails': False,
        'isELFFareDisplayAtFSR': False,
        'hashPinCode': '',
        'searchType': 'OW',
        'isYoungAdultBooking': False,
        'isCorporateBooking': False,
        'fareClass': '',
        'numberOfChildren2To4': 0,
        'getNonStopFlightsOnly': True,
        # "pageNumber": 100,
        # 'deviceId': 'DACE6F60-A777-4391-B360-2D2DB7A9E57D',
        'maxNumberOfStops': 2,
        'travelType': 'RA',
        'application': {
            'id': 1,
            'name': 'iOS',
            'isProduction': False,
            'version': {
                'minor': '4.1.83',
                'major': '4.1.83',
                'displayText': '',
                'build': '',
            },
        },
        'countryCode': 'US',
        'numberOfInfantWithSeat': 0,
        'promotionCode': '',
        'languageCode': 'en-US',
        'maxNumberOfTrips': 2500,
        'numberOfInfantOnLap': 0,
        'numberOfAdults': 0,
        # 'transactionId': 'DACE6F60-A777-4391-B360-2D2DB7A9E57D|F89BAF20-3E00-4C79-8081-F8B14A1CCDDC',
        'premierStatusLevel': 0,
        'pointOfSaleCountryName': 'United States',
        'catalogItems': [
            {
                'id': '11388',
                'currentValue': '1',
            },
            {
                'id': '11389',
                'currentValue': '0',
            },
            {
                'id': '11428',
                'currentValue': '1',
            },
            {
                'id': '11587',
                'currentValue': '1',
            },
            {
                'id': '11502',
                'currentValue': '1',
            },
            {
                'id': '11699',
                'currentValue': '1',
            },
            {
                'id': '11647',
                'currentValue': '1',
            },
            {
                'id': '11643',
                'currentValue': '1',
            },
            {
                'id': '11757',
                'currentValue': '1',
            },
            {
                'id': '11870',
                'currentValue': '1',
            },
            {
                'id': '12018',
                'currentValue': '0',
            },
            {
                'id': '11793',
                'currentValue': '1',
            },
            {
                'id': '11815',
                'currentValue': '1',
            },
            {
                'id': '11867',
                'currentValue': '1',
            },
            {
                'id': '11873',
                'currentValue': '1',
            },
            {
                'id': '11890',
                'currentValue': '1',
            },
            {
                'id': '12003',
                'currentValue': '1',
            },
            {
                'id': '11878',
                'currentValue': '1',
            },
            {
                'id': '11936',
                'currentValue': '1',
            },
        ],
        'numberOfChildren5To11': 0,
        'serviceType': '',
        'numberOfChildren12To17': 0,
        'experiments': [
            'NoChangeFee',
            'FSRRedesignA',
        ],
        'numberOfSeniors': 0,
    }

    response = requests.post(
        'https://mobileapi.united.com/shoppingservice/api/Shopping/Shop',
        headers=headers,
        json=json_data,
        proxies=get_proxy()
    
    )
    return response.json()


#%%


def get_others_search (country_oringin, airportsDestination, sessionId, cartId):


    headers = {
        'Host': 'mobileapi.united.com',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'User-Agent': 'UnitedCustomerFacingIPhone/4.1.83.0 CFNetwork/1408.0.4 Darwin/22.5.0',
        # 'Content-Length': '11167',
        'Accept-Language': 'en-US,en;q=0.9',
        'Content-Type': 'application/json',
    }

    data = {
            "deviceId": "DACE6F60-A777-4391-B360-2D2DB7A9E57D",
            "searchFiltersIn": {
                "stopCountExcl": -1,
                "filterSortPaging": False,
                "airportsOrigin": country_oringin,#"MEX",
                "stopCountMax": 2,
                "bookingCodes": "",
                "durationStopMax": -1,
                "pageNumber": 2,
                "airportsDestination": airportsDestination, #"YVR",
                "showDurationFilters": True,
                "carrierStar": True,
                # "equipmentTypes": "7M8,7M9,E7W,789,752,320,738,321,319,CR9,73G,739,333,77L,E70,77W,777,763,DH4,781,753,CR5",
                "sortType1": "",
                "aircraftTypes": "",
                "stopCountMin": 0
            },
            "cartId": cartId,
            "sessionId": sessionId,
            "lastTripIndexRequested": 1,
            "languageCode": "en-US",
            "accessCode": "ACCESSCODE",
            "application": {
                "id": 1,
                "name": "iOS",
                "isProduction": False,
                "version": {
                    "minor": "4.1.83",
                    "major": "4.1.83",
                    "displayText": "",
                    "build": ""
                }
            },
        }

    response = requests.post(
        'https://mobileapi.united.com/shoppingservice/api/Shopping/OrganizeShopResults',
        headers=headers,
        json=data,
        proxies=get_proxy()
    )
    print(len(response.json()['availability']['trip']['flattenedFlights']))
    return response.json()['availability']['trip']['flattenedFlights']


#%%


def upload_blob(folder_name,name_json):
    ''' Uploads the information  to the bucket '''

    secret = access_secret('projects/132532680167/secrets/ICE-SNM')  
    json_secret = json.dumps(ast.literal_eval(secret))

    with open("iceberg-data-5df1af170866.json", "w") as outfile:
        outfile.write(json_secret)

    storage_client = storage.Client.from_service_account_json(
        "iceberg-data-5df1af170866.json")

    bucket_name = 'ice-3-victors'

    # destination_file_name = str('test_info.json')

    bucket = storage_client.bucket(bucket_name)
    destination_blob_name = f"info_ua/{folder_name}/{name_json}"                                                                                                         
    blob = bucket.blob(destination_blob_name)
    pdf_file = name_json

    text_to_output = "https://console.cloud.google.com/storage/browser/_details/ice-3-victors/"+destination_blob_name
    blob.upload_from_filename(pdf_file)

    print(
        f"File {pdf_file} uploaded to {destination_blob_name}."
    )

    return "Proceso terminado, encuentre el archivo pdf en "+text_to_output
    # except:



def get_info_for_trip(list_input):

    try:
        country_oringin, airportsDestination, Date_mm_dd_yyyy , min_Date_mm_dd_yyyy,  max_new_date= list_input
        response = get_first_search (country_oringin, airportsDestination, Date_mm_dd_yyyy)
        response

        sessionId = response['shopRequest']['sessionId']
        cartId = response['availability']['cartId']
        # json_response = response.json()
        try:
            flights = response['availability']['trip']['flattenedFlights']
            response = get_others_search (country_oringin, airportsDestination, sessionId, cartId)

            flights += response

            timestamp = datetime.now(pytz.timezone('America/Bogota')).strftime('%Y%m%d')

            name = f'{country_oringin}_{airportsDestination}_{Date_mm_dd_yyyy}_{timestamp}.json'
            name = name.replace('/','')
            folder_name = f'{country_oringin}_{airportsDestination}_{min_Date_mm_dd_yyyy}_{max_new_date}'
            folder_name = folder_name.replace('/','')
            flights_ = []
            for each in flights:
                each['flight_date'] = Date_mm_dd_yyyy
                timestamp = datetime.now(pytz.timezone('America/Bogota')).strftime('%m%d%Y')
                each['search_date'] = timestamp
                flights_+=each

            with open(name, 'w') as outfile:
                json.dump(flights_, outfile)

            upload_blob(folder_name,name)

            return flights_
        except Exception as e:
            print(e)
            print(' There are less than 15')
            return flights
    except Exception as e:
        print(e)
        print('Search term does not exists')
        return None



def get_dates(date_string, num_days):
    dates = []
    date_format = '%m/%d/%Y'
    current_date = datetime.strptime(date_string, date_format)
    new_date = current_date + timedelta(days=num_days)

    for i in range(num_days):
        new_date = current_date + timedelta(days=i)
        dates.append(new_date.strftime(date_format))

    return dates



def create_list (country_oringin, airportsDestination, Date_mm_dd_yyyy, num_days):
    num_days = min(60,num_days)
    date_format = '%m/%d/%Y'
    current_date = datetime.strptime(Date_mm_dd_yyyy, date_format)
    new_date = current_date + timedelta(days=num_days)
    new_date = new_date.strftime(date_format)

    date_list = get_dates(Date_mm_dd_yyyy, num_days)
    input_list = []
    for i in date_list:
        a = [country_oringin,airportsDestination,i,Date_mm_dd_yyyy,  new_date]
        input_list+=[a]
    return input_list

# country_oringin= 'MEX'
# airportsDestination = 'YVR'
# Date_mm_dd_yyyy = '07/25/2023'

# test = create_list (country_oringin, airportsDestination, Date_mm_dd_yyyy, 24)
# country_oringin, airportsDestination, Date_mm_dd_yyyy = test[0]
# country_oringin
#%%


def get_info_on_threads (country_oringin, airportsDestination, Date_mm_dd_yyyy, num_days):
    search_list = create_list (country_oringin, airportsDestination, Date_mm_dd_yyyy, num_days)
    with ThreadPoolExecutor(max_workers=50) as executor:
        result_pool_sell = list(
                executor.map(get_info_for_trip, search_list),
            )
    result_pool_ = []
    for i in result_pool_sell:
        if i:
            # i['flight_date'] = Date_mm_dd_yyyy
            # timestamp = datetime.now(pytz.timezone('America/Bogota')).strftime('%m%d%Y')
            # i['search_date'] = timestamp
            result_pool_+=i
    return result_pool_
    # df = pl.DataFrame(result_pool_)


# get_dates(Date_mm_dd_yyyy, 15)

#%%
# a = get_info_on_threads ('JFK', 'YYZ', '06/29/2023', 10)

# %%
