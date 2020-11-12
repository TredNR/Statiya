from scrapy.item import Item, Field
 
class OrphanageItem(Item):
    id               = Field()
    region           = Field()
    district         = Field()
    type             = Field()
    name             = Field()
    post             = Field()
