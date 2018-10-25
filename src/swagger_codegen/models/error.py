# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401
from enum import Enum  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_codegen.models.base_model_ import Model  # noqa: F401
from swagger_codegen import util  # noqa: F401


class Error(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, code: str=None, field: str=None, message: str=None):  # noqa: E501
        """Error - a model defined in Swagger

        :param code: The code of this Error.  # noqa: E501
        :type code: str
        :param field: The field of this Error.  # noqa: E501
        :type field: str
        :param message: The message of this Error.  # noqa: E501
        :type message: str
        """
        self.swagger_types = {
            'code': str,
            'field': str,
            'message': str
        }

        self.attribute_map = {
            'code': 'code',
            'field': 'field',
            'message': 'message'
        }

        self._code = code
        self._field = field
        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'Error':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Error of this Error.  # noqa: E501
        :rtype: Error
        """
        return util.deserialize_model(dikt, cls)

    def validate(self):
        errors = []

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
    def code(self) -> str:
        """Gets the code of this Error.


        :return: The code of this Error.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code: str):
        """Sets the code of this Error.


        :param code: The code of this Error.
        :type code: str
        """
        self._code = code

    @property
    def field(self) -> str:
        """Gets the field of this Error.


        :return: The field of this Error.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field: str):
        """Sets the field of this Error.


        :param field: The field of this Error.
        :type field: str
        """
        self._field = field

    @property
    def message(self) -> str:
        """Gets the message of this Error.


        :return: The message of this Error.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this Error.


        :param message: The message of this Error.
        :type message: str
        """
        self._message = message