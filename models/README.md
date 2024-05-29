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

# 新数据集统计数据
>>> np.round(pgt[features].median(), 2)   
女方年龄          35.00
AFC           11.00
bFSH           5.90
AMH            2.50
促排方案           2.00
身高(cm)       158.00
体重(kg)        55.00
BMI           21.70
bLH            2.95
E2            32.00
FSH/LH         1.98
整倍体囊胚数         1.00
既往活产次数         0.00
男方年龄          37.00
是否中重度OHSS      0.00
是否PCOS         0.00
是否重少弱畸精症       0.00
PGT指征          2.00

>>> np.round(pgt[features].std(), 2)    
女方年龄          4.84
AFC           7.13
bFSH          1.95
AMH           2.68
促排方案          0.49
身高(cm)        4.93
体重(kg)        7.04
BMI           2.65
bLH           1.80
E2           14.27
FSH/LH        1.20
整倍体囊胚数        2.28
既往活产次数        0.57
男方年龄          5.89
是否中重度OHSS     0.13
是否PCOS        0.28
是否重少弱畸精症      0.16
PGT指征         1.84

>>> np.round(pgt[features].min(), 2) 
女方年龄          21.00
AFC            0.00
bFSH           1.77
AMH            0.05
促排方案           1.00
身高(cm)       142.00
体重(kg)        36.00
BMI           15.18
bLH            0.14
E2            10.00
FSH/LH         0.29
整倍体囊胚数         0.00
既往活产次数         0.00
男方年龄          23.00
是否中重度OHSS      0.00
是否PCOS         0.00
是否重少弱畸精症       0.00
PGT指征          1.00

>>> np.round(pgt[features].max(), 2) 
女方年龄          46.00
AFC           76.00
bFSH          24.56
AMH           23.11
促排方案           2.00
身高(cm)       176.00
体重(kg)        98.00
BMI           38.28
bLH           19.39
E2           122.00
FSH/LH        22.37
整倍体囊胚数        15.00
既往活产次数         3.00
男方年龄          67.00
是否中重度OHSS      1.00
是否PCOS         1.00
是否重少弱畸精症       1.00
PGT指征          6.00
# pos_model_1
- 'Gradient Boosting Regressor':GradientBoostingRegressor(n_estimators=150, max_depth=6,loss='absolute_error', random_state=42) # 正向预测，使用Gn预测卵子总数
- features = ['女方年龄','AFC','bFSH','AMH','促排方案','体重(kg)','bLH','E2','既往活产次数','男方年龄', 'PGT指征', '起始Gn剂量']# 正向预测，根据Gn预测卵子总数
- y = pgt['卵子总数'].values
# pos_model_2
- 'Gradient Boosting Regressor':GradientBoostingRegressor(n_estimators=100, max_depth=5, loss='absolute_error' ,random_state=42) # 正向预测，使用Gn预测可移植胚胎数
- features = ['女方年龄','AFC','bFSH','AMH','促排方案','E2','FSH/LH','既往活产次数','男方年龄','是否PCOS', 'PGT指征', '起始Gn剂量']# 正向预测，根据Gn预测可移植胚数量
- y = pgt['整倍体囊胚数'].values
# pos_model_3
- 'Random Forest Classifier': RandomForestClassifier(n_estimators=100 ,random_state=12), # 预测副作用模型
- features = ['女方年龄','AFC','bFSH','AMH','促排方案','身高(cm)','体重(kg)','BMI','bLH','E2','FSH/LH','男方年龄', 'PGT指征', '起始Gn剂量'] # 正向预测，根据Gn预测副作用
- y = pgt['是否中重度OHSS'].values