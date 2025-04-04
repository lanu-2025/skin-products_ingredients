import pandas as pd
import re
from rapidfuzz import process as rf_process

# Load datasets
df_products = pd.read_csv("/Users/Lanu/Desktop/cosmetic_p.csv")
df_ingredients = pd.read_csv("/Users/Lanu/Desktop/skincare_ingredients.csv")

# Standardize ingredient format
def clean_ingredients(text):
    if pd.isna(text):
        return ""
    text = text.lower()
    text = re.sub(r'[^a-z, ]', '', text)  # Remove special characters
    return text.strip()

df_products["ingredients"] = df_products["ingredients"].apply(clean_ingredients)

# Remove duplicates
df_products.drop_duplicates(inplace=True)

# Convert ingredient dataset into a dictionary for fast lookups
ingredient_dict = {row["Ingredient"].lower(): eval(row["Concerns"]) for _, row in df_ingredients.iterrows()}

# Optimized function using RapidFuzz for faster matching
def match_product_ingredients(ingredient_list):
    matched_concerns = set()
    for ingredient in ingredient_list.split(", "):
        ingredient = ingredient.lower().strip()
        best_match = rf_process.extractOne(ingredient, ingredient_dict.keys(), score_cutoff=80)
        if best_match:
            matched_concerns.update(ingredient_dict[best_match[0]])
    return list(matched_concerns)

# Apply the optimized matching function
df_products["Matched_Concerns"] = df_products["ingredients"].apply(match_product_ingredients)

# Save the cleaned and matched data
df_products.to_csv("/Users/Lanu/Desktop/matched_products.csv", index=False)

# Display preview
print(df_products[["name", "ingredients", "Matched_Concerns"]].head())
