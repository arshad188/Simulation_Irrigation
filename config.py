"""config.py — all tunable numbers for the irrigation simulation live here,
so you can experiment without touching the logic in the other modules."""


class Config:
    # Soil moisture thresholds (%)
    MOISTURE_LOW = 30      # below this while dry -> open the valve
    MOISTURE_HIGH = 60     # above this while watering -> close the valve

    # Air humidity threshold (%)
    HUMIDITY_HIGH = 70     # very humid air -> don't water even if soil is dry

    # How fast things change per simulation step
    IRRIGATION_RATE = 4.0    # % moisture gained per step while valve is open
    EVAPORATION_BASE = 1.5   # % moisture lost per step at 0% humidity

    # Simulation length / pacing
    TOTAL_STEPS = 60
    STEP_DELAY_SECONDS = 0.15   # only used by the browser/Pyodide animation
