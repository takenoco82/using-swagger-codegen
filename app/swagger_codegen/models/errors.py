# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401
from enum import Enum  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_codegen.models.base_model_ import Model  # noqa: F401
from swagger_codegen.models.error import Error  # noqa: F401,E501
from swagger_codegen import util  # noqa: F401


class Errors(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, errors: List[Error]=None):  # noqa: E501
        """Errors - a model defined in Swagger

        :param errors: The errors of this Errors.  # noqa: E501
        :type errors: List[Error]
        """
        self.swagger_types = {
            'errors': List[Error]
        }

        self.attribute_map = {
            'errors': 'errors'
        }

        self._errors = errors

    @classmethod
    def from_dict(cls, dikt) -> 'Errors':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Errors of this Errors.  # noqa: E501
        :rtype: Errors
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
    def errors(self) -> List[Error]:
        """Gets the errors of this Errors.


        :return: The errors of this Errors.
        :rtype: List[Error]
        """
        return self._errors

    @errors.setter
    def errors(self, errors: List[Error]):
        """Sets the errors of this Errors.


        :param errors: The errors of this Errors.
        :type errors: List[Error]
        """
        self._errors = errors
