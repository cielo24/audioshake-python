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

class InlineResponse2XXJobStemMetadata(object):
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
        'format': 'str',
        'stem_name': 'str',
        'name': 'str',
        'language': 'str',
        'custom_property': 'str',
        'residual': 'bool',
        'user_session_id': 'str',
        'audio_id': 'str',
        'failure_test': 'float',
        'is_test_job': 'bool'
    }

    attribute_map = {
        'format': 'format',
        'stem_name': 'stemName',
        'name': 'name',
        'language': 'language',
        'custom_property': 'customProperty',
        'residual': 'residual',
        'user_session_id': 'userSessionId',
        'audio_id': 'audioId',
        'failure_test': 'failureTest',
        'is_test_job': 'isTestJob'
    }

    def __init__(self, format=None, stem_name=None, name=None, language=None, custom_property=None, residual=None, user_session_id=None, audio_id=None, failure_test=None, is_test_job=None):  # noqa: E501
        """InlineResponse2XXJobStemMetadata - a model defined in Swagger"""  # noqa: E501
        self._format = None
        self._stem_name = None
        self._name = None
        self._language = None
        self._custom_property = None
        self._residual = None
        self._user_session_id = None
        self._audio_id = None
        self._failure_test = None
        self._is_test_job = None
        self.discriminator = None
        if format is not None:
            self.format = format
        if stem_name is not None:
            self.stem_name = stem_name
        if name is not None:
            self.name = name
        if language is not None:
            self.language = language
        if custom_property is not None:
            self.custom_property = custom_property
        if residual is not None:
            self.residual = residual
        if user_session_id is not None:
            self.user_session_id = user_session_id
        if audio_id is not None:
            self.audio_id = audio_id
        if failure_test is not None:
            self.failure_test = failure_test
        if is_test_job is not None:
            self.is_test_job = is_test_job

    @property
    def format(self):
        """Gets the format of this InlineResponse2XXJobStemMetadata.  # noqa: E501

        Audio format of the stem  # noqa: E501

        :return: The format of this InlineResponse2XXJobStemMetadata.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this InlineResponse2XXJobStemMetadata.

        Audio format of the stem  # noqa: E501

        :param format: The format of this InlineResponse2XXJobStemMetadata.  # noqa: E501
        :type: str
        """
        allowed_values = ["wav", "flac", "mp3", "aiff"]  # noqa: E501
        if format not in allowed_values:
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"  # noqa: E501
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def stem_name(self):
        """Gets the stem_name of this InlineResponse2XXJobStemMetadata.  # noqa: E501

        Name of the stem being generated  # noqa: E501

        :return: The stem_name of this InlineResponse2XXJobStemMetadata.  # noqa: E501
        :rtype: str
        """
        return self._stem_name

    @stem_name.setter
    def stem_name(self, stem_name):
        """Sets the stem_name of this InlineResponse2XXJobStemMetadata.

        Name of the stem being generated  # noqa: E501

        :param stem_name: The stem_name of this InlineResponse2XXJobStemMetadata.  # noqa: E501
        :type: str
        """

        self._stem_name = stem_name

    @property
    def name(self):
        """Gets the name of this InlineResponse2XXJobStemMetadata.  # noqa: E501

        Name of the stem being generated  # noqa: E501

        :return: The name of this InlineResponse2XXJobStemMetadata.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse2XXJobStemMetadata.

        Name of the stem being generated  # noqa: E501

        :param name: The name of this InlineResponse2XXJobStemMetadata.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def language(self):
        """Gets the language of this InlineResponse2XXJobStemMetadata.  # noqa: E501

        The language model to use for alignment (Default is auto)  # noqa: E501

        :return: The language of this InlineResponse2XXJobStemMetadata.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this InlineResponse2XXJobStemMetadata.

        The language model to use for alignment (Default is auto)  # noqa: E501

        :param language: The language of this InlineResponse2XXJobStemMetadata.  # noqa: E501
        :type: str
        """
        allowed_values = ["af", "ar", "az", "be", "bg", "bs", "ca", "cs", "cy", "da", "de", "el", "en", "es", "et", "fa", "fi", "fr", "gl", "he", "hi", "hr", "hu", "hy", "id", "is", "it", "ja", "kk", "kn", "ko", "lt", "lv", "mi", "mk", "mr", "ms", "ne", "nl", "no", "pl", "pt", "ro", "ru", "sk", "sl", "sr", "sv", "sw", "ta", "th", "tl", "tr", "uk", "ur", "vi", "zh", "auto"]  # noqa: E501
        if language not in allowed_values:
            raise ValueError(
                "Invalid value for `language` ({0}), must be one of {1}"  # noqa: E501
                .format(language, allowed_values)
            )

        self._language = language

    @property
    def custom_property(self):
        """Gets the custom_property of this InlineResponse2XXJobStemMetadata.  # noqa: E501

        Custom property of the stem  # noqa: E501

        :return: The custom_property of this InlineResponse2XXJobStemMetadata.  # noqa: E501
        :rtype: str
        """
        return self._custom_property

    @custom_property.setter
    def custom_property(self, custom_property):
        """Sets the custom_property of this InlineResponse2XXJobStemMetadata.

        Custom property of the stem  # noqa: E501

        :param custom_property: The custom_property of this InlineResponse2XXJobStemMetadata.  # noqa: E501
        :type: str
        """

        self._custom_property = custom_property

    @property
    def residual(self):
        """Gets the residual of this InlineResponse2XXJobStemMetadata.  # noqa: E501

        Flag indicating if the stem is or should generate a residual  # noqa: E501

        :return: The residual of this InlineResponse2XXJobStemMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._residual

    @residual.setter
    def residual(self, residual):
        """Sets the residual of this InlineResponse2XXJobStemMetadata.

        Flag indicating if the stem is or should generate a residual  # noqa: E501

        :param residual: The residual of this InlineResponse2XXJobStemMetadata.  # noqa: E501
        :type: bool
        """

        self._residual = residual

    @property
    def user_session_id(self):
        """Gets the user_session_id of this InlineResponse2XXJobStemMetadata.  # noqa: E501

        Identifier of the user session making the request. Widget specific.  # noqa: E501

        :return: The user_session_id of this InlineResponse2XXJobStemMetadata.  # noqa: E501
        :rtype: str
        """
        return self._user_session_id

    @user_session_id.setter
    def user_session_id(self, user_session_id):
        """Sets the user_session_id of this InlineResponse2XXJobStemMetadata.

        Identifier of the user session making the request. Widget specific.  # noqa: E501

        :param user_session_id: The user_session_id of this InlineResponse2XXJobStemMetadata.  # noqa: E501
        :type: str
        """

        self._user_session_id = user_session_id

    @property
    def audio_id(self):
        """Gets the audio_id of this InlineResponse2XXJobStemMetadata.  # noqa: E501

        Identifier of the audio source used for stem generation. Widget specific.  # noqa: E501

        :return: The audio_id of this InlineResponse2XXJobStemMetadata.  # noqa: E501
        :rtype: str
        """
        return self._audio_id

    @audio_id.setter
    def audio_id(self, audio_id):
        """Sets the audio_id of this InlineResponse2XXJobStemMetadata.

        Identifier of the audio source used for stem generation. Widget specific.  # noqa: E501

        :param audio_id: The audio_id of this InlineResponse2XXJobStemMetadata.  # noqa: E501
        :type: str
        """

        self._audio_id = audio_id

    @property
    def failure_test(self):
        """Gets the failure_test of this InlineResponse2XXJobStemMetadata.  # noqa: E501

        If this param has a value, use the corresponding code to force a failed test  # noqa: E501

        :return: The failure_test of this InlineResponse2XXJobStemMetadata.  # noqa: E501
        :rtype: float
        """
        return self._failure_test

    @failure_test.setter
    def failure_test(self, failure_test):
        """Sets the failure_test of this InlineResponse2XXJobStemMetadata.

        If this param has a value, use the corresponding code to force a failed test  # noqa: E501

        :param failure_test: The failure_test of this InlineResponse2XXJobStemMetadata.  # noqa: E501
        :type: float
        """

        self._failure_test = failure_test

    @property
    def is_test_job(self):
        """Gets the is_test_job of this InlineResponse2XXJobStemMetadata.  # noqa: E501

        Determines whether a job is a \"test job\" or not  # noqa: E501

        :return: The is_test_job of this InlineResponse2XXJobStemMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._is_test_job

    @is_test_job.setter
    def is_test_job(self, is_test_job):
        """Sets the is_test_job of this InlineResponse2XXJobStemMetadata.

        Determines whether a job is a \"test job\" or not  # noqa: E501

        :param is_test_job: The is_test_job of this InlineResponse2XXJobStemMetadata.  # noqa: E501
        :type: bool
        """

        self._is_test_job = is_test_job

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
        if issubclass(InlineResponse2XXJobStemMetadata, dict):
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
        if not isinstance(other, InlineResponse2XXJobStemMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
