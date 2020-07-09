# -*- coding: utf-8 -*-

"""
@author: guzhi
@file: hook_native_func.py
@time: 2020-07-09 15:53:21
@projectExplain: HOOK native
"""
import frida, sys

jscode = """
setImmediate(function () {
    send("start");
    // 遍历模块找基址
    Process.enumerateModules({
        onMatch: function (exp) {
            if (exp.name == 'libdemo.so') {
                send('enumerateModules find');
                send(exp.name + "|" + exp.base + "|" + exp.size + "|" + exp.path);
                send(exp);
                return 'stop';
            }
        },
        onComplete: function () {
            send('enumerateModules stop');
        }
    });
    
    // hook 导出函数
    var exports = Module.enumerateExportsSync("libdemo.so");
    for (var i=0; i<exports.length; i++) {
        send("name:" + exports[i].name + "  address:" + exports[i].address);
    }
    
    // 通过模块名直接查找基址
    var baseSOFile = Module.findBaseAddress("libdemo.so");
    Interceptor.attach(baseSOFile.add(0x00001270), {
        onEnter: function (args) {
            // console.log(Memory.readCString(args[0]));
            // console.log(Memory.readUtf16String(args[3]));
            console.log(args[2]);
            console.log(args[3]);
            console.log(args[4]);
        },
        onLeave: function (retval) {
            retval.replace(1);
            console.log("返回值 "+ retval);
        }
    });
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
