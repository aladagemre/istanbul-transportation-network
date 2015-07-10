# City SDK API Crawler for Istanbul Bus Network

## Installing Dependencies

    cd crawler
    virtualenv --distribute venv
    . venv/bin/activate
    pip install -r requirements.txt

## Crawlera settings (Optional)

Crawlera allows using a proxy for crawling operation so that you are not banned from the system. Uncomment corresponding lines and enter your API key in settings.py for Crawlera. See more details on [Crawlera manual](http://doc.scrapinghub.com/crawlera.html#crawlera-scrapy-cloud).

## Running the crawler

First run **LineListSpider** to get the list of routes.

    scrapy crawl linelist -o iett/resources/linelist.csv

This will create a list of lines: iett/resources/linelist.csv. Some of the fields are not really needed. We conly need *code* and *cdk*. Run the following command:

    Rscript simplify_lines.r

and this will create a simplified bus line list: *iett/resources/bus_lines.csv*

----

Now we will scrape bus line details:

    scrapy crawl linedetail

This will produce linedetails.csv (bus stop sequence) and stops.csv (coordinates of the stops) in output folder.

----

Now we will visualize this.

## Visualization

Open *visualizer/istanbul-transportation-network.Rmd* in RStudio and press **Knit HTML** button to see the results.
