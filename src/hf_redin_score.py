import pandas as pd
df = pd.read_csv('I:\\acs_failure\\resource\\hf_save.csv', encoding='GB2312')
for index, row in df.iterrows():
    src = row['肌酐(umol/l)']
    sex = row['性别']
    age = row['年龄']
    BNP = row['脑利纳肽前体(pg/ml)']
    if row['心率'] > 70:
        df.loc[index, 'Redin-Score'] = 4 + df.loc[index, 'Redin-Score']
    if row['贫血'] == 1:
        df.loc[index, 'Redin-Score'] = df.loc[index, 'Redin-Score'] + 4
    if not isinstance(BNP, str):
        if float(BNP) > 1000:
            df.loc[index, 'Redin-Score'] = df.loc[index, 'Redin-Score'] + 8
    if isinstance(BNP, str):
        df.loc[index, 'Redin-Score'] = df.loc[index, 'Redin-Score'] + 8
    if sex == 0:
        eGFR = 186*src/88.41 - 1.154*age - 0.203*0.742
    if sex == 1:
        eGFR = 186*src/88.41 - 1.154*age - 0.203
    if eGFR < 60:
        df.loc[index, 'Redin-Score'] = df.loc[index, 'Redin-Score'] + 4
    if row['左房内径（mm）']/row['体表面积'] > 26:
        df.loc[index, 'Redin-Score'] = df.loc[index, 'Redin-Score'] + 5

df.to_csv('I:\\hf\\hf_save_RSCORE.csv', encoding='gbk')





