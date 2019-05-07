import unittest
import random
import os
import json

from l1_2 import generator
from l1_2 import controller

random.seed()


class TestController(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.path = str(random.random())[2:] + '.json'
        width = random.randint(1, 10)
        height = random.randint(1, 10)
        frames = random.randint(5, 20)
        generator.generate(cls.path, 100, 100, 50)

    def test_animation(self):
        with open(self.path) as f:
            j = json.load(f)

        a = controller.Animation(self.path, 500000)

        self.assertEqual(j['width'], a.width)
        self.assertEqual(j['height'], a.height)
        self.assertEqual(j['frames'], a.frames)

        self.assertEqual(j['animation'], [*iter(a)])

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.path)
