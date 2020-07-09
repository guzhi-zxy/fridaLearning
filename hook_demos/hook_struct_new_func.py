# -*- coding: utf-8 -*-

"""
@author: guzhi
@file: hook_struct_new_func.py
@time: 2020-07-09 15:50:24
@projectExplain: HOOK 构造对象参数
"""
import frida, sys

jscode = """
Java.perform(function () {
    var utils = Java.use("com.qianyu.fridaapp.Utils"); 
    var money = Java.use("com.qianyu.fridaapp.Money"); 
    utils.test.overload().implementation = function() {
        // send("Hook Start...");
        var mon = money.$new(2000, '港币');
        // send(mon.getInfo());
        return this.test(800);
    }
});
"""


def message(message, data):
    if message["type"] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


process = frida.get_remote_device().attach('com.qianyu.fridaapp')  # 包名
script = process.create_script(jscode)
script.on("message", message)
script.load()
sys.stdin.read()
