from api.steady.models.prompt import Prompt
from api.steady.models.entry import Entry
from unittest import TestCase
from faker import Factory


class EntryTest(TestCase):
    def setUp(self):
        self.faker = Factory.create()

    def test_properties(self):
        score = 1
        prompt = Prompt()
        entry = Entry()
        entry.prompt = prompt
        prompt_text = self.faker.sentence()
        prompt.text = prompt_text
        entry.score = score
        self.assertEquals(entry.prompt, prompt)
        self.assertEquals(entry.prompt.text, prompt_text)
        self.assertEquals(entry.score, score)
