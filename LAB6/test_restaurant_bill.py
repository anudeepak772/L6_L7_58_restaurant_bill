import pytest
from restaurant_bill import bill_total, split_bill, table_wait

#Example test cases:
def test_dine_in_bill():
    assert bill_total("dine_in", 1000, 2, False) == 1155

def test_even_split():
    assert split_bill(1000, 4, 10) == 275

#Write the rest of the test cases so that the code is 90- 100% covered.

def test_dine_in_bill():
    # 1000 food + 10% service (100) = 1100 total + 5% tax (55) = 1155
    assert bill_total("dine_in", 1000, 2, False) == 1155

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


