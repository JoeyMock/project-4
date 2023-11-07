"""
Nose tests for acp_times.py

Write your tests HERE AND ONLY HERE.
"""

import nose    # Testing framework
import logging
import ../acp_times.py
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

def test first():
    assert  open_time(200, 200, arrow.now()) == arrow.now().shift(hours = 200/34)
    assert  close_time(200, 200, arrow.now()) == arrow.now().shift(hours = 200/15)

def test greater():
    assert open_time(205, 200, arrow.now()) == arrow.now().shift(hours = 200/34)

def test less():
    assert open_time(190, 200, arrow.now()) == arrow.now().shift(hours = 190/34)

def test bigger():
    assert open_time(300, 300, arrow.now()) == arrow.now().shift(hours = (200/34+100/32))

def test eBigger():
    assert open_time(600, 600, arrow.now()) == arrow.now().shift(hours = (200/34+200/32+200/30))
