import random

def get_proxy_new()-> dict:
    """
    It returns a dictionary with the keys 'http' and 'https' and the values are the proxy address to use the datacenter proxy
    :return: A dictionary with the keys 'http' and 'https' and the values are the entry variable.
    """

    

    # username = 'brd-customer-hl_435d7aea-zone-unblocker-country-mx'
    # password = 'dbp4d0vd1iqd'

    username = 'brd-customer-hl_d779d3e0-zone-zone_dc-country-mx'
    password = 'rd1j0pjs9u2n'

    # username = 'brd-customer-hl_435d7aea-zone-residential-country-co'
    # password = '3be0a9mtx4y5'

    port = 22225
    session_id = random.random()
    super_proxy_url = ('http://%s-session-%s:%s@zproxy.lum-superproxy.io:%d' %
        (username, session_id, password, port))
    proxy_handler = {
        'http': super_proxy_url,
        'https': super_proxy_url,
    } 
    return proxy_handler