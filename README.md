# Linear & Polynomial Regression (Tips or Iris)

A small machine learning exercise that fits **linear** and **degree-2 polynomial** regression on a dataset you choose at startup: Seaborn **`tips`** (total bill → tip) or scikit-learn **`iris`** (sepal length → petal length).

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/klaushell/machineLearning)

## 📋 Project Overview

You pick **Tips** or **Iris** when you run the script (or pass `--dataset`). For each choice, the script compares:

- **Linear model**: `LinearRegression` on one numeric feature  
- **Polynomial model**: `PolynomialFeatures(degree=2)` plus `LinearRegression`

| Dataset | Predictor (`X`) | Target (`y`) |
|--------|------------------|----------------|
| **Tips** (Seaborn) | `total_bill` | `tip` |
| **Iris** (scikit-learn) | Sepal length (cm) | Petal length (cm) |

Results are shown in a scatter plot with linear and quadratic fitted curves (sorted on `X` for smooth lines).

## 🚀 Quick Start

### Prerequisites

- Python 3.10+ (3.7+ is fine if your environment already works)
- pip
- Git (optional, for cloning)

### Installation & Setup

1. **Clone the repository** (adjust URL to your fork):

   ```bash
   git clone git@github.com:klaushell/machineLearning.git
   cd machineLearning
   ```

2. **Set up the environment:**

   ```bash
   make setup
   ```

   This creates a virtual environment and installs dependencies from `requirements.txt`.

3. **Run the script:**

   ```bash
   make run
   ```

   In an **interactive** terminal you are prompted: **1) Tips** or **2) Iris**.  
   For automation (e.g. CI or piping), use a flag and skip the prompt:

   ```bash
   python linear_regression.py --dataset tips
   python linear_regression.py --dataset iris
   ```

   If stdin is not a TTY (some automated runs), the script defaults to **Tips** unless you pass `--dataset`.

   On macOS a **matplotlib window** should open with the scatter plot and both regression lines. The script sets an interactive backend (`macosx` or `TkAgg`) before importing pyplot.

   **If no window appears:** unset `MPLBACKEND` if it is `Agg`, try **Terminal.app**, or rely on the saved file: **`tips_regression.png`** or **`iris_regression.png`** depending on the dataset.

## 📁 Project Structure

```
machineLearning/
├── linear_regression.py   # Tips or Iris; interactive menu or --dataset
├── requirements.txt       # Python dependencies
├── Makefile               # Setup and run commands
├── README.md              # This file
└── venv/                  # Virtual environment (created by make setup)
```

## 🛠️ Available Commands

| Command | Description |
|---------|-------------|
| `make help` | Show all available commands |
| `make run` | Run `linear_regression.py` |
| `make install` | Install dependencies from `requirements.txt` |
| `make clean` | Remove `__pycache__` and `.pyc` files |
| `make venv` | Create a new virtual environment |
| `make venv-activate` | Print the command to activate the venv |
| `make test` | Install dependencies and run the script |
| `make setup` | Full setup (venv + dependencies) |
| `make info` | Print short project metadata |

## 📊 Dataset Information

**Tips** (Seaborn): restaurant bills and tips — `total_bill` → `tip`.

**Iris** (scikit-learn `load_iris`): classic 150×4 flower measurements — for regression we use **sepal length** (column 0) to predict **petal length** (column 2), ignoring species labels.

## 🧠 Models

| Aspect | Linear | Polynomial (degree 2) |
|--------|--------|------------------------|
| **Features** | Raw `X` (one column) | `1`, `X`, `X²` |
| **Estimator** | `LinearRegression` | `LinearRegression` on expanded features |
| **Interpretation** | Straight line | Quadratic curve in feature space |

## 📈 What to Expect

- Both models fit quickly on this small dataset.
- The polynomial curve can bend; how much it differs from the line depends on the dataset (Tips vs Iris).
- Use the plot to compare **bias** (line) vs **flexibility** (quadratic).

## 🔧 Dependencies

- `numpy` — arrays and numerics
- `matplotlib` — plotting
- `seaborn` — `load_dataset("tips")` and styling
- `pandas` — tabular data behind Seaborn
- `scikit-learn` — `LinearRegression`, `PolynomialFeatures`, `load_iris`

Pinned loosely in `requirements.txt` for reproducibility.

## 📝 Code Workflow (`linear_regression.py`)

1. **Configure matplotlib backend** — before pyplot / seaborn  
2. **Args / prompt** — `--dataset` or interactive `1` / `2`  
3. **Load `X`, `y`** — Tips via Seaborn or Iris via `load_iris()`  
4. **Linear fit** — `LinearRegression` on `X`  
5. **Polynomial features** — degree 2 → second `LinearRegression`  
6. **Plot** — scatter; sort `X` for ordered lines; title/labels per dataset  
7. **`show()` or `savefig()`** — GUI or PNG fallback  

## 🎯 Usage Examples

### Default (via Make)

```bash
make setup
make run
```

### Manual venv

```bash
make venv
source venv/bin/activate
pip install -r requirements.txt
python linear_regression.py
python linear_regression.py --dataset iris
```

### One-off (system Python)

```bash
pip install -r requirements.txt
python linear_regression.py --dataset tips
```

## 📊 Output

Running the script shows a **figure** (no console metrics in the current script):

- Scatter of observed `y` vs `X`
- Linear and quadratic fitted curves

If no GUI is available, you get a message and a PNG is written: **`tips_regression.png`** or **`iris_regression.png`**.

To add printed metrics (e.g. train MSE or R²), extend the script with `sklearn.metrics`.

## 🔍 Understanding the Results

- **Linear model**: stable, interpretable slope; assumes approximate linear relationship.  
- **Polynomial model**: can reduce bias if the relationship is curved; risk of **overfitting** if you raise degree or use few points (here degree 2 on many rows is usually mild).  
- **Visual comparison** is the main takeaway in this demo.

## 🛠️ Customization

In `linear_regression.py` you can try:

```python
poly = PolynomialFeatures(degree=3)  # higher-degree curve (use with care)
```

Or change `load_tips()` / `load_iris()` to use other columns (e.g. `size` in tips, or other Iris measurements).

## 📚 Learning Resources

This repo illustrates:

- Choosing a dataset interactively or via CLI  
- Seaborn `tips` and scikit-learn `load_iris`  
- `LinearRegression` and `PolynomialFeatures`  
- Overlaying multiple fits on one plot  

## 🤝 Contributing

Ideas:

- Add train/test split and R² / RMSE on a holdout set  
- Add residual plots  
- Try other columns or regularized models (`Ridge`, `Lasso`)  

### Contributing Guidelines

1. Fork the repository  
2. Create a branch (`git checkout -b feature/your-feature`)  
3. Commit and push  
4. Open a Pull Request  

## 📄 License

Educational use. Dataset and libraries follow their respective licenses.

## 🔗 Repository Information

Update these if your remote differs:

- **GitHub**: [klaushell/machineLearning](https://github.com/klaushell/machineLearning)  
- **SSH clone**: `git@github.com:klaushell/machineLearning.git`  
- **HTTPS clone**: `https://github.com/klaushell/machineLearning.git`  
