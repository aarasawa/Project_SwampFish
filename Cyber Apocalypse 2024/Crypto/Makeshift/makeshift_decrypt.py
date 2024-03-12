enc_str = '!?}De!e3d_5n_nipaOw_3eTR3bt4{_THB'

dec_str = ''

for i in range(0, len(enc_str), 3):
  dec_str += enc_str[i + 2]
  dec_str += enc_str[i]
  dec_str += enc_str[i + 1]

print(dec_str[::-1])