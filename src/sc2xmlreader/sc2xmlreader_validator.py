"""Validate connection credentials."""
from __future__ import absolute_import

import logging
from urllib.parse import ParseResult, urlparse

import defusedxml
import requests
from requests.auth import HTTPDigestAuth
from requests.exceptions import HTTPError, Timeout

class SC2XMLReaderValidator:
    """Class to validate connection and credentials
    """

    def __init__(self, hostname: str) -> None:
        """Initialize."""
        self.host = hostname
        self.url = ""

    def __makeURL(self) -> str:
        url = urlparse(self.host, "http")
        netloc = url.netloc or url.path
        path = url.path if url.netloc else ""
        return ParseResult("http", netloc, path, *url[3:]).geturl()

    def validate_host(self) -> bool:
        """Test if given host responses to http get request in any way."""
        self.url = self.__makeURL()
        try:
            response = requests.get(self.url, timeout=10)
            if response.status_code in (401, 200):  # OK, this is expected
                return True
        except Timeout as err:
            logging.debug("""GET Request: Timeout Exception -- %s""", err)
        except HTTPError as err:
            logging.debug("""GET Request: HTTP Exception -- %s""", err)

        return False

    def authenticate(self, username: str, password: str) -> bool:
        """Test if we can authenticate with the host."""        
        try:
            if len(self.url) == 0:
                self.url = self.__makeURL()

            basic = HTTPDigestAuth(username, password)
            response = requests.get(self.url, stream=True, auth=basic, timeout=10)
            if response.status_code == 200:  # OK, got something
                return True
        except Timeout as err:
            logging.debug("""GET Request: Timeout Exception -- %s""", err)
        except HTTPError as err:
            logging.debug("""GET Request: HTTP Exception -- %s""", err)

        return False

    def validate_uri(self, username: str, password: str) -> bool:
        """Test if we can read from solvis remote the sc2_val.xml file."""

        if len(self.url) == 0:
            self.url = self.__makeURL()

        uri = """{self.url}/sc2_val.xml"""
        try:
            basic = HTTPDigestAuth(username, password)
            response = requests.get(uri, stream=True, auth=basic, timeout=10)
        except Timeout as err:
            logging.debug("""GET Request: Timeout Exception -- %s""", err)
            return False
        except HTTPError as err:
            logging.debug("""GET Request: HTTP Exception -- %s""", err)
            return False

        if response.status_code == 200:  # OK, got something
            response.raw.decode_content = True

            sc2_data = defusedxml.ElementTree.parse(response.raw)
            root = sc2_data.getroot()
            payload_data = root.find("data")
            if payload_data is not None:
                return True

        return False