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


class IamLdapBaseProperties(object):
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
        'attribute': 'str',
        'base_dn': 'str',
        'bind_dn': 'str',
        'bind_method': 'str',
        'domain': 'str',
        'enable_encryption': 'bool',
        'enable_group_authorization': 'bool',
        'filter': 'str',
        'group_attribute': 'str',
        'nested_group_search_depth': 'int',
        'password': 'str',
        'timeout': 'int'
    }

    attribute_map = {
        'attribute': 'Attribute',
        'base_dn': 'BaseDn',
        'bind_dn': 'BindDn',
        'bind_method': 'BindMethod',
        'domain': 'Domain',
        'enable_encryption': 'EnableEncryption',
        'enable_group_authorization': 'EnableGroupAuthorization',
        'filter': 'Filter',
        'group_attribute': 'GroupAttribute',
        'nested_group_search_depth': 'NestedGroupSearchDepth',
        'password': 'Password',
        'timeout': 'Timeout'
    }

    def __init__(self, attribute=None, base_dn=None, bind_dn=None, bind_method='LoginCredentials', domain=None, enable_encryption=None, enable_group_authorization=None, filter=None, group_attribute=None, nested_group_search_depth=None, password=None, timeout=None):
        """
        IamLdapBaseProperties - a model defined in Swagger
        """

        self._attribute = None
        self._base_dn = None
        self._bind_dn = None
        self._bind_method = None
        self._domain = None
        self._enable_encryption = None
        self._enable_group_authorization = None
        self._filter = None
        self._group_attribute = None
        self._nested_group_search_depth = None
        self._password = None
        self._timeout = None

        if attribute is not None:
          self.attribute = attribute
        if base_dn is not None:
          self.base_dn = base_dn
        if bind_dn is not None:
          self.bind_dn = bind_dn
        if bind_method is not None:
          self.bind_method = bind_method
        if domain is not None:
          self.domain = domain
        if enable_encryption is not None:
          self.enable_encryption = enable_encryption
        if enable_group_authorization is not None:
          self.enable_group_authorization = enable_group_authorization
        if filter is not None:
          self.filter = filter
        if group_attribute is not None:
          self.group_attribute = group_attribute
        if nested_group_search_depth is not None:
          self.nested_group_search_depth = nested_group_search_depth
        if password is not None:
          self.password = password
        if timeout is not None:
          self.timeout = timeout

    @property
    def attribute(self):
        """
        Gets the attribute of this IamLdapBaseProperties.
        An LDAP attribute that contains the role and locale information for the user. This property is always a name-value pair. The system queries the user record for the value that matches this attribute name. For example, CiscoAvPair  

        :return: The attribute of this IamLdapBaseProperties.
        :rtype: str
        """
        return self._attribute

    @attribute.setter
    def attribute(self, attribute):
        """
        Sets the attribute of this IamLdapBaseProperties.
        An LDAP attribute that contains the role and locale information for the user. This property is always a name-value pair. The system queries the user record for the value that matches this attribute name. For example, CiscoAvPair  

        :param attribute: The attribute of this IamLdapBaseProperties.
        :type: str
        """

        self._attribute = attribute

    @property
    def base_dn(self):
        """
        Gets the base_dn of this IamLdapBaseProperties.
        Base Distinguished Name(DN). This field describes where to load users and groups from. It must be in the dc=domain,dc=com format for Active Directory servers  

        :return: The base_dn of this IamLdapBaseProperties.
        :rtype: str
        """
        return self._base_dn

    @base_dn.setter
    def base_dn(self, base_dn):
        """
        Sets the base_dn of this IamLdapBaseProperties.
        Base Distinguished Name(DN). This field describes where to load users and groups from. It must be in the dc=domain,dc=com format for Active Directory servers  

        :param base_dn: The base_dn of this IamLdapBaseProperties.
        :type: str
        """

        self._base_dn = base_dn

    @property
    def bind_dn(self):
        """
        Gets the bind_dn of this IamLdapBaseProperties.
        Distinguished Name(DN) of the user, that is used to authenticate against LDAP servers. Applicable only when BindMethod='ConfiguredCredentials'  

        :return: The bind_dn of this IamLdapBaseProperties.
        :rtype: str
        """
        return self._bind_dn

    @bind_dn.setter
    def bind_dn(self, bind_dn):
        """
        Sets the bind_dn of this IamLdapBaseProperties.
        Distinguished Name(DN) of the user, that is used to authenticate against LDAP servers. Applicable only when BindMethod='ConfiguredCredentials'  

        :param bind_dn: The bind_dn of this IamLdapBaseProperties.
        :type: str
        """

        self._bind_dn = bind_dn

    @property
    def bind_method(self):
        """
        Gets the bind_method of this IamLdapBaseProperties.
        Authentication method to access LDAP servers. By default, it is 'LoginCredentials'  

        :return: The bind_method of this IamLdapBaseProperties.
        :rtype: str
        """
        return self._bind_method

    @bind_method.setter
    def bind_method(self, bind_method):
        """
        Sets the bind_method of this IamLdapBaseProperties.
        Authentication method to access LDAP servers. By default, it is 'LoginCredentials'  

        :param bind_method: The bind_method of this IamLdapBaseProperties.
        :type: str
        """
        allowed_values = ["LoginCredentials", "Anonymous", "ConfiguredCredentials"]
        if bind_method not in allowed_values:
            raise ValueError(
                "Invalid value for `bind_method` ({0}), must be one of {1}"
                .format(bind_method, allowed_values)
            )

        self._bind_method = bind_method

    @property
    def domain(self):
        """
        Gets the domain of this IamLdapBaseProperties.
        The IPv4 domain that all users must be in  

        :return: The domain of this IamLdapBaseProperties.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this IamLdapBaseProperties.
        The IPv4 domain that all users must be in  

        :param domain: The domain of this IamLdapBaseProperties.
        :type: str
        """

        self._domain = domain

    @property
    def enable_encryption(self):
        """
        Gets the enable_encryption of this IamLdapBaseProperties.
        Endpoint encrypts all information it sends to the LDAP server  

        :return: The enable_encryption of this IamLdapBaseProperties.
        :rtype: bool
        """
        return self._enable_encryption

    @enable_encryption.setter
    def enable_encryption(self, enable_encryption):
        """
        Sets the enable_encryption of this IamLdapBaseProperties.
        Endpoint encrypts all information it sends to the LDAP server  

        :param enable_encryption: The enable_encryption of this IamLdapBaseProperties.
        :type: bool
        """

        self._enable_encryption = enable_encryption

    @property
    def enable_group_authorization(self):
        """
        Gets the enable_group_authorization of this IamLdapBaseProperties.
        User authentication is also done on the group level for LDAP users that are not found in the local user database  

        :return: The enable_group_authorization of this IamLdapBaseProperties.
        :rtype: bool
        """
        return self._enable_group_authorization

    @enable_group_authorization.setter
    def enable_group_authorization(self, enable_group_authorization):
        """
        Sets the enable_group_authorization of this IamLdapBaseProperties.
        User authentication is also done on the group level for LDAP users that are not found in the local user database  

        :param enable_group_authorization: The enable_group_authorization of this IamLdapBaseProperties.
        :type: bool
        """

        self._enable_group_authorization = enable_group_authorization

    @property
    def filter(self):
        """
        Gets the filter of this IamLdapBaseProperties.
        Filter defines the criteria used to identify entries in search requests. This field must match the configured attribute in the schema on the LDAP server  

        :return: The filter of this IamLdapBaseProperties.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """
        Sets the filter of this IamLdapBaseProperties.
        Filter defines the criteria used to identify entries in search requests. This field must match the configured attribute in the schema on the LDAP server  

        :param filter: The filter of this IamLdapBaseProperties.
        :type: str
        """

        self._filter = filter

    @property
    def group_attribute(self):
        """
        Gets the group_attribute of this IamLdapBaseProperties.
        An LDAP attribute that indicates the groups to which an LDAP entry belongs. For example, memberOf is the name of the membership attribute that is used in Active Directory  

        :return: The group_attribute of this IamLdapBaseProperties.
        :rtype: str
        """
        return self._group_attribute

    @group_attribute.setter
    def group_attribute(self, group_attribute):
        """
        Sets the group_attribute of this IamLdapBaseProperties.
        An LDAP attribute that indicates the groups to which an LDAP entry belongs. For example, memberOf is the name of the membership attribute that is used in Active Directory  

        :param group_attribute: The group_attribute of this IamLdapBaseProperties.
        :type: str
        """

        self._group_attribute = group_attribute

    @property
    def nested_group_search_depth(self):
        """
        Gets the nested_group_search_depth of this IamLdapBaseProperties.
        Parameter to search for an LDAP group nested within another defined group in an LDAP group map. The parameter defines the depth of a nested group search  

        :return: The nested_group_search_depth of this IamLdapBaseProperties.
        :rtype: int
        """
        return self._nested_group_search_depth

    @nested_group_search_depth.setter
    def nested_group_search_depth(self, nested_group_search_depth):
        """
        Sets the nested_group_search_depth of this IamLdapBaseProperties.
        Parameter to search for an LDAP group nested within another defined group in an LDAP group map. The parameter defines the depth of a nested group search  

        :param nested_group_search_depth: The nested_group_search_depth of this IamLdapBaseProperties.
        :type: int
        """

        self._nested_group_search_depth = nested_group_search_depth

    @property
    def password(self):
        """
        Gets the password of this IamLdapBaseProperties.
        Password of the user. Applicable only when BindMethod='ConfiguredCredentials'  

        :return: The password of this IamLdapBaseProperties.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this IamLdapBaseProperties.
        Password of the user. Applicable only when BindMethod='ConfiguredCredentials'  

        :param password: The password of this IamLdapBaseProperties.
        :type: str
        """

        self._password = password

    @property
    def timeout(self):
        """
        Gets the timeout of this IamLdapBaseProperties.
        Timeout in seconds for LDAP authentication process   

        :return: The timeout of this IamLdapBaseProperties.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """
        Sets the timeout of this IamLdapBaseProperties.
        Timeout in seconds for LDAP authentication process   

        :param timeout: The timeout of this IamLdapBaseProperties.
        :type: int
        """

        self._timeout = timeout

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
        if not isinstance(other, IamLdapBaseProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
