def hard_voting(answer1, answer2, answer3):
  final_answer = []
  answers = [answer1, answer2, answer3]

  for i in range(len(answer1)):
    cnt0, cnt1 = 0, 0
    for a in answers:
      if a[i] == '1':
        cnt1 += 1
      else:
        cnt0 += 1
        
    if cnt1 > cnt0:
      final_answer.append(1)
    else:
      final_answer.append(0)

  with open('final_answer.txt', 'w') as f:
    for i, pred in enumerate(final_answer):
      f.write(f'{test_df.images[i]}\t{pred}\n')