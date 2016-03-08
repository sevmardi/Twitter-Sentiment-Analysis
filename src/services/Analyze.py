import re


class Analyze(object):
    def __init__(self):
        pass

    def word_in_text(word, text):
        word = word.lower()
        text = text.lower()
        match = re.search(word, text)
        if match:
            return True
        else:
            return False

    def extract_link(text):
        regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
        match = re.search(regex, text)
        if match:
            return match.group()
        return ''

    
