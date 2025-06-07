from datetime import datetime

"""
Contribution schedule for 'Hi, mom!' text
Arrays represent weeks of the year;
1's represent the days to contribute on for each week (Sun-Sat)
"""
hi_mom = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
]

def is_contribution_day(today: datetime) -> bool:
    """
    Determines if a day is a contribution day based on the week and weekday.
    
    Args:
        week (int): Week number of the year (ISO calendar)
        weekday (int): Day of the week (1-7, where 1 is Monday in ISO calendar)
    
    Returns:
        bool: True if the day is a contribution day, False otherwise
    """

    week = today.isocalendar().week - 1  # Convert to 0-based for array indexing
    weekday = today.isocalendar().weekday % 7  # Convert Sunday (7) to 0, Monday (1) to 1, etc.
    
    if 0 <= week < len(hi_mom):
        return hi_mom[week][weekday] == 1
    else:
        # If the week is outside of the hi_mom array range, only contribute on Wednesdays
        # to draw a horizontal line across the centre of the contribution calendar
        return weekday == 3
