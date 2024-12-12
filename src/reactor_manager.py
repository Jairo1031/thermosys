from .reactor import Reactor


class ReactorManager:
    def __init__(self):
        self.reactors = []

    def add_reactor(self, reactor):
        self.reactors.append(reactor)

    def get_all_reactors(self):
        return [reactor.get_status() for reactor in self.reactors]

    def get_all_reactors_with_recommendations(self):
        return [{
            **reactor.get_status(),
            'recommendations': reactor.generate_recommendations()
        } for reactor in self.reactors]

    def find_reactor_by_name(self, name):
        for reactor in self.reactors:
            if reactor.name == name:
                return reactor  # Return the Reactor object, not its status
        return None

    def save_reactors_to_file(self, filename):
        import json
        with open(filename, 'w') as file:
            json.dump([reactor.get_status()
                      for reactor in self.reactors], file, indent=4)

    def search_reactors_by_temperature(self, min_temp, max_temp):
        return [reactor.get_status() for reactor in self.reactors if min_temp <= reactor.temperature <= max_temp]

    def sort_reactors_by_power(self):
        self.reactors.sort(
            key=lambda reactor: reactor.power_output, reverse=True)
