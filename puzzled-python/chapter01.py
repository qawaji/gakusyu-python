cap1 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F']
cap3 = ['F', 'F', 'B', 'H', 'H', 'B', 'F', 'B', 'B', 'B', 'F', 'H', 'F', 'F']

def pleaseConfirm(caps):
  start = forward = backward = 0
  intervals = []
  caps = caps + ['END']
  for i in range(1, len(caps)):
    if caps[start] != caps[i]:
      intervals.append((start, i - 1, caps[start]))
      if caps[start] == 'F':
        forward += 1
      elif caps[start] == 'B':
        backward += 1
      else:
        pass
      start = i
  intervals.append((start, len(caps) - 1, caps[start]))
  flip = 'F' if forward < backward else 'B'

  for t in intervals:
    if t[2] == flip:
      if t[0] == t[1]:
        print('People in position', t[0], 'flip your cap!')
      else:
        print('People in positions', t[0], 'through', t[1], 'flip your caps!')

def pleaseConfirmOnepass(caps):
  caps = caps + [caps[0]]
  start = 0
  for i in range(1, len(caps)):
    if caps[i] != caps[i - 1]:
      if caps[i] != caps[0]:
        start = i
      else:
        if start == i - 1:
          print('People in position', start, 'flip your cap!')
        else:
          print('People in positions', start, 'through', i - 1, 'flip your caps!')

pleaseConfirm(cap1)
pleaseConfirmOnepass(cap1)
pleaseConfirm(cap3)

print(cap1)