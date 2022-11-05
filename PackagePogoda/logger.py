import requests
class logger():
    """Returns the dictionary full of weather information!"""
    def __init__(self,key:str,city_name:str) -> None:
        self._key = key
        self.city_name = city_name
        self._link = f"https://api.openweathermap.org/data/2.5/weather?q={self.city_name}&appid={self._key}"


    def __repr__(self) -> str:
        return "<class 'logger'>"
    def Api(self,item:str,*args):
        try:
            responce = requests.get(self._link).json()
            if(responce['cod'] == '404'):
                print(f"{self.city_name} was not found!")
            else:
                return responce[item]
        except KeyError as e:
            thing = ""
            for x in responce:
                thing = f"{thing},{x}"
            print(f"An error has occured: {e} doesn't exist, use for example:{thing}")