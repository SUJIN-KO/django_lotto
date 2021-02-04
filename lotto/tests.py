from django.test import TestCase
from .models import GuessNumbers
# Create your tests here.

# Create your tests here.
class GuessNumbersTestCase(TestCase):
    def test_generate(self):
        g = GuessNumbers(name='Test numbers', text='selected numbers')
        g.generate() # GuessNumbers 클래스의 generate 함수를 실행
        print(g.update_date)
        print(g.lottos)
        # 참인지 확인하겠다
        self.assertTrue(len(g.lottos) > 20)
