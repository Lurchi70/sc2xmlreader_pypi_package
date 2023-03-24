"""requesting and decode Remote Data. """
from __future__ import absolute_import

import logging

import defusedxml
import requests
from requests.auth import HTTPDigestAuth

from datetime import datetime

class SC2XMLReader:
    """class to read and analyze remote data."""

    def __init__(self, url: str, username: str, password: str, withWarmWaterStation=True, withSolar=True, withEastWest=False, withOven=False) -> None:
        """Initialize the data interpreter."""
        self.data = {}
        uri = f"""{url}/sc2_val.xml"""

        self.solar = withSolar
        self.east_west_solar = withEastWest

        self.oven = withOven
        self.warm_water_station = withWarmWaterStation

        try:
            basic = HTTPDigestAuth(username, password)
            response = requests.get(uri, stream=True, auth=basic, timeout=10)
        except Exception as err:
            logging.debug("""Catched Exception during reading data: %s""", err)
            raise

        if response.status_code == 200:  # OK, got something
            response.raw.decode_content = True

            sc2_data = defusedxml.ElementTree.parse(response.raw)
            root = sc2_data.getroot()
            payload_data = root.find("data")

            the_sc2_text = str(payload_data.text)

            if len(the_sc2_text) >= 439:
                self.data = self.create_array_from_data(the_sc2_text)
        else:
            logging.debug("""error response from http request: %s""", response.status_code)


    def create_array_from_data(self, data_sc2: str):
        """Interprets the remote data and transfors it into data_array."""
        data_array = {}
        value_int = 0
        value_float = 0.0

        # skip first 11 Bytes (in older versions neccessary)
        # possible to identify version of returned data and adopt?
        # value_ = string_[0: 11]
        # string_ = string_[11:]

        # Header
        # value_str = data_sc2[0:12]
        # print("Header: [{0}]".format(self.convertAtoH(value_str, 12)));
        data_sc2 = data_sc2[12:]

        # Uhrzeit
        # value_str = data_sc2[0:6]
        # print("Uhrzeit: [{0}]".format(self.convertAtoH(value_str, 6)));
        data_sc2 = data_sc2[6:]
        val1 = self.create_data_entry("time", "", datetime.now(), "")
        data_array["time"] = val1

        # Anlagentyp
        # value_str = data_sc2[0:4]
        # print("Anlagentyp: [{0}]".format(self.convertAtoH(value_str, 4)));
        data_sc2 = data_sc2[4:]

        # Systemnummer
        # value_str = data_sc2[0:4]
        # print("Systemnummer: [{0}]".format(self.convertAtoH(value_str, 4)));
        data_sc2 = data_sc2[4:]

        element_in_sc2_data = 0
        while element_in_sc2_data < 63:
            # Temps
            if element_in_sc2_data < 16:
                value_int = self.convert_data_to_int(data_sc2, 4)
                data_sc2 = data_sc2[4:]
                if value_int > 32767:
                    value_int = value_int - 65536
                value_float = value_int / 10

                the_name = f"S{element_in_sc2_data + 1}"
                val1 = self.create_data_entry(
                    the_name, "Temperature", value_float, "°C"
                )
                data_array[the_name] = val1
            elif element_in_sc2_data == 16:
                value_int = self.convert_data_to_int(data_sc2, 4)
                data_sc2 = data_sc2[4:]
                data_array["S18"] = self.create_data_entry(
                    "S17", "Volume Stream Solar", value_int, "l/h"
                )
            elif element_in_sc2_data == 17:
                value_int = self.convert_data_to_int(data_sc2, 4)
                data_sc2 = data_sc2[4:]
                data_array["S17"] = self.create_data_entry(
                    "S18", "Volume Stream Water", value_int, "l/h"
                )
            elif 18 <= element_in_sc2_data <= 20:
                # print("AnalogIn: [{0}]".format(self.convertAtoH(value_, 4)));
                data_sc2 = data_sc2[4:]
            elif 21 <= element_in_sc2_data <= 24:
                # print("AnalogOut: [{0}]".format(self.convertAtoH(value_, 2)));
                data_sc2 = data_sc2[2:]
            elif 25 <= element_in_sc2_data <= 27:
                value_int = self.convert_data_to_int(data_sc2, 4)
                data_sc2 = data_sc2[4:]
                if value_int > 32767:
                    value_int = value_int - 65536
                    # end if
                    value_float = value_int / 10
                    the_name = f"RF{element_in_sc2_data - 24}"
                    data_array[the_name] = self.create_data_entry(
                        the_name, "Roomtemperature", value_float, "°C"
                    )
            elif 28 <= element_in_sc2_data <= 41:
                value_int = self.convert_data_to_int(data_sc2, 2)
                data_sc2 = data_sc2[2:]
                the_name = f"A{element_in_sc2_data - 27}"
                data_array[the_name] = self.create_data_entry(
                    the_name, "Output", value_int, ""
                )
            element_in_sc2_data += 1

        value_int = self.convert_data_to_int(data_sc2, 4)
        data_sc2 = data_sc2[4:]
        data_array["Z1"] = self.create_data_entry(
            "Z1", "Runtime Burner", value_int, "h"
        )
        value_int = self.convert_data_to_int(data_sc2, 4)
        data_sc2 = data_sc2[4:]
        data_array["Z2"] = self.create_data_entry("Z2", "Number Burner Start", value_int, "")
        value_int = self.convert_data_to_int(data_sc2, 4)
        data_sc2 = data_sc2[4:]
        data_array["Z3"] = self.create_data_entry(
            "Z3", "Number 2nd Burner Start", value_int, ""
        )
        value_int = self.convert_data_to_int(data_sc2, 4)
        data_sc2 = data_sc2[4:]
        data_array["Z4"] = self.create_data_entry(
            "Z4", "Runtime Solarpump", value_int, "h"
        )
        value_int = self.convert_data_to_int(data_sc2, 4)
        data_sc2 = data_sc2[4:]
        data_array["SE"] = self.create_data_entry("SE", "Solaryield", value_int, "kWh")

        # skip 30 Byte
        # value_str = data_sc2[0:30]
        data_sc2 = data_sc2[30:]

        value_int = self.convert_data_to_int(data_sc2, 4)
        data_sc2 = data_sc2[4:]
        data_array["SL"] = self.create_data_entry(
            "SL", "Solarpower", value_int, "kW"
        )

        return data_array

    def print_data(self, array_=None):
        """Write sensor data to logger."""
        for value_ in array_:
            if value_["Key"][0:1] == "S":
                logging.debug(
                    value_["Key"] + "=>" + value_["Value"] + " - " + value_["Name"]
                )

    def create_data_entry(
        self, the_key=None, the_name=None, the_value=None, the_unit=None
    ) -> dict:
        """Return dictionary entry."""
        data_entry = {}
        data_entry["Key"] = the_key
        data_entry["Name"] = the_name
        data_entry["Value"] = the_value
        data_entry["Unit"] = the_unit
        return data_entry

    def convert_data_to_int(self, hex_string: str, size_: int) -> int:
        """Return integer value out of hex from solvis data."""
        hex_string = hex_string[0:size_]
        chunk_array = []
        element_count = 0
        while element_count < size_ / 2:
            sstr_ = hex_string[0:2]
            hex_string = hex_string[2:]
            chunk_array.append(sstr_)
            element_count += 1

        if len(hex_string):
            chunk_array.append(hex_string)

        arsz_ = len(chunk_array)
        while arsz_ > 0:
            hex_string += chunk_array[arsz_ - 1]
            arsz_ -= 1

        return int(hex_string, base=16)
