"""sensors.py — simulated soil moisture and air humidity sensors.

Real sensors would read hardware; these generate believable values so the
rest of the system (controller, valve, simulation loop) can be built and
tested without any physical hardware attached.
"""

import random


class MoistureSensor:
    """Soil moisture, as a percentage (0 = bone dry, 100 = saturated)."""

    def __init__(self, initial=45.0):
        self.value = initial

    def read(self):
        """Return a noisy reading, like a real sensor would give."""
        return round(self.value + random.uniform(-0.5, 0.5), 1)

    def apply_irrigation(self, amount):
        self.value = min(100.0, self.value + amount)

    def apply_evaporation(self, amount):
        self.value = max(0.0, self.value - amount)


class HumiditySensor:
    """Air humidity, as a percentage (0 = bone dry air, 100 = saturated air)."""

    def __init__(self, initial=50.0):
        self.value = initial

    def read(self):
        return round(self.value + random.uniform(-1.0, 1.0), 1)

    def drift(self):
        """Slow random walk, standing in for changing weather."""
        self.value = min(100.0, max(0.0, self.value + random.uniform(-2, 2)))
