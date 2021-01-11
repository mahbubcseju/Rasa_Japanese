import re
from typing import Any, List, Text

from rasa.nlu.components import Component
from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.tokenizers import Token, Tokenizer
from rasa.nlu.training_data import Message, TrainingData
import MeCab

class JapaneseTokenizer(Tokenizer, Component):

    provides = ["tokens"]

    def train(
        self, training_data: TrainingData, config: RasaNLUModelConfig, **kwargs: Any
    ) -> None:

        for example in training_data.training_examples:
            example.set("tokens", self.tokenize(example.text))

    def process(self, message: Message, **kwargs: Any) -> None:

        message.set("tokens", self.tokenize(message.text))

    @staticmethod
    def tokenize(text: Text) -> List[Token]:

        mt = MeCab.Tagger()
        parsed = mt.parse(text)
        # parsed returns token => POS separated by tab in multiple lines
        x = (parsed.replace('\n', '\t').split('\t'))
        words = []
        for i in range(0, len(x) - 2, 2):
            w = x[i]
            words.append(w)

        running_offset=0
        tokens = []
        for word in words:
            word_offset = text.find(word, running_offset) # origin-> text.index
            word_len = len(word)
            running_offset = word_offset + word_len
            tokens.append(Token(word, word_offset))
        return tokens



