import unittest
from app.swagger_codegen.models.employee import Employee
from app.swagger_codegen.models.contact import Contact
from parameterized import parameterized, param
from datetime import datetime


class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @parameterized.expand([
        param(
            "all",
            input={
                "employee_id": "0001",
                "employee_name": "employee_name1",
                "contact": {
                    "phone": "09012345678",
                    "address": "address1"
                }
            },
            expected=Employee(
                "0001",
                "employee_name1",
                Contact(
                    "09012345678",
                    "address1"
                )
            )),
        param(
            "no contact",
            input={
                "employee_id": "0001",
                "employee_name": "employee_name1",
                # "contact": {
                #     "phone": "09012345678",
                #     "address": "address1"
                # }
            },
            expected=Employee(
                "0001",
                "employee_name1"
            )),
    ])
    def test_from_dict(self, _, input, expected):
        employee = Employee.from_dict(input)

        self.assertEqual(employee, expected)

    @parameterized.expand([
        param(
            "no error",
            input={
                "employee_id": "0001",
                "employee_name": "employee_name1",
                "contact": {
                    "phone": "09012345678",
                    "address": "address1"
                }
            },
            expected=[]),
        param(
            "required employee_name",
            input={
                # "employee_id": "0001",
                "employee_name": "employee_name1",
                "contact": {
                    "phone": "09012345678",
                    "address": "address1"
                }
            },
            expected=[
                {
                    "code": "required",
                    "field": "employee_id",
                    "message": "Invalid value for `employee_id`, must not be `None`"
                }
            ]),
        param(
            "required contact",
            input={
                "employee_id": "0001",
                "employee_name": "employee_name1",
                # "contact": {
                #     "phone": "09012345678",
                #     "address": "address1"
                # }
            },
            expected=[
                {
                    "code": "required",
                    "field": "contact",
                    "message": "Invalid value for `contact`, must not be `None`"
                }
            ]),
        param(
            "required phone",
            input={
                "employee_id": "0001",
                "employee_name": "employee_name1",
                "contact": {
                    # "phone": "09012345678",
                    "address": "address1"
                }
            },
            expected=[
                {
                    "code": "required",
                    "field": "phone",
                    "message": "Invalid value for `phone`, must not be `None`"
                }
            ]),
    ])
    def test_validate(self, _, input, expected):
        employee = Employee.from_dict(input)
        errors = employee.validate()

        self.assertEqual(errors, expected)


if __name__ == '__main__':
    unittest.main()
