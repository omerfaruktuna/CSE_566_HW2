import numpy as np
import math

x = 1

with open('dataset.txt', 'r') as f:
  dataset = []
  content = f.readlines()

  for line in content:

    dataset.append([])
    for i in range(len(line.strip().split(" "))):
      asd = line.strip().split(" ")[i]
      try:
        if i == 0:
          dataset[x-1].append(float(asd))
        elif i == 1:
          dataset[x-1].append(int(asd))
      except ValueError:
        print("error on line {}".format(i))

    x+=1

#print(dataset)

features = np.array(dataset)[:,0]
labels = np.array(dataset)[:,-1]

class_0 = []
class_1 = []

for i in range(len(labels)):
  if labels[i] == 0:
    class_0.append(features[i])
  elif labels[i] == 1:
    class_1.append(features[i])


print("Data points for Class_0 in given dataset:{}".format(class_0))
print("Data points for Class_1 in given dataset:{}".format(class_1))

def find_mean(a_list):
  sum = 0
  for i in a_list:
    sum += i
  return sum/len(a_list)

print("\nMean of 2 classes is :")
print("For Class_0 :{}".format(find_mean(class_0)))
print("For Class_1 :{}".format(find_mean(class_1)))


def find_variance(a_list):
  mean = find_mean(a_list)
  sum = 0
  for i in a_list:
    sum += math.pow((i-mean),2)
  return sum/len(a_list)

print("\nVariances of 2 classes is :")
print("For Class_0 :{}".format(find_variance(class_0)))
print("For Class_1 :{}".format(find_variance(class_1)))

def find_standard_deviation(a_list):
  return math.sqrt( find_variance(a_list) )

print("\nStandard Deviation of 2 classes is :")
print("For Class_0 :{}".format(find_standard_deviation(class_0)))
print("For Class_1 :{}".format(find_standard_deviation(class_1)))

class_0_prob = len(class_0)/(len(class_0)+len(class_1))
class_1_prob = len(class_1)/(len(class_0)+len(class_1))

#print(class_0_prob)
#print(class_1_prob)

def model_output(input_value):

  g_0_a=-1/2*math.log(2*math.pi)
  #print("\ng_0_a is {}".format(g_0_a))
  g_0_b= math.log(find_standard_deviation(class_0))
  #print("g_0_b is {}".format(g_0_b))
  g_0_c= math.pow((input_value-find_mean(class_0)),2)/(2*find_variance(class_0))
  #print("g_0_c is {}".format(g_0_c))
  g_0_d= math.log(class_0_prob)
  #print("g_0_d is {}".format(g_0_d))
  g_0 = g_0_a- g_0_b - g_0_c + g_0_d
  print("\ng(x) calculation for class_0 is {}\n".format(g_0))

  g_1_a=-1/2*math.log(2*math.pi)
  #print("g_1_a is {}".format(g_1_a))
  g_1_b= math.log(find_standard_deviation(class_1))
  #print("g_1_b is {}".format(g_1_b))
  g_1_c= math.pow((input_value-find_mean(class_1)),2)/(2*find_variance(class_1))
  #print("g_1_c is {}".format(g_1_c))
  g_1_d= math.log(class_1_prob)
  #print("g_1_d is {}".format(g_1_d))
  g_1 = g_1_a- g_1_b - g_1_c + g_1_d

  print("g(x) calculation for class_1 is {}".format(g_1))
  
  if g_0 > g_1:
    return "\nTest Input Number Belongs to Class 0"
  elif g_0 < g_1:
    return "\nTest Input Number Belongs to Class 1"

print("\nTraining from the input dataset is completed..")

input_number    = float(input("\nEnter Some Number to Find Which Class It Belongs Based on Training Datset: "))

print(model_output(input_number))
