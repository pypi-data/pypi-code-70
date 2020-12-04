# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 50.3.1-BETA
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ScreenshotOutputV1(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'end': 'str',
        'height': 'int',
        'screenshot': 'str',
        'start': 'str',
        'status_message': 'str',
        'width': 'int'
    }

    attribute_map = {
        'end': 'end',
        'height': 'height',
        'screenshot': 'screenshot',
        'start': 'start',
        'status_message': 'statusMessage',
        'width': 'width'
    }

    def __init__(self, end=None, height=None, screenshot=None, start=None, status_message=None, width=None):
        """
        ScreenshotOutputV1 - a model defined in Swagger
        """

        self._end = None
        self._height = None
        self._screenshot = None
        self._start = None
        self._status_message = None
        self._width = None

        if end is not None:
          self.end = end
        if height is not None:
          self.height = height
        if screenshot is not None:
          self.screenshot = screenshot
        if start is not None:
          self.start = start
        if status_message is not None:
          self.status_message = status_message
        if width is not None:
          self.width = width

    @property
    def end(self):
        """
        Gets the end of this ScreenshotOutputV1.
        The end of the display range window used in the screenshot as an ISO-8601 timestamp

        :return: The end of this ScreenshotOutputV1.
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """
        Sets the end of this ScreenshotOutputV1.
        The end of the display range window used in the screenshot as an ISO-8601 timestamp

        :param end: The end of this ScreenshotOutputV1.
        :type: str
        """

        self._end = end

    @property
    def height(self):
        """
        Gets the height of this ScreenshotOutputV1.
        The screenshot height if a screenshot URL is being returned and a contentSelector was specified in the request

        :return: The height of this ScreenshotOutputV1.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height of this ScreenshotOutputV1.
        The screenshot height if a screenshot URL is being returned and a contentSelector was specified in the request

        :param height: The height of this ScreenshotOutputV1.
        :type: int
        """

        self._height = height

    @property
    def screenshot(self):
        """
        Gets the screenshot of this ScreenshotOutputV1.
        The Base64 encoded screenshot data, or the URL of the generated and cached screenshot if the screenshot request did not specify a period

        :return: The screenshot of this ScreenshotOutputV1.
        :rtype: str
        """
        return self._screenshot

    @screenshot.setter
    def screenshot(self, screenshot):
        """
        Sets the screenshot of this ScreenshotOutputV1.
        The Base64 encoded screenshot data, or the URL of the generated and cached screenshot if the screenshot request did not specify a period

        :param screenshot: The screenshot of this ScreenshotOutputV1.
        :type: str
        """

        self._screenshot = screenshot

    @property
    def start(self):
        """
        Gets the start of this ScreenshotOutputV1.
        The start of the display range window used in the screenshot as an ISO-8601 timestamp

        :return: The start of this ScreenshotOutputV1.
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """
        Sets the start of this ScreenshotOutputV1.
        The start of the display range window used in the screenshot as an ISO-8601 timestamp

        :param start: The start of this ScreenshotOutputV1.
        :type: str
        """

        self._start = start

    @property
    def status_message(self):
        """
        Gets the status_message of this ScreenshotOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation. Null if the status message has not been set.

        :return: The status_message of this ScreenshotOutputV1.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this ScreenshotOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation. Null if the status message has not been set.

        :param status_message: The status_message of this ScreenshotOutputV1.
        :type: str
        """

        self._status_message = status_message

    @property
    def width(self):
        """
        Gets the width of this ScreenshotOutputV1.
        The screenshot width if a screenshot URL is being returned and a contentSelector was specified in the request

        :return: The width of this ScreenshotOutputV1.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width of this ScreenshotOutputV1.
        The screenshot width if a screenshot URL is being returned and a contentSelector was specified in the request

        :param width: The width of this ScreenshotOutputV1.
        :type: int
        """

        self._width = width

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ScreenshotOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
