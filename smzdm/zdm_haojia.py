# -*- coding: utf-8 -*-

"""
@author: guzhi
@file: zdm_test_request.py
@time: 2020-04-21 18:18:05
@projectExplain:
"""

import time
import hashlib
import requests

cookies = {
    '__ckguid': 'G3u6v3bL33sBs2V1NkI59',
    'device_id': '2130706433157162818325369124f9971c5d211afedd050729ed61e228',
    'homepage_sug': 'l',
    'r_sort_type': 'score',
    '_ga': 'GA1.2.661160588.1571628218',
    'PHPSESSID': 'ff4a8e00a59c2709fa7bb90e2affb498',
    'smzdm_user_source': '8B8EBBD026D07D3BE111A440F9F0E115',
    'wt3_sid': '%3B999768690672041',
    'wt3_eid': '%3B999768690672041%7C2158452555500343166%232158605479400313884',
    'smzdm_user_view': '8B76F6815B00D2C35281FD5D9E59902A',
    'zdm_qd': '%7B%22referrer%22%3A%22https%3A%2F%2Fwww.dogedoge.com%2F%22%7D',
    'Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58': '1584524168,1586940104',
    'Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58': '1586940175',
    '_zdmA.uid': 'ZDMA.mCD_wvmaG.1586940175.2419200',
    '__jsluid_s': '498944086a7edb0a6c2aaf8867e2c643',
}

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    'Sec-Fetch-Dest': 'document',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

params = (
    # ('price_lt', ''),
    ('order', 'recommend'),
    # ('category_ids', ''),
    # ('price_gt', ''),
    ('refresh', '0'),
    ('haojia_tab_abtest', 'b'),
    ('haojia_title_abtest', 'a'),
    ('past_num', '0'),
    # ('hour', ''),
    # ('tag_id', ''),
    # ('mall_ids', ''),
    ('ab_test', 'n'),
    # ('time_sort', ''),
    # ('manual_sort', ''),
    ('page', 1),
    ('haojia_coupon_abtest', 'a'),
    ('limit', '20'),
    ('ad_info',
     '{"android_id":"647f1ec3c069885a","brand":"google","device_height":683,"device_width":411,"height":0,"imei":"","imei_md5":"e44116ed0fb0b5ec748aac5877ff5e0b","ip":"39.105.22.116","lan":"zh-CN","mac":"D4:61:4E:72:70:7F","manufacturer":"Huawei","model":"Nexus 6P","network":1,"operator":0,"os":"Android","osv":"6.0","pixel_ratio":560,"timezone_offset":480,"user_agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 6P Build/MDA89D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.0.2403.117 Mobile Safari/537.36","width":0}'),
    ('v', '9.7.0'),
    ('f', 'android'),
    ('time', int(time.time() * 1000)),
    ('weixin', '1'),
)
hashmap = dict(sorted(dict(params).items(), key=lambda x: x[0]))
print(hashmap)
sb = ""
for k, v in hashmap.items():
    sb += k + '=' + str(v).replace(" ", "") + "&"

str2 = 'key=apr1$AwP!wRRT$gJ/q.X24poeBInlUJC'
sb += str2
print('sb', sb)
print(hashlib.md5(sb.encode()).hexdigest().upper())
sign = hashlib.md5(sb.encode()).hexdigest().upper()
new_params= params + (("sign", sign),)
print(new_params)
response = requests.get('https://haojia-api.smzdm.com/home/list', headers=headers, params=new_params, cookies=cookies,
                        verify=False)

print(response.text)
