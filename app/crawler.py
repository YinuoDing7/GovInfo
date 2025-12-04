import requests
from bs4 import BeautifulSoup
import urllib.parse

def fetch_baidu_news(keyword):
    """
    Scrape Baidu News for a given keyword.
    
    Args:
        keyword (str): The search keyword.
        
    Returns:
        list: A list of dictionaries containing news details.
    """
    encoded_keyword = urllib.parse.quote(keyword)
    url = f"https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&rsv_dl=ns_pc&word={encoded_keyword}"
    
    # Headers provided by the user (modified for requests compatibility)
    # headers = {
    #     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    #     "accept-encoding": "gzip, deflate, br, zstd",
    #     "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    #     "cache-control": "max-age=0",
    #     "cookie": "BIDUPSID=70AE3B70A70B029F21D35F98F7E43746; BAIDUID=A69736F340BB537380DF27CE9321715E:FG=1; PSTM=1764066304; BD_UPN=12314753; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_WISE_SIDS_BFESS=60278_63146_65866_66107_66226_66194_66243_66371_66287_66262_66393_66529_66585_66583_66592_66640_66647_66664_66672_66670_66698_66686_66689_66710_66718_66743_66624; BDUSS=FlTaWpVZzlhNDBzdlhIWFJ0aX40dG90cHFkaFZjTzNwM3J2WnQ3dXcxUTNJbFpwRVFBQUFBJCQAAAAAAQAAAAEAAAAjwS1IxbXKssO0xbUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADeVLmk3lS5pZ; BDUSS_BFESS=FlTaWpVZzlhNDBzdlhIWFJ0aX40dG90cHFkaFZjTzNwM3J2WnQ3dXcxUTNJbFpwRVFBQUFBJCQAAAAAAQAAAAEAAAAjwS1IxbXKssO0xbUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADeVLmk3lS5pZ; bce-sessionid=0010085e5f416694367aac5a0f1be8634de; H_WISE_SIDS=60278_63146_65866_66107_66226_66194_66243_66371_66287_66262_66393_66529_66585_66583_66592_66640_66647_66664_66672_66670_66698_66686_66689_66710_66718_66743_66624_66775_66787_66792_66747; BAIDUID_BFESS=A69736F340BB537380DF27CE9321715E:FG=1; baikeVisitId=eb5a8347-9b32-43ae-a4d4-0bc440ee48f3; BD_CK_SAM=1; PSINO=2; COOKIE_SESSION=5214_0_4_6_4_10_1_0_4_5_9_2_255328_0_0_0_1764739285_0_1764744496%7C6%230_0_1764744496%7C1; delPer=0; BA_HECTOR=ag00a185ah8k0h21a02g20a52k2g821kivn9s25; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; ZFY=:APZXYR3Hy7NP8bgnbqbEoGsCx7FWi12vRdxOaxPQoLQ:C; H_PS_PSSID=60278_63146_66107_66226_66243_66371_66287_66262_66393_66529_66585_66583_66592_66647_66664_66672_66670_66698_66686_66689_66710_66718_66743_66624_66775_66787_66792_66747_66801_66599; arialoadData=false; BDRCVFR[C0p6oIjvx-c]=mk3SLVN4HKm; BDSVRTM=1229",
    #     "referer": "https://news.baidu.com/",
    #     "sec-ch-ua": '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
    #     "sec-ch-ua-mobile": "?0",
    #     "sec-ch-ua-platform": '"Windows"',
    #     "sec-fetch-dest": "document",
    #     "sec-fetch-mode": "navigate",
    #     "sec-fetch-site": "same-site",
    #     "sec-fetch-user": "?1",
    #     "upgrade-insecure-requests": "1",
    #     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
    # }
    
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "max-age=0",
        "Referer": "https://news.baidu.com/",
        
        "sec-ch-ua": "\"Chromium\";v=\"142\", \"Microsoft Edge\";v=\"142\", \"Not_A Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-site",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0",
        "Cookie": "BAIDUID_BFESS=4E31669E80D6C8FB954FF39ECECECB3F:FG=1; BDUSS_BFESS=UJoc3d2WDlQTk5RclJUOG5JdS1hYW9xdUN-S21VOWlhcktDMzNpdXJnR012aGhuSUFBQUFBJCQAAAAAAQAAAAEAAAAjwS1IxbXKssO0xbUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIwx8WaMMfFma; __bid_n=1921e22b7497472f726157; BIDUPSID=4E31669E80D6C8FB9E742F8311FC510C; PSTM=1730875459; H_WISE_SIDS_BFESS=60273_60942_61027_61022_61035_61055_60854; COOKIE_SESSION=665466_1_4_9_7_16_0_0_3_9_128_1_5334417_0_0_0_1731028145_1733564070_1734229656%7C9%230_1_1733564190%7C1; H_PS_PSSID=60273_63141_64004_66098_66108_66221_66205_66191_66365_66275_66261_66393_66529_66585_66580_66592_66603_66612_66654_66684_66719_66772_66787_66792_66599; BD_UPN=12314753; BA_HECTOR=a005al8g2ka0018l842421812la0031kj27er24; ZFY=:AOjKh1M60Ie24SB7osWLET1jjHeuVUKF3fgApUbatE0:C; BDRCVFR[C0p6oIjvx-c]=mbxnW11j9Dfmh7GuZR8mvqV; delPer=0; BD_CK_SAM=1; PSINO=2; arialoadData=false; BDSVRTM=611"
    }
    
    try:
        session = requests.Session()
        cookie_str = headers.get("Cookie", "")
        cookie_items = [c for c in cookie_str.split("; ") if c]
        cookies = {}
        for item in cookie_items:
            parts = item.split("=", 1)
            if len(parts) == 2:
                cookies[parts[0]] = parts[1]
        req_headers = dict(headers)
        req_headers.pop("Cookie", None)
        session.get("https://www.baidu.com/", headers=req_headers, cookies=cookies, allow_redirects=True, timeout=15)
        session.get("https://news.baidu.com/", headers=req_headers, cookies=cookies, allow_redirects=True, timeout=15)
        response = session.get(url, headers=req_headers, cookies=cookies, allow_redirects=True, timeout=15)
        response.encoding = 'utf-8' # Force UTF-8 encoding
        # response.raise_for_status() # verification page often returns 200, so this might not trigger
        
        # Check for security verification or block
        page_text = response.text
        if "安全验证" in page_text or "百度安全验证" in page_text or "网络不给力" in page_text:
            print("Warning: Baidu Security Verification triggered. Please update cookies.")
            return []

        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Baidu news items usually have class "c-container" or "result-op"
        news_items = soup.select('div.c-container')
        
        if not news_items:
             news_items = soup.select('div.result-op')

        results = []
        for item in news_items:
            news_data = {
                'title': '',
                'summary': '',
                'cover': '',
                'original_url': '',
                'source': ''
            }
            
            # 1. Title and Original URL
            title_tag = item.select_one('h3 a')
            if title_tag:
                news_data['title'] = title_tag.get_text(strip=True)
                news_data['original_url'] = title_tag.get('href')
            else:
                continue 
            
            # 2. Cover Image
            img_tag = item.select_one('img')
            if img_tag:
                news_data['cover'] = img_tag.get('src')
                
            # 3. Source
            source_tag = item.select_one('.c-color-gray')
            if source_tag:
                news_data['source'] = source_tag.get_text(strip=True)
                
            # 4. Summary
            summary_tag = item.select_one('.c-font-normal-three')
            if not summary_tag:
                 summary_container = item.select_one('.c-span-last')
                 if summary_container:
                     summary_tag = summary_container
            
            if summary_tag:
                news_data['summary'] = summary_tag.get_text(strip=True)
            else:
                texts = [t.strip() for t in item.stripped_strings]
                for text in texts:
                    if len(text) > 20 and text != news_data['title'] and text != news_data['source']:
                        news_data['summary'] = text
                        break
            
            results.append(news_data)
            
        if results:
            return results
        alt_url = f"https://www.baidu.com/s?ie=utf-8&rtt=1&bsst=1&cl=2&tn=news&rsv_dl=ns_pc&wd={encoded_keyword}"
        response2 = session.get(alt_url, headers=req_headers, cookies=cookies, allow_redirects=True, timeout=15)
        response2.encoding = 'utf-8'
        page_text2 = response2.text
        if "安全验证" in page_text2 or "百度安全验证" in page_text2 or "网络不给力" in page_text2:
            return []
        soup2 = BeautifulSoup(response2.content, 'html.parser')
        news_items2 = soup2.select('div.c-container')
        if not news_items2:
            news_items2 = soup2.select('div.result-op')
        results2 = []
        for item in news_items2:
            news_data = {
                'title': '',
                'summary': '',
                'cover': '',
                'original_url': '',
                'source': ''
            }
            title_tag = item.select_one('h3 a')
            if title_tag:
                news_data['title'] = title_tag.get_text(strip=True)
                news_data['original_url'] = title_tag.get('href')
            else:
                continue
            img_tag = item.select_one('img')
            if img_tag:
                news_data['cover'] = img_tag.get('src')
            source_tag = item.select_one('.c-color-gray')
            if source_tag:
                news_data['source'] = source_tag.get_text(strip=True)
            summary_tag = item.select_one('.c-font-normal-three')
            if not summary_tag:
                summary_container = item.select_one('.c-span-last')
                if summary_container:
                    summary_tag = summary_container
            if summary_tag:
                news_data['summary'] = summary_tag.get_text(strip=True)
            else:
                texts = [t.strip() for t in item.stripped_strings]
                for text in texts:
                    if len(text) > 20 and text != news_data['title'] and text != news_data['source']:
                        news_data['summary'] = text
                        break
            results2.append(news_data)
        return results2

    except Exception as e:
        print(f"Error scraping Baidu News: {e}")
        return []

if __name__ == "__main__":
    keyword = "北京"
    results = fetch_baidu_news(keyword)
    if not results:
        print("无结果或被拦截。")
    for i, news in enumerate(results):
        print(f"--- 新闻 {i+1} ---")
        print(f"标题：{news['title']}")
        print(f"概要：{news['summary']}")
        print(f"封面：{news['cover']}")
        print(f"原始URL：{news['original_url']}")
        print(f"来源：{news['source']}")
        print("----------------")
