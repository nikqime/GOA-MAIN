def water_in_litres(hours):
    water_per_hour = 0.5
    total_water = water_per_hour * hours
    return int(total_water)
hours_cycling = 3
water_consumed = water_in_litres(hours_cycling)
print("Nathan will drink approximately", water_consumed, "litres of water while cycling for", hours_cycling, "hours.")