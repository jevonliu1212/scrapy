# scrapy
- scrapy startproject 项目名(生成项目)

- 完善spider,定义爬取的地址以及生成item

-item生成后会送到pipleline,保存数据库的逻辑可以写在这里

-要启用pipeline需要配置setting，如：
``` python
ITEM_PIPELINES = {
    'mySpider.pipelines.MyspiderPipeline': 300
}
```

- scrapy crawl 爬虫名(运行爬虫)
