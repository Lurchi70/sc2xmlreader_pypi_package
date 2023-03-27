# Abstract
The `sc2xmlreader` allows to query the XML data interface of the solvis remote extension of a Solvis Heating system with a 
solvis control 2 board. The XML Interface provides a read-only access. Controlling the heating system is not possible.

SC2XMLReader returns the data and states of the Solvis Heating device.
The xml-file is public and can be retrieved via http://<your-device-ip>/sc2_val.xml

When querying this interface remote will return something like: 
```
<xml>
  <data>
    AA5555AA056B0C31350600120076028A013A018[...]0000000000
  </data>
</xml>
```
the returned payload data has a length of 439 Bytes in an coded format. 
At this point, many thanks to all the other persons that have decoded this format in the past and shared their insights.

## Interface
To verify your hostname and user credentials and get the correct url:
 ```
[...]
    from sc2xmlreader.sc2xmlreader_validator import SC2XMLReaderValidator

    [...]

    try:
        my_sc2_credential_validator = SC2XMLReaderValidate("hostname", "username", "password")
    except ConnectionError as err:
        # my be the hostname / ip is not correct
    except AuthenticationError as err:
        # my be the hostname / ip is not correct

    correct_url = my_sc2_credential_validator.url
```

To query data from solvis remote: 
```
    from sc2xmlreader.sc2xmlreader import SC2XMLReader

    [...]
    
    try:
        my_sc2_reader = SC2XMLReader(correct_url, "username", "password")
        the_solar_power = my_sc2_reader.data["solar_power"]
    except ConnectionError as err:
        # may be the hostname / ip is not correct
```

## Exceptions generated
- Alle kinds of exceptions from "requests" package
- ConnectionError - hostname wrong or solvis remote does not answer as expected
- AuthenticationError - User and/or password incorrect

## Hint
Before being able to use the integration, you have to own a solvis remote device and have it attached, configured and available in your network. 
To retrieve the xml interface, a username and password must be provided.   

## Sensor data provided
The following sensors are available in the data:

| key | name                         | Unit   | Description   |
|-----|------------------------------|--------|:-------------------------------------------|
| time| last_update                  |        | Timestamp of latest data update.                |
| Z4  | runtime_solar_pump           | h      | Total output runtime of the solar pump. |
| SL  | solar_power                  | W      | Current solar power from the solar panels. |
| S7  | solar_pressure               | bar    | Current pressure in the solar pipes. |
| SE  | solar_yield                  | kWh    | Total yield of the solar panels to the heating system |
| S1  | temperature_buffer_top       | °C     | current temperature in the buffer top |
| S3  | temperature_buffer_reference | °C     | current reference temperature in the buffer |
| S4  | temperature_H_buffer_top     | °C     | current temperature in the heating buffer top |
| S9  | temperature_H_buffer_bottom  | °C     | current temperature in the heating buffer bottom |
| S2  | temperature_warm_water_station | °C     | current temperature warm water station |
| S11 | temperature_circulation      | °C     | current temperature warm water circulation |
| S12 | temperature_heating_circuit_1_flow | °C     | current flow temperature heating circuit 1 |
| S13 | temperature_heating_circuit_2_flow | °C     | current flow temperature heating circuit 2 |
| S10 | temperature_outside          | °C     | current temperature out the building |
| S5  | temperature_solar_flow       | °C     | current flow temperature of solar heating  |
| S8  | temperature_solar_panel      | °C     | current temperature on the solar panel(s)  |
| S16 | temperature_solar_panel2     | °C     | current temperature on the solar2 panel(s) (if east/ west option) |
| S16 | temperature_oven             | °C     | current temperature on the solar2 panel(s) (if oven option) |
| S6  | temperature_solar_return     | °C     | current return temperature of solar heating  |
| S17 | volume_solar_pump            | l/h    | current volume of fluid stream in solar heating  |
| S18 | volume_warm_water            | l/min  | current volume of fluid stream in warm water station  |

## Binary states
The following binary states are available in the data:

|     | name                         | Description   |
|-----|------------------------------|:-------------------------------------------|
| A12 | burner                       | oil/gas burner started. |
| A13 | burner_s2                    | oil/gas s2 burner started |
| A5  | circulation_pump             | warm water circulation pump running |
| A8  | heating_circuit_1_mixer_open | indicates that the heating circuit 1 increases the flow temperature |
| A9  | heating_circuit_1_mixer_close| indicates that the heating circuit 1 decreases the flow temperature |
| A3  | heating_circuit_1_pump       | heating circuit 1 pump is running |
| A10 | heating_circuit_2_mixer_open | indicates that the heating circuit 2 increases the flow temperature |
| A11 | heating_circuit_2_mixer_close| indicates that the heating circuit 2 decreases the flow temperature |
| A4  | heating_circuit_2_pump       | heating circuit 2 pump is running |
| A6  | heating_circuit_3_pump       | heating circuit 3 pump is running |
| A14 | recovery                     | recovery is active |
| A1  | solar_pump                   | solar pump is active |
| A7  | solar_pump_2                 | second solar pump is active |
| A2  | warm_water_station_pump      | warm water station pump is started |
  
## Trademarks
Solvis is a registered trademark of Solvis GmbH, Braunschweig (www.solvis.de)
