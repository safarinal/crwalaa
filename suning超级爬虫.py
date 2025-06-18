import re
import ast
import time
import csv
f=open('data.csv',mode='w',encoding='utf-8',newline='')
csV_writer=csv.DictWriter(f,fieldnames=['title','small_img','price','neicun_yincun'])
csV_writer.writeheader()
from DrissionPage import WebPage, ChromiumOptions, ChromiumPage
from lxml import etree

cp = ChromiumPage()
# co.headless(False)
# # # 使用指定的Chromium选项创建WebPage实例
# cp = WebPage(chromium_options=co)
# cp.get('https://www.suning.com/')
# #
# cp.ele('css:#searchKeywords').input('手机')
# cp.ele('css:#searchSubmit').click()
# 遍历每个 <li>，提取 <a> 的 href 属性
count = 0

li_list = cp.ele('css:.general.clearfix').eles('css:li')
for li in li_list:
    # cp.scroll.to_bottom()
    href = li.ele('css:.title-selling-point').ele('css:a').attr('href')
    title_a = li.ele('css:.title-selling-point').ele('css:a')
    title = title_a.text if title_a else " "
    small_img = li.ele('css:.img-block').ele('css:img').attr('src')
    # print(img)
    price = li.ele('css:.def-price').text
    # print(price)
    neicun_yincun = li.ele('css:.item-bg').ele('css:.res-info').ele('css:.info-config').ele('css:em')
    neicun_yincun = neicun_yincun.text if neicun_yincun else " "
    count += 1
    # cp.get(href)
    # # 等待页面加载完成
    # cp.wait.load_start()
    # # 提取 og:image
    # meta_element = cp.ele('css:meta[property="og:image"]')
    # big_img = meta_element.attr('content') if meta_element else " "
    # print(big_img)
    print({
        "title": title,
        "small_img": small_img,
        "price": price,
        "neicun_yincun": neicun_yincun,
        # "big_img": big_img
    })

    # break
print(count)



csV_writer.writerow({
    "title": title,
    "small_img": small_img,
    "price": price,
    "neicun_yincun": neicun_yincun,
    # "big_img": big_img
})
