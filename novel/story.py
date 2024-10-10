import requests
from bs4 import BeautifulSoup

def get_url_info(page_url):
    url = 'https://www.douluodalumh.com'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
    }
    while page_url:
        response = requests.get(url + page_url, headers=headers)
        response.encoding = 'utf-8'
        try:
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                # 获取title内容
                title = soup.find('div', class_='m-title col-md-12').find('h1')
                title_content = title.text
                print(title_content)
                # 获取章节内容
                info = soup.find('div', class_="panel-body").find_all('p')[1:]
                clean_info = "".join(element.text for element in info if element.text)
                print(clean_info)

                # 进行存储
                with open('douluo.txt', 'a', encoding="utf-8") as f:
                    f.write(title_content + '\n\n' + clean_info + "\n\n")
                # 查找下一章
                flag = soup.find('li', class_="col-md-4 col-xs-12 col-sm-12")
                if flag and '下一章' in flag.text:
                    page_url=flag.a['href']
                else:
                    break
            else:
                print(f"请求失败，状态码：{response.status_code}")
                break
        except Exception as e:
            print(f"程序异常: {e}")

get_url_info('/xiaoshuo/2/689.html')