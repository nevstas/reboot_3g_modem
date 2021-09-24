import re
import json
import requests
import os
import time


def send_request_to_modem(val):
	try:
		headers = {
			'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0",
			'Accept': "*/*",
			'Accept-Language': "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
			'Connection': "keep-alive",
			'X-Requested-With': "XMLHttpRequest",
		}

		session = requests.Session()
		compose_url = 'http://192.168.1.1/api/webserver/token'
		response = session.get(compose_url,
								headers=headers,
								allow_redirects=False,
								timeout=10)

		response_code = response.status_code
		html = response.text

		m = re.search('<token>([^<]+)<', html)
		token = m.group(1)

		xml_data = '<?xml version: "1.0" encoding="UTF-8"?><request><dataswitch>' + str(val) + '</dataswitch></request>'

		headers = {
			'__RequestVerificationToken': token,
			'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0",
			'Accept': "*/*",
			'Accept-Language': "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
			'Connection': "keep-alive",
			'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
			'Referer': "http://192.168.1.1/html/home.html",
			'X-Requested-With': "XMLHttpRequest",
		}



		session = requests.Session()
		compose_url = 'http://192.168.1.1/api/dialup/mobile-dataswitch'
		response = session.post(compose_url,
								headers=headers,
								data=xml_data,
								allow_redirects=False,
							   timeout=10)

		response_code = response.status_code
		html = response.text
		m = re.search('<response>([^<]+)<', html)
		res = m.group(1)
		if res == 'OK':
			return True

		return False

	except:
		return False

def reboot_modem():
	result_off = send_request_to_modem(0)
	# time.sleep(0.1)
	result_on = send_request_to_modem(1)

	if result_off and result_on:
		return True
	else:
		return False

if reboot_modem():
	print("ok")
else:
	print("error")

#c:\Python38\python c:\modem\modem.py