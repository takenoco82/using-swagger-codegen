import unittest
# from swagger_server import log
from app.swagger_codegen.models.write_user import WriteUser
from parameterized import parameterized, param
from datetime import datetime


# logger = log.get_logger(__name__)


class TestClassName(unittest.TestCase):
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
            "all success",
            input={
                "username": "username1",
                "first_name": "first_name1",
                "last_name": "last_name1",
                "email": "hoge@example.com",
                "password": "password1",
                "phone": "09012345678",
                "user_status": 1,
                "height": 173.5,
                "born_on": "2001-10-15T12:34:56Z"
            },
            expected={
                "username": "username1",
                "first_name": "first_name1",
                "last_name": "last_name1",
                "email": "hoge@example.com",
                "password": "password1",
                "phone": "09012345678",
                "user_status": 1,
                "height": 173.5,
                "born_on": datetime(2001, 10, 15, 12, 34, 56)
            }),
        param(
            "no first_name",
            input={
                "username": "username1",
                # "first_name": "first_name1",
                "last_name": "last_name1",
                "email": "hoge@example.com",
                "password": "password1",
                "phone": "09012345678",
                "user_status": 1,
                "height": 173.5,
                "born_on": "2001-10-15T12:34:56Z"
            },
            expected={
                "username": "username1",
                "first_name": None,
                "last_name": "last_name1",
                "email": "hoge@example.com",
                "password": "password1",
                "phone": "09012345678",
                "user_status": 1,
                "height": 173.5,
                "born_on": datetime(2001, 10, 15, 12, 34, 56)
            }),
        param(
            "no user_status",
            input={
                "username": "username1",
                "first_name": "first_name1",
                "last_name": "last_name1",
                "email": "hoge@example.com",
                "password": "password1",
                "phone": "09012345678",
                "user_status": "string",
                "height": 173.5,
                "born_on": "2001-10-15T12:34:56Z"
            },
            expected={
                "username": "username1",
                "first_name": "first_name1",
                "last_name": "last_name1",
                "email": "hoge@example.com",
                "password": "password1",
                "phone": "09012345678",
                "user_status": None,
                "height": 173.5,
                "born_on": datetime(2001, 10, 15, 12, 34, 56)
            }),
        param(
            "no born_on",
            input={
                "username": "username1",
                "first_name": "first_name1",
                "last_name": "last_name1",
                "email": "hoge@example.com",
                "password": "password1",
                "phone": "09012345678",
                "user_status": 1,
                "height": 173.5,
                "born_on": "2001-10-15T12:34:56"
            },
            expected={
                "username": "username1",
                "first_name": "first_name1",
                "last_name": "last_name1",
                "email": "hoge@example.com",
                "password": "password1",
                "phone": "09012345678",
                "user_status": 1,
                "height": 173.5,
                "born_on": None
            })
    ])
    def test_from_dict(self, _, input, expected):
        user = WriteUser.from_dict(input)

        self.assertEqual(user.username, expected["username"])
        self.assertEqual(user.first_name, expected["first_name"])
        self.assertEqual(user.last_name, expected["last_name"])
        self.assertEqual(user.email, expected["email"])
        self.assertEqual(user.password, expected["password"])
        self.assertEqual(user.phone, expected["phone"])
        self.assertEqual(user.user_status, expected["user_status"])
        self.assertEqual(user.height, expected["height"])
        self.assertEqual(user.born_on, expected["born_on"])

    @parameterized.expand([
        param(
            "no error",
            input={
                "username": "username1",
                "first_name": "first_name1",
                "last_name": "last_name1",
                "email": "hoge@example.com",
                "password": "password1",
                "phone": "09012345678",
                "user_status": 1,
                "height": 173.5,
                "born_on": "2001-10-15T12:34:56Z"
            },
            expected=[]),
        param(
            "required",
            input={
                "username": "username1",
                # "first_name": "first_name1",
                "last_name": "last_name1",
                "email": "hoge@example.com",
                "password": "password1",
                "phone": "09012345678",
                "user_status": 1,
                "height": 173.5,
                "born_on": "2001-10-15T12:34:56Z"
            },
            expected=[
                {
                    "code": "required",
                    "field": "first_name",
                    "message": "Invalid value for `first_name`, must not be `None`"
                }
            ]),
        param(
            "maxLength",
            input={
                "username": "12345678901234567",
                "first_name": "first_name1",
                "last_name": "last_name1",
                "email": "hoge@example.com",
                "password": "password1",
                "phone": "09012345678",
                "user_status": 1,
                "height": 173.5,
                "born_on": "2001-10-15T12:34:56Z"
            },
            expected=[
                {
                    "code": "maxLength",
                    "field": "username",
                    "message": "Invalid value for `username`, length must be less than or equal to `16`"
                }
            ]),
        param(
            "minLength",
            input={
                "username": "username1",
                "first_name": "first_name1",
                "last_name": "last_name1",
                "email": "hoge@example.com",
                "password": "pw",
                "phone": "09012345678",
                "user_status": 1,
                "height": 173.5,
                "born_on": "2001-10-15T12:34:56Z"
            },
            expected=[
                {
                    "code": "minLength",
                    "field": "password",
                    "message": "Invalid value for `password`, length must be greater than or equal to `4`"
                }
            ]),
        param(
            "type integer",
            input={
                "username": "username1",
                "first_name": "first_name1",
                "last_name": "last_name1",
                "email": "hoge@example.com",
                "password": "password1",
                "phone": "09012345678",
                "user_status": "a",
                "height": 173.5,
                "born_on": "2001-10-15T12:34:56Z"
            },
            expected=[
                {
                    "code": "type",
                    "field": "user_status",
                    "message": "Invalid value for `user_status`, type must be `integer`"
                }
            ]),
        param(
            "type float",
            input={
                "username": "username1",
                "first_name": "first_name1",
                "last_name": "last_name1",
                "email": "hoge@example.com",
                "password": "password1",
                "phone": "09012345678",
                "user_status": 1,
                "height": "a",
                "born_on": "2001-10-15T12:34:56Z"
            },
            expected=[
                {
                    "code": "type",
                    "field": "height",
                    "message": "Invalid value for `height`, type must be `float`"
                }
            ]),
        param(
            "type datetime",
            input={
                "username": "username1",
                "first_name": "first_name1",
                "last_name": "last_name1",
                "email": "hoge@example.com",
                "password": "password1",
                "phone": "09012345678",
                "user_status": 1,
                "height": 173.5,
                "born_on": "2001-10-15T12:34:56"
            },
            expected=[
                {
                    "code": "type",
                    "field": "born_on",
                    "message": "Invalid value for `born_on`, type must be `datetime`"
                }
            ]),
        param(
            "x-digit",
            input={
                "username": "username1",
                "first_name": "first_name1",
                "last_name": "last_name1",
                "email": "hoge@example.com",
                "password": "password1",
                "phone": "09012a45678",
                "user_status": 1,
                "height": 173.5,
                "born_on": "2001-10-15T12:34:56Z"
            },
            expected=[
                {
                    "code": "digit",
                    "field": "phone",
                    "message": "Invalid value for `phone`, must not be only digit"
                }
            ])
    ])
    def test_validate(self, _, input, expected):
        user = WriteUser.from_dict(input)
        errors = user.validate()

        self.assertEqual(len(errors), len(expected))
        for index, expected_error in enumerate(expected):
            self.assertEqual(errors[index].get("code"), expected_error["code"])
            self.assertEqual(errors[index].get("message"), expected_error["message"])


if __name__ == '__main__':
    unittest.main()
