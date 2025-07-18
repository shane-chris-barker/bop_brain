from intent.strategies.angry_intent_strategy import AngryIntentStrategy
from intent.strategies.dance_intent_strategy import DanceIntentStrategy
from intent.resolvers.intent_resolver import IntentResolver
from intent.strategies.happy_intent_strategy import HappyIntentStrategy
from intent.strategies.love_intent_strategy import LoveIntentStrategy
from intent.strategies.sad_intent_strategy import SadIntentStrategy
from intent.strategies.weather_report_strategy import WeatherReportStrategy
from weather.client.open_meteo_client import OpenMeteoClient

def get_intent_resolver() -> IntentResolver:
    strategies = [
        DanceIntentStrategy(),
        HappyIntentStrategy(),
        AngryIntentStrategy(),
        SadIntentStrategy(),
        LoveIntentStrategy(),
        WeatherReportStrategy(client=OpenMeteoClient()),
    ]
    return IntentResolver(strategies)
