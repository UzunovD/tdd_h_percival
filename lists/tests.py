from django.test import TestCase


class SmokeTest(TestCase):
    """Тест на токсичность"""

    def test_math(self):
        """Тест: Неправильные математические рассчеты"""
        self.assertEqual(1 + 1, 3)
