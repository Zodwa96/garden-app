"""
Garden Advice App - Provides gardening tips based on month and season

This application helps gardening enthusiasts get appropriate gardening advice
based on the current month and season. The code has been refactored to use
well-organized functions for better maintainability.
"""

import datetime

# Constants for seasonal advice
SEASONAL_ADVICE = {
    "Spring": "Plant new flowers, prepare soil, and start vegetable seeds.",
    "Summer": "Water plants regularly, harvest vegetables, and watch for pests.",
    "Autumn": "Clean up fallen leaves, plant spring bulbs, and prepare for winter.",
    "Winter": "Protect plants from frost, plan next year's garden, and maintain tools."
}

# Monthly specific tasks
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


def get_current_month():
    """
    Get the current month number using datetime module.
    
    Returns:
        int: Current month number (1-12)
    """
    return datetime.datetime.now().month


def get_season(month):
    """
    Determine the season based on the month number.
    
    Args:
        month (int): Month number (1-12)
    
    Returns:
        str: Season name (Spring, Summer, Autumn, Winter)
    """
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
        season (str): Season name
    
    Returns:
        str: Gardening advice for the season
    """
    return SEASONAL_ADVICE.get(season, "No specific advice for this season.")


def get_monthly_task(month):
    """
    Get the gardening task for a specific month.
    
    Args:
        month (int): Month number (1-12)
    
    Returns:
        str: Monthly gardening task
    """
    return MONTHLY_TASKS.get(month, "No specific task for this month.")


def display_gardening_advice(month):
    """
    Display gardening advice based on the provided month.
    
    Args:
        month (int): Month number (1-12)
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
    Get month input from user with validation.
    
    Returns:
        int: Valid month number (1-12)
    """
    try:
        month = int(input("Enter month number (1-12): "))
        if 1 <= month <= 12:
            return month
        else:
            print("Please enter a number between 1 and 12.")
            return get_month_input()
    except ValueError:
        print("Please enter a valid number.")
        return get_month_input()


def main():
    """
    Main function to run the Garden Advice App.
    """
    print("Welcome to the Garden Advice App!")
    
    # Get user input for month
    month = get_month_input()
    
    # Display the gardening advice
    display_gardening_advice(month)
    
    print("\nThank you for using the Garden Advice App!")


if __name__ == "__main__":
    main()
