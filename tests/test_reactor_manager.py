import unittest
import json
import os
from src.reactor import Reactor
from src.reactor_manager import ReactorManager


class TestReactorManager(unittest.TestCase):
    def setUp(self):
        self.manager = ReactorManager()
        self.reactor1 = Reactor("Reactor1", 100, 300, 15)
        self.reactor2 = Reactor("Reactor2", 80, 320, 16)
        self.manager.add_reactor(self.reactor1)
        self.manager.add_reactor(self.reactor2)

    def test_add_reactor(self):
        self.assertEqual(len(self.manager.reactors), 2)

    def test_get_all_reactors(self):
        reactors = self.manager.get_all_reactors()
        self.assertEqual(len(reactors), 2)
        self.assertEqual(reactors[0]["name"], "Reactor1")
        self.assertEqual(reactors[1]["name"], "Reactor2")

    def test_find_reactor_by_name(self):
        reactor = self.manager.find_reactor_by_name("Reactor1")
        self.assertEqual(reactor["name"], "Reactor1")
        self.assertIsNone(
            self.manager.find_reactor_by_name("NonexistentReactor"))

    def test_sort_reactors_by_power(self):
        self.manager.sort_reactors_by_power()
        reactors = self.manager.get_all_reactors()
        self.assertEqual(reactors[0]["name"], "Reactor1")
        self.assertEqual(reactors[1]["name"], "Reactor2")

    def test_search_reactors_by_temperature(self):
        reactors = self.manager.search_reactors_by_temperature(290, 310)
        self.assertEqual(len(reactors), 1)
        self.assertEqual(reactors[0]["name"], "Reactor1")

    def test_save_reactors_to_file(self):
        filename = "test_reactors.json"
        self.manager.save_reactors_to_file(filename)
        self.assertTrue(os.path.exists(filename))
        with open(filename, "r") as file:
            data = json.load(file)
        self.assertEqual(len(data), 2)
        os.remove(filename)


if __name__ == '__main__':
    unittest.main()
