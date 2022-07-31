import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    """тест нового посителя"""

    def setUp(self):
        """установка"""
        self.browser = webdriver.Firefox()

    def tearDown(self):
        """демонтаж"""
        self.browser.quit()

    def test_can_start_a_list_and_retrive_it_later(self):
        """тест: можно начать список и получить его позже"""
        self.browser.get('http://localhost:8000')

        # Заголовок и шапка страницы говорят о списках неотложных дел
        self.assertIn('To-Do', self.browser.title)
        self.fail('Закончить тест!')

        # Предлагается ввести элелемент списка...

if __name__ == '__main__':
    unittest.main()
