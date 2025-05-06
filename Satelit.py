import requests
from logo import show_logo
from colorama import init, Fore, Style
import os,sys
class Satelite_Starlink:
    def __init__(self):
        r = requests.get("http://127.0.0.1:5000/data")
        self.data = r.json()
    def daftar_satelite(self):
        show_logo()
        print(Fore.YELLOW + "Noted: Masukan Jumlah Data Yang Ingin Di Tampilkan" + Style.RESET_ALL)
        jumlah = int(input(Fore.BLUE + "Masukan Jumlah:" + Style.RESET_ALL))
        for i  in range(jumlah):
            print("[%d] Nama Satelite : %s" % (i + 1, self.data[i]["spaceTrack"]["OBJECT_NAME"]))
        input(Fore.BLUE + "Enter Untuk Kembali Ke Menu : " + Style.RESET_ALL)
        self.welcome()
    def detail_satelite(self):
        show_logo()
        p = int(input(Fore.BLUE + "ID Nomor Satelit: " + Style.RESET_ALL))
        data = self.data[p]["spaceTrack"]
        field_width = 25
        value_width = 50
        line = "\033[33;1m+" + "-"*field_width + "+" + "-"*value_width + "+"
        ORANGE = "\033[33;1m"
        RESET = "\033[0m"
        print(line + ORANGE)
        print("| {:<{}} | {:<{}} |".format("FIELD", field_width, "VALUE", value_width))
        print(line + ORANGE)

        for key, value in data.items():
            value_str = str(value)
            if len(value_str) > value_width:
                value_str = value_str[:value_width - 3] + "..."
            print("| {:<{}} | {:<{}} |".format(key, field_width, value_str, value_width))

        print(line + RESET)
        input(Fore.BLUE + "Enter Untuk Kembali Ke Menu : " + Style.RESET_ALL)
        self.welcome()
    def print_semua_data(self):
        import json
        print(json.dumps(self.data, indent=4))

    def welcome(self):
        show_logo()
        menu = Fore.GREEN + """
        1. Liat Daftar Satelite
        2. Detail Satelite
        3. Keluar
         """ + Style.RESET_ALL
        print(menu)
        pilihan = input(Fore.BLUE + "Choices: " + Style.RESET_ALL)
        if pilihan=="1":
          os.system("clear")
          self.daftar_satelite()
        elif pilihan=="2":
          os.system("clear")
          self.detail_satelite()
        elif pilihan=="3":
          os.system("exit")
        else:
            print("Tolong Pilih Sesuatu")
if __name__=="__main__":
   data = Satelite_Starlink()
   data.welcome()

