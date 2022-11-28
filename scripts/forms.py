import pandas as pd


def not_valid(col):
  if col.startswith('Image Classified') or col.startswith('Email') or col.startswith('Type'):
    return False
  return True


def find_meme_type(df, col):
  hate, off, humor, max = 0, 0, 0, 0
  best = ''

 
  for row in df[col]:
    # print(row)
    if 'Hate' in str(row):
      hate += 1
      if hate >= max:
        best = 'hate_speech'
        max = hate
    elif 'humor' in str(row):
      humor += 1
      if humor > max:
        best = ' only humor'
        max = humor
    else:
      off += 1
      if off > max: 
        best = 'only offensive'
        max = off
    
  return best


def find_hate_type(df, col):
  rel, gen, org, ddd, race, max = 0, 0, 0, 0, 0, 0
  best = ''

  for row in df[col]:
    if not isinstance(row, str):
      continue

    if 'Religion' in row:
      rel += 1
      if rel > max:
        best = 'religion'
        max = rel
    if 'Gender' in row:
      gen += 1
      if gen > max:
        best = 'gender'
        max = gen
    if 'National' in row:
      org += 1
      if org > max: 
        best = 'national_origin'
        max = org
    if 'Disability' in row:
      ddd += 1
      if ddd > max: 
        best = 'ddd'
        max = ddd
    if 'Race' in row:
      race += 1
      if race > max: 
        best = 'race'
        max = race
    
  return best

def create_dataframe(df):
  dic = dict()

  is_hate = False
  current_img = ''
  for col in df.columns:
    if 'Image' in col:
      meme_type = find_meme_type(df, col)
      if meme_type == 'hate_speech':
        is_hate = True
      else:
        is_hate = False

      img_name = col[col.find("(")+1:col.find(")")]
      dic[img_name] = {'meme_type': meme_type}
      
      current_img = img_name

    elif 'Email' not in col:
      if is_hate:
        hate_type = find_hate_type(df, col)
        dic[current_img]['hate_type'] = hate_type
      else:
        dic[current_img]['hate_type'] = 'no hate'
  
  df_ready = pd.DataFrame(dic).T
  df_ready.reset_index(inplace=True)
  df_ready.rename({'index' : 'file_name'}, axis=1, inplace=True)

  return df_ready


def main():
    df_all = pd.DataFrame()

    for i in range(29):
        df = pd.read_csv(f'form{i+1}.csv')

        for col in df.columns:
            if not_valid(col):
                df.drop(col, axis=1, inplace=True)  
        

        df_ready = create_dataframe(df)

        df_all = pd.concat([df_all, df_ready], axis=0)
    
    df_all.reset_index(inplace=True)
    df_all.to_csv('all-forms.csv')




if __name__ == '__main__':
    main()