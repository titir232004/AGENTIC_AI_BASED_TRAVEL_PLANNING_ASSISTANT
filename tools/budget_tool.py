def estimate_budget(flight_price, hotel_price_per_night, nights, food_and_local):
    hotel_total = hotel_price_per_night * nights

    return {
        "flight": flight_price,
        "hotel": hotel_total,
        "food_and_local": food_and_local,
        "total_cost": flight_price + hotel_total + food_and_local
    }
