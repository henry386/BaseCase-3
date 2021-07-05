import operator
import os
from os import path
import requests
from bs4 import BeautifulSoup
import pyfiglet
from prettytable import PrettyTable
from os import system, name
from colorama import Fore, Back, Style
from tabulate import tabulate


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def scrape(url_sta):
    print("")
    print(Fore.RED + "Getting Site URLS...")
    print("")
    page_available = True
    page_no = 1
    while page_available:
        reqs = requests.get(url_sta + "?&sort=-week&page=" + str(page_no))
        if "No results matched your criteria" in reqs.text:
            page_available = False

        if page_available:
            print("")
            print("")
            print(Fore.LIGHTRED_EX + "Page No: " + str(page_no))
            print("")
            soup = BeautifulSoup(reqs.text, 'html.parser')
            for link in soup.find_all('a'):
                url = link.get('href')
                if str(url).startswith("/details"):
                    add_url, not_needed, not_needed = url_sta.partition('/details')
                    add_url = add_url + url
                    if add_url not in urls and '?' not in add_url and '@' not in add_url and add_url is not url_sta and '=' not in add_url:
                        urls.append(add_url)
                        print(Fore.RED + "NEW URL: " + Fore.CYAN + add_url)
            page_no = page_no + 1
    print("")
    print("Number of Pages: " + str(page_no))
    print("")
    print("Number of Individual Sites: " + str(len(urls)))
    print("")
    print(Fore.LIGHTGREEN_EX + "*" * 200)


def scrape_file():
    print("")
    print(Fore.RED + "Getting " + file_type + " URLS...")

    ii = 0
    while ii < len(urls):
        reqs = requests.get(urls[ii])
        soup = BeautifulSoup(reqs.text, 'html.parser')
        i = 0
        links = soup.find_all('a')

        for link in links:
            if str(link.get('href', [])).endswith('.' + file_type):
                i += 1
                print("")
                splitting = ("https://archive.org" + link.get('href')).split('/')
                print(Fore.RED + "NAME: " + Fore.CYAN + splitting[4])

                print(Fore.RED + "LOCATION: " + Fore.CYAN + "https://archive.org" + link.get('href'))
                pdf_files.update({"https://archive.org" + link.get('href'): splitting[4]})
        ii = ii + 1

    print("")
    print("")
    print(str(len(pdf_files)) + " Files")
    print("")
    print(Fore.LIGHTGREEN_EX + "*" * 200)


def get_download_size():
    size_table = PrettyTable(["File Location" + Fore.RED, "File Size" + Fore.BLUE])

    print("")
    print(Fore.RED + "Getting File Files Size...")
    print("")
    pdf_files.pop("URL")
    size = 0
    for x in pdf_files:
        try:
            file_size_temp = requests.get(x, stream=True).headers['Content-length']
            print(Fore.RED + "URL: " + Fore.CYAN + x + Fore.RED + " Size: " + Fore.LIGHTRED_EX +
                  file_size_temp + " Bytes")
            size = size + int(file_size_temp)
            size_table.add_row([x + Fore.RED, str(round(int(file_size_temp) / 1048576, 3)) + " MB" +
                                Fore.LIGHTRED_EX])
        except():
            print("ERROR")

    print("")
    print(Fore.LIGHTGREEN_EX + "*" * 200)
    print(size_table)
    size = size / 1048576
    print("")
    print("")
    print("Total Size: ~" + str(round(size)) + " MB")
    print("")
    print("")
    print("*" * 200)
    print("")


def download_files(location):
    print(Fore.RED + "Downloading Files...")
    for x in pdf_files:
        try:
            print("")
            print(Fore.CYAN + x)
            url = x
            r = requests.get(url, stream=True)

            download_location = location + '\\' + pdf_files[x] + '\\'

            if not os.path.isdir(download_location):
                os.mkdir(download_location)
            i = 0
            if not path.exists(download_location + pdf_files[x] + "." + file_type):
                with open(download_location + pdf_files[x] + "." + file_type, 'wb') as f:
                    f.write(r.content)
            else:
                exists = False
                while not exists:
                    if not path.exists(download_location + pdf_files[x] + "_" + str(i) + ".pdf"):
                        exists = True
                        with open(download_location + pdf_files[x] + "_" + str(i) + ".pdf", 'wb') as f:
                            f.write(r.content)
                    i = i + 1

        except():
            print("Error: " + x)


clear()
print(Fore.LIGHTGREEN_EX + "")
result = pyfiglet.figlet_format("BaseCase 3.0")
print(result)
print(Fore.RED + "-Archive.org Repository Scraper (Author: henry386)-")
print("")
pdf_files = {"URL": "Directory"}
urls = []
url_main = "https://archive.org/details/" + input(Fore.LIGHTGREEN_EX + "Enter Repository: ")
file_type = input(Fore.LIGHTGREEN_EX + "Enter File Type: ")
scrape(url_main)
scrape_file()
get_download_size()

download_files(input("Enter Download Location: "))
