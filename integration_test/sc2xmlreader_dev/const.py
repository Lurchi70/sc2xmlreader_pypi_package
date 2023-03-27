"""Constants for sc2reader package"""
from __future__ import absolute_import
from enum import Enum

# Default config for Solvis Remote.
DEFAULT_USERNAME = "solvis"
DEFAULT_PASSWORD = "solvis"
HEATING_MANUFACTURER = "Solvis"

class VIA_DEVICE(Enum): 
                XML = 1, 
                ModBus = 2

class HEATING_DEVICE_TYPE(Enum): 
    SolvisMax = 0, 
    SolvisMax_6 = 1, 
    SolvisMax_7 = 2, 
    SolvisStrato = 3,
    SolvisBen = 4 

class HEATING_TYPE(Enum): 
    Gas_Brennwert_SX = 1,
    Öl_Brennwert = 2,
    Öl_Niedertemperatur = 3,
    Pellet = 4,
    Fernwärme_FW = 5,
    Wärmepumpe_integriert = 6,
    Wärmepumpe_SolvisVaero = 7,
    Wärmepumpe_SolvisTeo = 8,
    Fremdhersteller = 9

class HEATING_CIRCUIT_TYPE(Enum):
    NONE = 0, 
    HT = 1,
    NT = 2

MAP_SOLVIS_TO_NAME_BASIC = dict()
MAP_SOLVIS_TO_NAME_BASIC["time"] = "last_update"
MAP_SOLVIS_TO_NAME_BASIC["Z1"] = "runtime_burner"
MAP_SOLVIS_TO_NAME_BASIC["Z2"] = "total_burner_start"
MAP_SOLVIS_TO_NAME_BASIC["Z3"] = "total_burner_2nd_start"
MAP_SOLVIS_TO_NAME_BASIC["Z4"] = "NA"
MAP_SOLVIS_TO_NAME_BASIC["SL"] = "NA"
MAP_SOLVIS_TO_NAME_BASIC["SD"] = "NA"
MAP_SOLVIS_TO_NAME_BASIC["S7"] = "NA"
MAP_SOLVIS_TO_NAME_BASIC["SE"] = "NA"
MAP_SOLVIS_TO_NAME_BASIC["S1"] = "temperature_buffer_top"
MAP_SOLVIS_TO_NAME_BASIC["S3"] = "temperature_buffer_reference"
MAP_SOLVIS_TO_NAME_BASIC["S4"] = "temperature_buffer_heating_top"
MAP_SOLVIS_TO_NAME_BASIC["S9"] = "temperature_buffer_heating_bottom"
MAP_SOLVIS_TO_NAME_BASIC["S2"] = "NA"
MAP_SOLVIS_TO_NAME_BASIC["S11"] = "NA"
MAP_SOLVIS_TO_NAME_BASIC["S12"] = "temperature_heating_circuit_1_flow"
MAP_SOLVIS_TO_NAME_BASIC["S13"] = "temperature_heating_circuit_2_flow"
MAP_SOLVIS_TO_NAME_BASIC["S10"] = "temperature_outside"
MAP_SOLVIS_TO_NAME_BASIC["S5"] = "NA"
MAP_SOLVIS_TO_NAME_BASIC["S8"] = "NA"
MAP_SOLVIS_TO_NAME_BASIC["S14"] = "NA"
MAP_SOLVIS_TO_NAME_BASIC["S15"] = "NA"
MAP_SOLVIS_TO_NAME_BASIC["S16"] = "NA"
MAP_SOLVIS_TO_NAME_BASIC["S6"] = "NA"
MAP_SOLVIS_TO_NAME_BASIC["S17"] = "NA"
MAP_SOLVIS_TO_NAME_BASIC["S18"] = "NA"

MAP_SOLVIS_TO_NAME_BASIC["A14"] = "recovery"
MAP_SOLVIS_TO_NAME_BASIC["A12"] = "burner"
MAP_SOLVIS_TO_NAME_BASIC["A13"] = "burner_s2"
MAP_SOLVIS_TO_NAME_BASIC["A5"] = "NA"
MAP_SOLVIS_TO_NAME_BASIC["A8"] = "heating_circuit_1_mixer_open"
MAP_SOLVIS_TO_NAME_BASIC["A9"] = "heating_circuit_1_mixer_close"
MAP_SOLVIS_TO_NAME_BASIC["A3"] = "heating_circuit_1_pump"
MAP_SOLVIS_TO_NAME_BASIC["A10"] = "heating_circuit_2_mixer_open"
MAP_SOLVIS_TO_NAME_BASIC["A11"] = "heating_circuit_2_mixer_close"
MAP_SOLVIS_TO_NAME_BASIC["A4"] = "heating_circuit_2_pump"
MAP_SOLVIS_TO_NAME_BASIC["A6"] = "heating_circuit_3_pump"
MAP_SOLVIS_TO_NAME_BASIC["A7"] = "NA"
MAP_SOLVIS_TO_NAME_BASIC["A1"] = "NA"
MAP_SOLVIS_TO_NAME_BASIC["A2"] = "NA"
MAP_SOLVIS_TO_NAME_BASIC["RF1"] = "temperature_room_1"
MAP_SOLVIS_TO_NAME_BASIC["RF2"] = "temperature_room_2"
MAP_SOLVIS_TO_NAME_BASIC["RF3"] = "temperature_room_3"

MAP_SOLVIS_TO_NAME_WITH_WARM_WATER_STATION = dict()
MAP_SOLVIS_TO_NAME_WITH_WARM_WATER_STATION["S2"] = "temperature_warm_water_station"
MAP_SOLVIS_TO_NAME_WITH_WARM_WATER_STATION["S11"] = "temperature_circulation"
MAP_SOLVIS_TO_NAME_WITH_WARM_WATER_STATION["S18"] = "volume_stream_warm_water"
MAP_SOLVIS_TO_NAME_WITH_WARM_WATER_STATION["A2"] = "warm_water_station_pump"
MAP_SOLVIS_TO_NAME_WITH_WARM_WATER_STATION["A5"] = "circulation_pump"

MAP_SOLVIS_TO_NAME_WITH_SOLAR = dict()
MAP_SOLVIS_TO_NAME_WITH_SOLAR["S5"] = "temperature_solar_flow"
MAP_SOLVIS_TO_NAME_WITH_SOLAR["S6"] = "temperature_solar_return"
MAP_SOLVIS_TO_NAME_WITH_SOLAR["S7"] = "solar_pressure"
MAP_SOLVIS_TO_NAME_WITH_SOLAR["S8"] = "temperature_solar_panel"
MAP_SOLVIS_TO_NAME_WITH_SOLAR["S17"] = "volume_stream_solar"
MAP_SOLVIS_TO_NAME_WITH_SOLAR["A1"] = "solar_pump"
MAP_SOLVIS_TO_NAME_WITH_SOLAR["SE"] = "solar_yield"
MAP_SOLVIS_TO_NAME_WITH_SOLAR["SL"] = "solar_power"
MAP_SOLVIS_TO_NAME_WITH_SOLAR["SD"] = "temperature_solar_diff_flow_return"
MAP_SOLVIS_TO_NAME_WITH_SOLAR["Z4"] = "runtime_solar_pump"

MAP_SOLVIS_TO_NAME_WITH_SOLAR_EAST_WEST = dict()
MAP_SOLVIS_TO_NAME_WITH_SOLAR_EAST_WEST["S16"] = "temperature_solar_panel2"
MAP_SOLVIS_TO_NAME_WITH_SOLAR_EAST_WEST["A6"] = "solar_valve_1"
MAP_SOLVIS_TO_NAME_WITH_SOLAR_EAST_WEST["A7"] = "solar_valve_2"

MAP_SOLVIS_TO_NAME_WITH_OVEN = dict()
MAP_SOLVIS_TO_NAME_WITH_OVEN["S16"] = "temperature_oven"
MAP_SOLVIS_TO_NAME_WITH_OVEN["A13"] = "oven_pump"

