import pandas as pd
import plotly.express as px

# Load your import data (assuming this file is in your GitHub repo)
df = pd.read_csv("imports_by_state.csv")  # Make sure this CSV file is also in your repo

# Create the choropleth map
fig = px.choropleth(
    df,
    locations="ID",  # 2-letter state abbreviation (e.g., CA, TX)
    locationmode="USA-states",
    color="Color by",  # Total import value
    scope="usa",
    color_continuous_scale=[
        "#fff5f0", "#fcbba1", "#fc9272", "#fb6a4a", "#cb181d"
    ],
    range_color=(0, 420000000000),  # Adjust max value as needed
    labels={"Color by": "Avg Imports (USD)"},
    title="Total Average in USD of All Imports by State (2015–2025)"
)

fig.update_layout(
    geo=dict(lakecolor="white"),
    title_font_size=20,
    margin=dict(l=0, r=0, t=50, b=0)
)

# Show the map in a browser
fig.show()

