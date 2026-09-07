"""controller.py — decides whether the valve should be open or closed by
comparing the moisture and humidity readings against the thresholds in
Config. Uses hysteresis (different thresholds for opening vs. closing) so
the valve doesn't flicker open/close every step near a single cutoff.
"""


class IrrigationController:
    def __init__(self, config):
        self.config = config

    def decide(self, moisture, humidity, valve_is_open):
        """Return True if the valve should be open, False if closed."""
        cfg = self.config

        if not valve_is_open:
            # Currently closed: only start watering if soil is clearly dry
            # AND the air isn't humid enough to do the job for us.
            if moisture < cfg.MOISTURE_LOW and humidity < cfg.HUMIDITY_HIGH:
                return True
            return False

        # Currently open: keep watering until the soil is clearly wet
        # enough, or stop early if the air turns humid (less evaporation,
        # less need to keep adding water).
        if moisture > cfg.MOISTURE_HIGH or humidity > cfg.HUMIDITY_HIGH:
            return False
        return True
