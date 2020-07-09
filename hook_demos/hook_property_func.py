# -*- coding: utf-8 -*-

"""
@author: guzhi
@file: hook_property_func.py
@time: 2020-07-09 15:52:21
@projectExplain: HOOK 修改对象属性
"""
import frida, sys

jscode = """
Java.perform(function () {
    // 包名.类名
    var utils = Java.use("com.qianyu.fridaapp.Utils"); 
    var money = Java.use("com.qianyu.fridaapp.Money"); 
    var clazz = Java.use("java.lang.Class"); 
    // test is function name
    utils.test.overload().implementation = function() {
        send("Hook Start...");
        var mon = money.$new(200, '港币');
        send(mon.getInfo());
        var numid = Java.cast(mon.getClass(), clazz).getDeclaredField('num');
        numid.setAccessible(true);
        // send(numid.get(mon));
        numid.setInt(mon, 1000);
        send(mon.getInfo());
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
