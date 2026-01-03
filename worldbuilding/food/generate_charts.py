import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Food data from the worldbuilding
data = [
    # Supercategory, Category, Food, FCR, Calorie%, CaloriePressure, LandScarcity, ReducedFlora, WeatherChaos, H2S_Anoxia, UV_Stress, Tier
    ("Microbial", "Fermented", "Yeast / SCP", 0.75, 12, 5, 5, 5, 5, 5, 5, "S"),
    ("Invertebrate", "Insects", "Black soldier fly larvae", 0.9, 8, 5, 5, 5, 4, 5, 4, "S"),
    ("Invertebrate", "Worms", "Earthworms", 1.0, 4, 5, 4, 5, 4, 5, 4, "S"),
    ("Microbial", "Algae", "Microalgae", 0.65, 6, 5, 5, 5, 4, 3, 3, "S"),
    ("Aquatic", "Seaweed", "Seaweed (kelp)", 0.55, 3, 5, 5, 4, 3, 2, 3, "S"),
    ("Plant", "Root/Tuber", "Potatoes", 0.10, 18, 5, 4, 4, 3, 5, 3, "S"),
    ("Plant", "Root/Tuber", "Cassava / yams", 0.12, 8, 5, 4, 4, 4, 5, 3, "S"),
    ("Plant", "Root/Tuber", "Sweet potatoes", 0.15, 6, 5, 4, 4, 3, 5, 3, "S"),
    ("Plant", "Grain", "Rice (paddy)", 0.175, 10, 5, 3, 4, 4, 4, 3, "S"),
    ("Plant", "Grain", "Wheat", 0.215, 7, 4, 3, 3, 3, 5, 3, "S"),
    ("Plant", "Grain", "Maize (corn)", 0.24, 5, 4, 3, 3, 2, 5, 3, "S"),
    ("Plant", "Legume", "Legumes (lentils, beans)", 0.285, 6, 4, 3, 3, 3, 5, 3, "S"),
    ("Invertebrate", "Insects", "Mealworms / grubs", 1.5, 3, 4, 5, 4, 4, 5, 4, "A"),
    ("Animal", "Poultry", "Duck (rice-integrated)", 2.6, 1.5, 3, 3, 4, 4, 4, 4, "A"),
    ("Animal", "Eggs", "Duck eggs", 2.5, 0.8, 3, 3, 4, 4, 4, 4, "A"),
    ("Animal", "Dairy", "Goat milk", 4.25, 0.5, 4, 3, 4, 4, 4, 4, "A"),
    ("Animal", "Dairy", "Buffalo milk", 3.5, 0.3, 4, 3, 4, 3, 4, 4, "A"),
    ("Animal", "Ruminant", "Goat (meat)", 5.0, 0.2, 3, 3, 4, 4, 4, 4, "A"),
    ("Aquatic", "Cephalopod", "Squid", 1.35, 0.4, 4, 5, 4, 3, 2, 3, "B"),
    ("Aquatic", "Fish", "Low-trophic fish", 1.3, 0.3, 4, 4, 4, 3, 2, 3, "B"),
    ("Animal", "Poultry", "Chicken (broiler)", 1.8, 0.6, 3, 3, 3, 3, 4, 4, "B"),
    ("Animal", "Eggs", "Eggs (grain-fed)", 2.2, 0.5, 3, 3, 3, 3, 4, 4, "B"),
    ("Animal", "Swine", "Pork", 3.5, 0.1, 2, 2, 2, 2, 4, 4, "C"),
    ("Animal", "Ruminant", "Sheep / lamb", 6.5, 0.05, 2, 2, 3, 3, 4, 4, "C"),
    ("Animal", "Ruminant", "Beef (industrial)", 8.0, 0.02, 1, 1, 2, 1, 4, 4, "C"),
    ("Aquatic", "Jellyfish", "Jellyfish", 1.0, 0.05, 3, 5, 2, 2, 1, 2, "D"),
]

# Create DataFrame
df = pd.DataFrame(data, columns=[
    "Supercategory", "Category", "Food", "FCR", "CaloriePct",
    "CaloriePressure", "LandScarcity", "ReducedFlora", "WeatherChaos",
    "H2S_Anoxia", "UV_Stress", "Tier"
])

# Calculate composite resilience (average of all resilience scores)
df["CompositeResilience"] = df[["CaloriePressure", "LandScarcity", "ReducedFlora",
                                 "WeatherChaos", "H2S_Anoxia", "UV_Stress"]].mean(axis=1)

# ============================================
# 1. TREEMAP
# ============================================

fig_treemap = px.treemap(
    df,
    path=["Supercategory", "Category", "Food"],
    values="CaloriePct",
    color="FCR",
    color_continuous_scale=["green", "yellow", "red"],
    range_color=[0, 8],
    title="Food Sources by Calorie Contribution (Color = FCR: Green=Efficient, Red=Inefficient)"
)

fig_treemap.update_layout(
    font=dict(size=14),
    margin=dict(t=50, l=10, r=10, b=10)
)

fig_treemap.update_traces(
    textinfo="label+percent root",
    hovertemplate="<b>%{label}</b><br>Calories: %{value:.1f}%<br>FCR: %{color:.2f}<extra></extra>"
)

fig_treemap.write_html("/Users/danpfeiffer/Documents/code/ai-book-project/worldbuilding/food/food_treemap.html")
print("Treemap saved to food_treemap.html")

# ============================================
# 2. SCATTER PLOT
# ============================================

# Color mapping for supercategories
color_map = {
    "Plant": "#2ecc71",
    "Microbial": "#9b59b6",
    "Invertebrate": "#e67e22",
    "Aquatic": "#3498db",
    "Animal": "#e74c3c"
}

fig_scatter = px.scatter(
    df,
    x="FCR",
    y="CompositeResilience",
    size="CaloriePct",
    color="Supercategory",
    color_discrete_map=color_map,
    hover_name="Food",
    hover_data={
        "FCR": ":.2f",
        "CompositeResilience": ":.2f",
        "CaloriePct": ":.1f",
        "Tier": True,
        "Supercategory": False
    },
    title="Food Sources: FCR vs Composite Resilience (Size = Calorie Contribution)",
    size_max=60
)

fig_scatter.update_layout(
    xaxis_title="Food Conversion Ratio (lower = more efficient)",
    yaxis_title="Composite Resilience Score (higher = more resilient)",
    font=dict(size=14),
    legend_title="Category",
    xaxis=dict(range=[-0.5, 9]),
    yaxis=dict(range=[1.5, 5.5])
)

# Add quadrant annotations
fig_scatter.add_annotation(x=0.5, y=5, text="IDEAL: Efficient + Resilient",
                           showarrow=False, font=dict(size=12, color="green"))
fig_scatter.add_annotation(x=7, y=5, text="Resilient but Inefficient",
                           showarrow=False, font=dict(size=12, color="orange"))
fig_scatter.add_annotation(x=0.5, y=2, text="Efficient but Fragile",
                           showarrow=False, font=dict(size=12, color="orange"))
fig_scatter.add_annotation(x=7, y=2, text="WORST: Inefficient + Fragile",
                           showarrow=False, font=dict(size=12, color="red"))

fig_scatter.write_html("/Users/danpfeiffer/Documents/code/ai-book-project/worldbuilding/food/food_scatter.html")
print("Scatter plot saved to food_scatter.html")

print("\nDone! Both charts saved to worldbuilding/food/")
