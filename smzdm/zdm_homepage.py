# -*- coding: utf-8 -*-

"""
@author: guzhi
@file: zdm_homepage.py
@time: 2020-04-21 19:19:57
@projectExplain:
"""

import time
import json
import random
import socket
import struct
import hashlib
import requests

from fake_useragent import UserAgent

cookies = {
    'smzdm_version': '9.7.0',
    'device_type': 'googleMi+9',
    'client_id': '86fab22d987544c9e4413b205d00458c.1586939163512',
    'rs_id2': '',
    'rs_id4': '',
    'imei': '',
    'login': '0',
    'smzdm_id': '',
    'session_id': '86fab22d987544c9e4413b205d00458c.1587442306680',
    'partner_name': 'wandoujia',
    'is_new_user': '0',
    'android_id': 'e44116ed0fb0b5ec748aac5877ff5e0b',
    'partner_id': '0',
    'rs_id3': '',
    'rs_id1': '',
    'pid': 'okZ1VIZZHe9bOGVaQYfaw9XP1ojHLh6Ddc2sLocBUVZzbfQDpoHn1A%3D%3D',
    'smzdm_user_source': 'e44116ed0fb0b5ec748aac5877ff5e0b',
    'device_smzdm_version_code': '625',
    'new_device_id': 'e44116ed0fb0b5ec748aac5877ff5e0b',
    'mac': 'D4%3A61%3A4E%3A72%3A70%3A7F',
    'rs_id5': '',
    'network': '1',
    'device_system_version': '6.0',
    'device_id': '86fab22d987544c9e4413b205d00458c',
    'device_push': '0',
    'sessionID': '86fab22d987544c9e4413b205d00458c.1587442306680',
    'device_smzdm': 'android',
    'device_s': 'e44116ed0fb0b5ec748aac5877ff5e0b',
    'device_smzdm_version': '9.7.0',
    'ab_test': 'b',
}

headers = {
    'User-Agent': 'smzdm_android_V9.7.0 rv:625 (Nexus 6P;Android6.0;zh)smzdmapp',
    'Host': 'homepage-api.smzdm.com',
}


def get_random(length):
    '''
    生成 16位android 或 32位imei_md5
    :param length:
    :return:
    '''
    return ''.join(random.sample('abcdefghijklmnopqrstuvwxyz1234567890', length))


def get_random_ip():
    '''
    生成IP
    :return:
    '''
    return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))


def random_mac():
    '''
    生成mac地址
    :return:
    '''
    mac = [0x52, 0x54, 0x00,
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: "%02x" % x, mac))


def get_userAgent():
    '''
    生成user-agent
    :return:
    '''
    return UserAgent(verify_ssl=False).random


def task():
    goods_url = set()
    for page in range(1, 100):
        params = (
            # ('is_show_guide', ''),
            ('recfeed_switch', '1'),
            ('refresh', '1'),
            # ('widget_id', ''),
            ('notice_first_feed', '1'),
            # ('oaid', ''),
            ('haojia_title_abtest', 'a'),
            ('update_timestamp', int(time.time() * 1000)),
            ('past_num', '0'),
            ('tab_id', '0'),
            ('smzdm_id', '0'),
            # ('time_sort', ''),
            ('time_sort', int(time.time() - random.randint(80, 100))),
            ('page', page),
            ('limit', '20'),
            # ('ad_info', '{"android_id":"647f1ec3c069885a","brand":"google","device_height":683,"device_width":411,"height":0,"imei":"","imei_md5":"e44116ed0fb0b5ec748aac5877ff5e0b","ip":"39.105.70.246","lan":"zh-CN","mac":"D4:61:4E:72:70:7F","manufacturer":"Huawei","model":"Nexus 6P","network":1,"operator":0,"os":"Android","osv":"6.0","pixel_ratio":560,"timezone_offset":480,"user_agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 6P Build/MDA89D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.0.2403.117 Mobile Safari/537.36","width":0}'),
            ('ad_info',
             '{"android_id":%s,"brand":"google","device_height":683,"device_width":411,"height":0,"imei":"","imei_md5":"%s","ip":"%s","lan":"zh-CN","mac":"%s","manufacturer":"Mi","model":"Mi9","network":1,"operator":0,"os":"Android","osv":"9.0","pixel_ratio":560,"timezone_offset":480,"user_agent":"%s","width":0}' % (
                 get_random(16), get_random(32), get_random_ip(), random_mac(), get_userAgent())),
            ('v', '9.7.0'),
            ('f', 'android'),
            # ('sign', 'B9355CD13C210E39108CF299A861E045'),
            ('time', int(time.time() * 1000) - random.randint(1000, 3000)),
            ('weixin', '1'),
        )

        hashmap = dict(sorted(dict(params).items(), key=lambda x: x[0]))
        sb = ""
        for k, v in hashmap.items():
            sb += k + '=' + str(v).replace(" ", "") + "&"

        str2 = 'key=apr1$AwP!wRRT$gJ/q.X24poeBInlUJC'
        sb += str2
        sign = hashlib.md5(sb.encode()).hexdigest().upper()
        new_params = params + (("sign", sign),)
        response = requests.get('https://homepage-api.smzdm.com/home', headers=headers, params=new_params,
                                cookies=cookies)
        print(page, response.text)
        rows = json.loads(response.text).get('data', {}).get('rows', [])
        if rows:
            for goods in rows:
                if goods.get('article_mall') in ("天猫精选", "淘宝精选"):
                    article_url = goods['article_url']
                    goods_url.add(article_url)
                    print('====', len(goods_url))
        # print('*' * 100)


if __name__ == '__main__':
    task()
