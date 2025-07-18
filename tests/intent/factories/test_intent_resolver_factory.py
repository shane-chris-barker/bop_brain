import unittest
from intent.factories.intent_resolver_factory import get_intent_resolver
from intent.resolvers.intent_resolver import IntentResolver

class TestIntentResolver(unittest.TestCase):
    def test_get_intent_resolver_returns_correct_instance(self):
        intent_resolver = get_intent_resolver()
        self.assertIsInstance(intent_resolver, IntentResolver)









