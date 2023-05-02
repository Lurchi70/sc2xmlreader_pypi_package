
from sc2xmlreader_dev.sc2xmlreader import SC2XMLReader
from sc2xmlreader_dev.const import DEFAULT_USERNAME, DEFAULT_PASSWORD

import pprint

class LocalDemo:    
    def __init__(self, url:str):
        self.url = url
        self.remote = SC2XMLReader(url, DEFAULT_USERNAME, DEFAULT_PASSWORD)


    def ShowSystemInfo(self):
        pprint.pprint("System Info ---------------------------")
        pprint.pprint("""   Manufacturer: {0}""".format(self.remote.manufacturer))
        pprint.pprint("""   Systemnummer: {0}""".format(self.remote.data["devicenumber"]["Value"]))
        pprint.pprint("""   Systemtype: {0}""".format(self.remote.data["devicetype"]["Value"]))

        pprint.pprint("""   Number of Burnerstart: {0} {1}""".format(self.remote.data["total_burner_start"]["Value"], self.remote.data["total_burner_start"]["Unit"]))
        pprint.pprint("""   Number of 2nd Burnerstart: {0} {1}""".format(self.remote.data["total_burner_2nd_start"]["Value"], self.remote.data["total_burner_2nd_start"]["Unit"]))
        pprint.pprint("""   Runtime Burner: {0} {1}""".format(self.remote.data["runtime_burner"]["Value"], self.remote.data["runtime_burner"]["Unit"]))
        pprint.pprint("""   Burner Capacity: {0} {1}""".format(self.remote.data["burner_capacity"]["Value"], self.remote.data["burner_capacity"]["Unit"]))
        pprint.pprint("""   Burner Consumption: {0} {1}""".format(self.remote.data["burner_consumption"]["Value"], self.remote.data["burner_consumption"]["Unit"]))
        pprint.pprint("""   Runtime Solarpump: {0} {1}""".format(self.remote.data["runtime_solar_pump"]["Value"], self.remote.data["runtime_solar_pump"]["Unit"]))

    def ShowSolarInfo(self):
        pprint.pprint("Solar Info ---------------------------")
        pprint.pprint("""   Solar Power: {0} {1}""".format(self.remote.data["solar_power"]["Value"], self.remote.data["solar_power"]["Unit"]))
        pprint.pprint("""   Solar Pump: {0} {1}""".format(self.remote.data["solar_pump"]["Value"], self.remote.data["solar_pump"]["Unit"]))
        pprint.pprint("""   Solar Temp Panel: {0} {1}""".format(self.remote.data["temperature_solar_panel"]["Value"], self.remote.data["temperature_solar_panel"]["Unit"]))
        pprint.pprint("""   Solar Temp Flow: {0} {1}""".format(self.remote.data["temperature_solar_flow"]["Value"], self.remote.data["temperature_solar_flow"]["Unit"]))
        pprint.pprint("""   Solar Temp Return: {0} {1}""".format(self.remote.data["temperature_solar_return"]["Value"], self.remote.data["temperature_solar_return"]["Unit"]))
        pprint.pprint("""   Solar Temp Diff: {0} {1}""".format(self.remote.data["temperature_solar_diff_flow_return"]["Value"], self.remote.data["temperature_solar_diff_flow_return"]["Unit"]))
        pprint.pprint("""   Buffer Temp Heat Top: {0} {1}""".format(self.remote.data["temperature_buffer_heating_top"]["Value"], self.remote.data["temperature_buffer_heating_top"]["Unit"]))
        pprint.pprint("""   Buffer Temp Ref: {0} {1}""".format(self.remote.data["temperature_buffer_reference"]["Value"], self.remote.data["temperature_buffer_reference"]["Unit"]))
        pprint.pprint("""   Volume Stream Solar: {0} {1}""".format(self.remote.data["volume_stream_solar"]["Value"], self.remote.data["volume_stream_solar"]["Unit"]))

    def ShowBufferInfo(self):
        pprint.pprint("Buffer Info ---------------------------")
        pprint.pprint("""   Buffer Temp Top: {0} {1}""".format(self.remote.data["temperature_buffer_top"]["Value"], self.remote.data["temperature_buffer_top"]["Unit"]))
        pprint.pprint("""   Buffer Temp Heat Top: {0} {1}""".format(self.remote.data["temperature_buffer_heating_top"]["Value"], self.remote.data["temperature_buffer_heating_top"]["Unit"]))
        pprint.pprint("""   Buffer Temp Heat Bottom: {0} {1}""".format(self.remote.data["temperature_buffer_heating_bottom"]["Value"], self.remote.data["temperature_buffer_heating_bottom"]["Unit"]))
        pprint.pprint("""   Buffer Temp Ref: {0} {1}""".format(self.remote.data["temperature_buffer_reference"]["Value"], self.remote.data["temperature_buffer_reference"]["Unit"]))
        pprint.pprint("""   Temp Outside: {0} {1}""".format(self.remote.data["temperature_outside"]["Value"], self.remote.data["temperature_outside"]["Unit"]))

    def ShowWarmWaterInfo(self):
        pprint.pprint("Warm Water Station Info ---------------")
        pprint.pprint("""   Warm Water Temp: {0} {1}""".format(self.remote.data["temperature_warm_water_station"]["Value"], self.remote.data["temperature_warm_water_station"]["Unit"]))
        pprint.pprint("""   Warm Water Circulation: {0} {1}""".format(self.remote.data["temperature_circulation"]["Value"], self.remote.data["temperature_circulation"]["Unit"]))
        pprint.pprint("""   Buffer Temp Heat Top: {0} {1}""".format(self.remote.data["temperature_buffer_heating_top"]["Value"], self.remote.data["temperature_buffer_heating_top"]["Unit"]))
        pprint.pprint("""   Buffer Temp Ref: {0} {1}""".format(self.remote.data["temperature_buffer_reference"]["Value"], self.remote.data["temperature_buffer_reference"]["Unit"]))
        pprint.pprint("""   Volume Stream Warm Water: {0} {1}""".format(self.remote.data["volume_stream_warm_water"]["Value"], self.remote.data["volume_stream_warm_water"]["Unit"]))
        pprint.pprint("""   Circulation Pump: {0} {1}""".format(self.remote.data["circulation_pump"]["Value"], self.remote.data["circulation_pump"]["Unit"]))

    def CheckElements(self):
        for value in self.remote.MAP_SOLVIS_TO_NAME.values():
            pprint.pprint(self.remote.data[value])

    def CheckSetups(self):
        o = SC2XMLReader(self.url, username=DEFAULT_USERNAME, password=DEFAULT_PASSWORD, withWarmWaterStation=False, withSolar=False)

        pprint.pprint("""Value = {0}""".format(o.get_value("temperature_buffer_top")))
        pprint.pprint("""Value = {0}""".format(o.get_value("volume_stream_warm_water")))
        pprint.pprint("""Value = {0}""".format(o.get_value("temperature_solar_panel")))

if __name__ == '__main__':
    o = LocalDemo('http://solvis.leu.loc')

    o.ShowSystemInfo()
    o.ShowSolarInfo()
    o.ShowBufferInfo()
    o.ShowWarmWaterInfo()
    o.CheckElements()
    o.CheckSetups()