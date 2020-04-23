Java.perform(function () {
   console.log("[*] Starting script");
   var util = Java.use('c.h.b.a.k.a.a');
   util.a.overload('java.util.Map', 'java.lang.String').implementation = function (arg1, arg2) {
     console.log('param1: ', arg1);
     console.log('param2: ', arg2);
     var result = this.a(arg1, arg2);
     console.log('return: ', result); return result; };
})