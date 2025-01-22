def grade_budget_advice(advice: str, guidelines: list[str]) -> float:
    """
    Grade the given budget advice based on predefined guidelines.
    """
    matches = sum(1 for guideline in guidelines if guideline.lower() in advice.lower())
    return (matches / len(guidelines)) * 100 if guidelines else 0

# Example guidelines
guidelines = [
    "Save at least 20% of your income",
    "Reduce discretionary spending",
    "Review your subscriptions"
]

# Example usage
grade = grade_budget_advice("Save 20% and cut subscriptions.", guidelines)
print(f"Grade: {grade}%")
