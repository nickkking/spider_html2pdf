#C:\Program Files\wkhtmltopdf\bin
import requests
import bs4,pdfkit

from tqdm import tqdm
def get_url_list():
    """
    获取所有URL现在录列外
    """
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"}

    response = requests.get('https://www.liaoxuefeng.com/wiki/1252599548343744',headers=headers)

    soup = bs4.BeautifulSoup(response.content,"html.parser")
    menu_tag = soup.find_all(class_="uk-nav uk-nav-side")[1]
    urls = []
    for a in menu_tag.find_all("a"):
        url = "http://www.liaoxuefeng.com" + a.get('href')
        urls.append(url)

    return urls

def parse_url_to_html(url):
    c=[]


    for i in url:
        pro = {"http": "http://127.0.0.1:1087", "https": "http://127.0.0.1:1087"}
        headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"}
        response = requests.get(i,headers=headers)
        soup = bs4.BeautifulSoup(response.content, "html5lib")
        body = soup.find_all(class_="x-wiki-content x-main-content")[0]
        #print(body)
        html = str(body).encode()
        with open("a.html", 'ab+') as f:
             f.write(html)

def save_pdf(htmls,file_name):
    """
    把所有html文件转换成pdf文件
    """
    config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

    options = {
        'page-size': 'Letter',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ]
    }
    pdfkit.from_file(htmls, file_name, options=options,configuration=config)
if __name__=="__main__":


        #u=get_url_list()
        #parse_url_to_html(u)#("https://www.liaoxuefeng.com/wiki/1252599548343744/1255876875896416")
        save_pdf('a.html','java_liao.pdf')
