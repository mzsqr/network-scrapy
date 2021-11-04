from urllib import parse
import scrapy
from urllib.parse import urlencode
import json


class ZhihuPlague(scrapy.Spider):
    name = "zhihu_plague"

    def start_requests(self):
        for word in ["黑死病", "新冠"]:
            for i in range(10):
                cookies = {
                    "__snaker__id": "jbRqAqaflv9uCokh",
                    "_9755xjdesxxd_": "32",
                    "_xsrf": "vvS28v5MlGmBQjClTnGZdulMrSCMTRlD",
                    "_zap": "eb03b78b-b3af-4ee2-9cb2-23c9e8c7054c",
                    "captcha_session_v2": '"2|1:0|10:1635463310|18:captcha_session_v2|88:SFJJNGFZVWJkRU00LzVqZ05EV0VZaEN4MlM2cXl1b2VndzJxY0cxRG9RbDJtc1NqN3piY3YzUUpVWlpRQmwxYg==|a9efe514a08aaad25c5f002ccac1d5fce538694dca1f93108183570bc7a4437d"',
                    "captcha_ticket_v2": '"2|1:0|10:1635463331|17:captcha_ticket_v2|704:eyJ2YWxpZGF0ZSI6IkNOMzFfaUhlZ2k1dzV6bmxKZ0NrTkVtX2ZNUU1JVkxTWUFaREpBOFhHRGVfcWNFTkxZQ20xMXl5T0pGcGlCLTJfbWIwbmNTRnk1N0pFS2ZwZndyUTRBV1hMUmFmbllraEJlQlI3a2l2WUpibFU3ZmhCOW5DaTVwLXBBN2IxN2FiLUJRT0JUOEpiWkJWdlBjMHhrN1hZaHlGOXFhUEtfVzZ2Xy1CSnBXa1MyUWtCN1ZGZ2ZJWVUxTFBEcnZEWVpjakh1ZHNnQmxMTGhacVNmanZPdk02aWpGZ2VOZ3MuYktKVk1yakExWWlWam5sZ29qdS1ienJOVC5nMTdBYXZmdjV5b1BBeXlBOXNILkFnbEZHWG45V3NmampMdW50T0U5aGlJdEItSXM4dkxaY3FvVzYwYnhxa3JFWFRnQ0xUR2JYNDVkc05jVUlBVUtZOXE1UmNWLVNCUnlPLmdpbXJseno0T1V3dUFGVThUZkJCcmlrLTZRVUduLi1kOXBvaS5MQ29KcjQteVNvSXl0eVdqYVBYTW4wbHUyb1ZTLXAyVzZXSVdRT25PMlNMWER5djBKbS5STWV6MVItRFBfamdWLVJxRnZFQXJ4Um01Q1U2TWFXRk5IOUlqdnBrUUVqcVpmUWxDc2NIMnktZGR0TE9EeW96MVlLZjliS2w4MmNZd3Z6MyJ9|d3fd91e6f77d5d27a5634181b488669b149f7f76b10340a0e16029cea28afaa6"',
                    "d_c0": '"AOBe3sie5BOPTvkx8sMoIQxZVaGyKV4KrA4=|1634539959"',
                    "gdxidpyhxdE": "yvsvbt\\pTf9o\\gYX0AeuGmj7WBxBxdUxVNZ/ynw9HjKd2bI0CTme\\DYJx0kq9dUNw0WT69gIlribJDrPhakkGLE3dJngZknxj3St1tvMg1zwmZ14n1YIBjl7EV0V/L8vTXvu+lhg6Me2viLibCL6ada1+5JuPLVnnim947Ixx81z6yvX:1635464169503",
                    "Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49": "1636011329",
                    "Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49": "1635759970,1636002142,1636008347,1636011274",
                    "JOID": "WlAQA0vPQYAmCzRcasdpEFzForB0iR_SEUpNOx_zJekbYnUUPs7EBk8DOVRvRXCHEh7U4PlGZE6kgLIaDKfVbWY=",
                    "KLBRSID": "4efa8d1879cb42f8c5b48fe9f8d37c16|1636011329|1636011273",
                    "NOT_UNREGISTER_WAITING": "1",
                    "osd": "UVkUAU3ESIQkDT9VbsVvG1XBoLZ_gBvQF0FEPx31LuAfYHMfN8rGAEQKPVZpTnmDEBjf6f1EYkWthLAcB67Rb2A=",
                    "SESSIONID": "FSW7Iyjp4dd8iIHY6RXk6hKLiOwK8DXcAxqI6bRIHkD",
                    "tst": "r",
                    "YD00517437729195:WM_NI": "xCI3/7LkD5REF8HZ6FZrHK0ciEWJHD0nAGws847KFQzucRMZGmHATBT47ddIidFr+hthed4Z6/V2B7s+UZHPpvAYzsBjak8YWBbbbkgLBayv+tkgLqBF7oqhHz4U5cS6Yjg=",
                    "YD00517437729195:WM_NIKE": "9ca17ae2e6ffcda170e2e6eea7f96bae9eb7b2d561aeef8ea6c45e978b8faaf87c8d8d99a8b14693e8fe95e72af0fea7c3b92abc9d87d4ae3d90b58cd6d14f86e888bbb54e9aae88acb369ab9b99abcb50f4b28fa8f679fcecf9acc55bbaabadb3d05285b388a2d74a98ecf985e743abbc8a93aa64b8b8ab85b752f6f19ad3c13db1f59bbbcb5cb4aa8fbaf97982b6af8cbb53959eae83e161a5948e82fc7ee9aca588cf7b829af990f4648ca6fcb6b86991ea978be637e2a3",
                    "YD00517437729195:WM_TID": "a7e2QapBpLFEBVQFEBYuoMYJSOSUG04Q",
                    "z_c0": '"2|1:0|10:1635463332|4:z_c0|92:Mi4xeUZxUUVRQUFBQUFBNEY3ZXlKN2tFeVlBQUFCZ0FsVk5wSDVvWWdBNkxGS1VZQV9CYkF1X1hWd180R2w2U3dqOUpB|0744a0a6dc07bc9d6baf2b08292b7a90fd358cfb748cceab8ae443aac9c87811"',
                }
                headers = {
                    "x-api-version": "3.0.91",
                    "x-app-za": "OS=Web",
                    "x-zse-93": "101_3_2.0",
                    "x-zse-96": "2.0_aTS0b7eqN9xpbMYqsXSq2iUBb_FxbTF8hCOyUgHqo_Of",
                    "Pragma": "no-cache",
                    "Cache-Control": "no-cache",
                    "Cookies": '_zap=eb03b78b-b3af-4ee2-9cb2-23c9e8c7054c; d_c0="AOBe3sie5BOPTvkx8sMoIQxZVaGyKV4KrA4=|1634539959"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1635759970,1636002142,1636008347,1636011274; captcha_session_v2="2|1:0|10:1635463310|18:captcha_session_v2|88:SFJJNGFZVWJkRU00LzVqZ05EV0VZaEN4MlM2cXl1b2VndzJxY0cxRG9RbDJtc1NqN3piY3YzUUpVWlpRQmwxYg==|a9efe514a08aaad25c5f002ccac1d5fce538694dca1f93108183570bc7a4437d"; gdxidpyhxdE=yvsvbt%5CpTf9o%5CgYX0AeuGmj7WBxBxdUxVNZ%2Fynw9HjKd2bI0CTme%5CDYJx0kq9dUNw0WT69gIlribJDrPhakkGLE3dJngZknxj3St1tvMg1zwmZ14n1YIBjl7EV0V%2FL8vTXvu%2Blhg6Me2viLibCL6ada1%2B5JuPLVnnim947Ixx81z6yvX%3A1635464169503; _9755xjdesxxd_=32; YD00517437729195%3AWM_NI=xCI3%2F7LkD5REF8HZ6FZrHK0ciEWJHD0nAGws847KFQzucRMZGmHATBT47ddIidFr%2Bhthed4Z6%2FV2B7s%2BUZHPpvAYzsBjak8YWBbbbkgLBayv%2BtkgLqBF7oqhHz4U5cS6Yjg%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eea7f96bae9eb7b2d561aeef8ea6c45e978b8faaf87c8d8d99a8b14693e8fe95e72af0fea7c3b92abc9d87d4ae3d90b58cd6d14f86e888bbb54e9aae88acb369ab9b99abcb50f4b28fa8f679fcecf9acc55bbaabadb3d05285b388a2d74a98ecf985e743abbc8a93aa64b8b8ab85b752f6f19ad3c13db1f59bbbcb5cb4aa8fbaf97982b6af8cbb53959eae83e161a5948e82fc7ee9aca588cf7b829af990f4648ca6fcb6b86991ea978be637e2a3; YD00517437729195%3AWM_TID=a7e2QapBpLFEBVQFEBYuoMYJSOSUG04Q; _xsrf=vvS28v5MlGmBQjClTnGZdulMrSCMTRlD; __snaker__id=jbRqAqaflv9uCokh; captcha_ticket_v2="2|1:0|10:1635463331|17:captcha_ticket_v2|704:eyJ2YWxpZGF0ZSI6IkNOMzFfaUhlZ2k1dzV6bmxKZ0NrTkVtX2ZNUU1JVkxTWUFaREpBOFhHRGVfcWNFTkxZQ20xMXl5T0pGcGlCLTJfbWIwbmNTRnk1N0pFS2ZwZndyUTRBV1hMUmFmbllraEJlQlI3a2l2WUpibFU3ZmhCOW5DaTVwLXBBN2IxN2FiLUJRT0JUOEpiWkJWdlBjMHhrN1hZaHlGOXFhUEtfVzZ2Xy1CSnBXa1MyUWtCN1ZGZ2ZJWVUxTFBEcnZEWVpjakh1ZHNnQmxMTGhacVNmanZPdk02aWpGZ2VOZ3MuYktKVk1yakExWWlWam5sZ29qdS1ienJOVC5nMTdBYXZmdjV5b1BBeXlBOXNILkFnbEZHWG45V3NmampMdW50T0U5aGlJdEItSXM4dkxaY3FvVzYwYnhxa3JFWFRnQ0xUR2JYNDVkc05jVUlBVUtZOXE1UmNWLVNCUnlPLmdpbXJseno0T1V3dUFGVThUZkJCcmlrLTZRVUduLi1kOXBvaS5MQ29KcjQteVNvSXl0eVdqYVBYTW4wbHUyb1ZTLXAyVzZXSVdRT25PMlNMWER5djBKbS5STWV6MVItRFBfamdWLVJxRnZFQXJ4Um01Q1U2TWFXRk5IOUlqdnBrUUVqcVpmUWxDc2NIMnktZGR0TE9EeW96MVlLZjliS2w4MmNZd3Z6MyJ9|d3fd91e6f77d5d27a5634181b488669b149f7f76b10340a0e16029cea28afaa6"; z_c0="2|1:0|10:1635463332|4:z_c0|92:Mi4xeUZxUUVRQUFBQUFBNEY3ZXlKN2tFeVlBQUFCZ0FsVk5wSDVvWWdBNkxGS1VZQV9CYkF1X1hWd180R2w2U3dqOUpB|0744a0a6dc07bc9d6baf2b08292b7a90fd358cfb748cceab8ae443aac9c87811"; NOT_UNREGISTER_WAITING=1; KLBRSID=4efa8d1879cb42f8c5b48fe9f8d37c16|1636011329|1636011273; tst=r; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1636011329; SESSIONID=FSW7Iyjp4dd8iIHY6RXk6hKLiOwK8DXcAxqI6bRIHkD; JOID=WlAQA0vPQYAmCzRcasdpEFzForB0iR_SEUpNOx_zJekbYnUUPs7EBk8DOVRvRXCHEh7U4PlGZE6kgLIaDKfVbWY=; osd=UVkUAU3ESIQkDT9VbsVvG1XBoLZ_gBvQF0FEPx31LuAfYHMfN8rGAEQKPVZpTnmDEBjf6f1EYkWthLAcB67Rb2A=',
                }
                url = "https://www.zhihu.com/api/v4/search_v3?"
                params = {
                    "t": "general",
                    "q": word,
                    "correction": 1,
                    "offset": 20*i,
                    "limit": 20,
                    "filter_fields": "",
                    "lc_idx": 0,
                    "show_all_topics": 0,
                }
                url += urlencode(params)
                yield scrapy.Request(url, callback=self.parse, headers=headers, cookies=cookies, cb_kwargs={"state": "initial"})

    def parse(self, response, **kwargs):
        if "state" in kwargs:
            res = json.loads(response.text)
            for item in res["data"]:
                if "object" in item and "url" in item["object"]:
                    yield scrapy.Request(item["object"]["url"], callback=self.parse)
        else:
            comps = response.url.split("/")
            filename = comps[-2]+comps[-1]
            try:
                json.loads(response.text)
            except ValueError:
                filename+=".html"
            else:
                filename+=".json"
            with open("target/zhihu/"+filename, "wb") as fd:
                fd.write(response.body)
            self.log(f"saved file {filename}")
