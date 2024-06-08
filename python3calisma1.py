class Library:
    def __init__(self,name,location):
        self.name=name
        self.location=location
class Personel(Library):
    def __init__(self,name,location,age):
        super().__init__(name,location)
        self.age=age
    def __str__(self):
        return f"{self.name}+{self.location}+{self.age}"

personel1=Personel("kemal","Kırıkkale",23)
print(personel1)

class WebPush:
    def __init__(self,platform,optin,global_frequency_capping, start_date, end_date, language, push_type):
        self.platform=platform
        self.optin=bool(optin)
        self.global_frequency_capping=global_frequency_capping
        self.start_date=start_date
        self.end_date=end_date
        self.language=language
        self.push_type=push_type


