import pytest
from restaurant_bill import bill_total, split_bill, table_wait


# Standard execution path through bill_total
def test_bill_total_standard():
    # Covers normal path with service charge and tax
    assert bill_total("dine_in", 1000, 2, False) == 1155


# Standard execution path through split_bill
def test_split_bill_standard():
    # Covers normal division path
    assert split_bill(1000, 4, 10) == 275


# Standard execution path through table_wait
def test_table_wait_standard():
    # Covers normal seating path        
    assert table_wait(4, 1, False) == "seat now"