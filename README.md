# Titanic Survival Analysis and Prediction

This is my CRISP-DM project where I analyze Titanic passenger data and build models to predict survival.

> **Python:** 3.10+ | **Environment:** Conda or pip/venv | **Notebooks:** run in order `01` -> `05`

---

## 1. Project Overview

In this project, I use Titanic passenger data to answer one main question: who survived, and what patterns can explain it.

I work with features like:

- Passenger class (`Pclass`)
- Gender (`Sex`)
- Age (`Age`)
- Fare (`Fare`)
- Family-related columns (`SibSp`, `Parch`, plus engineered features)

Main goals:

- Build a solid and understandable survival model
- Explain survival patterns in a clear way
- Follow the CRISP-DM workflow from start to finish

### Quick Start

If you want the shortest route to run this project:

1. Clone this repo.
2. Put `titanic.csv` in `data/raw/`.
3. Create or update the Conda environment from `environment.yml`.
4. Activate the environment.
5. Check that the key packages load.
6. Run notebooks `01` to `05`.

If this is your first time using Conda in PowerShell, run `conda init powershell` once and reopen the terminal.

```powershell
conda env create -f environment.yml
# if the environment already exists
# conda env update -f environment.yml --prune

conda activate titanic-surv
python -c "import pandas, numpy, sklearn, matplotlib, seaborn, jupyter; print('Environment OK')"
jupyter notebook
```

### FAIR Compliance

I organized this project to follow FAIR principles:

- **Findable:** clear folder structure, numbered notebooks, and this README
- **Accessible:** setup files are included (`requirements.txt`, `environment.yml`)
- **Interoperable:** data is in `.csv` format, and paths are relative
- **Reusable:** random seed is fixed (`42`), and the workflow is documented

### Citation and FAIR Metadata

The project includes a machine-readable citation file: `CITATION.cff`.

Why I include it:

- Better discovery through standard metadata
- Clear attribution and version info
- Transparent author and repository details

---

## 2. Project Structure

```text
├── LICENSE
├── Makefile
├── README.md
├── data
│   ├── metadata
│   │   ├── dataset_metadata.yaml
│   │   └── data_dictionary.csv
│   ├── external
│   ├── interim
│   ├── processed
│   └── raw
├── docs
├── models
├── notebooks
├── pyproject.toml
├── references
├── reports
│   └── figures
├── requirements.txt
├── requirements-lock.txt
├── CITATION.cff
├── environment.yml
└── titanic_surv
    ├── __init__.py
    ├── config.py
    ├── dataset.py
    ├── features.py
    ├── modeling
    │   ├── __init__.py
    │   ├── predict.py
    │   └── train.py
    └── plots.py
```

---

## 3. Getting Started

Clone the repository and move into the folder:

```powershell
git clone https://github.com/johnson-madumere/titanic_surv_pred_insights.git
cd titanic_surv_pred_insights
```

### Dataset Setup

The raw dataset is not stored in this repo.

1. Download `titanic.csv` from Saxion Brightspace:
   https://brightspace.saxion.nl/content/enforced/139122-ACT_MICT_DATAOPS_2526_3/titanic1.csv?ou=139122
2. Rename it to `titanic.csv`.
3. Place it in:

```text
data/raw/titanic.csv
```

### Dataset Integrity Check

To support reproducibility, you can save the SHA256 hash in `data/metadata/dataset_metadata.yaml`.

```powershell
certutil -hashfile data\raw\titanic.csv SHA256
```

---

## 4. Requirements

- Python 3.10+ (recommended)
- Conda or pip
- Jupyter Notebook or VS Code

---

## 5. Installation

### 5.1 First-time setup (if Conda is not installed)

Install Miniconda (recommended) or Anaconda first.

1. Download installer: https://www.anaconda.com/download/success
2. Install with default settings.
3. Open a new PowerShell terminal and run:

```powershell
conda --version
conda init powershell
```

4. Close and reopen PowerShell.

Optional on Windows:

```powershell
winget install -e --id Anaconda.Miniconda3
```

### 5.2 Initialize Conda for your shell

Run `conda init` once for your shell.

If `conda init powershell` says **`No action taken.`**, that is okay. It just means your shell is already initialized.

#### Windows (PowerShell)

```powershell
conda --version
conda init powershell
# close and reopen terminal
```

#### Windows (Command Prompt)

```bat
conda --version
conda init cmd.exe
:: close and reopen terminal
```

#### macOS / Linux (bash)

```bash
conda --version
conda init bash
# restart terminal or run: source ~/.bashrc
```

#### macOS (zsh)

```zsh
conda --version
conda init zsh
# restart terminal or run: source ~/.zshrc
```

#### Linux/macOS (fish)

```fish
conda --version
conda init fish
# restart terminal
```

Quick check:

```powershell
conda env list
```

### 5.3 Option A: Conda setup (main path)

```powershell
conda env list

# create environment if it does not exist
conda env create -f environment.yml

# if it already exists, update it
# conda env update -f environment.yml --prune

conda activate titanic-surv
```

If you get `EnvironmentNameNotFound`, create it first with:

```powershell
conda env create -f environment.yml
```

### 5.4 Option B: pip + venv setup

```powershell
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```

Use either Conda or pip/venv, not both at the same time.

### 5.5 Dependency Files

- `requirements.txt`: normal install
- `requirements-lock.txt`: pinned versions for reproducibility

Pinned install example:

```powershell
pip install -r requirements-lock.txt
pip install -e .
```

---

## 6. Environment Setup

### If you use VS Code

1. Open the project folder.
2. Select the Python interpreter from your Conda env or `.venv`.
3. Restart notebook kernel if needed.

### Verify installation

```powershell
python -c "import pandas, numpy, sklearn, matplotlib, seaborn, jupyter; print('Environment OK')"
```

### Path note

All paths are relative (for example `data/raw/titanic.csv`), so the project can run from different local locations.

---

## 7. Running the Project

This project is notebook-first.

### Start notebooks

```powershell
jupyter notebook
```

Then run notebooks in this order:

1. `01_business_understanding.ipynb`
2. `02_data_understanding.ipynb`
3. `03_data_preparation.ipynb`
4. `04_modeling.ipynb`
5. `05_evaluation.ipynb`

### Optional script entry points

```powershell
python -m titanic_surv.modeling.train
python -m titanic_surv.modeling.predict
```

### If you cannot run Jupyter

You can open exported notebook HTML files in:

```text
reports/notebooks/
```

To regenerate exports:

```powershell
jupyter nbconvert --to html notebooks/*.ipynb --output-dir reports/notebooks/
```

---

## 8. Workflow (CRISP-DM)

1. Business Understanding
2. Data Understanding
3. Data Preparation
4. Modeling
5. Evaluation
6. Deployment (outside this project scope)

Shared paths/config are in:

```text
titanic_surv/config.py
```

---

## 9. Usage

Typical flow:

1. Install dependencies
2. Place `titanic.csv` in `data/raw/`
3. Run `03_data_preparation.ipynb` if you need to regenerate processed data
4. Run modeling and evaluation notebooks
5. Review output tables/figures in `reports/`

### Processed Data

If you skip notebook 03, ready processed files are already included:

```text
data/processed/
├── titanic_training.csv
├── titanic_validate.csv
└── titanic_test.csv
```

---

## 10. Troubleshooting

- `conda init powershell` returns `No action taken.`: this is normal if init was already done.
- `EnvironmentNameNotFound` on `conda activate titanic-surv`: run `conda env create -f environment.yml` first.
- Missing package (for example `seaborn`): run `conda env update -f environment.yml --prune`.
- Error saving to `data/processed/`: the code now creates missing processed folders automatically when saving.
- Notebook fails in VS Code: reselect the correct interpreter/kernel and restart the kernel.

---

## 11. Definitions / Terminology

- **Survived**: Target variable (1 = survived, 0 = did not survive)
- **F1 Score**: Harmonic mean of precision and recall
- **ROC-AUC**: Model ranking quality across thresholds
- **Calibration**: How close predicted probabilities are to real outcomes
- **Random Seed**: Fixed at `42` across all notebooks and scripts to ensure reproducible results
- **Prediction Certainty and Confidence Report:** - Shows how confident the model is in its predictions based on probability scores.
- **Group Fairness and Accuracy Analysis:** - Compares model performance across groups such as gender or passenger class.
- **Error Breakdown Analysis:** - Shows where the model makes mistakes, including false positives, false negatives, and misclassified passengers.
- **Core Prediction Insight Table:** - Displays actual survival results, predicted outcomes, and the main reason for the prediction.
- **Enriched Prediction Insight Table:** - Combines passenger information with prediction results and probability values.
- **Smart Output Insight Table:** - Provides a short and simple summary of survival likelihood and the key reason behind the prediction.
- **Survival Probability:** - The predicted probability that a passenger survived.
- **Main Reason:** - The most important feature (primary driver) that influenced the prediction.
- **CRISP-DM:** - Cross-Industry Standard Process for Data Mining
- **Survival Prediction** - The task of predicting whether a Titanic passenger survived (1) or did not survive (0).
- **Target Variable** - The variable the model aims to predict. In this project, the target variable is Survived
- **Feature (Predictor Variable)** - An input variable used by the model to make predictions.
- **Feature Engineering** – The process of creating new variables from existing data to make patterns clearer.
- **Pclass_Code** - A numeric representation of passenger class, where 1 represents First Class, 2 Second Class, and 3 Third Class.
- **SibSp** - This represents the number of siblings or spouses traveling with the passenger.
- **Parch** - This represents the number of parents or children traveling with the passenger.
- **Data Cleaning** - The process of correcting errors and inconsistencies in the dataset.
- **Missing Value Imputation** - The process of replacing missing data with estimated values.
- **Exploratory Data Analysis (EDA)** - The process of analyzing and visualizing data to understand patterns, relationships, and potential issues before modeling.
- **Class Imbalance** – A situation where one outcome occurs more often than the other. In the Titanic dataset, more passengers did not survive than survived.
- **Stratified Sampling** – A data splitting method that keeps the same proportion of survival outcomes across the training, validation, and test datasets.
- **Training Set** – The portion of the dataset used to train machine learning models
- **Validation Set** - A dataset used to tune model parameters and compare model performance.
- **Test Set** – A dataset used to evaluate the final performance of the model after training and tuning.
- **Data Leakage** – A problem that occurs when information related to the target variable is accidentally included in the model features, which can lead to overly optimistic results.
- **Model-Ready Dataset** – A cleaned and formatted dataset where missing values are handled, categorical variables are encoded, and all features are prepared for machine learning models.
- **Normalization** – A data preprocessing technique that rescales numerical features so they fall within a similar range, often between 0 and 1.
- **Feature Scaling** – A general term for methods used to adjust the range of numerical variables so that no single feature dominates the model due to its larger numeric values.
- **Standardization** – A type of feature scaling where values are transformed so the feature has a mean of 0 and a standard deviation of 1.
- **Regularization** – A technique used during model training to prevent overfitting by adding a penalty for large model coefficients. It helps the model generalize better to unseen data.
- **Overfitting** – A situation where a model learns the training data too closely, including noise or random patterns, which causes poor performance on new data.
- **L1 Regularization (Lasso)** – A regularization method that adds a penalty based on the absolute values of model coefficients.
- **L2 Regularization (Ridge)** – A regularization method that adds a penalty based on the squared values of model coefficients.
- **GridSearchCV with 5-fold cross-validation** - Tests different model parameter combinations using five training splits to select the best-performing configuration.
- **Hyperparameter** – A configuration setting chosen before training a model, such as the regularization strength in logistic regression. Hyperparameters influence how the model learns from data.

---

## 12. Support

If you need help, open a GitHub issue and include:

1. Error message
2. Steps to reproduce
3. Python version and OS
4. Screenshot or logs (if available)

---

## 13. Authors and Acknowledgements

- **Author:** _Abuchi Johnson Madumere_
- **Email:** _583339@student.saxion.nl_
- **Acknowledgements:**
  - Cookiecutter Data Science template
  - Scikit-learn and open-source Python ecosystem
  - Standard evaluation methods referenced in the References section

---

## 14. License

This project is licensed under the terms in the `LICENSE` file.

---

## 15. References

[1] P. Chapman, J. Clinton, R. Kerber, T. Khabaza, T. Reinartz, C. Shearer, and R. Wirth, _CRISP-DM 1.0: Step-by-Step Data Mining Guide_. 2000.

[2] Encyclopaedia Britannica, "Titanic." [Online]. Available: https://www.britannica.com/topic/Titanic

[3] G. James, D. Witten, T. Hastie, and R. Tibshirani, _An Introduction to Statistical Learning_, 2nd ed. New York, NY, USA: Springer, 2021.

[4] B. S. Frey, D. A. Savage, and B. Torgler, "Behavior under extreme conditions: The Titanic disaster," _Journal of Economic Perspectives_, vol. 25, no. 1, pp. 209-222, 2011.

[5] J. W. Tukey, _Exploratory Data Analysis_. Reading, MA, USA: Addison-Wesley, 1977.

[6] W. McKinney, "Data Structures for Statistical Computing in Python," in _Proceedings of the 9th Python in Science Conference_, Austin, TX, USA, 2010, pp. 56-61.

[7] D. Gleicher, "The rescue of the Titanic survivors," _Journal of Social History_, vol. 40, no. 1, pp. 157-178, 2006.

[8] B. Iglewicz and D. C. Hoaglin, _How to Detect and Handle Outliers_. Milwaukee, WI, USA: ASQC Quality Press, 1993.

[9] D. A. Butler, _Unsinkable: The Full Story of the RMS Titanic_. Mechanicsburg, PA, USA: Stackpole Books, 1998.

[10] H. He and E. A. Garcia, "Learning from imbalanced data," _IEEE Transactions on Knowledge and Data Engineering_, vol. 21, no. 9, pp. 1263-1284, 2009.

[11] D. B. Rubin, _Multiple Imputation for Nonresponse in Surveys_. New York, NY, USA: John Wiley & Sons, 1987.

[12] Scikit-learn Developers, "train*test_split," \_Scikit-learn documentation*. [Online]. Available: https://scikit-learn.org/

[13] A. Zheng and A. Casari, _Feature Engineering for Machine Learning: Principles and Techniques for Data Scientists_. Sebastopol, CA, USA: O'Reilly Media, 2018.

[14] J. Han, M. Kamber, and J. Pei, _Data Mining: Concepts and Techniques_, 3rd ed. Waltham, MA, USA: Morgan Kaufmann, 2011.

[15] L. Breiman, J. H. Friedman, R. A. Olshen, and C. J. Stone, _Classification and Regression Trees_. Belmont, CA, USA: Wadsworth, 1984.

[16] J. D. Kelleher, B. Mac Namee, and A. D'Arcy, _Fundamentals of Machine Learning for Predictive Data Analytics_. Cambridge, MA, USA: MIT Press, 2015.

[17] K. Blagec, G. Dorffner, and M. Samwald, "A critical analysis of metrics used for measuring progress in artificial intelligence," _arXiv preprint arXiv:2008.02577_, Aug. 2020. [Online]. Available: https://arxiv.org/pdf/2008.02577

[18] Scikit-learn Developers, "Confusion matrix," _Scikit-learn documentation_. [Online]. Available: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html
