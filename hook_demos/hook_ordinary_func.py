# -*- coding: utf-8 -*-

"""
@author: guzhi
@file: hook_ordinary_func.py
@time: 2020-07-09 15:46:41
@projectExplain: HOOK 普通方法
"""
import frida, sys

jscode = """
Java.perform(function () {
    var utils = Java.use("com.qianyu.fridaapp.Utils"); 
    utils.getCalc.implementation = function(a, b) {
        console.log("Hook Start...");
        send(arguments[0]);
        send(arguments[1]);
        send("Success!");
        var num = arguments[0] + arguments[1];
        send(num);
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
