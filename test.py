# -*- coding:utf-8 -*-
# Author: cmzz
# @Time :19-3-19
import re
import requests
import os


def get_html(url):
    headers = { 'content-type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
    response = requests.get(url, timeout=10, headers=headers)
    response.encoding = 'utf8'
    html = response.text
    return html


def get_pic(url):
    headers = {'content-type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
    pic_response = requests.get(url, timeout=10, headers=headers)
    pic = pic_response.content
    return pic


def save_file(chdir_path, filename, content):
    if filename[-4:] in ['.jpg', '.png', 'webp','.png','jpeg', '.gif', '.bmp']:
        with open(chdir_path + '/' + 'images/' + filename , "wb+") as f:
            f.write(content)
            return print('写入{}'.format(filename) + '成功')
    elif filename[-2:] == 'js':
        with open(chdir_path + '/' + 'js/' + filename, 'w+') as f:
            f.write(content)
            return print('写入{}'.format(filename)+'成功')
    elif filename[-3:] == 'css':
        with open(chdir_path + '/' + 'css/' + filename, 'w+') as f:
            f.write(content)
            return print('写入{}'.format(filename)+'成功')
    else:
        with open(chdir_path + '/' + filename, 'w+') as f:
            f.write(content)
            return print('写入{}'.format(filename) + '成功')


def scarpy_web(url, web_name):
    local_path = os.getcwd()
    if not os.path.exists(web_name):
        os.makedirs(web_name+'/images')
        os.makedirs(web_name+'/css')
        os.makedirs(web_name+'/js')

    # if not os.path.exists(web_name+'/images'):
    #     os.makedirs('images')
    # save html file
    content = get_html(url)
    filename = web_name + '.html'
    chdir_path = local_path + '/' + web_name

    save_file(chdir_path, filename, content)

    # save css file
    patterncss1 = '<link href="(.*?)"'
    patterncss2 = '<link rel="stylesheet" href="(.*?)"'
    patterncss3 = '<link type="text/css" rel="stylesheet" href="(.*?)"'
    result = re.compile(patterncss1, re.S).findall(content)
    result += re.compile(patterncss2, re.S).findall(content)
    result += re.compile(patterncss3, re.S).findall(content)

    for link in result:
        css_name_model = '.*/(.*?).css'
        css_filename = re.compile(css_name_model, re.S).findall(link)
        try:
        # 这里匹配出来有些css和js文件是以http链接形式应用的，所以分开来写入
            if link[0] == 'h':
                resopnse1 = get_html(link)
                css_name1 = css_filename[0]+'.css'
                save_file(chdir_path, css_name1, resopnse1)
            else:
                css_url = url+link
                resopnse2 = get_html(css_url)
                css_name2 = css_filename[0]+'.css'
                save_file(chdir_path, css_name2, resopnse2)
        except Exception as e:
            print('css{}匹配失败'.format(css_filename), '原因:', e)

    # save js file
    patternjs1 = '<script src="(.*?)"'
    patternjs2 = '<script type="text/javascript" src="(.*?)"'
    list = re.compile(patternjs1, re.S).findall(content)
    list += re.compile(patternjs2, re.S).findall(content)

    for i in list:
        js_name_model = '.*/(.*?).js'
        js_filename = re.compile(js_name_model, re.S).findall(i)
        try:
            if i[0] == 'h':
                html1 = get_html(i)
                js_filename1 = js_filename[0]+'.js'
                save_file(chdir_path, js_filename1, html1)
            else:
                js_url = url+i
                html2 = get_html(js_url)
                js_filename2 = js_filename[0]+'.js'
                save_file(chdir_path, js_filename2, html2)
        except Exception as e:
            print('js{}匹配失败'.format(js_filename), '原因:', e)

    # save pic file
    patternimg = '<img src="(.*?)"'
    patternimg2 = '<img.*?src="(.*?)"'
    pic_list = re.compile(patternimg, re.S).findall(content)
    pic_list += re.compile(patternimg2, re.S).findall(content)

    print(pic_list)
    for i in pic_list:
        pic_name_model = '.*/(.*?).(jpg|webp|png|jpeg|gif|bmp)'
        pic_filename = re.compile(pic_name_model, re.S).findall(i)
        try:
            if i[0] == 'h':
                pic1 = get_pic(i)
                pic_filename1 = pic_filename[0][0]+'.' + pic_filename[0][1]
                save_file(chdir_path, pic_filename1, pic1)
            else:
                pic2 = url+i
                pic2 = get_pic(pic2)
                pic_filename2 = pic_filename[0][0]+'.' + pic_filename[0][1]
                save_file(chdir_path, pic_filename2, pic2)
        except Exception as e:
            print('图片{}匹配识别'.format(pic_filename), '原因', e)

if __name__ == '__main__':
    # url = input('输入你想要爬取的网页:')
    url = 'http://s.manmanbuy.com/Default.aspx?key=%F7%C8%D7%E516&btnSearch=%CB%D1%CB%F7&WebShieldDRSessionVerify=3v1ZDVCBNXDnKlljM7sO'
    web_name = 'manmankan'
    scarpy_web(url=url, web_name=web_name)