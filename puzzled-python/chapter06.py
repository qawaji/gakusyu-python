def compare(groupA, groupB):
  if sum(groupA) > sum(groupB):
    result = 'left'
  elif sum(groupA) < sum(groupB):
    result = 'right'
  elif sum(groupA) == sum(groupB):
    result = 'equal'
  return result

def splitCoins(coinsList):
  length = len(coinsList)
  group1 = coinsList[0:length//3]
  group2 = coinsList[length//3:length//3*2]
  group3 = coinsList[length//3*2:length]
  return group1, group2, group3

def findFakeGroup(group1, group2, group3):
  result1and2 = compare(group1, group2)
  if result1and2 == 'left':
    fakeGroup = group1
  elif result1and2 == 'right':
    fakeGroup = group2
  elif result1and2 == 'equal':
    fakeGroup = group3
  return fakeGroup

def CoinComparison(coinsList):
  counter = 0
  currList = coinsList
  while len(currList) > 1:
    group1, group2, group3 = splitCoins(currList)
    currList = findFakeGroup(group1, group2, group3)
    counter += 1
  fake = currList[0]
  index = coinsList.index(fake)

  allSameWeight = (coinsList[0] == coinsList[-1]) if index == 0 else False
  if allSameWeight:
    counter += 1
    print('All same weight!')
  else:
    print('Take fake coin is coin', index + 1, 'in the original list')
  
  print('Number of weighings:', counter)

coinsList = [ 10, 10, 10, 10, 10, 10, 11, 10, 10, 
              10, 10, 10, 10, 10, 10, 10, 10, 10, 
              10, 10, 10, 10, 10, 10, 10, 10, 10, ]

coinsList2 = [ 10, 10, 10, 10, 10, 10, 10, 10, 10, 
              10, 10, 10, 10, 10, 10, 10, 10, 10, 
              10, 10, 10, 10, 10, 10, 10, 10, 10, ]

coinsList3 = [ 11, 10, 10, 10, 10, 10, 10, 10, 10, 
              10, 10, 10, 10, 10, 10, 10, 10, 10, 
              10, 10, 10, 10, 10, 10, 10, 10, 10, ]

CoinComparison(coinsList)
CoinComparison(coinsList2)
CoinComparison(coinsList3)