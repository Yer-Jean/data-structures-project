"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest

from src.queue import Queue


class TestQueue(unittest.TestCase):

    def test_create_queue(self):
        queue = Queue()
        with self.assertRaises(AttributeError):
            _ = queue.head.data
        self.assertEqual(str(Queue()), '')

        queue.enqueue('test1')
        queue.enqueue('test2')
        queue.enqueue('test3')
        self.assertEqual(queue.head.data, 'test1')
        self.assertEqual(queue.head.next_node.data, 'test2')
        self.assertEqual(queue.tail.data, 'test3')
        self.assertIsNone(queue.tail.next_node)
        with self.assertRaises(AttributeError):
            _ = queue.tail.next_node.data

        # Проверяем магический метод __str__
        assert str(queue) == "test1\ntest2\ntest3"
