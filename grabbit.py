#!/usr/bin/python
import requests
import socket
import sys
from pyvirtualdisplay import Display
from selenium import webdriver
import os

all_ips = []
all_webservices = []
user_agent = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 Chrome/36.0.1985.125 Safari/537.36'}
targets = sys.argv[1]

inputfile = open(targets, "r")
all_ips = inputfile.readlines()
inputfile.close()

print ("\n    k0NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0l.    ")
print ("     .':d0WMMMMMMMMMMMMMMMMMMMMMMMMMMMWO:.      ")
print ("         .,o0WMMMMMMMMMMMMMMMMMMMMMMMKl.        ")
print ("    ,       .;xXMMMMMMMMMMMMMMMMMMMWO,          ")
print ("    k.         'oKWMMMMMMMMMMMMMMMWk.           ")
print ("    Wx.          .c0WMMMMMMMMMMMMWk.       .    ")
print ("    MWk'           .c0WMMMMMMMMMM0'        ,    ")
print ("    MMMK:            .c0WWMMMMMMNc         l    ")
print ("    MMMMNx'            .;oXMMMMMk.        .k    ")
print ("    MMMMMMXo'             'xNMMWl         cN    ")
print ("    MMMMMMMMXd,             :0WX;        '0M    ")
print ("    MMMMMMMMMMNOl'.          .xk'       .xWM    ")
print ("    MMMMMMMMMMMMMNOd:'.       ...      .xWMM    ")
print ("    MMMMMMMMMMMMMMMNKx:..             ;OWMMM    ")
print ("    MMMMMMMMMMMWKxc,.                ,0MMMMM    ")
print ("    MMMMMMMMMNk:.  .                  ,OWMMM    ")
print ("    MMMMMMMNk,   :xXx;                 .kWMM    ")
print ("    MMMMMMXl.   .-LRL-.                 ;XMM    ")
print ("    MMMMMWd.     .;:,.                  .OMM    ")
print ("    MMMMMNc                             .kMM    ")
print ("    MMMMMWd.                            .OMM    ")
print ("    MMMMMMNo.                           ;XMM    ")
print ("    MMMMMMMW0l'                         oWMM    ")
print ("    MMMMMMMMMWXOo:'.                   'OMMM    ")
print ("    MMMMMMMMMMMMMWNO,                .'xNMMM    ")
print ("    MMMMMMMMMMMMMMMK, ....',.    .;ldOXWMMMM    ")
print ("    MMMMMMMMMMMWOccc,''''':kd;:clool:;dNMMMM    ")
print ("    MMMMMMMMMMMWd.        .dx;,,,;:ldkXWMMMM    ")
print ("    MMMMMMMMMMMMO;,:ll;.. .okdk0XWMMMMMMMMMM    ")
print ("    MMMMMMMMMMMMWXNWMMW0ko;xWMMMMMMMMMMMMMMM    ")
print ("                                                ")
print ("           -=Grabbit Like A Rabbit=-            ")
print ("    https://github.com/lostrabbitlabs/grabbit   ")
print ("                      v0.1a                     ")
print ("                                                ")
print ("    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM    ")
print ("                                                ")
print ("    Attempting to Grabbit Like A Rabbit....    ")

try:
    os.mkdir("screenshots")
    os.mkdir("services")
except:
    pass

def screenshot_http(fullurl_http, fullurl_http_fuzz1, fullurl_http_fuzz2, fullurl_http_fuzz3, fullurl_http_fuzz4, fullurl_http_fuzz5, fullurl_http_fuzz6, host_str, ports_str):
    filename1 = "screenshots/HTTP--" + host_str + "-" + ports_str + ".png"
    filename2 = "screenshots/HTTP--" + host_str + "-" + ports_str + "-fuzz-percent.png"
    filename3 = "screenshots/HTTP--" + host_str + "-" + ports_str + "-fuzz-percent2x.png"
    filename4 = "screenshots/HTTP--" + host_str + "-" + ports_str + "-fuzz-amp.png"
    filename5 = "screenshots/HTTP--" + host_str + "-" + ports_str + "-fuzz-script.png"
    filename6 = "screenshots/HTTP--" + host_str + "-" + ports_str + "-fuzz-FLOOD.png"
    filename7 = "screenshots/HTTP--" + host_str + "-" + ports_str + "-fuzz-NullByte.png"
    display = Display(visible=0, size=(1024, 768))
    display.start()
    browser = webdriver.Firefox()
    browser.accept_untrusted_certs = True
    #browser.implicitly_wait(30)
    #browser.set_page_load_timeout(60)
    #browser.implicitly_wait(10)
    try:
        browser.get(fullurl_http)
        browser.get_screenshot_as_file(filename1)
    except:
        pass
    try:
        browser.get(fullurl_http_fuzz1)
        browser.get_screenshot_as_file(filename2)
    except:
        pass
    try:
        browser.get(fullurl_http_fuzz2)
        browser.get_screenshot_as_file(filename3)
    except:
        pass
    try:
        browser.get(fullurl_http_fuzz3)
        browser.get_screenshot_as_file(filename4)
    except:
        pass
    try:
        browser.get(fullurl_http_fuzz4)
        browser.get_screenshot_as_file(filename5)
    except:
        pass
    try:
        browser.get(fullurl_http_fuzz5)
        browser.get_screenshot_as_file(filename6)
    except:
        pass
    try:
        browser.get(fullurl_http_fuzz6)
        browser.get_screenshot_as_file(filename7)
    except:
        pass
    browser.close()
    display.stop()


def screenshot_https(fullurl_https, fullurl_https_fuzz1, fullurl_https_fuzz2, fullurl_https_fuzz3, fullurl_https_fuzz4, fullurl_https_fuzz5, fullurl_https_fuzz6, host_str, ports_str):
    filename1 = "screenshots/HTTPS--" + host_str + "-" + ports_str + ".png"
    filename2 = "screenshots/HTTPS--" + host_str + "-" + ports_str + "-fuzz-percent.png"
    filename3 = "screenshots/HTTPS--" + host_str + "-" + ports_str + "-fuzz-percent2x.png"
    filename4 = "screenshots/HTTPS--" + host_str + "-" + ports_str + "-fuzz-amp.png"
    filename5 = "screenshots/HTTPS--" + host_str + "-" + ports_str + "-fuzz-script.png"
    filename6 = "screenshots/HTTPS--" + host_str + "-" + ports_str + "-fuzz-FLOOD.png"
    filename7 = "screenshots/HTTPS--" + host_str + "-" + ports_str + "-fuzz-NullByte.png"
    display = Display(visible=0, size=(1024, 768))
    display.start()
    browser = webdriver.Firefox()
    browser.accept_untrusted_certs = True
    #browser.implicitly_wait(30)
    #browser.set_page_load_timeout(30)
    #browser.implicitly_wait(10)
    try:
        browser.get(fullurl_https)
        browser.get_screenshot_as_file(filename1)
    except:
        pass
    try:
        browser.get(fullurl_https_fuzz1)
        browser.get_screenshot_as_file(filename2)
    except:
        pass
    try:
        browser.get(fullurl_https_fuzz2)
        browser.get_screenshot_as_file(filename3)
    except:
        pass
    try:
        browser.get(fullurl_https_fuzz3)
        browser.get_screenshot_as_file(filename4)
    except:
        pass
    try:
        browser.get(fullurl_https_fuzz4)
        browser.get_screenshot_as_file(filename5)
    except:
        pass
    try:
        browser.get(fullurl_https_fuzz5)
        browser.get_screenshot_as_file(filename6)
    except:
        pass
    try:
        browser.get(fullurl_https_fuzz6)
        browser.get_screenshot_as_file(filename7)
    except:
        pass
    browser.close()
    display.stop()

print "\n"

for networks in all_ips:
    networks2 = networks.split(":")
    hosts = networks2[0]
    ports = networks2[1].strip("\n")   
    host_str = str(hosts)
    ports_str = str(ports).strip()
    if ports_str != '':
        print "================== " + host_str + " : " + ports_str + " ================ "
        try:
            host_str = str(hosts)
            fullurl_http = ('http://' + hosts + ":" + ports_str)
            fullurl_https = ('https://' + hosts + ":" + ports_str)
            fullurl_http_fuzz1 = ('http://' + hosts + ":" + ports_str + "/%")
            fullurl_http_fuzz2 = ('http://' + hosts + ":" + ports_str + "/%%")
            fullurl_http_fuzz3 = ('http://' + hosts + ":" + ports_str + "/&")
            fullurl_https_fuzz1 = ('https://' + hosts + ":" + ports_str + "/%")
            fullurl_https_fuzz2 = ('https://' + hosts + ":" + ports_str + "/%%")
            fullurl_https_fuzz3 = ('https://' + hosts + ":" + ports_str + "/&")
            fullurl_http_fuzz4 = ('http://' + hosts + ":" + ports_str + "/<script>alert('xss');</script>")
            fullurl_https_fuzz4 = ('https://' + hosts + ":" + ports_str + "/<script>alert('xss');</script>")
            fullurl_http_fuzz5 = ('http://' + hosts + ":" + ports_str + "/" + "%"*10050)
            fullurl_https_fuzz5 = ('https://' + hosts + ":" + ports_str + "/" + "%"*10050)
            fullurl_http_fuzz6 = ('http://' + hosts + ":" + ports_str + "/" + "%00")
            fullurl_https_fuzz6 = ('https://' + hosts + ":" + ports_str + "/" + "%00")
        except:
            pass
            print "!! error with ports_str, fulurl_http, etc"
        try:
            if ports_str != '':
                r = requests.get(fullurl_http, verify=False, timeout=30, headers=user_agent)
                print r.headers
                print "\n"
                print r.content
                try:
                    if ports_str != '':
                        screenshot_http(fullurl_http, fullurl_http_fuzz1, fullurl_http_fuzz2, fullurl_http_fuzz3, fullurl_http_fuzz4, fullurl_http_fuzz5, fullurl_http_fuzz6, host_str, ports_str)
                    all_webservices.append(hosts + ":" + ports_str)
                except:
                    pass
        except:
            pass
        try:
            if ports_str != '':
                r2 = requests.get(fullurl_https, verify=False, timeout=30, headers=user_agent)
            print r2.headers
            print r2.content
            try:
                if ports_str != '':
                    screenshot_https(fullurl_https, fullurl_https_fuzz1, fullurl_https_fuzz2, fullurl_https_fuzz3, fullurl_https_fuzz4, fullurl_https_fuzz5, fullurl_https_fuzz6, host_str, ports_str)
            except:
                pass
        except:
            pass
        try:
            if ports_str != '':
                DATA = 'GET / HTTP/1.1\r\nHost: ' + host_str + '\r\n\r\n'
                client = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
                client.settimeout(30)
                client.connect(( host_str, ports ))
                client.send(DATA)
                response = client.recv(2048)
                client.close()
                print response
            response = " "
        except:
            pass
        filename2 = "services/RESULTS-SERVICES--" + host_str + "--" + ports_str + ".txt"
        with open(filename2, "a") as output_file2:
            try:
                output_file2.write("=======================================")
                output_file2.write("\n")
                output_file2.write(response)
                output_file2.write("\n")
                output_file2.write("=======================================")
            except:
                pass
            try:
                output_file2.write("\n\n")
                full_headers = str(r.headers)
                output_file2.write(full_headers)
                output_file2.write("\n")
                output_file2.write("=======================================")
            except:
                pass
            try:
                output_file2.write("\n\n")
                output_file2.write(r.content)
                output_file2.write("\n")
                output_file2.write("=======================================")
            except:
                pass
            try:
                output_file2.write("\n\n")
                full_headers2 = str(r2.headers)
                output_file2.write(full_headers2)
                output_file2.write("\n")
                output_file2.write("=======================================")
            except:
                pass
            try:
                output_file2.write("\n\n")
                output_file2.write(r2.content)
                output_file2.write("=======================================")
            except:
                pass
            r = []
            r2 = []
            response = []
            full_headers = ""
            full_headers2 = ""
            print "\n"

print " .-= Grabbit Like A Rabbit has completed all tasks =-. \n"

sys.exit()

