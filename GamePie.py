human_turn = input('input human turn: ')
computer_turn = input('input computer turn: ')

if human_turn == computer_turn:
  print('draw!')
elif human_turn == 'rock' and computer_turn == 'scissor':
  print('Human wins!')
elif human_turn == 'paper' and computer_turn == 'rock':
  print('Human wins!')
elif human_turn == 'scissor' and computer_turn == 'paper':
 print('Human win!')
else:
  print('Computer wins')
