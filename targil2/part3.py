from datetime import datetime, timedelta

def generate_dates(start_date_str, num_dates, day_skip):
    return list(map(lambda x: datetime.strptime(start_date_str, "%Y-%m-%d") + timedelta(days=x * day_skip), range(num_dates)))


print(generate_dates("2024-01-01",5,2))