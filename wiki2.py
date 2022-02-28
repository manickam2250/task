
import requests
import os
from bs4 import BeautifulSoup

res=requests.get("https://en.wikipedia.org/wiki/List_of_sports")
soup=BeautifulSoup(res.content,"html.parser")

def main_func():
    main_content = soup.find('div', attrs={"id":"toc"}).find('ul')
    # print(main_content)
    level_1 = main_content.find_all('li', attrs={'class':'toclevel-1'})
    for i in level_1:
        heading_name = i.find('span',attrs={'class','toctext'}).text
        # print(heading_name)
        if heading_name != "See also" and heading_name != "References":
            if i.find("ul"):
                for j in i.find_all('li', attrs={'class':'toclevel-2'}):

                    sub_heading = j.find('span',attrs={'class','toctext'}).text
                    if not os.path.exists(f"{heading_name}/{sub_heading}"):
                      os.makedirs(f"{heading_name}/{sub_heading}")

                    sub_heading_href_value=j.find("a")["href"].replace("#","")
                    # print(sub_heading_href_value)
                    sub_head_content = soup.find("span",attrs={"id":sub_heading_href_value}).find_next("ul")
                    
                  
                        # print(contents.find("a")["href"])
                       

                            
                
                    with open(f"{heading_name}/{sub_heading}/data.txt","a") as  f1:
                        
                        for contents in sub_head_content.find_all("li"):
                                    print(contents.text)
                                    try:
                                        # f1.write("https://en.wikipedia.org"+contents.find("a")["href"]+"\n")
                                       

                                        url="https://en.wikipedia.org"+contents.find("a")["href"]
                                        f1.write(url+"\n")
                                        # f1.write("----->"+ contents.text + "\n")
                                        # print(url)
                                        # res2=requests.get(url=url)
                                        # soup2=Beautifulsoup(res2.content,"html.parser")
                                        
                                        #             # f1.write(contents.text + "\n")
                                    

                                    except:
                                        continue

                                        
                                    
                        
                    # print(sub_heading_href_value)

                # if j.find("ul"):
                #     for k in j.find_all('li', attrs={'class':'toclevel-3'}):
                #         inner_sub_heading = k.find('span',attrs={'class','toctext'}).text
                #         # print(inner_sub_heading)
                #         if not os.path.exists(f"{heading_name}/{sub_heading}/{inner_sub_heading}"):
                #             os.makedirs(f"{heading_name}/{sub_heading}/{inner_sub_heading}")
                        
                #         href_value = k.find('a')['href'].replace('#','')
                #         with open(f"{heading_name}/{sub_heading}/{inner_sub_heading}/data.txt", 'a') as f:
                #             content = soup.find('span', attrs={'id': href_value}).find_next('ul')
                #             for sports_name in content.find_all("li"):
                #                 f.write(sports_name.text + "\n")

                #     else:
                #         if not os.path.exists(f"{heading_name}/{sub_heading}"):
                #                 os.makedirs(f"{heading_name}/{sub_heading}")


  

main_func()

                    
                    
        


