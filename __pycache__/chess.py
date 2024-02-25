import chess
import chess.engine
import chess.svg

piece_values = {
    chess.PAWN: 10,
    chess.KNIGHT: 30,
    chess.BISHOP: 30,
    chess.ROOK: 50,
    chess.QUEEN: 90,
    chess.KING: 900
}

def evaluate_position(board):
    evaluation = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is None:
            continue
        if piece.color == chess.WHITE:
            evaluation += piece_values.get(piece.piece_type, 0)
        else:
            evaluation -= piece_values.get(piece.piece_type, 0)
    return evaluation


def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_position(board), None

    if maximizing_player:
        max_eval = float("-inf")
        best_move = None
        for move in board.legal_moves:
            board.push(move)
            eval, _ = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float("inf")
        best_move = None
        for move in board.legal_moves:
            board.push(move)
            eval, _ = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move


def chess_bot_ai(board, depth):
    _, best_move = minimax(board, depth, float("-inf"), float("inf"), True)
    if best_move:
        return best_move.uci()
    else:
        return " "


def visualize_board(board):
    return chess.svg.board(board=board)

if __name__ == "__main__":
    board = chess.Board()

    while not board.is_game_over():
        print(visualize_board(board))
        if board.turn == chess.WHITE:
            move_uci = input("Enter your move (e.g., 'e2e4'): ")
            board.push(chess.Move.from_uci(move_uci))
        else:
            best_move_uci = chess_bot_ai(board, depth=3)
            print("AI plays:", best_move_uci)
            board.push(chess.Move.from_uci(best_move_uci))
    print("Game Over")
    print("Result: " + board.result())
