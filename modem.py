import re
import json
import requests
import os


def send_request_off():
	try:

		xml_data = '<?xml version: "1.0" encoding="UTF-8"?><request><dataswitch>0</dataswitch></request>'

		headers = {
			'Content-Type': 'application/xml',
			'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0",
			'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
			'Accept-Language': "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
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
		return html

	except:
		return ''

send_request_off()

#c:\Python38\python c:\modem\modem.py