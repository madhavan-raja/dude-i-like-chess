import chess
import random


board = chess.Board()
is_player_turn = True


while not board.is_game_over():
  print(board)
  print()

  if is_player_turn:
    current_move = input("Enter current move: ")
    current_move = board.parse_san(current_move)
  else:
    current_move = random.choice(list(board.legal_moves))
    print(f"Computer plays {current_move}")

  board.push(current_move)
  is_player_turn = not is_player_turn
