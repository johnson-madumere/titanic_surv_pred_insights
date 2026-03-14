# Titanic Survival Analysis and Prediction

A CRISP-DM based data science project to analyze Titanic passenger data and predict survival outcomes.

> **Python:** 3.10+ | **Environment:** Conda or pip/venv | **Notebooks:** Run in order `01` -> `05`

---

## 1. Project Overview

This project builds and evaluates machine learning models to predict whether a Titanic passenger survived, using features such as:

- Passenger class (`Pclass`)
- Gender (`Sex`)
- Age (`Age`)
- Fare (`Fare`)
- Family context (`SibSp`, `Parch`, engineered features)

Main goals:

- Build a reliable and interpretable survival prediction model
- Explain **who survived** and **why**
- Follow a clear CRISP-DM workflow

### FAIR Compliance

This project follows the FAIR data principles:

- **Findable**: Clear folder structure, numbered notebooks, and this README
- **Accessible**: `requirements.txt` and `environment.yml` for any OS/tool
- **Interoperable**: Data stored as `.csv`, relative file paths used throughout
- **Reusable**: Fixed random seed (`RANDOM_SEED = 42`), documented workflow, open license

### Citation and FAIR Metadata

This repository includes a machine-readable citation file: `CITATION.cff`.

Why this matters:

- **Findable (FAIR):** standardized metadata improves indexing/discovery.
- **Reusable (FAIR):** provides clear attribution and versioned citation details.
- **Transparency:** author, version, release date, and repository link are explicit.

Location:

- `CITATION.cff` (project root)

---

## 2. Project Structure

```text
├── LICENSE
├── Makefile
├── README.md
├── data
│   ├── metadata
│   │   ├── dataset_metadata.yaml <- Dataset provenance and integrity
│   │   └── data_dictionary.csv   <- Column definitions and schema
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
├── requirements.txt         <- Scanned direct imports (generated)
├── requirements-lock.txt    <- Exact pinned dependencies for reproducibility
├── CITATION.cff
├── environment.yml          <- Optional Conda environment file
├── setup.cfg
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

Clone the repository and move into the project folder:

```powershell
git clone https://github.com/johnson-madumere/titanic_surv_pred_insights.git
cd titanic_surv_pred_insights
```

### Dataset Setup

The raw dataset is **not included** in this repository.

**Primary source**

1. Download `titanic.csv` from Saxion Brightspace:
   https://brightspace.saxion.nl/content/enforced/139122-ACT_MICT_DATAOPS_2526_3/titanic1.csv?ou=139122

2. Rename the downloaded file to `titanic.csv`

3. Place the file here:
   ```text
   data/raw/titanic.csv
   ```

### Dataset Access and FAIR Notes

- **Accessible:** Once the dataset is placed in `data/raw/`, the project can run fully offline.
- **Interoperable:** The dataset uses an open `.csv` format and is processed using relative paths only.
- **Reusable:** Dataset provenance, file format, and verification details should be documented in:
  - `data/metadata/dataset_metadata.yaml`
  - `data/metadata/data_dictionary.csv`

### Dataset Integrity Check

To support reproducibility, record the SHA256 checksum of the raw dataset in `data/metadata/dataset_metadata.yaml`.

Example command on Windows:

```powershell
certutil -hashfile data\raw\titanic.csv SHA256
```

---

## 4. Requirements

- Python 3.10+ (recommended)
- pip (for `requirements.txt`) or Conda (for `environment.yml`)
- Jupyter Notebook or VS Code (recommended)

---

## 5. Installation

### 5.1 First-time setup (Conda/Anaconda not installed yet)

If this is a new system, install **Miniconda** (lightweight) or **Anaconda** first.

**Option A (recommended): Miniconda**

1. Download installer: https://www.anaconda.com/download/success
2. Install with default settings.
3. Open a **new** PowerShell terminal and run:

```powershell
conda --version
conda init powershell
```

4. Close and reopen PowerShell.

> Optional (Windows + winget):

```powershell
winget install -e --id Anaconda.Miniconda3
```

---

### 5.2 Conda init and activation by OS/shell

After installing Miniconda/Anaconda, run `conda init` **once** for your shell, then restart terminal.

#### Windows (PowerShell)

```powershell
conda --version
conda init powershell
# close and reopen terminal
conda activate titanic-surv
```

#### Windows (Command Prompt / cmd)

```bat
conda --version
conda init cmd.exe
:: close and reopen terminal
conda activate titanic-surv
```

#### macOS / Linux (bash)

```bash
conda --version
conda init bash
# restart terminal or run: source ~/.bashrc
conda activate titanic-surv
```

#### macOS (zsh, default on newer macOS)

```zsh
conda --version
conda init zsh
# restart terminal or run: source ~/.zshrc
conda activate titanic-surv
```

#### Linux/macOS (fish shell)

```fish
conda --version
conda init fish
# restart terminal
conda activate titanic-surv
```

> If `conda` is not recognized, restart terminal first.  
> If still failing, open **Anaconda Prompt** (Windows) and run the same commands there.

<!-- ...existing code... -->

### 5.3 Option A: Install project with `requirements.txt` (pip + venv)

```powershell
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```

### 5.4 Option B: Install project with `environment.yml` (Conda)

```powershell
conda env create -f environment.yml
conda activate titanic-surv
```

> Use either pip/venv or Conda (not both).

### 5.5 Dependency Management

This project provides two dependency files:

- `requirements.txt` : standard install for normal use.
- `requirements-lock.txt` : exact pinned environment for reproducible grading/runs.

Use cases:

- **General run:** `pip install -r requirements.txt`
- **Exact reproducible run (recommended for grading):**
  ```powershell
  pip install -r requirements-lock.txt
  pip install -e .
  ```

> `requirements-lock.txt` was generated using `pip-compile` in a clean virtual environment
> with Python 3.13 and contains only project-relevant packages with exact version pins.

Why this matters (FAIR Reusable):

- Prevents version drift across devices and dates
- Improves consistency of notebook outputs
- Supports reproducible academic evaluation

---

## 6. Environment Setup

### If using VS Code

1. Open the project folder in VS Code.
2. Select the Python interpreter from `.venv` or Conda environment.
3. Restart the kernel for notebooks if needed.

### Verify installation

```powershell
python -c "import pandas, numpy, sklearn, matplotlib; print('Environment OK')"
```

### File Path Note

All file paths in this project are **relative** (e.g., `data/raw/titanic.csv`).  
The project will run correctly regardless of where it is placed on your machine.

---

## 7. Running the Project

### Start notebooks (recommended)

```powershell
jupyter notebook
```

Then open and run notebooks in order from `notebooks/`.

### Run training/inference scripts (if used)

```powershell
python -m titanic_surv.modeling.train
python -m titanic_surv.modeling.predict
```

Run notebooks in the following order:

1. `01_business_understanding.ipynb`
2. `02_data_understanding.ipynb`
3. `03_data_preparation.ipynb`
4. `04_modeling.ipynb`
5. `05_evaluation.ipynb`

### Cannot run Jupyter? Use pre-rendered HTML exports

Static HTML versions of all notebooks are available in:

```
reports/notebooks/
```

Open any `.html` file directly in a browser — no installation needed.

To regenerate them yourself:

```powershell
jupyter nbconvert --to html notebooks/*.ipynb --output-dir reports/notebooks/
```

---

## 8. Workflow (CRISP-DM Phases)

1. **Business Understanding** – Define objective and success criteria
2. **Data Understanding** – Explore data quality and survival patterns
3. **Data Preparation** – Clean, transform, and engineer features
4. **Modeling** – Train baseline and tuned models
5. **Evaluation** – Compare models, fairness/error checks, final conclusions
6. **Deployment (out of project scope)** – Export outputs/reports for usage

### Shared Configuration

All shared settings (paths) are defined in:

```
titanic_surv/config.py
```

---

## 9. Usage

Typical usage flow:

1. Install dependencies (`requirements.txt` or `environment.yml`)
2. Run preparation notebook/script to generate processed data
3. Train models
4. Evaluate models and generate reports in `/reports`
5. Review final insights in evaluation outputs and notebook conclusions

### Processed Data

If you skip running `03_data_preparation.ipynb`, pre-processed files are already included in:

```
data/processed/
├── titanic_training.csv
├── titanic_validate.csv
└── titanic_test.csv
```

---

## 10. Definitions / Terminology

- **Survived**: Target variable (1 = survived, 0 = did not survive)
- **F1 Score**: Harmonic mean of precision and recall
- **ROC-AUC**: Model ranking quality across thresholds
- **Calibration**: How close predicted probabilities are to real outcomes
- **Random Seed**: Fixed at `42` across all notebooks and scripts to ensure reproducible results
- **Prediction Certainty and Confidence Report:** - Shows how confident the model is in its predictions based on probability scores.
- **Group Fairness and Accuracy Analysis:** - Compares model performance across groups such as gender or passenger class.
- **Error Breakdown Analysis:** - Shows where the model makes mistakes, including false positives, false negatives, and misclassified passengers.
- **Core Prediction Table:** - Displays actual survival results, predicted outcomes, and the main reason for the prediction.
- **Enriched Prediction Table:** - Combines passenger information with prediction results and probability values.
- **Smart Output Table:** - Provides a short and simple summary of survival likelihood and the key reason behind the prediction.
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
- **Hyperparameter** – A configuration setting chosen before training a model, such as the regularization strength in logistic regression. Hyperparameters influence how the model learns from data.

---

## 11. Support

For questions regarding this project, please contact the author or open an issue in the repository.

1. Open a GitHub Issue
2. Include:
   - Error message
   - Steps to reproduce
   - Python version and OS
   - Screenshot/log (if possible)

---

## 12. Authors and Acknowledgements

- **Author(s):** _Abuchi Johnson Madumere_
- **Email:** _583339@student.saxion.nl_
- **Acknowledgements:**
  - Cookiecutter Data Science template
  - Scikit-learn and open-source Python ecosystem
  - Standard evaluation methods adapted from external sources are properly cited in the **References** section.
  - Adapted concepts include reliability curves, calibration interpretation, grouped metric auditing, and confusion-matrix-based error analysis.
  - The author confirms understanding of each code block, including why it was used, how it works, and its limitations for this dataset.
  - In line with Saxion University’s AI policy, a Large Language Model (LLM) was used only as a writing aid to improve academic flow. All data extraction, analysis, synthesis, and final decisions were completed manually by the author to ensure originality and accountability.

---

## 13. License

This project is licensed under the terms in the `LICENSE` file.

---

## 14. References

[1] P. Chapman, J. Clinton, R. Kerber, T. Khabaza, T. Reinartz, C. Shearer, and R. Wirth, _CRISP-DM 1.0: Step-by-Step Data Mining Guide_. 2000.

[2] Encyclopaedia Britannica, “Titanic.” [Online]. Available: https://www.britannica.com/topic/Titanic

[3] G. James, D. Witten, T. Hastie, and R. Tibshirani, _An Introduction to Statistical Learning_, 2nd ed. New York, NY, USA: Springer, 2021.

[4] B. S. Frey, D. A. Savage, and B. Torgler, “Behavior under extreme conditions: The Titanic disaster,” _Journal of Economic Perspectives_, vol. 25, no. 1, pp. 209–222, 2011.

[5] J. W. Tukey, _Exploratory Data Analysis_. Reading, MA, USA: Addison-Wesley, 1977.

[6] W. McKinney, “Data Structures for Statistical Computing in Python,” in _Proceedings of the 9th Python in Science Conference_, Austin, TX, USA, 2010, pp. 56–61.

[7] D. Gleicher, “The rescue of the Titanic survivors,” _Journal of Social History_, vol. 40, no. 1, pp. 157–178, 2006.

[8] B. Iglewicz and D. C. Hoaglin, _How to Detect and Handle Outliers_. Milwaukee, WI, USA: ASQC Quality Press, 1993.

[9] D. A. Butler, _Unsinkable: The Full Story of the RMS Titanic_. Mechanicsburg, PA, USA: Stackpole Books, 1998.

[10] H. He and E. A. Garcia, “Learning from imbalanced data,” _IEEE Transactions on Knowledge and Data Engineering_, vol. 21, no. 9, pp. 1263–1284, 2009.

[11] D. B. Rubin, _Multiple Imputation for Nonresponse in Surveys_. New York, NY, USA: John Wiley & Sons, 1987.

[12] Scikit-learn Developers, "train*test_split," \_Scikit-learn documentation*. [Online]. Available: https://scikit-learn.org/

[13] A. Zheng and A. Casari, _Feature Engineering for Machine Learning: Principles and Techniques for Data Scientists_. Sebastopol, CA, USA: O’Reilly Media, 2018.

[14] J. Han, M. Kamber, and J. Pei, _Data Mining: Concepts and Techniques_, 3rd ed. Waltham, MA, USA: Morgan Kaufmann, 2011.

[15] L. Breiman, J. H. Friedman, R. A. Olshen, and C. J. Stone, _Classification and Regression Trees_. Belmont, CA, USA: Wadsworth, 1984.

[16] J. D. Kelleher, B. Mac Namee, and A. D’Arcy, _Fundamentals of Machine Learning for Predictive Data Analytics_. Cambridge, MA, USA: MIT Press, 2015.

[17] K. Blagec, G. Dorffner, and M. Samwald, “A critical analysis of metrics used for measuring progress in artificial intelligence,” _arXiv preprint arXiv:2008.02577_, Aug. 2020. [Online]. Available: https://arxiv.org/pdf/2008.02577

[18] Scikit-learn Developers, “Confusion matrix,” _Scikit-learn documentation_. [Online]. Available: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html
