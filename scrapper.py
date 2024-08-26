import requests 
from bs4 import BeautifulSoup


def search_incruit(keyword):
    jobs = []

    response = requests.get(f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}&startno=0")
    soup = BeautifulSoup(response.text, "html.parser")
    lis = soup.find_all("li", class_="c_col")

    for li in lis: 
        company = li.find("a", class_="cpname").text
        title = li.find("div", class_="cell_mid").find("a").text
        location = li.find("div", class_="cl_md").find_all("span")[2].text
        link = li.find("div", class_="cell_mid").find("a").get("href")
        
        job_data = {
            "title": title, 
            "company": company,
            "location": location, 
            "link": link
        }

        jobs.append(job_data)
    
    return jobs


def search_jobkorea(keyword, page=1):
    jobs = []

    for i in range(page):

        page = i + 1
        response = requests.get(f"https://www.jobkorea.co.kr/Search/?stext={keyword}&tabType=recruit&Page_No={page}")
        soup = BeautifulSoup(response.text, "html.parser")
        lis = soup.find_all("article", class_="list-item")

        for li in lis: 
            try: 
                company = li.find("div", class_="list-section-corp").find("a").text.strip()
                title = li.find("div", class_="information-title").find("a").text.strip()
                location = li.find("ul", class_="chip-information-group").find_all("li")[3].text
                link = li.find("div", class_="information-title").find("a").get("href")
                link = f"https://www.jobkorea.co.kr{link}"

                job_data = {
                    "title": title, 
                    "company": company, 
                    "location": location, 
                    "link": link
                }

                jobs.append(job_data)
            except: 
                pass

    return jobs


result = search_jobkorea("파이썬", 10)
print(result)
print(len(result))




    