def validate_ingredients(ingredients: str) -> str:
    valid = ["fire", "water", "earth", "air"]
    
    for i in valid:
        if i in ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
