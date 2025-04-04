import pandas as pd
import json

# Define the ingredient dataset with mappings to skin concerns
ingredient_data = [
    {"Ingredient": "Salicylic Acid", "Concerns": ["Acne", "Pores", "Blemishes"]},
    {"Ingredient": "Hyaluronic Acid", "Concerns": ["Hydration", "Wrinkles", "Clear Skin"]},
    {"Ingredient": "Niacinamide", "Concerns": ["Acne", "Pores", "Pigmentation"]},
    {"Ingredient": "Retinol", "Concerns": ["Wrinkles", "Pigmentation", "Blemishes"]},
    {"Ingredient": "Vitamin C", "Concerns": ["Pigmentation", "Clear Skin", "Wrinkles"]},
    {"Ingredient": "Glycolic Acid", "Concerns": ["Acne", "Wrinkles", "Pores"]},
    {"Ingredient": "Lactic Acid", "Concerns": ["Hydration", "Wrinkles", "Blemishes"]},
    {"Ingredient": "Benzoyl Peroxide", "Concerns": ["Acne", "Blemishes"]},
    {"Ingredient": "Azelaic Acid", "Concerns": ["Acne", "Pigmentation", "Blemishes"]},
    {"Ingredient": "Ceramides", "Concerns": ["Hydration", "Clear Skin"]},
    {"Ingredient": "Centella Asiatica", "Concerns": ["Blemishes", "Hydration"]},
    {"Ingredient": "Peptides", "Concerns": ["Wrinkles", "Clear Skin"]},
    {"Ingredient": "Tea Tree Oil", "Concerns": ["Acne", "Pores"]},
    {"Ingredient": "Zinc Oxide", "Concerns": ["Pigmentation", "Blemishes"]},
    {"Ingredient": "Licorice Extract", "Concerns": ["Pigmentation", "Clear Skin"]},
    {"Ingredient": "Kojic Acid", "Concerns": ["Pigmentation", "Blemishes"]},
    {"Ingredient": "Rosehip Oil", "Concerns": ["Wrinkles", "Hydration"]},
    {"Ingredient": "Argan Oil", "Concerns": ["Hydration", "Wrinkles"]},
    {"Ingredient": "Bakuchiol", "Concerns": ["Wrinkles", "Pigmentation"]},
    {"Ingredient": "Aloe Vera", "Concerns": ["Hydration", "Blemishes"]},
    {"Ingredient": "Green Tea Extract", "Concerns": ["Pores", "Clear Skin"]},
    {"Ingredient": "Beta Glucan", "Concerns": ["Hydration", "Wrinkles"]},
    {"Ingredient": "Willow Bark Extract", "Concerns": ["Pores", "Blemishes"]},
    {"Ingredient": "Squalane", "Concerns": ["Hydration", "Clear Skin"]}
]

# Convert to DataFrame
df = pd.DataFrame(ingredient_data)

# Save as CSV
df.to_csv("skincare_ingredients.csv", index=False)

# Save as JSON
with open("skincare_ingredients.json", "w") as json_file:
    json.dump(ingredient_data, json_file, indent=4)

print("CSV and JSON files have been created successfully!")
