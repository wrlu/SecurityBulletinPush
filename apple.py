import requests
import re


def get_latest_security_update():
    response = __send_request__('/')
    if response.status_code == 200:
        result = response.text
        ul_list = re.findall('The latest version of iOS and iPadOS is (.+?)\.&nbsp;Learn', result)
        if len(ul_list) == 0 or (len(ul_list) == 1 and ul_list[0].find('and') != -1):
            ul_list = re.findall('The latest version of iOS and iPadOS is (.+?), and', result)
        if len(ul_list) == 0:
            print("Unable to parse ul_list.")
        latest_ver = ul_list[0]
        print("Latest iOS version is "+latest_ver)
        link_no_cve_re = '<td>iOS {0} and iPadOS {0}<br>\\s+<span class="note">(.+?)</span></td>'.format(latest_ver)
        link_cve_re = '<td><a href="(.+?)">iOS {0} and iPadOS {0}</a></td>'.format(latest_ver)
        td_list = re.findall(link_no_cve_re, result)
        if len(td_list) == 1:
            latest_link = td_list[0]
        else:
            td_list = re.findall(link_cve_re, result)
            latest_link = td_list[0]
        return latest_ver, latest_link
    return ''


def __send_request__(path: str):
    base_url = 'https://support.apple.com/en-us/HT201222'
    response = requests.get(base_url + path)
    return response


def do():
    print(get_latest_security_update())
