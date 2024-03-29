import os
import asyncio
import random
from dotenv import load_dotenv
load_dotenv()

loop = asyncio.get_event_loop()

host = os.getenv('HOST')
port = os.getenv('PORT')
org_id = os.getenv('ORG_ID')
app_id = os.getenv('APP_ID')
api_key = os.getenv('API_KEY')
ussd_code = os.getenv('USSD_CODE')
purse_id = os.getenv('PURSE_ID')
mpesa_paybill = os.getenv('MPESA_PAYBILL')
sms_short_code = os.getenv('SMS_SHORT_CODE')
sms_sender_id = os.getenv('SMS_SENDER_ID')
telegram_number = os.getenv('TELEGRAM_NUMBER')
voice_number = os.getenv('VOICE_NUMBER')
messenger_number = os.getenv('MESSENGER_NUMBER')
customer_number = {'number': f'+2547{random.randint(10000000,99999999)}',
                   'provider': 'cellular'}
adopted_customer = {'number': f'+2547{random.randint(10000000,99999999)}',
                    'provider': 'cellular'}
