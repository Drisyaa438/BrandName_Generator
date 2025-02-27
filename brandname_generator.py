import random

def get_user_inputs():
    """Collects details from the user to generate brand names."""
    product_type = input("Enter the type of product/service your brand represents: ")
    location = input("Enter a location you like (e.g., city, country, street): ")
    pet_name = input("Enter your favorite pet's name (or a favorite word): ")
    adjective = input("Enter a word that describes your brand (e.g., cool, fast, elegant): ")
    founder_name = input("Enter your name or initials: ")
    
    return product_type, location, pet_name, adjective, founder_name

def generate_brand_names(product_type, location, pet_name, adjective, founder_name):
    """Generates brand name suggestions based on user input."""
    name_combinations = [
        f"{adjective}{product_type.capitalize()}",
        f"{pet_name}{location}",
        f"{founder_name}{product_type.capitalize()}",
        f"{location}{adjective}{product_type.capitalize()}",
        f"{product_type.capitalize()}by{founder_name}",
        f"{founder_name}{pet_name}",
        f"{adjective}{location}{product_type.capitalize()}",
        f"{pet_name}{adjective}",
        f"{founder_name} & {pet_name}",
        f"{location} {product_type.capitalize()}"
    ]
    
    return random.sample(name_combinations, min(len(name_combinations), 5))  # Return up to 5 unique names

def main():
    print("🔥 Welcome to the Brand Name Generator 🔥")
    print("Answer a few questions, and I'll generate brand name ideas for you!")
    print("=" * 50)
    
    user_inputs = get_user_inputs()
    brand_names = generate_brand_names(*user_inputs)
    
    print("\n✨ Here are your brand name suggestions: ✨")
    for i, name in enumerate(brand_names, 1):
        print(f"{i}. {name}")

if __name__ == "__main__":
    main()
