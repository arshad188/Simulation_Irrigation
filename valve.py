"""valve.py — the water inlet valve. Tracks its own state and remembers
every time it was switched, which is handy for reviewing what the system
did after the fact."""


class Valve:
    def __init__(self):
        self.is_open = False
        self.log = []   # list of (step_number, "OPEN" | "CLOSE")

    def open(self, step):
        if not self.is_open:
            self.is_open = True
            self.log.append((step, "OPEN"))

    def close(self, step):
        if self.is_open:
            self.is_open = False
            self.log.append((step, "CLOSE"))
