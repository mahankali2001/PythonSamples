import pytest
from linkedlist import solution, node, linkedlist

@pytest.fixture
def sol_instance():
    return solution()
    
def test_llc1(sol_instance):
    ll = linkedlist(1)
    expected_output = False
    assert sol_instance.findCycleInLL(ll) == expected_output

def test_llc2(sol_instance):
    ll = linkedlist(1)
    n2 = node(2)
    n3 = node(3)
    n4 = node(4)
    ll.head.next = n2
    n2.next = n3
    n3.next = n4
    expected_output = False
    assert sol_instance.findCycleInLL(ll) == expected_output

def test_llc3(sol_instance):
    ll = linkedlist(1)
    n2 = node(2)
    n3 = node(3)
    n4 = node(4)
    ll.head.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2
    expected_output = True
    assert sol_instance.findCycleInLL(ll) == expected_output


#pytest linkedlistcyclicpytest.py