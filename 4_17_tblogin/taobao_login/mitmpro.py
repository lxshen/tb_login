# -*-coding: utf-8 -*-
import mitmproxy.http


t0 = 'Object.defineProperties(navigator,{webdriver:{get:() => false}});'
t1 = 'window.navigator.chrome = {runtime: {},// etc.};'
t2 = '''
Object.defineProperty(navigator, 'languages', {
      get: () => ['en-US', 'en']
    });
'''
t3 = '''
Object.defineProperty(navigator, 'plugins', {
    get: () => [1, 2, 3, 4, 5,6],
  });
'''
t4 = '''
           Object.defineProperties(navigator,{
             userAgent:{
               get: () => Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36;
             }
           })
'''

js1 = '''() =>{

           Object.defineProperties(navigator,{
             webdriver:{
               get: () => false
             }
           })
        }'''
js3 = '''() => {
        window.navigator.chrome = {
    runtime: {},
    // etc.
  };
    }'''

js4 = '''() =>{
Object.defineProperty(navigator, 'languages', {
      get: () => ['en-US', 'en']
    });
        }'''

js5 = '''() =>{
Object.defineProperty(navigator, 'plugins', {
    get: () => [1, 2, 3, 4, 5,6],
  });
        }'''

js6 = '''
           Object.defineProperties(navigator,{
             userAgent:{
               get: () => Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36;
             }
           })
'''


class Tb(object):
    def response(slef, flow: mitmproxy.http.HTTPFlow):
        # print(flow.request.url)
        # if '114.js' in flow.request.url or 'um.js' in flow.request.url:
        #     # flow.response.text = t3 + t2 + t4 + t0 + flow.response.text
        #     print('注入成功')

        if '114.js' in flow.request.url:
            flow.response.text = js1 + js3 + js4 + js5 + js6 + flow.response.text
            print('注入成功')
addons = [
    Tb()
]

