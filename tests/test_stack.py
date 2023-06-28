"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import pytest

from src.stack import Node, Stack


def test_create_stack():
    node1 = Node('Test', None)
    node2 = Node({'Test1', 'Test2'}, None)
    node3 = Node(3.141592, None)
    assert node1.data == 'Test'
    assert node2.data == {'Test1', 'Test2'}
    assert node3.data == 3.141592

def test_push_to_stack():
    stack = Stack()
    assert stack.top == None
    stack.push('Level1')
    stack.push('Level2')
    stack.push('Level3')
    assert stack.top.data == 'Level3'
    assert stack.top.next_node.data == 'Level2'
    assert stack.top.next_node.next_node.data == 'Level1'
    with pytest.raises(AttributeError):
        stack.top.next_node.next_node.next_node.data
