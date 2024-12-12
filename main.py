from src.reactor import Reactor
from src.reactor_manager import ReactorManager
import json


def load_reactor_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def main():
    # Load reactor data
    reactor_data = load_reactor_data('data/reactor_data.json')

    # Create ReactorManager instance
    manager = ReactorManager()

    # Add reactors to the manager
    for data in reactor_data:
        reactor = Reactor(**data)
        manager.add_reactor(reactor)

    # Display all reactors
    print("All Reactors:")
    for reactor in manager.get_all_reactors():
        print(reactor)

    # Sort reactors by power and display
    manager.sort_reactors_by_power()
    print("\nReactors sorted by power:")
    for reactor in manager.get_all_reactors():
        print(reactor)

    # Search reactors by temperature range
    temp_range_reactors = manager.search_reactors_by_temperature(300, 310)
    print("\nReactors with temperature between 300 and 310:")
    for reactor in temp_range_reactors:
        print(reactor)

    # Save reactors to a file
    manager.save_reactors_to_file("data/updated_reactors.json")
    print("\nReactors saved to 'data/updated_reactors.json'")


if __name__ == "__main__":
    main()
