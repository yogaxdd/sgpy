import requests, threading, datetime, sys, os, time

def main():
	global auth, maxerr, api, pos, dely
	os.system('cls' if os.name == 'nt' else 'clear')
	print(f"YogaHost Stumble 0.37")
	print(f"Jika Tidak Terjadi Apa Apa Maka Auth Salah")
	print(f"Key : WR0nYMPSQW50ZF1x")
	print(f"Kadaluarsa : 23 Agustus 2022")
	print(f"")
	print(f"Jika Error Pada Python Silahkan Chat Tele @yogaxdddd")
	print(f"Copyright 2022 yogadev-hsid.blogspot.com")
	print(f"")
	api = "kitkabackend.eastus.cloudapp.azure.com:5010"
	auth = str(input("[!] Auth Dari Httpcanary : "))
	pos = int(input("""
Pilih Salah 1 :
0 = Round 1 (Tereliminasi)
1 = Round 2 (Tereliminasi)
2 = Round 3 (Tereliminasi)
3 = Round 3 (Menang)
Input: """))
	dely = float(input("\nDelay (Misal 0.5 | 1.0 | 2.0 Dan Seterusnya ): "))
	thr = int(input("\nThreads ( Default '1' | Jangan Memasukan Lebih Dari 1 ): "))
	print("="*64)
	for _ in range(thr):
	        threading.Thread(target=s).start()

def s():
        global maxerr
        while True:
                dt = datetime.datetime.now()
                try:
                        headers = {
                            'authorization': auth,
                            'use_response_compression': 'true',
                            'Accept-Encoding': 'gzip',
                            'Host': api,
                            'Connection': None,
                            'User-Agent': None,
                        }
                        response = requests.get(f'http://{api}/round/finishv2/{pos}', headers=headers)
                        if response.status_code == 200:
                                negara = response.text.split('"Country":')[1].split(',')[0]
                                nama = response.text.split('"Username":')[1].split(',')[0]
                                trophy = response.text.split('"SkillRating":')[1].split(',')[0]
                                crown = response.text.split('"Crowns":')[1].split(',')[0]
                                sys.stdout.write(f"\r[{dt.hour}:{dt.minute}:{dt.second}] {negara} | Username: {nama} | Trophy: {trophy} | Crowns: {crown}")
                                sys.stdout.flush()
                        elif response.status_code == 403 and response.text == "BANNED":
                                print(f"[{dt.hour}:{dt.minute}:{dt.second}] Sorry Bang Keban!")
                                break
                                sys.exit(0)
                        elif response.text == "SERVER_ERROR":
                                continue
                                print(f"[{response.status_code}] Auth Salah!")
                        if dely > 0: time.sleep(dely)
                except Exception as e:
                        pass

if __name__ == "__main__":
	main()
