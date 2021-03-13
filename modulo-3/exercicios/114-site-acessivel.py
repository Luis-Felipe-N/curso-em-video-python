import urllib
import urllib.request

try:
    urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('\033[31mO site não está acessível\033[m')
else:
    print('\033[32mO site está acessível\033[m')