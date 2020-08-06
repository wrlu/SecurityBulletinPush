import requests
import re


def get_latest_security_update():
    response = __send_request__('/')
    if response.status_code == 200:
        result = response.text
        ul_list = re.findall('iOS 和 iPadOS 的最新版本是 (.+?)。', result)
        latest_ver = ul_list[0]
        link_no_cve_re = '<td>iOS {0} 和 iPadOS {0}<br>\\s+<span class="note">(.+?)</span></td>'.format(latest_ver)
        link_cve_re = '<td><a href="(.+?)">iOS {0} 和 iPadOS {0}</a></td>'.format(latest_ver)
        td_list = re.findall(link_no_cve_re, result)
        if len(td_list) == 1:
            latest_link = td_list[0]
        else:
            td_list = re.findall(link_cve_re, result)
            latest_link = td_list[0]
        return latest_ver, latest_link
    return ''


def __send_request__(path: str):
    base_url = 'https://support.apple.com/zh-cn/HT201222'
    response = requests.get(base_url + path)
    return response


def do():
    print(get_latest_security_update())
