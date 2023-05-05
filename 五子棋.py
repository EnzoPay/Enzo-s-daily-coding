# --------------------------------------------Initialize Settings----------------------------------------------------------------------------------------------------------------------------------

board = [[" " for _ in range(11)] for _ in range(11)]
color = "white"
# --------------------------------------------Define Functions----------------------------------------------------------------------------------------------------------------------------------
def print_board():
    for i in range(len(board)):
        if i < 9:
            print(i+1,"  ",board[i])
        else:
            print(i + 1, " ", board[i])
    print("     ",[str(_) + " " for _ in range(1,11)])

def check_winner(board):
    height = len(board)
    width = len(board[0])
    for i in range(height):
        for j in range(width):
            if board[i][j] != " ":
                # Check horizontal
                count = 1
                while count < 5:
                    if j+1 >= width:
                        break
                    if board[i][j] == board[i][j+1]:
                        count += 1
                        j += 1

                    else:
                        break
                if count == 5:
                    return True
                # Check vertical
                count = 1
                while count < 5:
                    if i+1 >= height:
                        break
                    if board[i][j] == board[i+1][j]:
                        count += 1
                        i += 1

                    else:
                        status = False
                        break
                if count == 5:
                    return True
                # Check slant
                count = 1
                while count < 5:
                    if i + 1 >= height or j + 1 >= width:
                        break
                    if board[i][j] == board[i + 1][j + 1]:
                        count += 1
                        i += 1
                        j += 1

                    else:
                        break
                if count == 5:
                    return True
                # Check slant
                count = 1
                while count < 5:
                    if i-1 < 0 or j+1 >= width:
                        break

                    if board[i][j] == board[i - 1][j + 1]:
                        count += 1
                        i += 1
                        j -= 1

                    else:
                        break

                if count == 5:
                    return True
# -------------------------------------------Run the Code------------------------------------------------------------------------------------------------------------------------
while True:
    if check_winner(board):
        #Check winner
        if color == "white":
            print("BLACK WINS")
            break
        else:
            print("WHITE WINS")
            break

    print_board()
    print("input position like this 3,10")
    print("It is " + color + "'s term")
    position = input("position: ").split(",")
    col = int(position[0])
    row = int(position[1])
    # Input pieces
    if board[col-1][row-1] == " ":
        if color == "white":
            board[col-1][row-1] = "O"
            color = "black"
        else:
            board[col-1][row-1] = "0"
            color = "white"
    else:
        print("change the position")







