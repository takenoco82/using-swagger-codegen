# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401
from enum import Enum  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_codegen.models.base_model_ import Model  # noqa: F401
from swagger_codegen.models.contact import Contact  # noqa: F401,E501
from swagger_codegen import util  # noqa: F401


class Employee(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, employee_id: str=None, employee_name: str=None, contact: Contact=None):  # noqa: E501
        """Employee - a model defined in Swagger

        :param employee_id: The employee_id of this Employee.  # noqa: E501
        :type employee_id: str
        :param employee_name: The employee_name of this Employee.  # noqa: E501
        :type employee_name: str
        :param contact: The contact of this Employee.  # noqa: E501
        :type contact: Contact
        """
        self.swagger_types = {
            'employee_id': str,
            'employee_name': str,
            'contact': Contact
        }

        self.attribute_map = {
            'employee_id': 'employee_id',
            'employee_name': 'employee_name',
            'contact': 'contact'
        }

        self._employee_id = employee_id
        self._employee_name = employee_name
        self._contact = contact

    @classmethod
    def from_dict(cls, dikt) -> 'Employee':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Employee of this Employee.  # noqa: E501
        :rtype: Employee
        """
        return util.deserialize_model(dikt, cls)

    def validate(self):
        errors = []
        if self._employee_id is None:
            errors.append({
                "code": "required",
                "field": "employee_id",
                "message": "Invalid value for `employee_id`, must not be `None`"  # noqa: E501
            })
        if self._employee_id is not None and len(self._employee_id) < 1:
            errors.append({
                "code": "minLength",
                "field": "employee_id",
                "message": "Invalid value for `employee_id`, length must be greater than or equal to `1`"  # noqa: E501
            })
        if self._employee_name is not None and len(self._employee_name) < 1:
            errors.append({
                "code": "minLength",
                "field": "employee_name",
                "message": "Invalid value for `employee_name`, length must be greater than or equal to `1`"  # noqa: E501
            })
        if self._contact is None:
            errors.append({
                "code": "required",
                "field": "contact",
                "message": "Invalid value for `contact`, must not be `None`"  # noqa: E501
            })
        # TODO Object(Modelのサブクラス) のチェック処理を追加

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
    def employee_id(self) -> str:
        """Gets the employee_id of this Employee.


        :return: The employee_id of this Employee.
        :rtype: str
        """
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id: str):
        """Sets the employee_id of this Employee.


        :param employee_id: The employee_id of this Employee.
        :type employee_id: str
        """
        self._employee_id = employee_id

    @property
    def employee_name(self) -> str:
        """Gets the employee_name of this Employee.


        :return: The employee_name of this Employee.
        :rtype: str
        """
        return self._employee_name

    @employee_name.setter
    def employee_name(self, employee_name: str):
        """Sets the employee_name of this Employee.


        :param employee_name: The employee_name of this Employee.
        :type employee_name: str
        """
        self._employee_name = employee_name

    @property
    def contact(self) -> Contact:
        """Gets the contact of this Employee.


        :return: The contact of this Employee.
        :rtype: Contact
        """
        return self._contact

    @contact.setter
    def contact(self, contact: Contact):
        """Sets the contact of this Employee.


        :param contact: The contact of this Employee.
        :type contact: Contact
        """
        self._contact = contact
