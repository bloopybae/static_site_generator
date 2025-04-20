import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_not_eq_different_text(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("Different text", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_not_eq_different_type(self):
        node1 = TextNode("Same text", TextType.BOLD)
        node2 = TextNode("Same text", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_eq_with_url(self):
        node1 = TextNode("Link text", TextType.LINK, "https://example.com")
        node2 = TextNode("Link text", TextType.LINK, "https://example.com")
        self.assertEqual(node1, node2)

    def test_not_eq_different_url(self):
        node1 = TextNode("Link text", TextType.LINK, "https://example.com")
        node2 = TextNode("Link text", TextType.LINK, "https://another.com")
        self.assertNotEqual(node1, node2)

    def test_default_url_none(self):
        node1 = TextNode("No URL", TextType.TEXT)
        self.assertIsNone(node1.url)

if __name__ == "__main__":
    unittest.main()

