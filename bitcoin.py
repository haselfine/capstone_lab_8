import requests
import logging

logging.basicConfig(filename='debug.log', level=logging.DEBUG, format=f'%(asctime)s - %(name)s - %(levelname)s - %(message)s')
bitcoin_api_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

def main():
    usd_bc_ex_rate = api_call()
    if usd_bc_ex_rate != 'API_Error':
        bitcoin = 4 #normally get_user_bitcoin()
        bc_in_usd = convert_to_bitcoin(bitcoin, usd_bc_ex_rate)
        print(f'Your bitcoin is worth {bc_in_usd}')

def api_call():
    try:
        response = requests.get(bitcoin_api_url)
        data = response.json()
        return data['bpi']['USD']['rate_float']
    except:
        logging.exception(f'Error requesting url.')
        return 'API_Error'

def get_user_bitcoin():
    while True:
        try:        
            user_bitcoin = input('How many bitcoin you got? ')
            if is_float(user_bitcoin):
                return float(user_bitcoin)
        except Exception as e:
            logging.debug(e)
            continue
        print('Please enter a digit for your bitcoin.')


def convert_to_bitcoin(bitcoin, usd_bc_ex_rate):
    return bitcoin * usd_bc_ex_rate
    

def is_float(user_bitcoin):
    try:
        float(user_bitcoin)
        return True
    except:
        return False

if __name__ == '__main__':
    main()