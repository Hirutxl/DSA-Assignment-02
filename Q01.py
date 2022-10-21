import array as arr

#main code

items = 10;
knapsack = 30;
current_weight = knapsack;
Ttl_price = 0;

max_weight = arr.array('i', [1,6,8,5,4,6,1,2,3,5])    #respectively items
prices      = arr.array('f',[1050.00,600.00,400.00,1500.00,800.00,1800.00,300.00,900.00,600.00,1000.00])
PtoW = [0]*items


for i in range (10):
  PtoW[i] = prices[i]
  #print(PtoW[i])

while current_weight > 0:
  max = 0
  item = 0
  for i in range (10):
    if(PtoW[i]>max and PtoW[i] != 0):
      max = PtoW[i]
      item = i
  
  if current_weight >= max_weight[item] and PtoW[item] != 0:
    print(f"take item: {item+1}, {max_weight[item]}KG")
    Ttl_price += max
    current_weight -= max_weight[item]
  else:
    print(f"take item: {item+1}, {current_weight}KG")
    Ttl_price += max/max_weight[item] * current_weight
    current_weight -= current_weight
  PtoW[item] = 0

print(f"Total price of the bag: {Ttl_price}")