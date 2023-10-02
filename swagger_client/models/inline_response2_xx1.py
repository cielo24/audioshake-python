# coding: utf-8

"""
    Groovy API

    AudioShake API  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse2XX1(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'name': 'str',
        'id': 'str',
        'file_type': 'str',
        'format': 'str',
        'link': 'str',
        'jobs': 'list[InlineResponse2XXJobSourceAssetJobs]'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'file_type': 'fileType',
        'format': 'format',
        'link': 'link',
        'jobs': 'jobs'
    }

    def __init__(self, name=None, id=None, file_type=None, format=None, link=None, jobs=None):  # noqa: E501
        """InlineResponse2XX1 - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._id = None
        self._file_type = None
        self._format = None
        self._link = None
        self._jobs = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if file_type is not None:
            self.file_type = file_type
        if format is not None:
            self.format = format
        if link is not None:
            self.link = link
        if jobs is not None:
            self.jobs = jobs

    @property
    def name(self):
        """Gets the name of this InlineResponse2XX1.  # noqa: E501

        Name of the asset  # noqa: E501

        :return: The name of this InlineResponse2XX1.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse2XX1.

        Name of the asset  # noqa: E501

        :param name: The name of this InlineResponse2XX1.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this InlineResponse2XX1.  # noqa: E501

        Unique identifier of the asset  # noqa: E501

        :return: The id of this InlineResponse2XX1.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse2XX1.

        Unique identifier of the asset  # noqa: E501

        :param id: The id of this InlineResponse2XX1.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def file_type(self):
        """Gets the file_type of this InlineResponse2XX1.  # noqa: E501

        Type of the file of the asset  # noqa: E501

        :return: The file_type of this InlineResponse2XX1.  # noqa: E501
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this InlineResponse2XX1.

        Type of the file of the asset  # noqa: E501

        :param file_type: The file_type of this InlineResponse2XX1.  # noqa: E501
        :type: str
        """

        self._file_type = file_type

    @property
    def format(self):
        """Gets the format of this InlineResponse2XX1.  # noqa: E501

        Format of the asset  # noqa: E501

        :return: The format of this InlineResponse2XX1.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this InlineResponse2XX1.

        Format of the asset  # noqa: E501

        :param format: The format of this InlineResponse2XX1.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def link(self):
        """Gets the link of this InlineResponse2XX1.  # noqa: E501

        URL link of the asset  # noqa: E501

        :return: The link of this InlineResponse2XX1.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this InlineResponse2XX1.

        URL link of the asset  # noqa: E501

        :param link: The link of this InlineResponse2XX1.  # noqa: E501
        :type: str
        """

        self._link = link

    @property
    def jobs(self):
        """Gets the jobs of this InlineResponse2XX1.  # noqa: E501

        Array of jobs containing the stem assets generated from the asset  # noqa: E501

        :return: The jobs of this InlineResponse2XX1.  # noqa: E501
        :rtype: list[InlineResponse2XXJobSourceAssetJobs]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this InlineResponse2XX1.

        Array of jobs containing the stem assets generated from the asset  # noqa: E501

        :param jobs: The jobs of this InlineResponse2XX1.  # noqa: E501
        :type: list[InlineResponse2XXJobSourceAssetJobs]
        """

        self._jobs = jobs

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(InlineResponse2XX1, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse2XX1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
