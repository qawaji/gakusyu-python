sched = [(6, 8), (6, 12), (6, 7), (7, 8),
         (7, 10), (8, 9), (8, 10), (9, 12),
         (9, 10), (10, 11), (10, 12), (11, 12)]

sched2 = [(6.0, 8.0), (6.5, 12.0), (6.5, 7.0), (7.0, 8.0),
          (7.5, 10.0), (8.0, 9.0), (8.0, 10.0), (9.0, 12.0),
          (9.5, 10.0), (10.0, 11.0), (10.0, 12.0), (11.0, 12.0)]

def bestTimeToParty(schedule):
  start = schedule[0][0]
  end = schedule[0][1]

  for c in schedule:
    start = min(c[0], start)
    end = max(c[1], end)

  count = celebrityDensity(schedule, start, end)

  maxcount = 0
  for i in range(start, end + 1):
    if count[i] > maxcount:
      maxcount = count[i]
      time = i
  
  print('Best time to attend the party is at', time, 'o\'clock',
        ':', maxcount, 'celebrities will be attending!')

def celebrityDensity(schedule, start, end):
  count = [0] * (end + 1)
  for i in range(start, end + 1):
    count[i] = 0
    for c in sched:
      if c[0] <= i and i < c[1]:
        count[i] += 1
  return count

def bestTimeToPartySmart(schedule, ystart, yend):
  times = []
  for c in schedule:
    times.append((c[0], 'start'))
    times.append((c[1], 'end'))
  sortList(times)
  maxcount, time = chooseTime(times, ystart, yend)
  print('Best time to attend the party is at', time, 'o\'clock',
        ':', maxcount, 'celebrities will be attending!')

def sortList(tlist):
  for ind in range(len(tlist) - 1):
    iSm = ind
    for i in range(ind, len(tlist)):
      if tlist[iSm][0] > tlist[i][0]:
        iSm = i
    tlist[ind], tlist[iSm] = tlist[iSm], tlist[ind]

def chooseTime(times, ystart, yend):
  rcount = 0
  maxcount = time = 0
  for t in times:
    if t[1] == 'start':
      rcount += 1
    elif t[1] == 'end':
      rcount -= 1
    if ystart <= t[0] and t[0] < yend and rcount > maxcount:
      maxcount = rcount
      time = t[0]
  return maxcount, time

def bestTimeToParty2(schedule):
  maxcount = time = 0
  for iTarget in range(len(schedule)):
    count = 1 # include target
    for iAnother in range(len(schedule)):
      if iTarget == iAnother:
        continue      
      target = schedule[iTarget]
      another = schedule[iAnother]      
      if another[0] <= target[0] and target[0] < another[1]:
        count += 1
        if count > maxcount:
          maxcount = count
          time = target[0]

  print('Best time to attend the party is at', time, 'o\'clock',
        ':', maxcount, 'celebrities will be attending!')


bestTimeToParty(sched)
bestTimeToPartySmart(sched2, 5.0, 13.0)
bestTimeToParty2(sched2)