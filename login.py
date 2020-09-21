import requests
import socket

hostname = socket.gethostname()
ipaddr = socket.gethostbyname(hostname)

id = input('请输入一卡通号：\n')

url = 'http://10.9.10.100:801/eportal/?c=Portal&a=login&callback=dr1003&login_method=1&user_account=%2C0%2CXXXXXXXXX&user_password=123456&wlan_user_ip=10.11.XXX.XXX&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=10.1.1.1&wlan_ac_name=&jsVersion=3.3.2&v=6886'
url1 = 'http://10.9.10.100:801/eportal/?c=Portal&a=login&callback=dr1003&login_method=1&user_account=%2C0%2C'
url2 = '&user_password=123456&wlan_user_ip='
url3 = '&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=10.1.1.1&wlan_ac_name=&jsVersion=3.3.2&v=6886'
url = url1 + id + url2 + ipaddr + url3

headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    'Accept': '*/*',
    'Referer': 'http://10.9.10.100/',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en-US;q=0.7,en;q=0.6',
    'Cookie': 'PHPSESSID=rgt9afsli28dbu6p3hv9h4fmte'
    }

req = requests.get(url, headers = headers)
print(url)
print(req)