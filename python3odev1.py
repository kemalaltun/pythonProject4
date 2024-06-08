class WebPush:
    def __init__(self,platform,optin,global_frequency_capping, start_date, end_date, language, push_type):
        self.platform=platform
        self.optin=bool(optin)
        self.global_frequency_capping=global_frequency_capping
        self.start_date=start_date
        self.end_date=end_date
        self.language=language
        self.push_type=push_type
    def sendPush(self):
        return f"{self.platform,self.optin,self.global_frequency_capping, self.start_date, self.end_date, self.language, self.push_type} push gönderildi"

class TriggerPush(WebPush):
    def __init__(self,platform,optin,global_frequency_capping, start_date, end_date, language, push_type,triggerPage):
        super().__init__(platform,optin,global_frequency_capping, start_date, end_date, language, push_type)
        self.triggerPage=str(triggerPage)

class BulkPush(WebPush):
    def __init__(self,platform,optin,global_frequency_capping, start_date, end_date, language, push_type,sendDate):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.sendDate=int(sendDate)

class SegmentPush(WebPush):
    def __init__(self,platform,optin,global_frequency_capping, start_date, end_date, language, push_type,segmentName):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.segmentName=str(segmentName)

class PriceAlertPush(WebPush):
    def __init__(self,platform,optin,global_frequency_capping, start_date, end_date, language, push_type, priceInfo, discountRate):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.priceInfo=int(priceInfo)
        self.discountRate=float(discountRate)

    def discountPrice(self,priceInfo,discountRate):
        self.priceInfo=priceInfo
        self.discountRate=discountRate
        return priceInfo*(discountRate/100)

class InstockPush(WebPush):
    def __init__(self,platform,optin,global_frequency_capping, start_date, end_date, language, push_type, stockInfo):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.stockInfo=bool(stockInfo)

    def stockUpdate(self):
        self.stockInfo = not self.stockInfo
        return self.stockInfo

triggerPush1=TriggerPush("Mobile",True,2,100527,101527,"tr_TR","Trigger Push","Cart")
print(triggerPush1.sendPush())
bulkPush1=BulkPush("Web",True,2,100527,101527,"en_EN","Bulk Push",100527)
print(bulkPush1.sendPush())
segmentPush1=SegmentPush("Tablet",True,3,100527,101527,"en_EN","Segment Push","New Users")
print(segmentPush1.sendPush())
priceAlertPush1=PriceAlertPush("Mobile",True,2,100527,101527,"tr_TR","Price Alert Push",100,5.27)
print(priceAlertPush1.discountPrice(100, 5.27))
print(priceAlertPush1.sendPush())
instockPush1=InstockPush("Web",True,0,100347,102457,"ru_RU","In Stock Push",True)
print(instockPush1.sendPush())
print(instockPush1.stockUpdate())
print(instockPush1.stockUpdate())
