# Tip Prediction: Linear & Polynomial Regression

A small machine learning exercise that fits **linear** and **degree-2 polynomial** regression models to predict restaurant **tip** amount from **total bill**, using the classic Seaborn `tips` dataset and scikit-learn.

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/klaushell/machineLearning)

## 📋 Project Overview

This project compares two regression approaches on the same features:

- **Input**: `total_bill` (single feature)
- **Target**: `tip`
- **Linear model**: ordinary least squares (`LinearRegression` on raw `total_bill`)
- **Polynomial model**: quadratic features via `PolynomialFeatures(degree=2)`, then `LinearRegression` on the expanded design matrix

Results are visualized with a scatter plot of the data and both fitted curves.

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

   A matplotlib window opens with the scatter plot and both regression lines.

## 📁 Project Structure

```
machineLearning/
├── linear_regression.py   # Linear + polynomial regression on tips data
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

The Seaborn **`tips`** dataset includes restaurant bills and tips. This script uses:

- **`total_bill`**: predictor (reshaped to a single column for sklearn)
- **`tip`**: target

Typical use in tutorials: explore simple regression and residuals; here we overlay linear vs quadratic fits on the same plot.

## 🧠 Models

| Aspect | Linear | Polynomial (degree 2) |
|--------|--------|------------------------|
| **Features** | `total_bill` | `1`, `total_bill`, `total_bill²` |
| **Estimator** | `LinearRegression` | `LinearRegression` (on poly features) |
| **Interpretation** | Straight line | Parabola in bill space |

## 📈 What to Expect

- Both models fit quickly on this small dataset.
- The polynomial curve can bend; whether it visibly differs from the line depends on the data sample (Seaborn’s bundled `tips` is fixed).
- Use the plot to compare **bias** (line) vs **flexibility** (quadratic).

## 🔧 Dependencies

- `numpy` — arrays and numerics
- `matplotlib` — plotting
- `seaborn` — `load_dataset("tips")` and styling
- `pandas` — tabular data behind Seaborn
- `scikit-learn` — `LinearRegression`, `PolynomialFeatures`

Pinned loosely in `requirements.txt` for reproducibility.

## 📝 Code Workflow (`linear_regression.py`)

1. **Imports** — numpy, matplotlib, seaborn, sklearn regression utilities  
2. **Load data** — `sns.load_dataset("tips")`  
3. **Prepare `X`, `y`** — bill as `(n, 1)`, tip as 1D  
4. **Linear fit** — `fit` / `predict` on `X`  
5. **Polynomial features** — `PolynomialFeatures(degree=2)` → `fit_transform(X)`  
6. **Polynomial linear fit** — second `LinearRegression` on `X_poly`  
7. **Plot** — scatter + both prediction curves + legend  

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
```

### One-off (system Python)

```bash
pip install -r requirements.txt
python linear_regression.py
```

## 📊 Output

Running the script opens a **figure** (no console metric in the current script):

- Scatter: observed `tip` vs `total_bill`
- Line: linear regression predictions
- Curve: quadratic (polynomial) regression predictions

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

Or swap the target/feature columns to explore other columns in `tips` (e.g. `size`).

## 📚 Learning Resources

This repo illustrates:

- Loading a built-in dataset via Seaborn  
- `LinearRegression` in scikit-learn  
- Feature expansion with `PolynomialFeatures`  
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
