class Reactor:
    def __init__(self, name, power_output, temperature, pressure):
        self.name = name
        self.power_output = power_output
        self.temperature = temperature
        self.pressure = pressure

    def update_status(self, power_output=None, temperature=None, pressure=None):
        if power_output is not None:
            self.power_output = power_output
        if temperature is not None:
            self.temperature = temperature
        if pressure is not None:
            self.pressure = pressure

    def get_status(self):
        return {
            "name": self.name,
            "power_output": self.power_output,
            "temperature": self.temperature,
            "pressure": self.pressure
        }

    def generate_recommendations(self):
        recommendations = []
        if self.temperature > 300:
            recommendations.append("Reduce reactor temperature")
        if self.pressure > 15:
            recommendations.append("Reduce reactor pressure")
        if self.power_output < 50:
            recommendations.append("Increase power output")
        return recommendations
