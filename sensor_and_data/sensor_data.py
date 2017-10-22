from time import sleep
from MS5607 import MS5607
from MS5803_02BA import get_temp_pres

sensor = MS5607()
def get_alt():
    temperature = sensor.getDigitalTemperature()
    pressure = sensor.getDigitalPressure()
    converted = sensor.convertPressureTemperature(pressure, temperature)
    altitude = sensor.getMetricAltitude(converted, sensor.inHgToHectoPascal(31.13))
    return altitude

def get_data():
    data = get_temp_pres()
    data.append(get_alt())
    return data
