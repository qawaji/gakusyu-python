sched = [(6, 8), (6, 12), (6, 7), (7, 8),
         (7, 10), (8, 9), (8, 10), (9, 12),
         (9, 10), (10, 11), (10, 12), (11, 12)]

sched2 = [(6.0, 8.0), (6.5, 12.0), (6.5, 7.0), (7.0, 8.0),
          (7.5, 10.0), (8.0, 9.0), (8.0, 10.0), (9.0, 12.0),
          (9.5, 10.0), (10.0, 11.0), (10.0, 12.0), (11.0, 12.0)]

sched3 = [(6.0, 8.0, 2), (6.5, 12.0, 1), (6.5, 7.0, 2), 
          (7.0, 8.0, 2), (7.5, 10.0, 3), (8.0, 9.0, 2), 
          (8.0, 10.0, 1), (9.0, 12.0, 2),
          (9.5, 10.0, 4), (10.0, 11.0, 2), 
          (10.0, 12.0, 3), (11.0, 12.0, 7)]

def bestTimeToParty(schedule):
  start = schedule[0][0]
  end = schedule[0][1]

  for (cs, ce) in schedule:
    start = min(cs, start)
    end = max(ce, end)

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
    for (cs, ce) in sched:
      if cs <= i and i < ce:
        count[i] += 1
  return count

def bestTimeToPartySmart(schedule, ystart, yend):
  times = []
  for (cs, ce) in schedule:
    times.append((cs, 'start'))
    times.append((ce, 'end'))
  times.sort(key=lambda x: x[0])
  maxcount, time = chooseTime(times, ystart, yend)
  print('Best time to attend the party is at', time, 'o\'clock',
        ':', maxcount, 'celebrities will be attending!')

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
  maxvalue = time = 0
  for ict, (ct_start, ct_end, ct_f) in enumerate(schedule):
    value = ct_f # include target
    for ica, (ca_start, ca_end, ca_f) in enumerate(schedule):
      if ict == ica:
        continue      
      if ca_start <= ct_start and ct_start < ca_end:
        value += ca_f
        if value > maxvalue:
          maxvalue = value
          time = ct_start

  print('Best time to attend the party is at', time, 'o\'clock',
        ': celebrities value is', maxvalue, '!')


bestTimeToParty(sched)
bestTimeToPartySmart(sched2, 5.0, 13.0)
bestTimeToParty2(sched3)