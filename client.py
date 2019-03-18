import requests
from random import randint
import json

class RouteYou_Json_Client:
    key = None
    def __init__(self, service, version, timeout = 10):
        self.url = 'http://api.routeyou.com/%version%/json/%service%/k-%key%'
        self.key = RouteYou_Json_Client.key
        
        self._service = service
        self._version = version
        self._timeout = timeout
        
        self._needsToken = True
        self._httpClient = None
    def __getattr__(self, name):
        #magic function to call methods in RouteYou webservice
        def wrapper(*args, **kwargs):
            return self._execurteCall(name, args)
        return wrapper
    def _getHttpClient(self):
        self.url = self.url.replace('%service%',self._service)
        self.url = self.url.replace('%version%',self._version)
        self.url = self.url.replace('%key%',self.key)
    def _execurteCall(self, method, params, retry = False):
        self._getHttpClient()
        id = randint(1,1000) 
        data = {
            'jsonrpc' : self._version,
            'id' : id,
            'method' : method,
            'params' : params
            }     
        req = requests.post(self.url, json.dumps(data))
        response = req.json()
        if req.status_code == 200:
            return response
        else:
            return False
    def getKey(self):
        return self.key

'''RouteYou_Json_Client.key = 'your-key-here'

#example call to route webservice 2.0
routeService = RouteYou_Json_Client('Route', '2.0')
print routeService.getFull(44, 'en')'''