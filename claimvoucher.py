from urllib.parse import urlparse, parse_qs
import requests
import base64
import datetime
import time 
url = input("Type url:")
parsed = urlparse(url)
params = parse_qs(parsed.query)
promotion_id = int(params["promotionId"][0])
voucher_code = base64.b64decode(params["evcode"][0]).decode("utf-8")
signature = params["signature"][0]
api = "https://shopee.vn/api/v2/voucher_wallet/get_voucher_detail"
payload = {
    "promotionid": promotion_id,
    "voucher_code": voucher_code,
    "signature": signature,
    "need_basic_info": True,
    "need_user_voucher_status": True,
    "source": "0",
    "addition": []
}
while(1):
    print("type the target time")
    month = int(input("target month:"))
    day = int(input("target date:"))
    hour = int(input("target hour:"))
    minute = int(input("target minute:"))
    targettime = datetime.datetime(2026, month, day, hour, minute) 
    if(targettime > datetime.datetime.now()): break
while(1): 
    r = requests.post(api, json=payload)
    fully_used = bool(r.json()["data"]["voucher_basic_info"]["fully_used"])
    if fully_used: print("no vouchers left")
    else:
        print("claim now")
        break
    print(datetime.datetime.now())
    if(targettime - datetime.datetime.now()).total_seconds() > 3: time.sleep(0.5)