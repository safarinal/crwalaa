import os
import re
import ast
import time
import csv
from DrissionPage import WebPage, ChromiumOptions, ChromiumPage
from lxml import etree

# 使用绝对路径
file_path = r'C:\Users\admin\Desktop\bibitao-master\crawl_bbt\data.csv'
directory = os.path.dirname(file_path)

# 确保目录存在
if not os.path.exists(directory):
    os.makedirs(directory)

# 检查文件是否被占用
try:
    with open(file_path, mode='w', encoding='utf-8', newline='') as f:
        csv_writer = csv.DictWriter(f, fieldnames=['title', 'small_img', 'price', 'yuncun', 'neicun', 'pingmu'])
        csv_writer.writeheader()

        cp = ChromiumPage()
        cp.get('https://www.suning.com/')

        cp.ele('css:#searchKeywords').input('手机')
        cp.ele('css:#searchSubmit').click()

        # 处理分页
        page_count = 10  # 假设最多爬取10页
        for page in range(1, page_count + 1):
            if page > 1:
                cp.get(f'https://search.suning.com/手机/{page}-0-0-0-0-0-0-0-0-0-0-0.html')

            # 模拟滚动操作
            for _ in range(5):  # 滚动5次，每次间隔2秒
                cp.scroll.to_bottom()
                time.sleep(2)

            # 遍历每个 <li>，提取 <a> 的 href 属性
            li_list = cp.ele('css:.general.clearfix').eles('css:li')
            for li in li_list:
                href = li.ele('css:.title-selling-point').ele('css:a').attr('href')
                title_a = li.ele('css:.title-selling-point').ele('css:a')
                title = title_a.text if title_a else " "
                small_img = li.ele('css:.img-block').ele('css:img').attr('src')

                # 显式等待价格信息加载
                price_element = li.ele('css:.def-price', timeout=10)
                price = price_element.text if price_element else " "

                info_config = li.ele('css:.item-bg .res-info .info-config')
                em_elements = info_config.eles('css:em')

                yuncun = em_elements[0].text.strip() if len(em_elements) > 0 else " "
                neicun = em_elements[1].text.strip() if len(em_elements) > 1 else " "
                pingmu = em_elements[2].text.strip() if len(em_elements) > 2 else " "

                # 调试输出
                print({
                    "title": title,
                    "small_img": small_img,
                    "price": price,
                    "yuncun": yuncun,
                    "neicun": neicun,
                    "pingmu": pingmu,
                })

                # 写入 CSV 文件
                csv_writer.writerow({
                     "title": title,
                    "small_img": small_img,
                    "price": price,
                    "yuncun": yuncun,
                    "neicun": neicun,
                    "pingmu": pingmu,
                })

        print(f"共爬取 {count} 条记录")

except PermissionError:
    print(f"权限错误：无法写入文件 {file_path}")
    print("请确保文件未被其他程序占用，并且你有足够的权限写入该文件。")
    print("如果问题仍然存在，请尝试以管理员身份运行此脚本。")

class V_writer:
    pass
