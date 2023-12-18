def is_valid_date(date_str):
    try:
        day, month, year = map(int, date_str.split('.'))
        
        if month < 1 or month > 12:
            return False
        
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if day < 1 or day > 31:
                return False
        elif month in [4, 6, 9, 11]:
            if day < 1 or day > 30:
                return False
        else:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                if day < 1 or day > 29:
                    return False
            else:
                if day < 1 or day > 28:
                    return False
        
        return True
    except (ValueError, IndexError):
        return False

# Пример использования
date_to_prove = "15.4.2023"
result = is_valid_date(date_to_prove)
print(result)  # Выведет True

date_to_prove = '0.5.2022'
result = is_valid_date(date_to_prove)
print(result)  # Выведет False

