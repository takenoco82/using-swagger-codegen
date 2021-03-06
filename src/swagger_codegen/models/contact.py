# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401
from enum import Enum  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_codegen.models.base_model_ import Model  # noqa: F401
from swagger_codegen import util  # noqa: F401


class Contact(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, phone: str=None, address: str=None):  # noqa: E501
        """Contact - a model defined in Swagger

        :param phone: The phone of this Contact.  # noqa: E501
        :type phone: str
        :param address: The address of this Contact.  # noqa: E501
        :type address: str
        """
        self.swagger_types = {
            'phone': str,
            'address': str
        }

        self.attribute_map = {
            'phone': 'phone',
            'address': 'address'
        }

        self._phone = phone
        self._address = address

    @classmethod
    def from_dict(cls, dikt) -> 'Contact':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Contact of this Contact.  # noqa: E501
        :rtype: Contact
        """
        return util.deserialize_model(dikt, cls)

    def validate(self):
        errors = []
        if self._phone is None:
            errors.append({
                "code": "required",
                "field": "phone",
                "message": "Invalid value for `phone`, must not be `None`"  # noqa: E501
            })
        if self._phone is not None and len(self._phone) < 1:
            errors.append({
                "code": "minLength",
                "field": "phone",
                "message": "Invalid value for `phone`, length must be greater than or equal to `1`"  # noqa: E501
            })
        if self._address is not None and len(self._address) < 1:
            errors.append({
                "code": "minLength",
                "field": "address",
                "message": "Invalid value for `address`, length must be greater than or equal to `1`"  # noqa: E501
            })

        for attr, attr_type in self.swagger_types.items():
            # List[xxx] の場合
            if type(List) == type(attr_type):
                attr_values = getattr(self, attr)
                if not attr_values:
                    continue
                for i, attr_value in enumerate(attr_values):  # pylint: disable=E1133
                    attr_errors = attr_value.validate()
                    for attr_error in attr_errors:
                        attr_error["field"] = "{parent_attr}[{index}]{child_attr}".format(
                            parent_attr=attr, index=i, child_attr=attr_error["field"])
                    errors.extend(attr_errors)

            # Model のサブクラスの場合
            elif issubclass(attr_type, Model):
                attr_value = getattr(self, attr)
                if not attr_value:
                    continue
                attr_errors = attr_value.validate()
                for attr_error in attr_errors:
                    attr_error["field"] = "{parent_attr}.{child_attr}".format(
                        parent_attr=attr, child_attr=attr_error["field"])
                errors.extend(attr_errors)
        return errors

    @property
    def phone(self) -> str:
        """Gets the phone of this Contact.


        :return: The phone of this Contact.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone: str):
        """Sets the phone of this Contact.


        :param phone: The phone of this Contact.
        :type phone: str
        """
        self._phone = phone

    @property
    def address(self) -> str:
        """Gets the address of this Contact.


        :return: The address of this Contact.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address: str):
        """Sets the address of this Contact.


        :param address: The address of this Contact.
        :type address: str
        """
        self._address = address
