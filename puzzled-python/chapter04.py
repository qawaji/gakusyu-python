import copy

B = [[0, 0, 1, 0],
     [1, 0, 0, 0],
     [0, 0, 0, 1],
     [0, 1, 0, 0]]

def noConflicts(board, current, qindex, n):
  for j in range(current):
    if board[qindex][j] == 1:
      return False
  k = 1
  while qindex - k >= 0 and current - k >= 0:
    if board[qindex - k][current - k] == 1:
      return False
    k += 1

  k = 1
  while qindex + k < n and current - k >= 0:
    if board[qindex + k][current - k] == 1:
      return  False
    k += 1
  
  return True

def FourQueens(n=4):
  board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
  for i in range(n):
    board[i][0] = 1
    for j in range(n):
      board[j][1] = 1
      if noConflicts(board, 1, j, n):
        for k in range(n):
          board[k][2] = 1
          if noConflicts(board, 2, k, n):
            for m in range(n):
              board[m][3] = 1
              if noConflicts(board, 3, m, n):
                print(board)
              board[m][3] = 0
          board[k][2] = 0
      board[j][1] = 0
    board[i][0] = 0
  return

# 1次元配列
def noConflicts1(board, current):
  for i in range(current):
    if(board[i] == board[current]):
      return False
    if(current - i == abs(board[current] - board[i])):
      return False
  return True

def EightQueens(n=8):
  results = []
  board = [-1] * n
  for i in range(n):
    board[0] = i
    for j in range(n):
      board[1] = j
      if not noConflicts1(board, 1):
        continue
      for k in range(n):
        board[2] = k
        if not noConflicts1(board, 2):
          continue
        for l in range(n):
          board[3] = l
          if not noConflicts1(board, 3):
            continue
          for m in range(n):
            board[4] = m
            if not noConflicts1(board, 4):
              continue
            for o in range(n):
              board[5] = o
              if not noConflicts1(board, 5):
                continue
              for p in range(n):
                board[6] = p
                if not noConflicts1(board, 6):
                  continue
                for q in range(n):
                  board[7] = q
                  if noConflicts1(board, 7):
                    results.append(copy.copy(board))
  return results

def EightQueensWithCount(count):
  results = EightQueens()
  results = results[0:count]
  for r in results:
    print(r)
  return results

def EightQueensWithLocation(location):
  # locationで設定されている場所に女王がある場合はTrue
  def isEqualsLocation(lst, lct):
    if len(lst) != len(lct):
      return False
    
    for i in range(len(lct)):
      if lct[i] == -1:
        continue
      if lst[i] != lct[i]:
        return False
    return True


  results = EightQueens()
  results = list(filter(lambda x: isEqualsLocation(x, location), results))
  for r in results:
    print(r)
  return results

#FourQueens()
#EightQueensWithCount(8)
EightQueensWithLocation([0, -1, 7, -1, -1, -1, -1, -1])