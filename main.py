# Updated implementation for emoji game handler

# Update the game initialization in _show_emoji_game_setup
# Adding the missing game_mode and other required fields.

def _show_emoji_game_setup():
    # ... code before initialization
    game_state = {
        'game_mode': '<desired_game_mode>',  # assuming a placeholder
        'game': '<game_instance>',  # assuming you will set this
        'p_pts': 0,
        'b_pts': 0,
        'cur_rolls': [],
        'p_rolls': [],  # Properly initialize p_rolls
        'emoji_wait': 0,
        'created_at': datetime.utcnow().isoformat()  # Assuming you want to track creation time
    }
    # ... rest of the code

# Ensure p_rolls are updated in handle_emoji_response method

def handle_emoji_response(response):
    # assuming response has an attribute 'roll'
    result = process_response(response)
    game_state['p_rolls'].append(result['roll'])  # Update p_rolls list
    # ... rest of your method code