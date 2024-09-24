import logging


def test_add():
    assert 2 + 2 == 4, "asserting addition"
    print("good morning")
    logging.info("test_add")


def test_sub():
    assert 2 - 3 == -1, "asserting subtraction"
    print("hellow world")
    logging.info("test_sub")


def test_mul():
    assert 2 * 2 == 4, "multiplication failure "
    print("hello sir")
    logging.info("test_mul")
