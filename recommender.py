import pandas as pd
from ast import literal_eval

# Load dataset
df = pd.read_csv("matched_product.csv")
df["Matched_Concerns"] = df["Matched_Concerns"].apply(lambda x: literal_eval(str(x)))


# Function to recommend based on concerns and skin type
def recommend_products(user_concerns, skin_type, df, top_n=5):
    def jaccard_similarity(set1, set2):
        if not set1 or not set2:
            return 0
        return len(set1 & set2) / len(set1 | set2)

    # Step 1: Filter by skin type
    skin_type = skin_type.capitalize()
    if skin_type not in ["Combination", "Dry", "Normal", "Oily", "Sensitive"]:
        raise ValueError("Invalid skin type. Choose from Combination, Dry, Normal, Oily, Sensitive.")

    filtered_df = df[df[skin_type] == 1].copy()

    # Step 2: Compute similarity
    user_concerns = set(user_concerns)
    filtered_df["Similarity"] = filtered_df["Matched_Concerns"].apply(
        lambda concerns: jaccard_similarity(user_concerns, set(concerns)))

    # Step 3: Sort and return top results
    return filtered_df.sort_values(by="Similarity", ascending=False).head(top_n)


# ✅ Example test
user_input_concerns = ['Acne', 'Wrinkles']
user_skin_type = "Oily"

top_products = recommend_products(user_input_concerns, user_skin_type, df)

print(top_products[["brand", "name", "price", "rank", "Matched_Concerns", "Similarity"]])
