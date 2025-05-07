import board
import busio

import time
#from sensirion_i2c_driver import LinuxI2cTransceiver, I2cConnection, CrcCalculator
from sensirion_i2c_driver import I2cTransceiver,I2cConnection, CrcCalculator
from sensirion_driver_adapters.i2c_adapter.i2c_channel import I2cChannel
from sensirion_i2c_sen66.device import Sen66Device


SEN66_DEFAULT_ADDRESS = 0x6B


i2c = busio.I2C(scl=board.IO5, sda=board.IO4, frequency=20000)
i2c_transceiver = I2cTransceiver(i2c, SEN66_DEFAULT_ADDRESS)
channel = I2cChannel(
    I2cConnection(i2c_transceiver),
    slave_address=SEN66_DEFAULT_ADDRESS,
    crc=CrcCalculator(8, 0x31, 0xff, 0x0)
)

sen66_device = Sen66Device(channel)

sen66_device.device_reset()

serial_number = sen66_device.get_serial_number()

print(f'serial number: {serial_number}')

sen66_device.start_continuous_measurement()

try:
    time.sleep(1.0)
    data = sen66_device.read_measured_values()

    (
        mass_concentration_pm1p0,
        mass_concentration_pm2p5,
        mass_concentration_pm4p0,
        mass_concentration_pm10p0,
        humidity,
        temperature,
        voc_index,
        nox_index,
        co2
    ) = sen66_device.read_measured_values()

    print(f'''mass_concentration_pm1p0: {mass_concentration_pm1p0}
mass_concentration_pm2p5: {mass_concentration_pm2p5}
mass_concentration_pm4p0: {mass_concentration_pm4p0}
mass_concentration_pm10p0: {mass_concentration_pm10p0}
humidity: {humidity}
temperature: {temperature}
voc_index: {voc_index}
nox_index: {nox_index}
co2: {co2}''')

except BaseException:
    pass

sen66_device.stop_measurement()
