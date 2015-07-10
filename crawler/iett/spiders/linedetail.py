# -*- coding: utf-8 -*-
import json
import scrapy
from iett.items import LineDetailItem, StopItem
from os.path import join, dirname
import iett

import csv

class LinedetailSpider(scrapy.Spider):
    name = "linedetail"
    allowed_domains = ["apicitysdk.ibb.gov.tr"]
    start_urls = [
    #    'http://apicitysdk.ibb.gov.tr/gtfs.line.1.98t-0/select/nodes?per_page=200&geom',
    ]

    def __init__(self):
        filename = join(dirname(iett.__file__), "resources", "bus_lines.csv")

        with open(filename, "rb") as csvfile:
            reader = csv.reader(csvfile, delimiter=",", quotechar='"')
            colnames = reader.next()
            cdk_index = colnames.index("cdk_id")
            template = 'http://apicitysdk.ibb.gov.tr/%s/select/nodes?per_page=200&geom'
            urls = []
            #i = 0
            for row in reader:
                urls.append(template % row[cdk_index])
                #i+=1
                #if i==3:
                #    break
            self.start_urls.extend(urls)
            print self.start_urls

    def parse(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        next_page = jsonresponse["next_page"]
        if next_page != -1:
            print "Could not get it."
        else:
            # do as normal
            results = jsonresponse["results"]

            # Line Detail (cdk_id and stop list)
            line_detail = LineDetailItem()

            cdk_id = response.url.split("/")[3]
            line_detail["cdk_id"] = cdk_id
            stop_list = ";".join([stop["cdk_id"] for stop in results])
            line_detail["stop_list"] = stop_list

            yield line_detail

            for stop in results:
                stop_item = StopItem()
                stop_item["layer"] = stop["layer"]
                stop_item["cdk_id"] = stop["cdk_id"]
                stop_item["node_type"] = stop["node_type"]
                stop_item["name"] = stop["name"]

                lon, lat = stop["geom"]["coordinates"]
                stop_item["lat"] = lat
                stop_item["lon"] = lon

                yield stop_item
