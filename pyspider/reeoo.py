#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-07-05 08:05:03
# Project: reo

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
        
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://reeoo.com/', callback=self.index_page,validate_cert=False)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('div.thumb').items():
             detail_url = each('a').attr.href
             print (detail_url)
             self.crawl(detail_url, callback=self.detail_page,validate_cert=False)

    @config(priority=2)
    def detail_page(self, response):
        header=response.doc('body>article>section>header')
        title=header('h1').text()
        tags=[]
        for each in header.items('a'):
           tags.append(each.text())
        content = response.doc('div[id="post_content"]')
        description=content('blockquote>p').text()
        print description
        website_url = content('a').attr.href
        img_list=[]
        for each in content.items('img[data-src]'):
           img_list.append(each.attr('data-src'))
        return {
            "url": response.url,
            "title": response.doc('title').text(),
            "img_list":img_list,
            "tags": tags,
            "website_url": website_url,
        }
