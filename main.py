import requests 
from dotenv import load_dotenv
import os
import argparse

def shorten_link(token, url):
  headers = {'Authorization': 'Bearer ' + token}
  payload = {'long_url': url}
  response = requests.post('https://api-ssl.bitly.com/v4/bitlinks', headers=headers, json=payload)
  response.raise_for_status()
  link_parameters = response.json()
  short_link = link_parameters['link'] 
  return short_link

def parse_the_link(link):
  if link.startswith('https'): 
    parsed_link = link[8:]
  elif link.startswith('http'):
    parsed_link = link[7:]
  return parsed_link
  
def count_clicks(token, link):
  headers = {'Authorization': 'Bearer ' + token}
  payload = {'unit': 'day', 'units': '-1'}
  response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks/summary', headers=headers, params=payload)
  response.raise_for_status()
  clicks_summary = response.json()
  number_of_clicks = clicks_summary['total_clicks']
  return number_of_clicks

def main():
  load_dotenv()
  bitly_token = os.getenv("BITLY_TOKEN")
  parser = argparse.ArgumentParser(description='Link shortener and clicks counter')
  parser.add_argument('url', help='Your link starting with http or https')
  url = parser.parse_args().url

  if url.startswith(('https://bit.ly', 'http://bit.ly')):
    try:
      parsed_link = parse_the_link(url)
      print('Число кликов:', count_clicks(bitly_token, parsed_link))
    except requests.exceptions.HTTPError:
      print('Ошибка!')
  else:
    try:
      short_link = shorten_link(bitly_token, url)
      parsed_link = parse_the_link(short_link)
      print('Битлинк:', short_link)
      print('Число кликов:', count_clicks(bitly_token, parsed_link))
    except requests.exceptions.HTTPError:
      print('Ошибка!')

if __name__ == '__main__':
  main()
