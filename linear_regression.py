"""
Linear and polynomial regression on two sample datasets.
Run interactively to choose Tips or Iris; use --dataset for non-interactive runs.
"""

from __future__ import annotations

import argparse
import sys

import matplotlib

# Interactive window: set backend before pyplot/seaborn (they lock the backend).
if sys.platform == "darwin":
    try:
        matplotlib.use("macosx", force=True)
    except Exception:
        matplotlib.use("TkAgg", force=True)
else:
    try:
        matplotlib.use("TkAgg", force=True)
    except Exception:
        matplotlib.use("Agg", force=True)

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Linear vs polynomial regression on Tips or Iris data.",
    )
    parser.add_argument(
        "--dataset",
        choices=("tips", "iris"),
        help="Dataset to use (skips the prompt; required in non-interactive mode).",
    )
    return parser.parse_args()


def choose_dataset(cli_choice: str | None) -> str:
    if cli_choice:
        return cli_choice
    if not sys.stdin.isatty():
        print(
            "Non-interactive terminal: using 'tips'. "
            "Pass --dataset tips or --dataset iris explicitly.",
        )
        return "tips"
    print()
    print("Which dataset do you want to use?")
    print("  1) Tips  — predict tip from total bill (Seaborn)")
    print("  2) Iris  — predict petal length from sepal length (scikit-learn)")
    while True:
        raw = input("Enter 1 or 2 [1]: ").strip() or "1"
        if raw in ("1", "tips", "Tips"):
            return "tips"
        if raw in ("2", "iris", "Iris"):
            return "iris"
        print("Please type 1 for Tips or 2 for Iris.")


def load_tips() -> tuple[np.ndarray, np.ndarray, str, str, str, str]:
    tips = sns.load_dataset("tips")
    x = tips["total_bill"].values.reshape(-1, 1)
    y = tips["tip"].values
    title = "Tips: tip vs total bill"
    xlabel = "Total bill"
    ylabel = "Tip"
    outfile = "tips_regression.png"
    return x, y, title, xlabel, ylabel, outfile


def load_iris() -> tuple[np.ndarray, np.ndarray, str, str, str, str]:
    iris = load_iris()
    # Columns: sepal length, sepal width, petal length, petal width
    x = iris.data[:, 0].reshape(-1, 1)
    y = iris.data[:, 2]
    title = "Iris: petal length vs sepal length"
    xlabel = "Sepal length (cm)"
    ylabel = "Petal length (cm)"
    outfile = "iris_regression.png"
    return x, y, title, xlabel, ylabel, outfile


def load_xy(choice: str) -> tuple[np.ndarray, np.ndarray, str, str, str, str]:
    if choice == "tips":
        return load_tips()
    return load_iris()


def main() -> None:
    args = parse_args()
    choice = choose_dataset(args.dataset)
    x, y, title, xlabel, ylabel, outfile = load_xy(choice)

    linear_model = LinearRegression()
    linear_model.fit(x, y)
    pred_linear = linear_model.predict(x)

    poly = PolynomialFeatures(degree=2)
    x_poly = poly.fit_transform(x)
    polynomial_model = LinearRegression()
    polynomial_model.fit(x_poly, y)
    pred_polynomial = polynomial_model.predict(x_poly)

    order = np.argsort(x.ravel())
    x_sorted = x[order]
    pred_lin_sorted = pred_linear[order]
    pred_poly_sorted = pred_polynomial[order]

    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, alpha=0.6, edgecolors="k", linewidths=0.3)
    plt.plot(x_sorted, pred_lin_sorted, label="Linear regression")
    plt.plot(x_sorted, pred_poly_sorted, label="Polynomial (degree 2)")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.tight_layout()

    if matplotlib.get_backend().lower() == "agg":
        plt.savefig(outfile, dpi=150, bbox_inches="tight")
        print(f"No GUI backend available; saved plot to {outfile}")
    else:
        plt.show(block=True)


if __name__ == "__main__":
    main()
