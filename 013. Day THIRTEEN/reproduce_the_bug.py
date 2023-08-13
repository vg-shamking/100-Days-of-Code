# Reproduce the Bug

from random import randint

dice_image = ["""
1111
  11
  11
  11
111111""",
              """
 2222
22  22
   22
  22
222222""",
              """
 3333
33  33
   333
33  33
 3333""",
              """
44  44
44  44
444444
    44
    44""",
              """
555555
55
55555
    55
55555""",
              """
 6666
66
66666
66  66
 6666"""]
dice_num = randint(0, 5)
print(dice_image[dice_num])
