import geopandas as gpd

wards = gpd.read_file("data/processed/wards.gpkg", layer="wards")
wards.to_file("data/processed/week-10_outputs.gpkg", layer="wards_copy")
wards.drop(columns="geometry").to_csv("month_3/week-10/wards_table.csv", index=False)
print(gpd.list_layers("data/processed/week-10_outputs.gpkg"))
print(gpd.list_layers("data/processed/wards.gpkg"))