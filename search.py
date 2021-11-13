from flask import Flask, request
from glob import glob
import json
from peoplelist import p_list
from json2html import *

app = Flask(__name__)

@app.route("/")
def main():
    names, info = p_list("/home/ravidh/wis-advanced-python-2021-2022/students/")
    names.sort()
    names_links = []

    for name in names:
        link = "<a href=/"+name.split(' ')[0]+">"+name+"</a>"
        names_links.append(link)

    names_links.append("<br><a href=/search>Search</a>")
    names_links.append("<br><a href=/>Home</a>")
    list_names = '<br>'.join(names_links)
    return list_names

@app.route("/search")
def search():
    return '''
     <form action="/result" method="GET">
         <input name="text">
         <input type="submit" value="Go!">
     </form>
     '''

@app.route("/result")
def result():
    names, info = p_list("/home/ravidh/wis-advanced-python-2021-2022/students/",request.args.get('text',''))
    names.sort()
    names_links = []

    for name in names:
        link = "<a href=/"+name.split(' ')[0]+">"+name+"</a>"
        names_links.append(link)

    if len(info) == 0:
        names_links.insert(0,"No mathes found!<br>")
    else:
        names_links.append("<br><a href=/search>Search</a>")

    names_links.append("<br><a href=/>Home</a>")
    list_names = '<br>'.join(names_links)
    return list_names

@app.route("/<name>")
def name_info(name):
    names, info = p_list("/home/ravidh/wis-advanced-python-2021-2022/students/")
    for i in info:
        if name in i["name"]:
            return json2html.convert(json = i)+"<br><a href=/>Home</a>"
