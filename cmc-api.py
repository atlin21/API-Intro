import requests
from requests import Session
import secrets
from pprint import pprint as pp
url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/map"
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': secrets.api_key,
}
r = requests.get(url, headers = headers)
class CMC:
  def __init__(self, token):
    self.apiurl = "https://pro-api.coinmarketcap.com"
    self.headers = {'Accepts': 'application/json','X-CMC_PRO_API_KEY': token}
    self.session = Session()
    self.session.headers.update(self.headers)
  def getALLCoins(self):
    url = self.apiurl + '/v1/cryptocurrency/map'
    r = self.session.get(url)
    data = r.json()['data']
    return data
  def getPrice(self, symbol):
    url = self.apiurl + '/v1/global-metrics/quotes/latest'
    pars = {'convert': symbol}
    r = self.session.get(url, params=pars)
    data = r.json()['data']
    return data

cmc = CMC(secrets.api_key)
pp(cmc.getPrice('BTC'))
