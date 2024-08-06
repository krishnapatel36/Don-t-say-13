
import random
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_moves(current_sum, moves, human_turn):
    if current_sum >= 13:
        return [moves] if not human_turn else []

    all_moves = []
    if human_turn:
        for i in range(1, 3):
            if current_sum + i <= 13:
                new_moves = moves + [(human_turn, i)]
                all_moves.extend(generate_moves(current_sum + i, new_moves, not human_turn))
    else:
        computer_move = computer_turn(current_sum)
        if current_sum + computer_move <= 13:
            new_moves = moves + [(human_turn, computer_move)]
            all_moves.extend(generate_moves(current_sum + computer_move, new_moves, not human_turn))
    
    return all_moves

def computer_turn(current_sum):
    for i in range(1, 3):
        if (current_sum + i) % 3 == 0 and current_sum + i <= 13:
            return i
    for i in range(1, 3):
        if current_sum + i <= 13:
            return i
    return 1

def save_to_pdf(file_name, states):
    c = canvas.Canvas(file_name, pagesize=letter)
    width, height = letter

    margin = 50
    line_height = 12

    def print_line(text, current_height):
        c.drawString(margin, current_height, text)
        return current_height - line_height

    def new_page():
        c.showPage()
        return height - margin

    c.setFont("Helvetica", 10)

    # Write introduction and instructions
    current_height = height - margin
    current_height = print_line("Welcome to 'Don't Say 13'!", current_height)
    current_height = print_line("This is an interactive book where you play against the book.", current_height)
    current_height = print_line("Players take turns saying a number between 1 and 2.", current_height)
    current_height = print_line("The numbers accumulate until a player is forced to say 13.", current_height)
    current_height = print_line("The player who says 13 loses the game.", current_height)
    current_height = print_line("Let's start!", current_height)
    current_height = new_page()

    # Write the game states
    for state, transitions in states.items():
        current_sum, player_choice = state
        current_height = print_line(f"Current sum: {current_sum}", current_height)
        
        if current_sum >= 13:
            result = "You lose! Computer wins!" if player_choice else "Computer loses! You win!"
            current_height = print_line(result, current_height)
        else:
            current_height = print_line(f"Your options:", current_height)
            if player_choice:
                if 1 in transitions:
                    next_page_1 = transitions[1]
                    current_height = print_line(f"If you choose 1, go to page {next_page_1}", current_height)
                if 2 in transitions:
                    next_page_2 = transitions[2]
                    if next_page_1 != next_page_2:
                        current_height = print_line(f"If you choose 2, go to page {next_page_2}", current_height)
            else:
                next_page = transitions[1]
                computer_move = next_page - current_sum
                current_height = print_line(f"Computer says: {computer_move}", current_height)
                current_height = print_line(f"Current sum: {next_page}", current_height)
                current_height = print_line(f"Go to page {next_page}", current_height)
        
        current_height = new_page()

    c.save()

def main():
    all_games = generate_moves(0, [], human_turn=True)
    states = {}
    page_counter = 1

    for game in all_games:
        current_sum = 0
        player_choice = True

        for is_human, move in game:
            state = (current_sum, player_choice)
            next_sum = current_sum + move
            next_state = (next_sum, not player_choice)

            if state not in states:
                states[state] = {}

            if player_choice:
                states[state][move] = next_state
            else:
                states[state][1] = next_state

            current_sum = next_sum
            player_choice = not player_choice

    state_pages = {}
    for state in states.keys():
        state_pages[state] = page_counter
        page_counter += 1

    resolved_states = {}
    for state, transitions in states.items():
        resolved_transitions = {}
        for move, next_state in transitions.items():
            if next_state in state_pages:
                resolved_transitions[move] = state_pages[next_state]
        resolved_states[state] = resolved_transitions

    save_to_pdf("dont_say_13_book.pdf", resolved_states)

# Run the main function
main()
import random
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_moves(current_sum, moves, human_turn):
    if current_sum >= 13:
        return [moves] if not human_turn else []

    all_moves = []
    if human_turn:
        for i in range(1, 3):
            if current_sum + i <= 13:
                new_moves = moves + [(human_turn, i)]
                all_moves.extend(generate_moves(current_sum + i, new_moves, not human_turn))
    else:
        computer_move = computer_turn(current_sum)
        if current_sum + computer_move <= 13:
            new_moves = moves + [(human_turn, computer_move)]
            all_moves.extend(generate_moves(current_sum + computer_move, new_moves, not human_turn))
    
    return all_moves

def computer_turn(current_sum):
    for i in range(1, 3):
        if (current_sum + i) % 3 == 0 and current_sum + i <= 13:
            return i
    for i in range(1, 3):
        if current_sum + i <= 13:
            return i
    return 1

def save_to_pdf(file_name, states):
    c = canvas.Canvas(file_name, pagesize=letter)
    width, height = letter

    margin = 50
    line_height = 12

    def print_line(text, current_height):
        c.drawString(margin, current_height, text)
        return current_height - line_height

    def new_page():
        c.showPage()
        return height - margin

    c.setFont("Helvetica", 10)

    # Write introduction and instructions
    current_height = height - margin
    current_height = print_line("Welcome to 'Don't Say 13'!", current_height)
    current_height = print_line("This is an interactive book where you play against the book.", current_height)
    current_height = print_line("Players take turns saying a number between 1 and 2.", current_height)
    current_height = print_line("The numbers accumulate until a player is forced to say 13.", current_height)
    current_height = print_line("The player who says 13 loses the game.", current_height)
    current_height = print_line("Let's start!", current_height)
    current_height = new_page()

    # Write the game states
    for state, transitions in states.items():
        current_sum, player_choice = state
        current_height = print_line(f"Current sum: {current_sum}", current_height)
        
        if current_sum >= 13:
            result = "You lose! Computer wins!" if player_choice else "Computer loses! You win!"
            current_height = print_line(result, current_height)
        else:
            current_height = print_line(f"Your options:", current_height)
            if player_choice:
                if 1 in transitions:
                    next_page_1 = transitions[1]
                    current_height = print_line(f"If you choose 1, go to page {next_page_1}", current_height)
                if 2 in transitions:
                    next_page_2 = transitions[2]
                    if next_page_1 != next_page_2:
                        current_height = print_line(f"If you choose 2, go to page {next_page_2}", current_height)
            else:
                next_page = transitions[1]
                computer_move = next_page - current_sum
                current_height = print_line(f"Computer says: {computer_move}", current_height)
                current_height = print_line(f"Current sum: {next_page}", current_height)
                current_height = print_line(f"Go to page {next_page}", current_height)
        
        current_height = new_page()

    c.save()

def main():
    all_games = generate_moves(0, [], human_turn=True)
    states = {}
    page_counter = 1

    for game in all_games:
        current_sum = 0
        player_choice = True

        for is_human, move in game:
            state = (current_sum, player_choice)
            next_sum = current_sum + move
            next_state = (next_sum, not player_choice)

            if state not in states:
                states[state] = {}

            if player_choice:
                states[state][move] = next_state
            else:
                states[state][1] = next_state

            current_sum = next_sum
            player_choice = not player_choice

    state_pages = {}
    for state in states.keys():
        state_pages[state] = page_counter
        page_counter += 1

    resolved_states = {}
    for state, transitions in states.items():
        resolved_transitions = {}
        for move, next_state in transitions.items():
            if next_state in state_pages:
                resolved_transitions[move] = state_pages[next_state]
        resolved_states[state] = resolved_transitions

    save_to_pdf("dont_say_13_book.pdf", resolved_states)

# Run the main function
main()
