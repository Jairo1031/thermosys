import unittest
from src.reactor import Reactor


class TestReactor(unittest.TestCase):
    def setUp(self):
        self.reactor = Reactor("TestReactor", 100, 300, 15)

    def test_init(self):
        self.assertEqual(self.reactor.name, "TestReactor")
        self.assertEqual(self.reactor.power_output, 100)
        self.assertEqual(self.reactor.temperature, 300)
        self.assertEqual(self.reactor.pressure, 15)

    def test_update_status(self):
        self.reactor.update_status(power_output=110, temperature=310)
        self.assertEqual(self.reactor.power_output, 110)
        self.assertEqual(self.reactor.temperature, 310)
        self.assertEqual(self.reactor.pressure, 15)

    def test_get_status(self):
        status = self.reactor.get_status()
        self.assertEqual(status, {
            "name": "TestReactor",
            "power_output": 100,
            "temperature": 300,
            "pressure": 15
        })


if __name__ == '__main__':
    unittest.main()
