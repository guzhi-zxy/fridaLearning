Java.perform(function () {
   var util = Java.use('com.smzdm.client.base.utils.ZDMKeyUtil');
   util.b.implementation = function () {
     var result = this.b();
     console.log('return: ', result); return result; };
})