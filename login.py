import json
import os
import random
import requests
import string
from bs4 import BeautifulSoup
from requests_toolbelt import MultipartEncoder




def main():
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'en-GB,en-US;q=0.8,en;q=0.6',
        'Upgrade-Insecure-Requests': '1',
    }

    s = requests.Session()
    s.headers.update(header)

    r = s.get('https://www.adidas.com.cn')
    r = s.get('https://www.adidas.com.cn/customer/account/login/')
    # print(r.headers)
    cashedInHtml(r)

    payloads = MultipartEncoder(fields={
            'login[username]': 'dd@gmail.com',
            'login[password]': 'asdfasdf',
            'send': ''
        })

    s.headers.update({
        'Origin': 'https://www.adidas.com.cn',
        'Referer': 'https://www.adidas.com.cn/customer/account/login/',
        'Content-Type': payloads.content_type,
    })

    r = s.post('https://www.adidas.com.cn/customer/account/loginPost/', data=payloads)
    print(r.cookies)


    # header = {
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    #     'Accept-Encoding': 'gzip, deflate, sdch, br',
    #     'Accept-Language': 'en-GB,en-US;q=0.8,en;q=0.6',
    #     'Upgrade-Insecure-Requests': '1',
    # }
    # print('after login:', s.cookies)
    #
    # s.headers.update(header)
    r = s.get('https://www.adidas.com.cn/customer/account/')

    cashedInHtml(r)
    loginCheck(r)



    """
    P3p': 'CP="CAO PSA OUR"',
    'Content-Type': 'text/html; charset=UTF-8',
    'Date': 'Mon, 20 Mar 2017 09:00:24 GMT',
    'Content-Length': '16690', 'X-Akamai-Transformed':
    'h - 0 pmb=mTOE,2', 'Login-Required': 'true',
    'X-Powered-By': 'PHP/5.3.12', 'Connection': 'keep-alive',
     'Server': 'ADIDAS-WEB-PRD', 'Content-Encoding': 'gzip',
     'Set-Cookie': 'frontend=8m47e2qfomcad86glc5qvlmmn6;
     expires=Mon, 20-Mar-2017 11:01:15 GMT;
     path=/, ak_bmsc=D7D0C87ACF9FF7B7E815536EC7A10AD3D2C07407DA450000289ACF585CF08E78~plzgijIxvHbUEIqNPCUQ1GVidbro4CwjFrpBiZjG5FNh+IyRH31RYwxpT8nXQ5ru9NsEiScKgbQpsJu16jB7wRWxQ14+2nZngMQj37aXctkC47/3s8OgFd6es+khzZ3AMFBfVyrXjkf5dW/YLSJhfj2fqyMtgo/lbdxIB5uZC069wurbSrM8Wc1fXKlL23bJ2D5SFkXUPkGdWuf+2s/r84S6Cc1YmbACw3KeLTe3S1cBszygvptmm3Rx3ABKT6IwxRKbEzrhc13ryV06TPSFpw2a9j+eWrB82O0zszoRBN5YYWSMfwmkrc5VQEUFSGkB1i; expires=Mon, 20 Mar 2017 11:00:24 GMT; max-age=7200; path=/; domain=.adidas.com.cn; HttpOnly', 'wh': '83', 'Cache-Control': 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0', 'Pragma': 'no-cache', 'Expires': 'Thu, 19 Nov 1981 08:52:00 GMT', 'Vary': 'Accept-Encoding'}
<
"""

    """
    Cookie:
    AMCVS_7ADA401053CCF9130A490D4C%40AdobeOrg=1;
    s_sess=%20c12%3DULTRABOOST%3B;
    __v3_c_sesslist_11403=eo5p38vh6g_db1%252Ceo50cki0y0_db0%252Cdb0;
    __v3_c_uactiveat_11403=1489992468433;
    AMCV_7ADA401053CCF9130A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C17245%7CMCMID%7C44349097738674292026852552657972134309%7CMCAAMLH-1490513093%7C11%7CMCAAMB-1490597272%7CNRX38WO0n5BH8Th-nqAG_A%7CMCOPTOUT-1489999672s%7CNONE%7CMCAID%7CNONE; ak_bmsc=16B69B04100F6D4E9EA7B4CEA86946963D93A52421160000127BCF580972B814~plnwsSTcJRMwh/zHyeq7wlIHu1k10MZhvrmf15rQ6kdBVxaOAFoPOM0EUdf2SKuOs2ishMmXv0vWa4B2Hq0BwLgN3GXvzJeejFr2oMuSb8xIQhGEPekwNRpQhib1cNRHe6V8jlhk2i7JThRAV9nxrQlqs1PAxL5dsPBcatZcNC7lhl0E7xTlKesYtaawzzB/3fyI6klolSwViE71XQzzc4wL40ZS++UngdsE1/WM2SaoNqEdwEU4DAId9rYkOxB8UfmfQzDph3fEjGmKP0dpj8oA==; Hm_lvt_690ef42ff30759b60f6c189b11f82369=1489908582; Hm_lpvt_690ef42ff30759b60f6c189b11f82369=1489998253; Hm_lvt_c29ad6ea0a27499743676357b8867377=1489908587; Hm_lpvt_c29ad6ea0a27499743676357b8867377=1489998253; _
    ga=GA1.3.1400054808.1489908289;
    _gat=1;
    utag_main=v_id:015ae5745dce00154634ed47f1990407800e707000838$_sn:7$_ss:0$_st:1490001402106$ses_id:1489997957875%3Bexp-session$_pn:10%3Bexp-session; __v3_c_isactive_11403=1; __v3_c_pv_11403=44; __v3_c_session_11403=1489992467819704; __v3_c_today_11403=1; __v3_c_review_11403=2; __v3_c_last_11403=1489999601632; __v3_c_visitor=1489908281124799; s_cc=true; __v3_c_session_at_11403=1489999612313; s_pers=%20v56%3D%255B%255B%2527EXTERNAL%252520CHANNEL%2527%252C%25271489908294110%2527%255D%252C%255B%2527INTERNAL%252520SEARCH%25257CSEARCH-QUERY%2527%252C%25271489947364981%2527%255D%255D%7C1647713764981%3B%20s_vnum%3D1490976000100%2526vn%253D7%7C1490976000100%3B%20pn%3D26%7C1492589972909%3B%20c4%3DACCOUNT%257CLOGIN%7C1490001419266%3B%20s_invisit%3Dtrue%7C1490001419268%3B; s_sq=ag-adi-cn-prod%3D%2526pid%253DACCOUNT%25257CLOGIN%2526pidt%253D1%2526oid%253D%2525E7%252599%2525BB%252520%2525E5%2525BD%252595%2526oidt%253D3%2526ot%253DSUBMIT; frontend=7fl3ss1vus7slesqm1gbambg54; customer_id=1295730; loginSendError=0; frontend=7fl3ss1vus7slesqm1gbambg54
    """



def cashedInHtml(response):
    with open('./adidas.html', 'wb') as f:
        f.write(response.content)


def loginCheck(response):
    t = BeautifulSoup(response.text, "html.parser").h1
    print(t)
    if t==None:
        return False
    else:
        return True

if __name__ == "__main__":
    main()
