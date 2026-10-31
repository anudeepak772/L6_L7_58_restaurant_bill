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


def test_bill_total_invalid_section_branch():
    # Evaluates: section not in SERVICE_CHARGE -> True
    with pytest.raises(ValueError, match="unknown section"):
        bill_total("outdoor", 1000, 2, False)


def test_bill_total_invalid_food_total_branch():
    # Evaluates: food_total < 0 -> True
    with pytest.raises(ValueError, match="invalid order"):
        bill_total("dine_in", -10, 2, False)


def test_bill_total_invalid_guests_branch():
    # Evaluates: guests < 1 -> True
    with pytest.raises(ValueError, match="invalid order"):
        bill_total("dine_in", 1000, 0, False)


def test_bill_total_happy_hour_and_not_takeaway_branch():
    # Evaluates: is_happy_hour == True AND section != "takeaway" -> True
    assert bill_total("dine_in", 1000, 2, True) == 924


def test_bill_total_happy_hour_takeaway_branch():
    # Evaluates: is_happy_hour == True AND section != "takeaway" -> False
    assert bill_total("takeaway", 1000, 2, True) == 1050


def test_bill_total_large_party_service_surcharge_branch():
    # Evaluates: guests >= 8 -> True (and rooftop section service charge)
    assert bill_total("rooftop", 1000, 8, False) == 1417


# ==========================================
# Branch Coverage: split_bill()
# ==========================================

def test_split_bill_invalid_people_branch():
    # Evaluates: people < 1 -> True
    with pytest.raises(ValueError, match="invalid people count"):
        split_bill(1000, 0, 10)


def test_split_bill_invalid_tip_branch():
    # Evaluates: tip_percent < 0 -> True
    with pytest.raises(ValueError, match="invalid tip"):
        split_bill(1000, 4, -5)


def test_split_bill_remainder_ceiling_branch():
    # Evaluates: grand_total % people != 0 -> True
    assert split_bill(1000, 3, 10) == 367


# ==========================================
# Branch Coverage: table_wait()
# ==========================================

def test_table_wait_party_too_large_branch():
    # Evaluates: party_size > 12 -> True
    assert table_wait(13, 5, True) == "call ahead"


def test_table_wait_has_reservation_branch():
    # Evaluates: has_reservation -> True
    assert table_wait(4, 0, True) == "seat now"


def test_table_wait_no_free_tables_branch():
    # Evaluates: free_tables == 0 -> True
    assert table_wait(4, 0, False) == "waitlist"


def test_table_wait_large_party_insufficient_tables_branch():
    # Evaluates: party_size > 6 AND free_tables < 2 -> True
    assert table_wait(7, 1, False) == "waitlist"


def test_table_wait_large_party_sufficient_tables_branch():
    # Evaluates: party_size > 6 -> True, free_tables < 2 -> False
    assert table_wait(7, 2, False) == "seat now"

