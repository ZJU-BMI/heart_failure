import pandas as pd
df = pd.read_csv('I:\\acs_failure\\resource\\hf_save.csv', encoding='GB2312')
for index, row in df.iterrows():
    AVE = row['心肌梗死']
    enjection_fraction = row['射血分数（%）']
    AF = row['房颤']
    #将钠的原子价都当作+1。
    hyponatremia = row['钠(mmol/l)']
    BNP = row['脑利纳肽前体(pg/ml)']
    #前百分之一的病人为阳性，7.5个取前8个。
    troponin = row['肌钙蛋白T']
    sex = row['性别']
    src = row['肌酐(umol/l)']
    age = row['年龄']

    if AVE == 1:
        df.loc[index, 'cox'] = 3 + df.loc[index, 'cox']
    if row['左房内径（mm）'] / row['体表面积'] > 26:
        df.loc[index, 'cox'] = 8 + df.loc[index, 'cox']
    if enjection_fraction <= 35:
        df.loc[index, 'cox'] = 5 + df.loc[index, 'cox']
    if AF == 1:
        df.loc[index, 'cox'] = 3 + df.loc[index, 'cox']
    if sex == 0:
        eGFR = 186*src/88.41 - 1.154*age - 0.203*0.742
    if sex == 1:
        eGFR = 186*src/88.41 - 1.154*age - 0.203
    if eGFR < 60:
        df.loc[index, 'cox'] = df.loc[index, 'cox'] + 4
    if hyponatremia <= 138:
        df.loc[index, 'cox'] = df.loc[index, 'cox'] + 3
    if not isinstance(BNP, str):
        if float(BNP) > 1000:
            df.loc[index, 'cox'] = df.loc[index, 'cox'] + 7
    if isinstance(BNP, str):
        df.loc[index, 'cox'] = df.loc[index, 'cox'] + 7
    if troponin >= 0.543:
        df.loc[index, 'cox'] = df.loc[index, 'cox'] + 4
df.to_csv('I:\\hf\\hf_save_cox.csv', encoding='gbk')
