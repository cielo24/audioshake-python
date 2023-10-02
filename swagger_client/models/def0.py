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

class Def0(object):
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
        'id': 'str',
        'name': 'str',
        'client_id': 'str',
        'job_id': 'str',
        'file_id': 'str',
        'format': 'str',
        'file_type': 'str',
        'metadata': 'object',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'client_id': 'clientId',
        'job_id': 'jobId',
        'file_id': 'fileId',
        'format': 'format',
        'file_type': 'fileType',
        'metadata': 'metadata',
        'type': 'type'
    }

    def __init__(self, id=None, name=None, client_id=None, job_id=None, file_id=None, format=None, file_type=None, metadata=None, type=None):  # noqa: E501
        """Def0 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._client_id = None
        self._job_id = None
        self._file_id = None
        self._format = None
        self._file_type = None
        self._metadata = None
        self._type = None
        self.discriminator = None
        self.id = id
        self.name = name
        self.client_id = client_id
        if job_id is not None:
            self.job_id = job_id
        if file_id is not None:
            self.file_id = file_id
        if format is not None:
            self.format = format
        if file_type is not None:
            self.file_type = file_type
        if metadata is not None:
            self.metadata = metadata
        self.type = type

    @property
    def id(self):
        """Gets the id of this Def0.  # noqa: E501


        :return: The id of this Def0.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Def0.


        :param id: The id of this Def0.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Def0.  # noqa: E501


        :return: The name of this Def0.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Def0.


        :param name: The name of this Def0.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def client_id(self):
        """Gets the client_id of this Def0.  # noqa: E501


        :return: The client_id of this Def0.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this Def0.


        :param client_id: The client_id of this Def0.  # noqa: E501
        :type: str
        """
        if client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def job_id(self):
        """Gets the job_id of this Def0.  # noqa: E501


        :return: The job_id of this Def0.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this Def0.


        :param job_id: The job_id of this Def0.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    @property
    def file_id(self):
        """Gets the file_id of this Def0.  # noqa: E501


        :return: The file_id of this Def0.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this Def0.


        :param file_id: The file_id of this Def0.  # noqa: E501
        :type: str
        """

        self._file_id = file_id

    @property
    def format(self):
        """Gets the format of this Def0.  # noqa: E501

        The mimetype format of the asset.  # noqa: E501

        :return: The format of this Def0.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this Def0.

        The mimetype format of the asset.  # noqa: E501

        :param format: The format of this Def0.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def file_type(self):
        """Gets the file_type of this Def0.  # noqa: E501

        The mimetype format of the asset.  # noqa: E501

        :return: The file_type of this Def0.  # noqa: E501
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this Def0.

        The mimetype format of the asset.  # noqa: E501

        :param file_type: The file_type of this Def0.  # noqa: E501
        :type: str
        """

        self._file_type = file_type

    @property
    def metadata(self):
        """Gets the metadata of this Def0.  # noqa: E501

        Metadata associated with a asset.  # noqa: E501

        :return: The metadata of this Def0.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Def0.

        Metadata associated with a asset.  # noqa: E501

        :param metadata: The metadata of this Def0.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

    @property
    def type(self):
        """Gets the type of this Def0.  # noqa: E501

        Describes the type of asset.  # noqa: E501

        :return: The type of this Def0.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Def0.

        Describes the type of asset.  # noqa: E501

        :param type: The type of this Def0.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["source", "stem"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(Def0, dict):
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
        if not isinstance(other, Def0):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other