cap1 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F']

def pleaseConfirm(capsin):
  start = forward = backward = 0
  intervals = []
  caps = capsin + ['END']
  for i in range(1, len(caps)):
    if caps[start] != caps[i]:
      intervals.append((start, i - 1, caps[start]))
      if caps[start] == 'F':
        forward += 1
      else:
        backward += 1
      start = i
  intervals.append((start, len(caps) - 1, caps[start]))
  flip = 'F' if forward < backward else 'B'

  for t in intervals:
    if t[2] == flip:
      print('People in positions', t[0], 'through', t[1], 'flip your caps!')

pleaseConfirm(cap1)