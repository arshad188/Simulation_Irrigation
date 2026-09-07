"""simulation.py — ties the sensors, controller, and valve together and
steps the whole system forward in time."""


class Simulation:
    def __init__(self, config, moisture_sensor, humidity_sensor, valve,
                 controller, on_step=None):
        self.config = config
        self.moisture = moisture_sensor
        self.humidity = humidity_sensor
        self.valve = valve
        self.controller = controller
        self.on_step = on_step  # optional callback(step, moisture, humidity, valve_open)

    def step(self, step_number):
        # weather drifts a little every step
        self.humidity.drift()

        m = self.moisture.read()
        h = self.humidity.read()

        should_open = self.controller.decide(m, h, self.valve.is_open)
        if should_open and not self.valve.is_open:
            self.valve.open(step_number)
        elif not should_open and self.valve.is_open:
            self.valve.close(step_number)

        if self.valve.is_open:
            self.moisture.apply_irrigation(self.config.IRRIGATION_RATE)
        else:
            # humid air slows evaporation
            evap = self.config.EVAPORATION_BASE * (1 - h / 100 * 0.5)
            self.moisture.apply_evaporation(evap)

        if self.on_step:
            self.on_step(step_number, m, h, self.valve.is_open)

    def run(self, steps=None):
        steps = steps or self.config.TOTAL_STEPS
        for i in range(steps):
            self.step(i)
