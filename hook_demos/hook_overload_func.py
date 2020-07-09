# -*- coding: utf-8 -*-

"""
@author: guzhi
@file: hook_overload_func.py
@time: 2020-07-09 15:49:25
@projectExplain: HOOK 重载方法
"""
import frida, sys

jscode = """
Java.perform(function () {
    var utils = Java.use("com.qianyu.fridaapp.Utils"); 
    utils.test.overload("int").implementation = function(a) {
        console.log("Hook Start...");
        send(arguments[0]);
        send("Success!");
        return "qianyu";
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
