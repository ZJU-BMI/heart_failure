import pandas as pd
import math
df = pd.read_csv('I:\\acs_failure\\resource\\hf_save.csv', encoding='GB2312')
for index, row in df.iterrows():
    age = row['年龄']
    sex = row['性别']
    BMI = row['BMI']
    #NYHA ==  3
    NYHA = 3
    ejection_fraction = row['射血分数（%）']
    #缺血ischemic取0
    ischemic = 0
    SBP = row['收缩压']
    #diuretic利尿剂取0,allopurinol取0
    diuretic = 0
    allopurinol = 0
    statin = row['Statin']
    #mmol/l换算成mEg/l，把钠当成均以+1存在的离子
    sodium = row['钠(mmol/l)']
    creatinine = row['肌酐(umol/l)']/88.41
    #胆固醇mmol/L换算成mg/dL
    cholesterol = 100/(row['总胆固醇（mmol/L）']*38.67)
    white_cell = row['白细胞计数（10^9/L）']
    hemoglobin = row['血红蛋白（g/l）']/10
    lym = row['淋巴细胞比例']
    uric_acid = row['尿酸（umol/L）'] * 0.0168
    df.loc[index, 'seattle'] = df.loc[index, 'seattle'] + math.log(1.090)*age/10 + NYHA * math.log(1.6) + math.log(1.354) * ischemic + \
            math.log(1.03) * 100 / ejection_fraction + math.log(1.178) * diuretic + math.log(1.571) * allopurinol + \
            math.log(0.63) * statin + math.log(2.206) * cholesterol
    if sex == 1:
        df.loc[index, 'seattle'] = df.loc[index, 'seattle'] + math.log(1.089)
    if SBP > 160:
        df.loc[index, 'seattle'] = df.loc[index, 'seattle'] + 160 * math.log(0.877)/10
    else:
        df.loc[index, 'seattle'] = df.loc[index, 'seattle'] + SBP * math.log(0.877)/10
    if sodium < 138:
        df.loc[index, 'seattle'] = df.loc[index, 'seattle'] + (138 - sodium) * math.log(1.05)
    if hemoglobin > 16:
        df.loc[index, 'seattle'] = df.loc[index, 'seattle'] + (hemoglobin - 16) * math.log(1.336)
    else:
        df.loc[index, 'seattle'] = df.loc[index, 'seattle'] + (16 - hemoglobin) * math.log(1.124)
    if lym < 0.47:
        df.loc[index, 'seattle'] = df.loc[index, 'seattle'] + lym*100/5 * math.log(0.897)
    else:
        df.loc[index, 'seattle'] = df.loc[index, 'seattle'] + 47/5 * math.log(0.897)
    if uric_acid > 3.4:
        df.loc[index, 'seattle'] = df.loc[index, 'seattle'] + uric_acid * math.log(1.064)
    else:
        df.loc[index, 'seattle'] = df.loc[index, 'seattle'] + 3.4 * math.log(1.064)
df.to_csv('I:\\hf\\hf_save_seattle.csv', encoding='gbk')
