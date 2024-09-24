import pytest


@pytest.fixture(scope="module")
def shared_state():
    state = {}
    yield state
    state.clear()  # Clean up after tests


def test_case1(shared_state):
    shared_state['data'] = 'test data'
    assert 'data' in shared_state


def test_case2(shared_state):
    assert shared_state['data'] == 'test data'


@pytest.fixture(scope="class")
def class_state():
    return {}


class TestState:
    def test_case1(self, class_state):
        class_state['data'] = 'test data'
        assert 'data' in class_state

    def test_case2(self, class_state):
        assert class_state.get('data') == 'test data'


@pytest.mark.dependency()
def test_case3():
    return 'test data'


@pytest.mark.dependency(depends=["test_case3"])
def test_case4():
    assert test_case3() == 'test data'
