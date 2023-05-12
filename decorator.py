from collections import deque

class Decoradora:
    @staticmethod
    def decorator(func):
        def cache(*args):
            cache.append(args)
            return func(*args)

        return cache


    def __init__(self):
        self.lista = deque()
cache = []


    @decorator
    def somar(self):
        print('Eu')


