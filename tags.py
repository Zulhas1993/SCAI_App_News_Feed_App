import requests
from bs4 import BeautifulSoup

with open("sample.html", "r") as f:
    html_doc=f.read()
soup = BeautifulSoup(html_doc, 'html.parser')


# with open("times.html", "r") as f:
#     html_doc=f.read()
# soup = BeautifulSoup(html_doc, 'html.parser')


# print(soup.prettify())
# print(soup.title)
#print(soup.title.string,type(soup.title.string))
#print(soup.div)
#print(soup.find_all("div"))
#print(soup.find_all("div")[0])

#Get all links comments##############

# for links in soup.find_all("a"):
#     #print(links)
#    # print(links.get("href"))
       #print(links.get_text())

#     s=soup.find(id="link3")
#     #print(s)
#     print(s.get("href"))

# print(soup.select("div.italic"))
# print(soup.get("class"))


# Outside the loop  ############

# s = soup.find(id="link3")
# if s:
#     print(s.get("href"))
#     print(s.get_text())
# else:
#     print("No element found with id='link3'")



# Get child attribute #########

# for child in soup.find(class_="container").children:
#     print(child)

# Get parents attribute #########
# i =0
# for parent in soup.find(class_= "box").parent:
#     i+=1
#     print(parent)
#     if(i==2):
#         break

# modify the atribute##########

# cont =soup.find(class_="container")
# cont.name="span"
# cont["class"] = "myclass class2"
# cont.string="I am a string"
# print(cont)


# Create new html file and get other html atribute and here modify  or add new atribute

# ulTag= soup.new_tag("ul")

# liTag= soup.new_tag("li")
# liTag.string="Home"
# ulTag.append(liTag)

# liTag= soup.new_tag("li")
# liTag.string="About"
# ulTag.append(liTag)

# soup.html.body.insert(0,ulTag)
# with open("modified.html","w") as f:
#     f.write(str(soup))


# cont = soup.find(class_="container")
# print(cont.has_attr("class"))

def has_class_but_not_id(tag):
    return tag.has_attr("class") and not tag.has_attr("id")

def has_content(tag):
     return tag.has_attr("content")

#results =soup.find_all(has_class_but_not_id)
results =soup.find_all(has_content)
for result in results:
   print(result,"\n\n")
