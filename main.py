import requests
from bs4 import BeautifulSoup
import json
import zipfile
import os
import configparser
import webbrowser
# 配置文件
path = os.getcwd() + 'config.ini'
def generate_config():
    config = configparser.ConfigParser()
    config["Path_Config"] = {"Path": 'C:\\Users\\Administrator\\Documents\\LiteLoaderQQNT\\plugins'}

    with open("config.ini", "w") as file:
        config.write(file)
if not os.path.exists("config.ini"):
    generate_config()
config = configparser.ConfigParser()
config.read("config.ini")
path = config["Path_Config"]['Path']
print('请修改配置文件为你的LiteLoader脚本路径')
# 发送HTTP请求，获取网页内容
url1 = 'https://github.moeyy.xyz/https://raw.githubusercontent.com/LiteLoaderQQNT/LiteLoaderQQNT-Plugin-List/v3/plugins.json'  # 替换为你想获取链接的网页地址
response = requests.get(url1)
html_content = response.text
def extract_zip_file(zip_file_path, extract_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

def delete_zip_file(zip_file_path):
    os.remove(zip_file_path)
# 检测请求
if response.status_code == 200:
    # 使用BeautifulSoup解析网页内容
    soup = BeautifulSoup(html_content, 'html.parser')
    # 提取内容
    data = soup.get_text()
    # 保存json  
    result = json.loads(data)
    for i in range(len(result)):
        repo = result[i]['repo']
        branch = result[i]['branch']
        url3 = 'https://github.moeyy.xyz/https://raw.githubusercontent.com/'+repo+'/'+branch+'/manifest.json'
        response = requests.get(url3)
        html_content = response.text
        # 使用BeautifulSoup解析网页内容
        soup = BeautifulSoup(html_content, 'html.parser')
        # 提取内容
        data1 = soup.get_text()
        # 保存json  
        result1 = json.loads(data1)
        description = result1['description']
        print(str(i+1)+'.插件：'+repo+'\n描述：'+description)
    while True:
        a = int(input('请输入序号：')) - 1
        repo1 = result[a]['repo']
        branch1 = result[a]['branch']
        url2 = 'https://github.moeyy.xyz/https://github.com/'+repo1+'/archive/refs/heads/'+branch1+'.zip'
        print('开始下载'+repo1)
        response = requests.get(url2)
        with open('file', "wb") as file:
            file.write(response.content)
        extract_zip_file('file', path)
        delete_zip_file('file')
        print('下载完成')
else:
    print('请求失败，请检查网络')
