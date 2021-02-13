#!/usr/bin/pythn3

import urllib3
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime
from threading import Thread
from multiprocessing.pool import ThreadPool


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

amazon_link_standard_ita = "https://www.amazon.it/dp/B08KKJ37F7/ref=sxts_spkl_2_0_07b25a9a-1f5d-4493-96dd-716b3478304c?pd_rd_w=RtPZX&pf_rd_p=07b25a9a-1f5d-4493-96dd-716b3478304c&pf_rd_r=V8SM9HBNQXTAGYND9MMJ&pd_rd_r=6955e45a-08e8-4f5a-b6e6-dbfee383857c&pd_rd_wg=IFwx3&qid=1611686866"
amazon_link_digital_ita = "https://www.amazon.it/Sony-PlayStation-5-Digital-Edition/dp/B08KJF2D25/ref=sr_1_1?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=ps5+console&qid=1611515471&s=videogames&sr=1-1"
amazon_link_standard_es = "https://www.amazon.es/dp/B08KKJ37F7/ref=sxts_spkl_2_1_19702538-81b7-4e26-8a68-a475cc66898a?pf_rd_p=19702538-81b7-4e26-8a68-a475cc66898a&pf_rd_r=S9R83MV42T0S1FFWBZHA&pd_rd_wg=wfqb6&pd_rd_w=SP3Nh&qid=1612558396&pd_rd_r=91ddc19f-cdc1-4d47-9040-23f0816650a2"
amazon_link_standard_uk = "https://www.amazon.co.uk/PlayStation-9395003-5-Console/dp/B08H95Y452/ref=sr_1_1?dchild=1&keywords=ps5&qid=1612559440&sr=8-1&th=1"
amazon_link_standard_nl = "https://www.amazon.nl/Sony-PlayStation-PlayStation%C2%AE5-Console/dp/B08H93ZRK9/ref=sr_1_2?dchild=1&pd_rd_r=117cb213-33b5-4630-903d-923790a8d6d9&pd_rd_w=jK8Sv&pd_rd_wg=gqFTP&pf_rd_p=77407219-c937-4a14-85ff-6ad2a54ebbc8&pf_rd_r=045CBSP1C0J1XE2Q006Z&qid=1612559576&s=videogames&sr=1-2"
amazon_link_digital_nl = "https://www.amazon.nl/Sony-PlayStation-PlayStation%C2%AE5-Console/dp/B08H98GVK8/ref=sr_1_2?dchild=1&pd_rd_r=117cb213-33b5-4630-903d-923790a8d6d9&pd_rd_w=jK8Sv&pd_rd_wg=gqFTP&pf_rd_p=77407219-c937-4a14-85ff-6ad2a54ebbc8&pf_rd_r=045CBSP1C0J1XE2Q006Z&qid=1612559576&s=videogames&sr=1-2&th=1"

amazon_link_standard_2 = "https://www.amazon.it/Playstation-Sony-PlayStation-5/dp/B08KKJ37F7/ref=sr_1_2?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=ps5+console&qid=1611602689&s=videogames&sr=1-2"
amazon_link_digital_2 = "https://www.amazon.it/Sony-PlayStation-5-Digital-Edition/dp/B08KJF2D25/ref=sr_1_1?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=ps5+console+digitale&qid=1611602805&s=videogames&sr=1-1"
unieuro_link_standard = "https://www.unieuro.it/online/Playstation-5/PlayStation-5-pidSONPS5DISC"
unieuro_link_digital = "https://www.unieuro.it/online/Playstation-5/PlayStation-5-Digital-Edition-pidSONPS5DIGITAL"
gamestop_link_standard = "https://www.gamestop.it/PS5/Games/131468"
gamestop_link_digital = "https://www.gamestop.it/PS5/Games/131469/playstation-5-digital-edition"
euronics_link_standard = "https://www.euronics.it/console/sony-computer/playstation-5/eProd202008906/"
euronics_link_digital = "https://www.euronics.it/siem/console/sony-computer/playstation-5-digital-edition/eProd202008907/"
euronics_link_digital_2 = "https://www.euronics.it/console/sony-computer/playstation-5-digital-edition/eProd202008907/"
mediaworld_link_standard = "https://www.mediaworld.it/product/i-147513"


isNotAvailable = ["Non disponibile", "display: block;", "Disponibile presso questi venditori", "No disponible", "Currently unavailable", "Momenteel niet verkrijgbaar", "Disponible a través de estos vendedores"]
headers = {
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
    'cache-control':'max-age=0',
    'cookie':'lc-acbit=it_IT; csrf=-427947707; ubid-acbit=261-0977178-1405068; session-id=262-9703843-9759913; csd-key=eyJ3YXNtVGVzdGVkIjp0cnVlLCJ3YXNtQ29tcGF0aWJsZSI6dHJ1ZSwid2ViQ3J5cHRvVGVzdGVkIjpmYWxzZSwidiI6MSwia2lkIjoiNWE1YzdhIiwia2V5IjoiaXN3TlduRGRJV3R6N05XSmJFemxQK3o2RDBNZm9HOXZRS3Jtb0oxdmU4alhMQk9xNGNNQnhYdWdzT3ArQmU4aVFiUkJvZmpEWEY4KzdueFA5bGhYb3NsN0U5UXhvQ1pVMTRyODVnK0dDRGhyK3o1V0VpTWxyRFQ1UXpiRFpqQXlpUmFPS3VsbmJUL2h2cHJLNW1OMW56RVRqeWR1V1JpbGlWUUtoc0NSU0d5RVVvMFVHTGMrYS9hRHFQTjJCVWplb0VOSmhxUU9yb05CWkU1ai9oRkY1Kzloc01OaStLTjVGN1MvaG5jZDFoRmhkSzc1UXdYUmF3eExhYm1Qam42a2lYbzNpTGk2Z3djaTJOQSt5SXhxNWgyNTNtY1Q5d01tcWxXUDRBaldoRFl1SXFjcFBvZGNUV1c0L0JTd0ZHMFB5K3owYVZneGd2OUR4WW5RTHNBUktRPT0ifQ==; s_vnum=2039530808056%26vn%3D5; sid="f6GdZLi2pG8PEnhIyChe9A==|WWzB9gxTjuJPKusdrOAluVoM8DRZ0O2SEprpiCCKlQg="; s_nr=1611401953743-Repeat; s_dslv=1611401953746; x-acbit="Hr7a7bC2tTj1jwE51sUjOPAW1LMFzkam7@sWOifeoV490DdBgba4nchFtdNiKa8j"; at-acbit=Atza|IwEBIBHZg0K4x0OwxuUAUyDID4n-ypFSoCttprUOJgKJgxpXkLtZd5pvlsQSXXzWonWtbuMC1wtk2IHoZMEvBjR7fnN7D6fKRPR5257awYCBGET6qvPlE7ESyxHoCH2tpR6oMYH77ZxFyLC7i0NcxLK0ieOWXmoGmLTC4DvXDkPsaUWnl8XbyXL32odD0MbZbkI80lM-2m0zAYtio8EDIYtFpn2FlTc4uDNMi0AmcEXAtKtSqQ; sess-at-acbit="xcL9zLm8KE8IXHuuono1VMni2QMHv1JMWnJXI1TOQNw="; sst-acbit=Sst1|PQEt_ISN9hxN3nsTyk8NlZYUCbM3nY2Gxu9RI_-lCtscQceK5ZBkQWaK-5sL7ONTYrGOxBNSungsZ-Ffx1he4qJGqMI50RMvR6cU3WtUyKonjDJofMvTMqdK94vdoM155KmD-HAqFyu_f4N-NISDpEV0mOM_NnzF2ZNc3W7Ax6ZqXD-JOtjepnQsPfzQmMKPLu8qAuMfNp1nDVVXLtZo_aZXO0SVBzd35qEAlArxpSYB8gniSKA7TyieyThjug8yWpxA1rPujhDAraaVKdQCKRzRKKA6-jaCtz9hH8YNJFI--2s; i18n-prefs=EUR; session-token="6mfKkq76vSjbyvOwILpnkYr6uMY4kHCfk2QEXN4kU6vHZYnUQv9YAYvWKFei80Nqg++6IKU7duIgBlMoECuOIKzhbqr0KnY6SskLSrPjyTQhB/qZLs2jygcYzLXod3A1vEC8e7hdbwfy7ZhbBZoJRp7LvgUnYDnkc85LDD2JFZnnPLD9GP/2Y1BKT7k9jJsCMa/HiuQPi3bahRXAFsAdLw=="; session-id-time=2082758401l; csm-hit=tb:GT7TZBQCRD6VPZ24P3QM+s-3XXCT2GB6E17DYZS4XGE|1611853996707&t:1611853996707&adb:adblk_yes',
    'downlink':'10',
    'ect':'4g',
    'rtt':'100',
    'sec-ch-ua':'"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
    'sec-ch-ua-mobile':'?0',
    'sec-fetch-dest':'document',
    'sec-fetch-mode':'navigate',
    'sec-fetch-site':'same-origin',
    'sec-fetch-user':'?1',
    'upgrade-insecure-requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'Cache-Control':'no-cache',
    'Pragma':'no-cache'
}


http = urllib3.PoolManager()

def check_web_site(link: str, website_name: str, colored: bool):
    web_url = http.request('GET', link, headers=headers)
    data = web_url.data

    soup = BeautifulSoup(data, 'html.parser')

    if "Amazon".lower() in website_name.lower():
        availability = soup.find(id='availability')
        price = availability.find('span').text
    elif "Unieuro".lower() in website_name.lower():
        availability = soup.find_all("div", {"class": "product-availability"})
        price = availability[0].getText().replace("\n", "")
    elif "Euronics".lower() in website_name.lower():
        availability = soup.find_all("div", {"class": "productDetail__mainInfo"})
        price = availability[1].find('span').text
    elif "GameStop".lower() in website_name.lower():
        availability = soup.find("a", {"class": "megaButton buyDisabled"})
        price = availability["style"]
    elif "Mediaworld".lower() in website_name.lower():
        availability = soup.find_all("div", {"class": "price-container"})
        price = "".join(availability[1].find('span').text.split())
        if price != "499.99" and price != "399.99":
            price = "Non disponibile"

    today = datetime.now()

    to_print = "[" + today.strftime("%d/%m/%Y - %H:%M:%S") + "] " + website_name + " "
    if colored:
        to_print = color.BOLD + "[" + today.strftime("%d/%m/%Y - %H:%M:%S") + "] " + color.BLUE + website_name + color.RED + " "
    for isAva in isNotAvailable:
        if isAva.lower() in price.lower():
            print(to_print + "Non Disponibile" + color.END)
            return (str(website_name), "NON DISPONIBILE", str(link))
    if colored:
        to_print = to_print + color.GREEN
    print(to_print + "Disponibile" + color.END)
    return (str(website_name), "DISPONIBILE", str(link))

result_list = []
def log_result(result):
    result_list.append(result)

def check_ps5(colored: bool):
#    check_web_site(mediaworld_link_standard, "Mediaworld Standard Edition", colored)
    pool = ThreadPool(processes=6)

    pool.apply_async(check_web_site, args = (amazon_link_standard_ita, "Amazon ITA Standard Edition", colored, ), callback = log_result)
    pool.apply_async(check_web_site, args = (amazon_link_digital_ita, "Amazon ITA Digital Edition", colored, ), callback = log_result)
#    pool.apply_async(check_web_site, args = (amazon_link_standard_es, "Amazon ES Standard Edition", colored, ), callback = log_result)
    pool.apply_async(check_web_site, args = (amazon_link_standard_uk, "Amazon UK Standard Edition", colored, ), callback = log_result)
    pool.apply_async(check_web_site, args = (amazon_link_standard_nl, "Amazon NL Standard Edition", colored, ), callback = log_result)
    pool.apply_async(check_web_site, args = (amazon_link_digital_nl, "Amazon NL Digital Edition", colored, ), callback = log_result)

    pool.apply_async(check_web_site, args = (unieuro_link_standard, "Unieuro Standard Edition", colored, ), callback = log_result)
    pool.apply_async(check_web_site, args = (unieuro_link_digital, "Unieuro Digital Edition", colored, ), callback = log_result)
    pool.apply_async(check_web_site, args = (gamestop_link_standard, "GameStop Standard Edition", colored, ), callback = log_result)
    pool.apply_async(check_web_site, args = (gamestop_link_digital, "GameStop Digital Edition", colored, ), callback = log_result)
    pool.apply_async(check_web_site, args = (euronics_link_standard, "Euronics Standard Edition", colored, ), callback = log_result)
    pool.apply_async(check_web_site, args = (euronics_link_digital, "Euronics Digital Edition", colored, ), callback = log_result)
    pool.apply_async(check_web_site, args = (euronics_link_digital_2, "Euronics Digital Edition", colored, ), callback = log_result)
    pool.apply_async(check_web_site, args = (mediaworld_link_standard, "Mediaworld Standard Edition", colored, ), callback = log_result)

    pool.close()
    pool.join()
    return result_list


# DEBUG ONLY
#while 1:
#    check_web_site(mediaworld_link_standard, "Mediaworld Standard Edition", True)
#    check_ps5(True)
#    print(result_list)
#    result_list.clear()

