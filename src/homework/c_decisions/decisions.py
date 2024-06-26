# 

def get_options_ratio(options, total):
    if total == 0: 
        return 0.0 
    ratio = options // total 
    return ratio 

def get_faculty_rating(ratio): 
    if ratio >= 0.9: 
        return 'Excellent'
    elif ratio >= 0.8: 
        return 'Very Good' 
    elif ratio >= 0.7: 
        return 'Good' 
    elif ratio >= 0.6:
        return 'Needs Improvement' 
    else: 
        return 'Unacceptable' 