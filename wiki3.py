
import requests
import os
from bs4 import BeautifulSoup   

res=requests.get("https://en.wikipedia.org/wiki/List_of_sports")
soup=BeautifulSoup(res.content,"html.parser")

def main_func():
    main_content = soup.find('div', attrs={"id":"toc"}).find('ul')
    # print(main_content)
    # print("===========================")
    
    
    level_1 = main_content.find_all('li', attrs={'class':'toclevel-1'})
    # print(level_1)
    # print("=======================================")
    for i in level_1:
        heading_name = i.find('span',attrs={'class','toctext'}).text
        # print(heading_name)
       
        if heading_name != "See also" and heading_name != "References":
            if i.find("ul"):
                for j in i.find_all('li', attrs={'class':'toclevel-2'}):

                    sub_heading = j.find('span',attrs={'class':'toctext'}).text
                    # print(sub_heading)
                    if not os.path.exists(f"{heading_name}/{sub_heading}"):
                      os.makedirs(f"{heading_name}/{sub_heading}")

                    sub_heading_href_value=j.find("a")["href"].replace("#","")
             
                    sub_head_content = soup.find("span",attrs={"id":sub_heading_href_value}).find_next("ul")

                    # print(sub_head_content)
                    
                  
                      
                       

                            
                
                    with open(f"{heading_name}/{sub_heading}/data.txt","a") as  f1:
                        
                        for contents in sub_head_content.find_all("li"):
                                   
                                    try:
                                    
                                       

                                        url="https://en.wikipedia.org"+contents.find("a")["href"]
                                        f1.write(url+"\n")
                                     
                                        
                                    

                                    except:
                                        continue

                                        
                                    
                        
                    

                    if j.find("ul"):
                        for k in j.find("ul").find_all('li', attrs={'class':'toclevel-3'}):
                            # print(k)
                            inner_sub_heading = k.find('span',attrs={'class':'toctext'}).text
                            # print(inner_sub_heading)
                            if not os.path.exists(f"{heading_name}/{sub_heading}/{inner_sub_heading}"):
                                os.makedirs(f"{heading_name}/{sub_heading}/{inner_sub_heading}")

                            last_href_value = k.find('a')['href'].replace('#','')
                            last_sub_head_content = soup.find("span",attrs={"id":last_href_value}).find_next("ul")
                            for last in last_sub_head_content.find_all("li"):
                                with open(f"{heading_name}/{sub_heading}/{inner_sub_heading}/data.txt","a")as file2:
                                    try:

                                        url2="https://en.wikipedia.org"+last.find("a")["href"]
                                        file2.write(url2 + "\n")

                                    except:
                                         continue

   

                 
  

main_func()

                    
                    
        


