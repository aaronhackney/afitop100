from unittest import TestCase
from afitop100.afi import AFITop100


class TestAFITop100(TestCase):
    def setUp(self):
        self.afitop100 = AFITop100()

    def test_get_top_100_of_all_time(self):
        self.afitop100.get_afi_all_time()
        self.assertGreater(len(self.afitop100.afi_list), 99)
