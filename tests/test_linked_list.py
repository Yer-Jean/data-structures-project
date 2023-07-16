"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest

from src.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_create_linked_list_from_beginning(self):
        ll = LinkedList()

        self.assertEqual(str(ll), "None")
        with self.assertRaises(AttributeError):
            _ = ll.head.data

        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})
        ll.insert_at_end({'id': 4})
        self.assertEqual(ll.head.data, {'id': 0})
        self.assertEqual(ll.head.next_node.data, {'id': 1})
        self.assertEqual(ll.tail.data, {'id': 4})
        with self.assertRaises(AttributeError):
            _ = ll.head.next_node.next_node.next_node.next_node.next_node.data

        self.assertEqual(str(ll), "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> {'id': 4} -> None")

    def test_create_linked_list_from_end(self):
        ll = LinkedList()

        ll.insert_at_end({'id': 2})
        ll.insert_beginning({'id': 1})
        self.assertEqual(ll.head.data, {'id': 1})
        self.assertEqual(ll.head.next_node.data, {'id': 2})
        self.assertEqual(ll.tail.data, {'id': 2})
        with self.assertRaises(AttributeError):
            _ = ll.head.next_node.next_node.next_node.data

        self.assertEqual(str(ll), "{'id': 1} -> {'id': 2} -> None")

    def test_delete(self):
        ll = LinkedList()
        self.assertEqual(ll.delete_beginning(), None)
        self.assertEqual(ll.delete_at_end(), None)

        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})
        self.assertEqual(str(ll), "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")

        ll.delete_at_end()
        ll.delete_beginning()
        self.assertEqual(str(ll), "{'id': 1} -> {'id': 2} -> None")

        ll.delete_beginning()
        ll.delete_at_end()
        self.assertEqual(str(ll), "None")

        ll.insert_beginning({'id': 1})
        ll.delete_beginning()
        self.assertEqual(str(ll), "None")
