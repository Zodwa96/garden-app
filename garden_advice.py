"""
Garden Advice App - Provides gardening tips based on month and season

This application helps gardening enthusiasts get appropriate gardening advice
based on the current month and season. It includes TODO comments for potential
improvements.
"""

# TODO: Create a function to get the current month instead of hardcoding
# TODO: Add proper documentation (docstrings) for all functions
# TODO: Replace hardcoded values with configurable constants

# Seasonal gardening advice dictionary
gardening_advice = {
    "Spring": "Plant new flowers, prepare soil, and start vegetable seeds.",
    "Summer": "Water plants regularly, harvest vegetables, and watch for pests.",
    "Autumn": "Clean up fallen leaves, plant spring bulbs, and prepare for winter.",
    "Winter": "Protect plants from frost, plan next year's garden, and maintain tools."
}

# Monthly specific tasks
monthly_tasks = {
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

# TODO: Create a separate function to display advice instead of doing it directly
def display_gardening_advice():
    """
    Display gardening advice based on the current month.
    
    This function retrieves the current month and displays seasonal advice
    along with monthly tasks.
    """
    # TODO: Use datetime module to get current month automatically
    current_month = 6  # Hardcoded for demonstration
    
    season = get_season(current_month)
    
    print("=" * 60)
    print("GARDENING ADVICE FOR TODAY")
    print("=" * 60)
    print(f"\nSeason: {season}")
    print(f"Advice: {gardening_advice.get(season, 'No specific advice for this season.')}")
    
    print(f"\nMonthly Task for Month {current_month}:")
    print(monthly_tasks.get(current_month, "No specific task for this month."))
    print("\n" + "=" * 60)

# TODO: Add error handling for invalid inputs
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

if __name__ == "__main__":
    print("Welcome to the Garden Advice App!")
    display_gardening_advice()
    print("\nThank you for using the Garden Advice App!")