
def calculate_priority(urgency, affected_user):
    urgency = urgency.lower()
    if urgency == "high" and affected_user >= 10:
        return "critical"
    elif urgency == "high" or affected_user >= 10:
        return "high"
    elif urgency == "medium" or affected_user >= 3:
        return "medium"
    else:
        return "low"
    
