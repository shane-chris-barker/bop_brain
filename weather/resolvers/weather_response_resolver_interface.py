from bop_common.dtos.weather.weather_data_dto import WeatherDataDTO

class WeatherResponseResolverInterface:
    def resolve(self, raw: dict, location: str) -> WeatherDataDTO:
        raise NotImplementedError()
