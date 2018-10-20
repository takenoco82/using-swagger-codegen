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
        )
    ])
    def test_from_dict(self, _, input, expected):
        parent = Parent.from_dict(input)

        self.assertEqual(parent.parent_field1, expected.parent_field1)
        self.assertEqual(len(parent.children), len(expected.children))
        for i, expected_child in enumerate(expected.children):
            child = parent.children[i]
            self.assertEqual(child.child_field1, expected_child.child_field1)
            self.assertEqual(len(child.grandchildren), len(expected_child.grandchildren))
            for i, expected_grandchild in enumerate(expected_child.grandchildren):
                grandchild = child.grandchildren[i]
                self.assertEqual(grandchild.grandchild_field1, expected_grandchild.grandchild_field1)


if __name__ == '__main__':
    unittest.main()
