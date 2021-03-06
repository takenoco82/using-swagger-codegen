# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401
from enum import Enum  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_codegen.models.base_model_ import Model  # noqa: F401
from swagger_codegen.models.user import User  # noqa: F401,E501
from swagger_codegen import util  # noqa: F401


class Users(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, users: List[User]=None):  # noqa: E501
        """Users - a model defined in Swagger

        :param users: The users of this Users.  # noqa: E501
        :type users: List[User]
        """
        self.swagger_types = {
            'users': List[User]
        }

        self.attribute_map = {
            'users': 'users'
        }

        self._users = users

    @classmethod
    def from_dict(cls, dikt) -> 'Users':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Users of this Users.  # noqa: E501
        :rtype: Users
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
    def users(self) -> List[User]:
        """Gets the users of this Users.


        :return: The users of this Users.
        :rtype: List[User]
        """
        return self._users

    @users.setter
    def users(self, users: List[User]):
        """Sets the users of this Users.


        :param users: The users of this Users.
        :type users: List[User]
        """
        self._users = users
