def estimate_budget(flight_price, hotel_price_per_night, nights):
    """
    Estimate total trip cost
    """
    hotel_total = hotel_price_per_night * nights
    food_and_local = 2500

    return {
        "flight": flight_price,
        "hotel": hotel_total,
        "food_and_local": food_and_local,
        "total_cost": flight_price + hotel_total + food_and_local
    }
