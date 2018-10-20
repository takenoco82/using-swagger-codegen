import unittest
# from swagger_server import log
from app.swagger_codegen.models.parent import Parent
from app.swagger_codegen.models.child import Child
from app.swagger_codegen.models.grandchild import Grandchild
from parameterized import parameterized, param


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
                "parent_field1": "parent_value1",
                "parent_field2": "parent_value2",
                "children": [
                    {
                        "child_field1": "child_value11",
                        "child_field2": "child_value12",
                        "grandchildren": [
                            {
                                "grandchild_field1": "grandchild_value111",
                                "grandchild_field2": "grandchild_value112",
                            },
                            {
                                "grandchild_field1": "grandchild_value121",
                                "grandchild_field2": "grandchild_value122",
                            }
                        ]
                    },
                    {
                        "child_field1": "child_value21",
                        "child_field2": "child_value22",
                        "grandchildren": [
                            {
                                "grandchild_field1": "grandchild_value211",
                                "grandchild_field2": "grandchild_value212",
                            }
                        ]
                    }
                ],
            },
            expected=Parent(
                "parent_value1",
                "parent_value2",
                [
                    Child(
                        "child_value11",
                        "child_value12",
                        [
                            Grandchild("grandchild_value111", "grandchild_value112"),
                            Grandchild("grandchild_value121", "grandchild_value122")]),
                    Child(
                        "child_value21",
                        "child_value22",
                        [
                            Grandchild("grandchild_value211", "grandchild_value212")])
                ]
            )
        ),
        param(
            "no children",
            input={
                "parent_field1": "parent_value1",
                "parent_field2": "parent_value2",
            },
            expected=Parent(
                "parent_value1",
                "parent_value2"
            )
        ),
        param(
            "no grandchildren",
            input={
                "parent_field1": "parent_value1",
                "parent_field2": "parent_value2",
                "children": [
                    {
                        "child_field1": "child_value11",
                        "child_field2": "child_value12",
                    },
                    {
                        "child_field1": "child_value21",
                        "child_field2": "child_value22",
                        "grandchildren": [
                            {
                                "grandchild_field1": "grandchild_value211",
                                "grandchild_field2": "grandchild_value212",
                            }
                        ]
                    }
                ],
            },
            expected=Parent(
                "parent_value1",
                "parent_value2",
                [
                    Child(
                        "child_value11",
                        "child_value12"),
                    Child(
                        "child_value21",
                        "child_value22",
                        [
                            Grandchild("grandchild_value211", "grandchild_value212")])
                ]
            )
        ),
    ])
    def test_from_dict(self, _, input, expected):
        parent = Parent.from_dict(input)

        print("actual={}".format(parent))
        print("expected={}".format(expected))
        self.assertEqual(parent, expected)

    @parameterized.expand([
        param(
            "no error",
            input={
                "parent_field1": "parent_value1",
                "parent_field2": "parent_value2",
                "children": [
                    {
                        "child_field1": "child_value11",
                        "child_field2": "child_value12",
                        "grandchildren": [
                            {
                                "grandchild_field1": "grandchild_value111",
                                "grandchild_field2": "grandchild_value112",
                            },
                            {
                                "grandchild_field1": "grandchild_value121",
                                "grandchild_field2": "grandchild_value122",
                            }
                        ]
                    },
                    {
                        "child_field1": "child_value21",
                        "child_field2": "child_value22",
                        "grandchildren": [
                            {
                                "grandchild_field1": "grandchild_value211",
                                "grandchild_field2": "grandchild_value212",
                            }
                        ]
                    }
                ],
            },
            expected=[]),
        param(
            "required child_field1",
            input={
                "parent_field1": "parent_value1",
                "parent_field2": "parent_value2",
                "children": [
                    {
                        # "child_field1": "child_value11",
                        "child_field2": "child_value12",
                        "grandchildren": [
                            {
                                "grandchild_field1": "grandchild_value111",
                                "grandchild_field2": "grandchild_value112",
                            },
                            {
                                "grandchild_field1": "grandchild_value121",
                                "grandchild_field2": "grandchild_value122",
                            }
                        ]
                    },
                    {
                        "child_field1": "child_value21",
                        "child_field2": "child_value22",
                        "grandchildren": [
                            {
                                "grandchild_field1": "grandchild_value211",
                                "grandchild_field2": "grandchild_value212",
                            }
                        ]
                    }
                ],
            },
            expected=[
                {
                    "code": "required",
                    "field": "child_field1",
                    "message": "Invalid value for `child_field1`, must not be `None`"
                }
            ]),
        param(
            "required grandchild_field1",
            input={
                "parent_field1": "parent_value1",
                "parent_field2": "parent_value2",
                "children": [
                    {
                        "child_field1": "child_value11",
                        "child_field2": "child_value12",
                        "grandchildren": [
                            {
                                # "grandchild_field1": "grandchild_value111",
                                "grandchild_field2": "grandchild_value112",
                            },
                            {
                                "grandchild_field1": "grandchild_value121",
                                "grandchild_field2": "grandchild_value122",
                            }
                        ]
                    },
                    {
                        "child_field1": "child_value21",
                        "child_field2": "child_value22",
                        "grandchildren": [
                            {
                                "grandchild_field1": "grandchild_value211",
                                "grandchild_field2": "grandchild_value212",
                            }
                        ]
                    }
                ],
            },
            expected=[
                {
                    "code": "required",
                    "field": "grandchild_field1",
                    "message": "Invalid value for `grandchild_field1`, must not be `None`"
                }
            ]),
        param(
            "required multi",
            input={
                "parent_field1": "parent_value1",
                "parent_field2": "parent_value2",
                "children": [
                    {
                        "child_field1": "child_value11",
                        "child_field2": "child_value12",
                        "grandchildren": [
                            {
                                # "grandchild_field1": "grandchild_value111",
                                "grandchild_field2": "grandchild_value112",
                            },
                            {
                                "grandchild_field1": "grandchild_value121",
                                "grandchild_field2": "grandchild_value122",
                            }
                        ]
                    },
                    {
                        # "child_field1": "child_value21",
                        "child_field2": "child_value22",
                        "grandchildren": [
                            {
                                "grandchild_field1": "grandchild_value211",
                                "grandchild_field2": "grandchild_value212",
                            }
                        ]
                    }
                ],
            },
            expected=[
                {
                    "code": "required",
                    "field": "grandchild_field1",
                    "message": "Invalid value for `grandchild_field1`, must not be `None`"
                },
                {
                    "code": "required",
                    "field": "child_field1",
                    "message": "Invalid value for `child_field1`, must not be `None`"
                }
            ]),
        param(
            "required children",
            input={
                "parent_field1": "parent_value1",
                "parent_field2": "parent_value2",
            },
            expected=[
                {
                    "code": "required",
                    "field": "children",
                    "message": "Invalid value for `children`, must not be `None`"
                }
            ]),
        param(
            "required grandchildren",
            input={
                "parent_field1": "parent_value1",
                "parent_field2": "parent_value2",
                "children": [
                    {
                        "child_field1": "child_value11",
                        "child_field2": "child_value12",
                    },
                    {
                        "child_field1": "child_value21",
                        "child_field2": "child_value22",
                        "grandchildren": [
                            {
                                "grandchild_field1": "grandchild_value211",
                                "grandchild_field2": "grandchild_value212",
                            }
                        ]
                    }
                ],
            },
            expected=[
                {
                    "code": "required",
                    "field": "grandchildren",
                    "message": "Invalid value for `grandchildren`, must not be `None`"
                }
            ]),
    ])
    def test_validate(self, _, input, expected):
        parent = Parent.from_dict(input)
        errors = parent.validate()

        self.assertEqual(len(errors), len(expected))
        for index, expected_error in enumerate(expected):
            self.assertEqual(errors[index].get("code"), expected_error["code"])
            self.assertEqual(errors[index].get("field"), expected_error["field"])
            self.assertEqual(errors[index].get("message"), expected_error["message"])


if __name__ == '__main__':
    unittest.main()
