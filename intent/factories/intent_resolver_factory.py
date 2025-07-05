from intent.strategies.dance_intent_strategy import DanceIntentStrategy
from intent.resolvers.intent_resolver import IntentResolver

def get_intent_resolver() -> IntentResolver:
    strategies = [
        DanceIntentStrategy(),
    ]
    return IntentResolver(strategies)