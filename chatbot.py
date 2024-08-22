"""nltk chat is a class for simple chatbots"""

"""Perform simple pattern matching on sentences typed by users, 
and respond with automatically generated sentences"""

from nltk.chat.util import Chat, reflections

""" Pairs is a list of regex-patterns and responses """
pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?", ]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you ", ]
    ],
    [
        r"(.*) your name ?",
        ["My name is thecleverprogrammer, but you can just call me robot and I'm a chatbot .", ]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well", "i am great !"]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind that", ]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that", "Alright, great !", ]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there", ]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse", ]

    ],
    [
        r"(.*)created(.*)",
        ["Dragana created me using Python's NLTK library ", "top secret ;)", ]
    ],
    [
        r"(.*) (location|city) ?",
        ['Pernik, Bulgaria', ]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2", "In %2 there is a 50% chance of rain", ]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ", ]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Biathlon", ]
    ],
    [
        r"who (.*) (Biathlete|Athlete)?",
        ["Dorothea Wierer"]
    ],
    [
        r"bye",
        ["Bye for now. See you soon :) ", "It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['That is nice to hear']
    ],
]

""" Reflections is a dictionary file that contains a set of input values and corresponding output values"""

print(reflections)

""" default message at the start of chat """
print("Hi, I'm thecleverprogrammer and I like to chat\nPlease type lowercase English language to start a conversation. Type bye to leave ")

""" Create Chat Bot """
chat = Chat(pairs, reflections)

""" Start conversation """
chat.converse()