# pandas_practice

A small, well-structured project to learn pandas step by step.

## Structure

```
pandas_practice/
├── data/                 # input datasets (sales.csv)
├── notebooks/            # Jupyter exploration (01_pandas_basics.ipynb)
├── output/               # generated CSV + chart
├── src/
│   ├── config.py         # paths
│   ├── loader.py         # 1. read CSV
│   ├── explore.py        # 2. head/info/describe/isna
│   ├── cleaning.py       # 3. missing values, duplicates
│   ├── transform.py      # 4. new columns
│   ├── analysis.py       # 5. filter, groupby, pivot_table
│   ├── exporter.py       # 6. CSV + matplotlib chart
│   ├── pipeline.py       # chains everything
│   └── test_pandas.py    # your free sandbox
├── tests/                # pytest checks
├── main.py               # entry point
└── requirements.txt
```

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

## Run

```bash
python main.py                # full pipeline
python -m src.test_pandas     # sandbox
pytest                        # tests
jupyter notebook notebooks/   # notebook
```

## Exercises

1. Add a `discount` column (10% off if `total > 10000`).
2. Find the best-selling product by quantity.
3. Sort by date and compute a running total with `cumsum()`.
4. Add a second CSV (`customers.csv`) and combine it with `merge()`.
5. Use `apply()` to label orders as "small / medium / large".
