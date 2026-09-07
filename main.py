"""main.py — run the irrigation simulation in a plain Python interpreter.

    python3 main.py

For the browser / Pyodide version with a live status panel, see
irrigation_pyodide.html instead — it uses the exact same logic.
"""

from config import Config
from sensors import MoistureSensor, HumiditySensor
from valve import Valve
from controller import IrrigationController
from simulation import Simulation


def print_step(step, moisture, humidity, valve_open):
    state = "OPEN  " if valve_open else "CLOSED"
    print(f"Step {step:3d} | Moisture: {moisture:5.1f}% | "
          f"Humidity: {humidity:5.1f}% | Valve: {state}")


def main():
    config = Config()
    sim = Simulation(
        config=config,
        moisture_sensor=MoistureSensor(initial=40.0),
        humidity_sensor=HumiditySensor(initial=45.0),
        valve=Valve(),
        controller=IrrigationController(config),
        on_step=print_step,
    )
    sim.run()
    print(f"\nValve switched {len(sim.valve.log)} times.")


if __name__ == "__main__":
    main()
