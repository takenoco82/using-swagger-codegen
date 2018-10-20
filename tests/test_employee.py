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


if __name__ == '__main__':
    unittest.main()
