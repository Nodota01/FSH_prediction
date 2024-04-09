# single_regression.joblib
- Gradient Boosting Regressor
- features = ['女方年龄','AFC','bFSH','AMH','促排方案','身高(cm)','体重(kg)','BMI','bLH','E2','FSH/LH','男方年龄','既往活产次数' , '卵子总数']
- y = pgt['起始Gn剂量']
- X = X.fillna(X.median())
``` python
>>> X.median()
女方年龄       32.000000
AFC        12.000000
bFSH        5.630000
AMH         3.230000
促排方案        1.000000
身高(cm)    158.000000
体重(kg)     53.000000
BMI        20.960000
bLH         3.205000
E2         31.000000
FSH/LH      1.799004
男方年龄       33.000000
既往活产次数      0.000000
卵子总数       15.000000
```
# dual_regression.joblib
- Gradient Boosting Regressor
- features = ['女方年龄','AFC','bFSH','AMH','促排方案','身高(cm)','体重(kg)','BMI','bLH','E2','FSH/LH','男方年龄','既往活产次数']
- y = pgt['起始Gn剂量']
- y2 = (y / (pgt['Gn总量'] / pgt['Gn天数']))

# s1s2_regression
- Gradient Boosting Regressor
- Step1 根据生理指标和可移植胚胎数→卵子总数
- features = ['女方年龄','AFC','bFSH','AMH','促排方案','身高(cm)','体重(kg)','BMI','bLH','E2','FSH/LH','男方年龄','既往活产次数' , '可移植胚胎数', '是否中重度OHSS', '卵子总数是否≤25']
- y = pgt['卵子总数']
- Step2 根据生理指标和卵子总数→起始Gn
- features = ['女方年龄','AFC','bFSH','AMH','促排方案','身高(cm)','体重(kg)','BMI','bLH','E2','FSH/LH','男方年龄','既往活产次数' , '卵子总数', '是否中重度OHSS', '卵子总数是否≤25']
- y = pgt['起始Gn剂量']

# prop_class
- RandomForestClassifier( n_estimators=225, min_samples_leaf= 1, min_samples_split=13, max_features='sqrt', max_depth=10, criterion='gini',random_state=12),
- features = ['女方年龄','AFC','bFSH','AMH','促排方案','身高(cm)','体重(kg)','BMI','bLH','E2','FSH/LH','男方年龄','既往活产次数' , '是否中重度OHSS', '卵子总数是否≤25']
- y = pgt['可移植胚胎数分类'].values