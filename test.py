import pytest

from engine import generator
from engine import varification
from engine import util


class TestPasswordGenerator:
    """
    def test_password_length(self):
        length = 4
        gen = generator.Generator(length, ['alpha', 'numeric', 'special'])
        for i in range(100):
            password = gen.generate()
            assert len(password) == length

        length = 10
        gen = generator.Generator(length, ['alpha', 'numeric', 'special'])
        for i in range(100):
            password = generator.generate()
            assert len(password) == length

    """
    """
    def test_length(self):
        length = 7
        generator = engine.Generator(length, ['alpha', 'numeric', 'special'])
        for i in range(100):
            password = generator.generate()
            ve = vengine.Varification(password)
            assert ve.varify()['length'] == vengine.PasswordLength.SHORT

        length = 8
        generator = engine.Generator(length, ['alpha', 'numeric', 'special'])
        for i in range(100):
            password = generator.generate()
            ve = vengine.Varification(password)
            assert ve.varify()['length'] == vengine.PasswordLength.LONG

    def test_strength_vstrong(self):
        generator = engine.Generator(16, ['alpha', 'numeric', 'special'])
        for i in range(1000):
            password = generator.generate()
            print(f"password: {password}")
            ve = vengine.Varification(password)
            assert ve.varify()['strength'] == vengine.PasswordStrength.VSTRONG

    """

    def test_strength_strong(self):
        for i in range(1):
            gen = generator.Generator(16, ['alpha', 'numeric'])
            password = gen.generate()
            ve = varification.Varification(password)
            assert ve.varify()['strength'] == util.PasswordStrength.STRONG

    def test_strength_weak(self):
        gen = generator.Generator(16, ['alpha'])
        for i in range(10):
            password = gen.generate()
            ve = varification.Varification(password)
            assert ve.varify()['strength'] == util.PasswordStrength.WEAK
