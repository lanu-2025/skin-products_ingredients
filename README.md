# Skin Ingredient-Based Product Recommendation System

This project is part of a Capstone focused on developing a skincare recommendation system. It maps real-world skincare products to specific skin issues based on their active ingredients. This repository contains the dataset creation and recommendation logic based on skincare ingredients and skin issues.

## 🔍 Project Overview

The aim of this module is to recommend skincare products based on skin issues by:

1. Creating a curated dataset mapping **active skincare ingredients** to **common skin issues** (e.g., acne, dryness, hyperpigmentation).
2. Scraping a real-world **e-commerce skincare website** to collect product information and ingredient lists.
3. Mapping products to the most suitable skin concerns based on ingredient overlap and match.

---

## 🧪 Dataset Descriptions

### 1. **Ingredients-to-Skin Issues Mapping**

- Manually compiled from dermatological research and cosmetic science sources.
- CSV format with columns:
  - `ingredient_name`
  - `skin_issue` (e.g., "acne", "dryness", "sensitivity")

### 2. **Product Dataset (Web Scraped)**

- Scraped product data includes:
  - `product_name`
  - `brand`
  - `ingredient_list`
  - `product_url`

- Source: [Include the URL or website name if allowed]

- Scraped using BeautifulSoup and Requests (see `scraper.py`)

---

## 🧠 Recommendation Logic

- For a given **skin issue**, the system:
  - Retrieves all ingredients known to treat that issue.
  - Searches the product dataset for products containing one or more matching ingredients.
  - Ranks products based on the number of matching ingredients and/or effectiveness score.
  
- Implemented in `recommender.py`.

---

## 📂 Repository Structure

