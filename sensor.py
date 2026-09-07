sim = Simulation(
    config=config,
    moisture_sensor=MoistureSensor(initial=40.0),
    humidity_sensor=HumiditySensor(initial=45.0),
    valve=Valve(),
    controller=IrrigationController(config),
    on_step=print_step,
)