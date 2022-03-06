#!/usr/bin/env python
# coding: utf-8

# In[97]:


from typing import List
from textdistance import hamming
from textdistance import bag
from numpy.random import randint


# In[98]:


def bullscows(guess: str, secret: str) -> (int, int):
    l = len(guess)
    bulls = l - hamming(guess, secret[0:l])
    cows = max(0, l - bag(guess, secret[0:l]) - bulls)
    return (bulls, cows)


# In[99]:


def ask(prompt: str, valid: List[str] = None) -> str:
    print(prompt)
    inp = str(input())
    if valid is None:
        return inp
    else:
        while inp not in valid:
            print(prompt)
            inp = str(input())
    return inp


# In[100]:


def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))


# In[101]:


def gameplay(ask: callable, inform: callable, words: List[str]) -> int:
    secret = words[randint(0, len(words))]
    num_ask = 0
    while 1:
        secret_len = len(secret)
        guess = ask("Введите слово: ", words)
        num_ask += 1
        bulls, cows = bullscows(guess, secret)
        inform("Быки: {}, Коровы: {}", bulls, cows)
        if bulls == secret_len:
            return num_ask


# In[ ]:




