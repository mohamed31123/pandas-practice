"""Full pipeline: load -> explore -> clean -> transform -> analyze -> export."""
from src import analysis, exporter
from src.cleaning import clean
from src.explore import explore
from src.loader import load_sales
from src.transform import add_columns


def run() -> None:
    df = load_sales()
    explore(df)

    df = add_columns(clean(df))

    outputs = {
        "big_orders": analysis.big_orders(df),
        "revenue_by_city": analysis.revenue_by_city(df),
        "revenue_by_month": analysis.revenue_by_month(df),
        "stats_by_category": analysis.stats_by_category(df),
        "top_customers": analysis.top_customers(df),
        "city_category_pivot": analysis.city_category_pivot(df),
    }
    for name, value in outputs.items():
        print(f"\n=== {name} ===")
        print(value)

    exporter.export_csv(df, "sales_clean.csv")
    exporter.export_csv(outputs["revenue_by_city"], "revenue_by_city.csv")
    exporter.export_csv(outputs["city_category_pivot"], "city_category_pivot.csv")
    exporter.export_monthly_chart(outputs["revenue_by_month"])
    print("\nExports written to the output/ folder.")
