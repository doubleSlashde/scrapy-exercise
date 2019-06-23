# -*- coding: utf-8 -*-

class AuthorNameProcessingPipeline(object):
    def process_item(self, item, spider):
        # split author name into forename and surname
        item["author_forename"] = item["author"].split()[0]
        item["author_surname"] =  item["author"].split()[1]
        return item
