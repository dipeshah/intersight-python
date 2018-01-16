# coding: utf-8

"""
    UCS Starship API

    This is the UCS Starship REST API

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class BootSdCard(object):
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
        'enabled': 'bool',
        'name': 'str',
        'lun': 'int',
        'subtype': 'str'
    }

    attribute_map = {
        'enabled': 'Enabled',
        'name': 'Name',
        'lun': 'Lun',
        'subtype': 'Subtype'
    }

    def __init__(self, enabled=None, name=None, lun=None, subtype='None'):
        """
        BootSdCard - a model defined in Swagger
        """

        self._enabled = None
        self._name = None
        self._lun = None
        self._subtype = None

        if enabled is not None:
          self.enabled = enabled
        if name is not None:
          self.name = name
        if lun is not None:
          self.lun = lun
        if subtype is not None:
          self.subtype = subtype

    @property
    def enabled(self):
        """
        Gets the enabled of this BootSdCard.
        Specifies if the boot device is enabled or disabled.  

        :return: The enabled of this BootSdCard.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this BootSdCard.
        Specifies if the boot device is enabled or disabled.  

        :param enabled: The enabled of this BootSdCard.
        :type: bool
        """

        self._enabled = enabled

    @property
    def name(self):
        """
        Gets the name of this BootSdCard.
        Specifies the name of the boot device. It should start and end with an alphanumeric character. It can have underscores and hyphens. It cannot be more than 30 characters.   

        :return: The name of this BootSdCard.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BootSdCard.
        Specifies the name of the boot device. It should start and end with an alphanumeric character. It can have underscores and hyphens. It cannot be more than 30 characters.   

        :param name: The name of this BootSdCard.
        :type: str
        """

        self._name = name

    @property
    def lun(self):
        """
        Gets the lun of this BootSdCard.
        Specifies the Logical Unit Number(LUN) of the device.  

        :return: The lun of this BootSdCard.
        :rtype: int
        """
        return self._lun

    @lun.setter
    def lun(self, lun):
        """
        Sets the lun of this BootSdCard.
        Specifies the Logical Unit Number(LUN) of the device.  

        :param lun: The lun of this BootSdCard.
        :type: int
        """

        self._lun = lun

    @property
    def subtype(self):
        """
        Gets the subtype of this BootSdCard.
        Specifies the subtype for the selected device type.   

        :return: The subtype of this BootSdCard.
        :rtype: str
        """
        return self._subtype

    @subtype.setter
    def subtype(self, subtype):
        """
        Sets the subtype of this BootSdCard.
        Specifies the subtype for the selected device type.   

        :param subtype: The subtype of this BootSdCard.
        :type: str
        """
        allowed_values = ["None", "flex-util", "flex-flash"]
        if subtype not in allowed_values:
            raise ValueError(
                "Invalid value for `subtype` ({0}), must be one of {1}"
                .format(subtype, allowed_values)
            )

        self._subtype = subtype

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
        if not isinstance(other, BootSdCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
