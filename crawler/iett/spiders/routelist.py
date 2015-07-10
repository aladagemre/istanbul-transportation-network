# -*- coding: utf-8 -*-
import scrapy
import json
from iett.items import LineListingItem


class LineListSpider(scrapy.Spider):
    name = "linelist"
    allowed_domains = ["apicitysdk.ibb.gov.tr"]
    start_urls = (
        'http://apicitysdk.ibb.gov.tr/ptlines?per_page=1000&page=1',
    )

    def parse(self, response):
        jsonresponse = json.loads(response.body_as_unicode())

        results = jsonresponse["results"]
        for row in results:
            item = LineListingItem()
            for field in ["cdk_id", "name", "node_type", "layer"]:
                item[field] = row[field]


            cols = row["name"].split()

            if len(cols) > 3:
                name = " ".join(cols[2:])
                item["clear_name"] = name
                item["type"] = cols[1]

            elif len(cols) == 3:
                item["code"] = cols[2]
                item["type"] = cols[1]

            yield item
