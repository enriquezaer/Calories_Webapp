import requests
from selectorlib import Extractor


class Temperature:
    base_url = "https://www.timeanddate.com/weather/"
    yml_path = "temperature.yaml"

    def __init__(self, country, location):
        self.location = location.replace(" ", "-")
        self.country = country.replace(" ", "-")

    def _build_url(self):
        url = self.base_url + self.country + "/" + self.location
        return url

    def _scrape(self):
        url = self._build_url()
        extractor = Extractor.from_yaml_file(self.yml_path)
        r = requests.get(url)
        full_content = r.text
        raw_content = extractor.extract(full_content)
        return raw_content

    def get(self):
        return float(self._scrape()["temp"].replace('°C', '').strip())


if __name__ == "__main__":
    temperature = Temperature(country="honduras", location="tegucigalpa")
    print(temperature.get())
