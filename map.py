import pandas as pd
import plotly.express as px

# Load your data (make sure the filename matches your uploaded CSV!)
df = pd.read_csv("Total Average in USD of all Imports by State - New report 1 (2).csv")

# If your columns are not named "ID", "Label", "Color by", adjust these as needed:
df = df.rename(columns={
    df.columns[0]: "ID",
    df.columns[1]: "Label",
    df.columns[2]: "Color by"
})

# Remove commas from numbers if present and convert to float
df["Color by"] = df["Color by"].replace({',': ''}, regex=True).astype(float)

fig = px.choropleth(
    df,
    locations="ID",
    locationmode="USA-states",
    color="Color by",
    scope="usa",
    color_continuous_scale="Blues",
    labels={"Color by": "Avg Imports (USD)"},
    title="Total Average in USD of All Imports by State (2015–2025)"
)

fig.update_layout(
    geo=dict(lakecolor="white"),
    title_font_size=20,
    margin=dict(l=0, r=0, t=50, b=0)
)

fig.show()
