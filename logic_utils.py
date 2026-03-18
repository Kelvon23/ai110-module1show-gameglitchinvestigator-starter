def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        # Bug found & fixed together: Hard was returning 1-50, which made it
        # easier than Normal (1-100). Fixed to 1-200 so Hard is actually harder.
        return 1, 200
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # Bug found & fixed together: app.py was casting secret to a string on even
    # attempts, causing string comparison instead of numeric (e.g. "9" > "10"
    # is True as a string). Fixed by casting both values to int before comparing.
    guess = int(guess)
    secret = int(secret)

    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        # Bug found & fixed together: messages were backwards. Guessing 29 when
        # secret is 25 was saying "Go HIGHER!" — fixed to correctly say "Go LOWER!"
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        # Bug found & fixed together: was awarding +5 points when attempt number
        # was even, which rewarded wrong guesses. Fixed so wrong guesses always
        # deduct 5 points.
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
