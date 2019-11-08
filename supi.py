import requests as req
from bs4 import BeautifulSoup as bs
import json
import time as tm
from colorama import init,Fore
import csv


init()
headers ={
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
	'Accept': '*/*',
	'Sec-Fetch-Site': 'cross-site',
	'Sec-Fetch-Mode': 'cors',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'en-US,en;q=0.9,id;q=0.8',
	'Cookie': '_gcl_au=1.1.1805060871.1573050834; csrftoken=o2vL1uM6rjqnZeoF8DL1TvxV3UTNEQ0Q; SPC_IA=-1; SPC_EC=-; SPC_U=-; SPC_F=mLEuEMmtcbYOuxFXoeu1LhVm3sVPaYWI; REC_T_ID=764ae7e6-00a2-11ea-9518-ccbbfe5deb6f; SPC_SI=y19ecj3o4kc4z755mc14k0ogtct4bjro; REC_T_ID=76a057eb-00a2-11ea-95e2-ccbbfe5d5dc7; welcomePkgShown=true; _ga=GA1.3.507803947.1573050840; _gid=GA1.3.1036868182.1573050840; SPC_RW_HYBRID_ID=53; language=id; AMP_TOKEN=%24NOT_FOUND; REC_MD_20=1573055624; SPC_T_IV="qqYfP57NxFROEOr2gCk2rQ=="; SPC_T_ID="rhIBTy5XHQDYjc2Be34aQnc37c2A7D7Zpl7wBBUHzrzsdUsyH4jTMpS65f8G+Q0+EqhDmGdQyJmUfZSx0zt35b3s5q1OHlgbwNoHlrjbXZU="'

}

def time(sec):
	tm.sleep(sec)
def curl(shop,headers):
	return req.get('https://shopee.co.id/api/v2/search_users/?keyword='+shop+'&limit=1&with_search_cover=true',headers=headers)
def prod(item,shop):
	return req.get('https://shopee.co.id/api/v2/item/get?itemid='+item+'&shopid='+shop)
def get(shopid,headers):
	return req.get('https://shopee.co.id/api/v2/search_items/?by=pop&limit=30&match_id='+shopid+'&newest=0&order=desc&page_type=shop&version=2',headers=headers)


print (" ##########################")
print (" #                        #")
print (" #        Insomniac       #")
print (" #  https://insomniac.id  #")
print (" #       Supi Scraper     #")
print (" #                        #")
print (" ##########################")
try:
	print(' Cuma GET 100 Items')
	shop = input(' Search keyword : ')
	print(" Searching "+ shop + " on shopee")
	p = curl(shop,headers)
	time(2)
	scrape = json.loads(p.text)
	data = scrape['data']['users'][0]
	shopid = str(data['shopid'])
	shopname = data['shopname']
	print(" Found",shopname)
	time(2)
	getitems = json.loads(get(shopid,headers).text)
	items = getitems['items']
	time(2)
	# print(items)
	# print("\n")
	# print(items[0])
		# file = open('Supi.csv','w') # w untuk write/mengganti data sebelumnya 
	 #                                # a untuk menambah data tanpa menghapus data sebelumnya
		# writer = csv.writer(file)
		# writer.writerow(['Nama Barang', 'Item ID','Shop ID', 'Harga'])
	for item in items:
		itemid = str(item['itemid'])
		infoses = prod(itemid,shopid)
		# time(5)
		infos = json.loads(infoses.text)
		info = infos['item']
		print(Fore.GREEN + "[+] " +Fore.YELLOW + info['name'])
		print(Fore.GREEN + "[+]" +Fore.YELLOW, info['itemid'])
		print(Fore.GREEN + "[+]" +Fore.YELLOW, info['shopid'])
		print(Fore.GREEN + "[+] " +Fore.YELLOW+"Rp", str(info['price_max'])[0:-5],"\n")
		# writer.writerow([info['name'], info['itemid'], info['shopid'],str(info['price_max'])[0:-5]])
		time(1)
	# 	# file.close()
except:
    print(" There was an error!")
