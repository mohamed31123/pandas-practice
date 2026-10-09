from src import analysis
from src.cleaning import clean
from src.loader import load_sales
from src.transform import add_columns


def _df():
    return add_columns(clean(load_sales()))


def test_no_missing_quantity():
    assert _df()["quantity"].isna().sum() == 0


def test_total_column():
    df = _df()
    assert (df["total"] == df["quantity"] * df["unit_price"]).all()


def test_revenue_by_city_sorted():
    s = analysis.revenue_by_city(_df())
    assert s.is_monotonic_decreasing


def test_top_customers_size():
    assert len(analysis.top_customers(_df(), 3)) == 3
