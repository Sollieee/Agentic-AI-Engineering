
import math


def calculate_fertilizer_budget(
    farm_area_ha: float,
    application_rate_kg_ha: float,
    bag_size_kg: float,
    price_per_bag: float,
    transport_cost: float = 0,
    labour_cost: float = 0,
) -> dict:
    """Calculate fertilizer quantity and estimated budget."""

    values = {
        "farm_area_ha": farm_area_ha,
        "application_rate_kg_ha": application_rate_kg_ha,
        "bag_size_kg": bag_size_kg,
        "price_per_bag": price_per_bag,
        "transport_cost": transport_cost,
        "labour_cost": labour_cost,
    }

    for name, value in values.items():
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be a number.")

        if not math.isfinite(value):
            raise ValueError(f"{name} must be a finite number.")

        if value < 0:
            raise ValueError(f"{name} cannot be negative.")

    if farm_area_ha <= 0:
        raise ValueError("Farm area must be greater than zero.")

    if application_rate_kg_ha <= 0:
        raise ValueError("Application rate must be greater than zero.")

    if bag_size_kg <= 0:
        raise ValueError("Bag size must be greater than zero.")

    if price_per_bag <= 0:
        raise ValueError("Price per bag must be greater than zero.")

    total_fertilizer_kg = farm_area_ha * application_rate_kg_ha

    bags_needed = math.ceil(total_fertilizer_kg / bag_size_kg)

    fertilizer_cost = bags_needed * price_per_bag

    total_cost = fertilizer_cost + transport_cost + labour_cost

    return {
        "farm_area_ha": farm_area_ha,
        "total_fertilizer_kg": total_fertilizer_kg,
        "bag_size_kg": bag_size_kg,
        "bags_needed": bags_needed,
        "fertilizer_cost": round(fertilizer_cost, 2),
        "transport_cost": round(transport_cost, 2),
        "labour_cost": round(labour_cost, 2),
        "total_cost": round(total_cost, 2),
    }
