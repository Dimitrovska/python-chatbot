import unittest
from nltk.chat.util import Chat, reflections

# Sample chatbot pairs (regex patterns and responses)
pairs = [
    [r"(.*)my name is (.*)", ["Hello %2, How are you today ?", ]],
    [r"bye", ["Bye for now. See you soon :) "]],
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)


class TestChatbot(unittest.TestCase):

    def test_my_name_is(self):
        # Directly test the response for "my name is john"
        response = chatbot.respond("my name is john")
        self.assertIn("Hello john, How are you today ?", response)

    def test_bye(self):
        # Directly test the response for "bye"
        response = chatbot.respond("bye")
        self.assertIn("Bye for now. See you soon :) ", response)


if __name__ == '__main__':
    unittest.main()
