import requests

def get_html(url):
    # get请求       输入url     返回网页的html源码
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
    try:
        a=requests.get(url,headers=headers)
        if a.status_code==200:
            a.encoding=a.apparent_encoding
            return a.content
        return None
    except Exception as e :
        print(f"请求失败__原因{e}")
        return None
def save(data,ty):
    with open(f'cs.{ty}',"wb") as f:
        f.write(data)        

if __name__ == "__main__":
    url="https://upos-sz-mirrorkodoo1.bilivideo.com/upgcxcode/83/46/411784683/411784683-1-30077.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1632410168&gen=playurlv2&os=kodoo1bv&oi=2062423369&trid=0a25768f0837440ebee715e0241a8860u&platform=pc&upsig=af9d8a9971ad2b418004287753f0816d&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=62868472&bvc=vod&nettype=0&orderid=0,3&agrr=0&logo=80000000"
    data=get_html(url)
    print(data)
    ty="mp3"
    # save(data,ty)