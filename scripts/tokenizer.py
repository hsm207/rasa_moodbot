from typing import List, Text, Tuple

from rasa.nlu.constants import TOKENS_NAMES
from rasa.nlu.tokenizers.tokenizer import Token
from rasa.nlu.tokenizers.whitespace_tokenizer import WhitespaceTokenizer
from rasa.shared.nlu.constants import (ACTION_NAME, ACTION_TEXT, INTENT,
                                       INTENT_NAME_KEY, INTENT_RESPONSE_KEY,
                                       RESPONSE, TEXT)
from rasa.shared.nlu.training_data.message import Message
from rasa.shared.nlu.training_data.training_data import TrainingData

text = "Excuse me, where is your name?"

tk = WhitespaceTokenizer()
message = Message.build(text=text)
tokens = tk.tokenize(message, attribute=TEXT)

print(f"The tokens are: {[t.text for t in tokens]}")
