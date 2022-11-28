import pandas as pd
from statsmodels.stats.inter_rater import fleiss_kappa


def not_valid(col):
  if col.startswith('Image Classified') or col.startswith('Email') or col.startswith('Type'):
    return False

  return True


def prepare_df(df):
    for col in df.columns:
        if not_valid(col):
            df.drop(col, axis=1, inplace=True)

    df.reset_index(inplace=True, drop=True)

    df_kappa = pd.DataFrame(df)
    for col in df_kappa:
        if col.startswith("Type"):
            df_kappa.drop(col, axis=1, inplace=True)

    df_kappa.replace({'Only humor فكاهة فقط' : 1, 'Only offensive اساءة فقط' : 2, 'Hate Speech الكلام الذي يحض على الكراهية' : 0}, inplace=True)
    df_kappa.drop('Email address', axis=1, inplace=True)

    kappa_dict = dict()
    for col in df_kappa:
        img_name = col[col.find("(")+1:col.find(")")]
        kappa_dict[img_name] = {'0': 0, '1' : 0, '2' : 0}

        for row in df_kappa[col]:
            if row == 0:
                kappa_dict[img_name]['0'] += 1
            elif row == 1:
                kappa_dict[img_name]['1'] += 1
            else:
                kappa_dict[img_name]['2'] += 1

    df_kappa = pd.DataFrame(kappa_dict).T

    return df_kappa


def main():
    df_kappa = pd.DataFrame()

    for i in range(0,29):
        df = pd.read_csv(f'form{i+1}.csv')
        df = prepare_df(df)
        df_kappa = pd.concat([df_kappa, df])
        
    score = fleiss_kappa(df_kappa, method='fleiss')
    print(score)
    
if __name__ == '__main__':
    main()