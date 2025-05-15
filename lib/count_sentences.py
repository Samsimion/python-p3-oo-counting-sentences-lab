#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value =""):
        self.value = value
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self,value):
        if isinstance(value,str):
            self._value = value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        if self._value.endswith("."):
            return True
        else:
            return False
        
    def is_question(self):
        if self._value.endswith("?"):
            return True
        else:
            return False
        
    def is_exclamation(self):
        if self._value.endswith("!"):
            return True
        else:
            return False
        
    def count_sentences(self):
        cuts = re.split(r'[!.?]', self._value)
        sentences = [s for s in cuts if s.strip()]
        return len(sentences)
        
        
