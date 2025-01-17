"""NLP package for Python

>>> import nlp
>>> nlp.tokenize('Walking on sunshine!')
['walk', 'sunshine']
>>> [nlp.stem(word) for word in ['works', 'working', 'work']]
['work', 'work', 'work']
"""
# Документація до пакету NLP. Вона описує, як працюють функції `tokenize` та `stem`, наводячи приклади використання.


import re
# Імпорт модуля `re` для роботи з регулярними виразами.

from .stop_words import stop_words
# Імпорт списку стоп-слів із модуля `stop_words` у поточному пакеті.
# Стоп-слова – це загальновживані слова (на кшталт "a", "the"), які зазвичай ігноруються під час аналізу тексту.
from .sentences import sentencize  # noqa
# Імпорт функції `sentencize` з модуля `sentences`. 
# `# noqa` вказує лінтерам (наприклад, Flake8) ігнорувати цей рядок, навіть якщо функція не використовується.


__version__ = '0.1.0'
# Змінна, яка визначає версію пакету.



def stem(word):
    """Stem a word

    >>> stem('working')
    'work'
    >>> stem('works')
    'work'
    """
    return re.sub(r'(s|ing)$', '', word)
# Функція `stem` скорочує слово до його кореня.
# Використовується регулярний вираз для видалення суфіксів `s` або `ing` із кінця слова.



def tokenize(text):
    """Return list of tokens found in text

    >>> tokenize('Mary had a little lamb')
    ['mary', 'little', 'lamb']
    """
    tokens = []  # Ініціалізується порожній список для збереження токенів.
    for tok in re.findall('[a-zA-Z]+', text):  
        # Знаходить усі слова, що складаються тільки з літер (як великих, так і малих).
        tok = tok.lower()  
        # Приводить слово до нижнього регістру.
        tok = stem(tok)  
        # Застосовує функцію `stem` для отримання кореня слова.
        if tok and tok not in stop_words:  
            # Перевіряє, чи слово не є порожнім і не входить до списку стоп-слів.
            tokens.append(tok)  
            # Додає слово до списку токенів.
    return tokens
    # Повертає список токенів.

