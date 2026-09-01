"""
Garden Advice App - Provides gardening tips based on month and season

This application helps gardening enthusiasts get appropriate gardening advice
based on the current month and season. The code has been fully documented
with comprehensive docstrings following PEP 257 conventions.

Example:
    $ python garden_advice.py
    Welcome to the Garden Advice App!
    Enter month number (1-12): 6
    ============================================================
    GARDENING ADVICE FOR TODAY
    ============================================================
    
    Season: Summer
    Advice: Water plants regularly, harvest vegetables, and watch for pests.
    
    Monthly Task for Month 6:
    Water deeply during dry spells.
    
    ============================================================
    Thank you for using the Garden Advice App!
"""

import datetime


# Constants

# Seasonal gardening advice dictionary
SEASONAL_ADVICE = {
    "Spring": "Plant new flowers, prepare soil, and start vegetable seeds.",
    "Summer": "Water plants regularly, harvest vegetables, and watch for pests.",
    "Autumn": "Clean up fallen leaves, plant spring bulbs, and prepare for winter.",
    "Winter": "Protect plants from frost, plan next year's garden, and maintain tools."
}

# Monthly specific tasks dictionary
MONTHLY_TASKS = {
    1: "Prune dormant trees and shrubs.",
    2: "Start planning your spring garden layout.",
    3: "Begin planting cool-season vegetables.",
    4: "Plant warm-season vegetables and flowers.",
    5: "Mulch garden beds to retain moisture.",
    6: "Water deeply during dry spells.",
    7: "Harvest summer vegetables regularly.",
    8: "Prepare for autumn planting.",
    9: "Plant fall vegetables and bulbs.",
    10: "Clean up garden debris and compost.",
    11: "Protect sensitive plants from cold.",
    12: "Plan next year's garden and order seeds."
}


# Core Functions

def get_current_month():
    """
    Get the current month number using the datetime module.
    
    This function uses datetime.datetime.now() to retrieve the current
    system date and extracts the month component.
    
    Returns:
        int: Current month number (1-12)
    
    Example:
        >>> get_current_month()
        6
    """
    return datetime.datetime.now().month


def get_season(month):
    """
    Determine the season based on the month number.
    
    The function maps month numbers to seasons as follows:
        - Spring: March (3), April (4), May (5)
        - Summer: June (6), July (7), August (8)
        - Autumn: September (9), October (10), November (11)
        - Winter: December (12), January (1), February (2)
    
    Args:
        month (int): Month number (1-12)
    
    Returns:
        str: Season name ('Spring', 'Summer', 'Autumn', or 'Winter')
    
    Raises:
        ValueError: If month is not between 1 and 12
    
    Example:
        >>> get_season(6)
        'Summer'
    """
    if not 1 <= month <= 12:
        raise ValueError(f"Invalid month: {month}. Must be between 1 and 12.")
    
    if month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    elif month in [9, 10, 11]:
        return "Autumn"
    else:
        return "Winter"


def get_seasonal_advice(season):
    """
    Get gardening advice for a specific season.
    
    Args:
        season (str): Season name ('Spring', 'Summer', 'Autumn', or 'Winter')
    
    Returns:
        str: Gardening advice for the season
    
    Example:
        >>> get_seasonal_advice('Summer')
        'Water plants regularly, harvest vegetables, and watch for pests.'
    """
    return SEASONAL_ADVICE.get(
        season, 
        "No specific advice available for this season."
    )


def get_monthly_task(month):
    """
    Get the recommended gardening task for a specific month.
    
    Args:
        month (int): Month number (1-12)
    
    Returns:
        str: Monthly gardening task
    
    Example:
        >>> get_monthly_task(6)
        'Water deeply during dry spells.'
    """
    return MONTHLY_TASKS.get(
        month,
        f"No specific task defined for month {month}."
    )


def display_gardening_advice(month):
    """
    Display gardening advice based on the provided month.
    
    This function orchestrates the display of seasonal advice and
    monthly tasks in a formatted output.
    
    Args:
        month (int): Month number (1-12)
    
    Example:
        >>> display_gardening_advice(6)
        ============================================================
        GARDENING ADVICE FOR TODAY
        ============================================================
        
        Season: Summer
        Advice: Water plants regularly, harvest vegetables, and watch for pests.
        
        Monthly Task for Month 6:
        Water deeply during dry spells.
        
        ============================================================
    """
    season = get_season(month)
    season_advice = get_seasonal_advice(season)
    monthly_task = get_monthly_task(month)
    
    print("=" * 60)
    print("GARDENING ADVICE FOR TODAY")
    print("=" * 60)
    print(f"\nSeason: {season}")
    print(f"Advice: {season_advice}")
    print(f"\nMonthly Task for Month {month}:")
    print(monthly_task)
    print("\n" + "=" * 60)


def get_month_input():
    """
    Get month input from user with robust error handling.
    
    This function continuously prompts the user until a valid month
    number (1-12) is entered. It handles both ValueError for
    non-integer inputs and validates the range.
    
    Returns:
        int: Valid month number (1-12)
    
    Example:
        >>> get_month_input()
        Enter month number (1-12): 13
        Please enter a number between 1 and 12.
        Enter month number (1-12): abc
        Please enter a valid number.
        Enter month number (1-12): 6
        6
    """
    while True:
        try:
            month = int(input("Enter month number (1-12): "))
            if 1 <= month <= 12:
                return month
            else:
                print("Please enter a number between 1 and 12.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    """
    Main entry point for the Garden Advice App.
    
    This function orchestrates the entire application flow:
    1. Displays welcome message
    2. Gets month input from user
    3. Displays gardening advice
    4. Shows exit message
    
    Returns:
        None
    
    Example:
        Running the main function will start the interactive app:
        >>> main()
        Welcome to the Garden Advice App!
        Enter month number (1-12): 6
        ...
        Thank you for using the Garden Advice App!
    """
    print("Welcome to the Garden Advice App!")
    
    month = get_month_input()
    
    display_gardening_advice(month)
    
    print("\nThank you for using the Garden Advice App!")


if __name__ == "__main__":
    main()
