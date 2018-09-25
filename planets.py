
def weight_on_planets():

   counter = 1
   text1 = "What do you weigh on earth? "
   text2 = "On Mars you would weigh"
   text3 = "On Jupiter you would weigh"
   marsWeight = ""
   jupiterWeight = ""
   weight = 0.0

   for i in range(2):
      if counter == 1:
         weight = float(input(text1))
         counter += 1
      else:
         marsWeight = weight * 0.38
         jupiterWeight = weight * 2.34
         print("\n" + text2, marsWeight, 'pounds.' + "\n" + text3, jupiterWeight, 'pounds.')

if __name__ == '__main__':
   weight_on_planets()