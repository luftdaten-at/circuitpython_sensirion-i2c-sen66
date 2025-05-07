> ⚠️ This is a modified and bundled version of the official Sensirion CircuitPython drivers.
> Original copyright (c) Sensirion AG.
> Modifications by Luftdaten.at, 2025.
> Licensed under the BSD 3-Clause License (see [LICENSE](LICENSE)).



# CircuitPython I2C Driver for Sensirion SEN66

This repository contains the CircuitPython driver to communicate with a Sensirion SEN66 sensor over I2C.

<img src="https://raw.githubusercontent.com/Sensirion/python-i2c-sen66/master/images/sen6x.png"
    width="300px" alt="SEN66 picture">


Click [here](https://sensirion.com/sen6x-air-quality-sensor-platform) to learn more about the Sensirion SEN66 sensor.



The default I²C address of [SEN66](https://www.sensirion.com/products/catalog/SEN66) is **0x6B**.



## Connect the sensor

<details><summary>Sensor pinout</summary>
<p>
<img src="https://raw.githubusercontent.com/Sensirion/python-i2c-sen66/master/images/sen6x-pinout.png"
     width="300px" alt="sensor wiring picture">

| *Pin* | *Cable Color* | *Name* | *Description*  | *Comments* |
|-------|---------------|:------:|----------------|------------|
| 1 | red | VDD | Supply Voltage | 3.3V ±5%
| 2 | black | GND | Ground |
| 3 | green | SDA | I2C: Serial data input / output | TTL 5V compatible
| 4 | yellow | SCL | I2C: Serial clock input | TTL 5V compatible
| 5 |  | NC | Do not connect | Ground (Pins 2 and 5 are connected internally)
| 6 |  | NC | Do not connect | Supply voltage (Pins 1 and 6 are connected internally)


</p>
</details>


## Example usage

See [example_usage_circuitpython_sen66.py](examples/example_usage_circuitpython_sen66.py)


## License

See [LICENSE](LICENSE).