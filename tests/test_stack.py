"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest

from src.stack import Node, Stack


# def test_create_stack():
class TestStack(unittest.TestCase):
    def test_create_stack(self):
        node1 = Node('Test', None)
        node2 = Node({'Test1', 'Test2'}, None)
        node3 = Node(3.141592, None)
        self.assertEqual(node1.data, 'Test')
        self.assertEqual(node2.data, {'Test1', 'Test2'})
        self.assertEqual(node3.data, 3.141592)

    def test_push_to_stack(self):
        stack = Stack()
        self.assertEqual(stack.top, None)
        stack.push('Level1')
        stack.push('Level2')
        stack.push('Level3')
        self.assertEqual(stack.top.data, 'Level3')
        self.assertEqual(stack.top.next_node.data, 'Level2')
        self.assertEqual(stack.top.next_node.next_node.data, 'Level1')
        with self.assertRaises(AttributeError):
            _ = stack.top.next_node.next_node.next_node.data

    def test_pop_from_stack(self):
        stack = Stack()
        stack.push('Level1')
        stack.push('Level2')
        self.assertEqual(stack.top.data, 'Level2')
        self.assertEqual(stack.pop(), 'Level2')
        self.assertEqual(stack.top.data, 'Level1')
        stack.pop()
        self.assertEqual(stack.pop(), None)


if __name__ == '__main__':
    unittest.main()
