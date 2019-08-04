deck = ['A_C', 'A_D', 'A_H', 'A_S',
        '2_C', '2_D', '2_H', '2_S',
        '3_C', '3_D', '3_H', '3_S',
        '4_C', '4_D', '4_H', '4_S',
        '5_C', '5_D', '5_H', '5_S',
        '6_C', '6_D', '6_H', '6_S',
        '7_C', '7_D', '7_H', '7_S',
        '8_C', '8_D', '8_H', '8_S',
        '9_C', '9_D', '9_H', '9_S',        
        '10_C', '10_D', '10_H', '10_S',
        'J_C', 'J_D', 'J_H', 'J_S',
        'Q_C', 'Q_D', 'Q_H', 'Q_S',
        'K_C', 'K_D', 'K_H', 'K_S',]

class Card:
  def __init__(self, name):
    self.name = name
    self.idx = deck.index(name)
    self.suit = self.idx % 4
    self.number = self.idx // 4

def AssistantOrdersCards():
  print('Cards are character strings as shown below.')
  print('Ordering is:', deck)
  cards = []
  numsuits = [0, 0, 0, 0]
  for i in range(5):
    print('Please give card', i + 1, end = ' ')
    name = input('in above format:')
    card = Card(name)
    cards.append(card)
    numsuits[card.suit] += 1
    if numsuits[card.suit] > 1:
      pairsuit = card.suit

  cardh = []
  for c in cards:
    if c.suit == pairsuit:
      cardh.append(c)
  hidden, other, encode = outputFirstCard(cardh)

  remindices = []
  for c in cards:
    if c.name != hidden.name and c.name != other.name:
      remindices.append(c)

  remindices.sort(key=lambda x:x.idx)
  outcards = [other]
  outcards.extend(outputNext3Cards(encode, remindices))
  return outcards

def outputFirstCard(oneTwo):
  encode = (oneTwo[0].number - oneTwo[1].number) % 13
  if encode > 0 and encode <= 6:
    hidden = oneTwo[0]
    other = oneTwo[1]
  else:
    hidden = oneTwo[1]
    other = oneTwo[0]
    encode = (oneTwo[1].number - oneTwo[0].number) % 13
  print('First card is:', other.name)
  return hidden, other, encode

def outputNext3Cards(code, cards):
  if code == 1:
    s, t, f = cards[0], cards[1], cards[2]
  elif code == 2:
    s, t, f = cards[0], cards[2], cards[1]
  elif code == 3:
    s, t, f = cards[1], cards[0], cards[2]
  elif code == 4:
    s, t, f = cards[1], cards[2], cards[0]
  elif code == 5:
    s, t, f = cards[2], cards[0], cards[1]
  else:
    s, t, f = cards[2], cards[1], cards[0]
  print('Second card is:', s.name)
  print('Third card is:', t.name)
  print('Fourth card is:', f.name)
  return [s, t, f]

def MagicianGuessesCard():
  print('Cards are character strings as shown below.')
  print('Ordering is:', deck)
  cards = []
  for i in range(4):
    print('Please give card', i + 1, end = ' ')
    name = input('in above format:')
    card = Card(name)
    cards.append(card)

  if cards[1].idx < cards[2].idx and cards[1].idx < cards[3].idx:
    if cards[2].idx < cards[3].idx:
      encode = 1
    else:
      encode = 2
  elif ((cards[1].idx < cards[2].idx and cards[1].idx > cards[3].idx)
  or (cards[1].idx > cards[2].idx and cards[1].idx < cards[3].idx)):
    if cards[2] < cards[3]:
      encode = 3
    else:
      encode = 4
  elif cards[1].idx > cards[2].idx and cards[1].idx > cards[3].idx:
    if cards[2].idx < cards[3].idx:
      encode = 5
    else:
      encode = 6
      
  suit = cards[0].suit
  number = cards[0].number
  hiddennumber = (number + encode) % 13
  index = hiddennumber * 4 + suit
  print('Hidden card is:', deck[index])


outcards = AssistantOrdersCards()
print(list(map(lambda x: x.name, outcards)))

MagicianGuessesCard()
