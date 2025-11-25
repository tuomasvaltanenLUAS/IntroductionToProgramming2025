def get_energy_costs(y_count, m_cons, p_kwh, m_fee):
    # year = 12 * monthly consumption
    year_consumption = m_cons * 12
    total = 0

    # calculate all years
    for y in range(y_count):
        year_energy_cost = year_consumption * (p_kwh / 100)
        year_cost = (year_energy_cost + (12 * m_fee)) * 1.24

        total += year_cost
        # prices increase each year
        p_kwh += 0.35
        m_fee += 0.15

    # round to two decimals and return result
    total = round(total, 2)
    return total




