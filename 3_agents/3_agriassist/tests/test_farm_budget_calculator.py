
import pytest

from tools.farm_budget_calculator import calculate_fertilizer_budget


def test_calculates_fertilizer_budget():
    result = calculate_fertilizer_budget(
        farm_area_ha=2,
        application_rate_kg_ha=200,
        bag_size_kg=50,
        price_per_bag=45000,
        transport_cost=10000,
        labour_cost=15000,
    )

    assert result["total_fertilizer_kg"] == 400
    assert result["bags_needed"] == 8
    assert result["fertilizer_cost"] == 360000
    assert result["total_cost"] == 385000


def test_rounds_bags_up():
    result = calculate_fertilizer_budget(
        farm_area_ha=1,
        application_rate_kg_ha=101,
        bag_size_kg=50,
        price_per_bag=45000,
    )

    assert result["bags_needed"] == 3
    assert result["fertilizer_cost"] == 135000


@pytest.mark.parametrize(
    "field, value",
    [
        ("farm_area_ha", 0),
        ("farm_area_ha", -1),
        ("application_rate_kg_ha", 0),
        ("bag_size_kg", 0),
        ("price_per_bag", 0),
        ("transport_cost", -1),
        ("labour_cost", -1),
    ],
)
def test_rejects_invalid_numeric_values(field, value):
    params = {
        "farm_area_ha": 2,
        "application_rate_kg_ha": 200,
        "bag_size_kg": 50,
        "price_per_bag": 45000,
        "transport_cost": 0,
        "labour_cost": 0,
    }

    params[field] = value

    with pytest.raises(ValueError):
        calculate_fertilizer_budget(**params)


def test_rejects_invalid_type():
    with pytest.raises(TypeError):
        calculate_fertilizer_budget(
            farm_area_ha="two",
            application_rate_kg_ha=200,
            bag_size_kg=50,
            price_per_bag=45000,
        )
