Java.perform(function () {
   var util = Java.use('com.smzdm.client.base.utils.Aa');
   util.a.overload('java.lang.String').implementation = function (arg1) {
     console.log('param1: ', arg1);
     var result = this.a(arg1);
     console.log('return: ', result); return result; };
})