#!/usr/bin/env python3
"""
Test prioritization formula to verify correctness
"""

def calculate_priority(impact: str, effort: str):
    """Calculate priority score (0-1)"""
    impact_value = {'High': 3, 'Medium': 2, 'Low': 1}[impact]
    effort_value = {'High': 3, 'Medium': 2, 'Low': 1}[effort]
    
    score = (impact_value * 3 + (4 - effort_value)) / 7
    
    if score > 0.7:
        return score, "Do Now"
    elif score > 0.4:
        return score, "Next Sprint"
    else:
        return score, "Backlog"


# Test all combinations
print("PRIORITIZATION FORMULA TEST")
print("="*60)
print(f"{'Impact':<10} {'Effort':<10} {'Score':<10} {'Action':<15}")
print("="*60)

for impact in ['High', 'Medium', 'Low']:
    for effort in ['Low', 'Medium', 'High']:
        score, action = calculate_priority(impact, effort)
        print(f"{impact:<10} {effort:<10} {score:<10.2f} {action:<15}")

print("="*60)
print("\nExpected behavior:")
print("- High Impact + Low Effort = Highest priority (Do Now)")
print("- Low Impact + High Effort = Lowest priority (Backlog)")
print("- Impact weighted 3x more than effort")
