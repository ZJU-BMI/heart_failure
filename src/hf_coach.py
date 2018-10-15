import pandas as pd
import math
df = pd.read_csv('I:\\acs_failure\\resource\\hf_save.csv', encoding='GB2312')
for index, row in df.iterrows():
    age = row['年龄']
    sex = row['性别']
    SBP = row['收缩压']
    DBP = row['舒张压']
    BNP = row['脑利纳肽前体(pg/ml)']

    if sex == 0:
        df.loc[index, '性别'] = 1
    else:
        df.loc[index, '性别'] = 0
    pulse_pressure = SBP - DBP
    if not isinstance(BNP, str):
        df.loc[index, 'coach'] = -4.206 + sex * (-0.534) + 0.047 * age + \
                                 (-0.018) * pulse_pressure - 0.362 * 1 + 0.186 * math.log(BNP)
    if isinstance(BNP, str):
        df.loc[index, 'coach'] = -4.206 + sex * (-0.534) + 0.047 * age + \
                                 (-0.018) * pulse_pressure - 0.362 * 1 + 0.186 * math.log(35000)

    x = df.loc[index, 'coach']
    p = 1/(1 + math.exp(-x))
    df.loc[index, 'coach_P'] = 1 - p
df.to_csv('I:\\hf\\hf_save_coach.csv', encoding='gbk')


