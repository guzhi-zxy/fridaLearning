# -*- coding: utf-8 -*-

"""
@author: guzhi
@file: hook_struct_func.py
@time: 2020-07-09 15:47:59
@projectExplain: HOOK 构造方法
"""
import frida, sys

jscode = """
Java.perform(function () {
    var money = Java.use("com.qianyu.fridaapp.Money"); 
    money.$init.implementation = function(a, b ) {
        console.log("Hook Start...");
        send(arguments[0]);
        send(arguments[1]);
        send("Success!");
        return this.$init(10000, "美元");
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
