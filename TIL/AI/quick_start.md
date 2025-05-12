# 🧪 데이터 분석 및 AI 모델 파이프라인 핵심 메서드 정리

## ✅ 1. 데이터 로딩 & 전처리  
**사용 모듈**: `numpy`, `pandas`, `scipy`

### 🐼 pandas
- `pd.read_csv()`, `pd.read_excel()`: 데이터 로딩  
- `.info()`, `.describe()`: 데이터 요약  
- `.isnull()`, `.fillna()`, `.dropna()`: 결측값 처리  
- `.astype()`, `.map()`, `.apply()`: 타입 변환  
- `.groupby()`, `.pivot_table()`: 집계  
- `.merge()`, `.concat()`: 데이터 병합  

### 🔢 numpy
- `np.array()`: 배열 생성  
- `np.isnan()`, `np.where()`: 결측값 및 조건 처리  
- `np.mean()`, `np.std()`, `np.sum()`: 통계  

### 📊 scipy
- `scipy.stats.zscore()`, `ttest_ind()`, `pearsonr()`: 통계 분석  
- `scipy.sparse`: 희소 행렬 처리  

---

## ✅ 2. 데이터 시각화 & 탐색  
**사용 모듈**: `matplotlib`, `pandas`

### 📈 matplotlib
- `plt.plot()`, `plt.bar()`, `plt.scatter()`, `plt.hist()`: 기본 시각화  
- `plt.title()`, `plt.xlabel()`, `plt.legend()`: 꾸미기  
- `plt.subplot()`: 다중 그래프 구성  

### 🐼 pandas
- `.plot(kind='bar'/'hist'/'box')`: 간단한 시각화  

---

## ✅ 3. 데이터 전처리 (피처 엔지니어링 포함)  
**사용 모듈**: `pandas`, `scikit-learn`, `scipy`

### ⚙️ scikit-learn (preprocessing)
- `StandardScaler`, `MinMaxScaler`: 스케일링  
- `LabelEncoder`, `OneHotEncoder`: 인코딩  
- `PolynomialFeatures`: 다항 피처 생성  
- `SimpleImputer`: 결측값 대체  

### 🔍 scikit-learn (feature_selection)
- `SelectKBest`, `RFE`, `mutual_info_classif()`: 피처 선택  

---

## ✅ 4. 모델 선택 및 학습  
**사용 모듈**: `scikit-learn`, `xgboost`, `torch`, `torchvision`

### 🔬 scikit-learn (model_selection)
- `train_test_split`: 데이터 분리  
- `GridSearchCV`, `RandomizedSearchCV`: 하이퍼파라미터 튜닝  
- `cross_val_score`: 교차 검증  

### 🤖 scikit-learn (모델)
- `LogisticRegression`, `RandomForestClassifier`, `SVC`: 분류  
- `LinearRegression`, `Ridge`, `Lasso`: 회귀  

### 🚀 xgboost
- `XGBClassifier`, `XGBRegressor`  
- `.fit()`, `.predict()`, `.score()`, `.feature_importances_`  

### 🔥 PyTorch (`torch`, `torchvision`)
- `torch.nn`: 모델 구성 (예: `nn.Linear`, `nn.ReLU`)  
- `torch.optim`: 옵티마이저 (`Adam`, `SGD`)  
- `torch.utils.data`: 데이터 로더  
- `torchvision.transforms`: 이미지 전처리  
- `.train()`, `.eval()`, `.backward()`, `.step()`  

---

## ✅ 5. 모델 평가  
**사용 모듈**: `scikit-learn`, `matplotlib`

### 📏 scikit-learn (metrics)
- `accuracy_score`, `precision_score`, `recall_score`, `f1_score`: 분류 평가  
- `confusion_matrix`, `classification_report`: 분류 분석  
- `mean_squared_error`, `r2_score`: 회귀 평가  
- `roc_auc_score`, `roc_curve`, `precision_recall_curve`: 이진 분류  

### 📊 matplotlib
- ROC curve, confusion matrix 등 시각화  

---

## ✅ 6. 모델 저장 및 불러오기  
**사용 모듈**: `joblib`, `torch`, `xgboost`

### 💾 joblib
- `joblib.dump(model, 'model.pkl')`: 저장  
- `joblib.load('model.pkl')`: 로드  

### 💾 PyTorch
- `torch.save(model.state_dict(), 'model.pth')`  
- `model.load_state_dict(torch.load('model.pth'))`  

### 💾 xgboost
- `.save_model()`, `.load_model()`  

---

## 🧩 전체 요약 (단계별 정리)

| 단계 | 주요 모듈 | 주요 메서드 |
|------|-----------|-------------|
| 데이터 로딩/전처리 | `pandas`, `numpy`, `scipy` | `read_csv`, `dropna`, `fillna`, `astype`, `zscore`, `where` |
| 탐색/시각화 | `matplotlib`, `pandas` | `plot`, `hist`, `scatter`, `subplot`, `title` |
| 전처리 | `sklearn.preprocessing` | `StandardScaler`, `OneHotEncoder`, `PolynomialFeatures` |
| 모델 선택/학습 | `sklearn`, `xgboost`, `torch` | `fit`, `predict`, `train_test_split`, `cross_val_score`, `GridSearchCV` |
| 모델 평가 | `sklearn.metrics` | `accuracy_score`, `confusion_matrix`, `roc_curve`, `r2_score` |
| 모델 저장 | `joblib`, `torch`, `xgboost` | `dump`, `load`, `save_model`, `state_dict` |