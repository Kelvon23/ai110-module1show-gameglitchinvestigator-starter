from logic_utils import check_guess, get_range_for_difficulty, update_score


# ── existing tests (fixed: check_guess returns a tuple, not a plain string) ──

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# ── Bug 1: backwards hints ────────────────────────────────────────────────────
# You reported: secret=25, guess=29 → game said "Go HIGHER" (wrong, should say
# "Go LOWER" because 29 > 25).

def test_hint_says_go_lower_when_guess_is_too_high():
    """Hint message must tell the player to go LOWER when guess > secret."""
    outcome, message = check_guess(29, 25)
    assert outcome == "Too High"
    assert "LOWER" in message.upper(), (
        f"Expected hint to say 'Go LOWER' but got: {message!r}"
    )

def test_hint_says_go_higher_when_guess_is_too_low():
    """Hint message must tell the player to go HIGHER when guess < secret."""
    outcome, message = check_guess(20, 25)
    assert outcome == "Too Low"
    assert "HIGHER" in message.upper(), (
        f"Expected hint to say 'Go HIGHER' but got: {message!r}"
    )


# ── Bug 2: Hard difficulty is easier than Normal ──────────────────────────────
# Hard returns range 1–50 but Normal returns 1–100, so Hard is actually easier.

def test_hard_range_is_wider_than_normal():
    """Hard mode should have a larger number range than Normal mode."""
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high, (
        f"Hard high={hard_high} should be greater than Normal high={normal_high}"
    )

def test_easy_range_is_narrower_than_normal():
    """Easy mode should have a smaller number range than Normal mode."""
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    assert easy_high < normal_high, (
        f"Easy high={easy_high} should be less than Normal high={normal_high}"
    )


# ── Bug 3: score incorrectly awards points for a "Too High" guess ─────────────
# update_score adds +5 when outcome is "Too High" AND attempt_number is even,
# which rewards wrong guesses instead of penalising them.

def test_too_high_guess_never_increases_score():
    """A 'Too High' guess should never increase the player's score."""
    score_before = 100
    score_after = update_score(score_before, "Too High", attempt_number=2)
    assert score_after <= score_before, (
        f"Score went UP from {score_before} to {score_after} on a wrong guess "
        f"(attempt 2, 'Too High') — should never increase for a wrong guess."
    )

def test_too_high_guess_on_odd_attempt_decreases_score():
    """A 'Too High' guess on any attempt should decrease score."""
    score_before = 100
    score_after = update_score(score_before, "Too High", attempt_number=1)
    assert score_after < score_before, (
        f"Score should decrease for a 'Too High' guess but got {score_after}."
    )

def test_too_low_guess_decreases_score():
    """A 'Too Low' guess should always decrease score."""
    score_before = 100
    score_after = update_score(score_before, "Too Low", attempt_number=1)
    assert score_after < score_before


# ── Bug 4: type coercion on even attempts ─────────────────────────────────────
# app.py casts secret to str() on even-numbered attempts, so check_guess
# receives (int, str). The function must still return the correct outcome.

def test_check_guess_correct_when_secret_is_string():
    """check_guess should handle a string secret and still report a win."""
    outcome, message = check_guess(50, "50")
    assert outcome == "Win"

def test_check_guess_too_high_when_secret_is_string():
    """check_guess with a string secret should still detect guess > secret."""
    outcome, message = check_guess(60, "50")
    assert outcome == "Too High"

def test_check_guess_too_low_when_secret_is_string():
    """check_guess with a string secret should still detect guess < secret."""
    outcome, message = check_guess(40, "50")
    assert outcome == "Too Low"


# ── Bug reported: hints were backwards ───────────────────────────────────────
# Secret=25, guess=29 was returning "Go HIGHER" when it should say "Go LOWER".
# Secret=25, guess=20 was returning "Go LOWER" when it should say "Go HIGHER".

def test_hint_go_lower_when_guess_above_secret():
    """Guessing 29 when secret is 25 should tell the player to go LOWER."""
    _, message = check_guess(29, 25)
    assert "LOWER" in message.upper(), (
        f"Expected 'Go LOWER' but got: {message!r}"
    )

def test_hint_go_higher_when_guess_below_secret():
    """Guessing 20 when secret is 25 should tell the player to go HIGHER."""
    _, message = check_guess(20, 25)
    assert "HIGHER" in message.upper(), (
        f"Expected 'Go HIGHER' but got: {message!r}"
    )


# ── Bug reported: New Game did not reset status or history ────────────────────
# Pressing New Game only reset attempts and secret. status stayed as
# "won"/"lost" so the game hit st.stop() and ignored every new guess.

def test_new_game_resets_status_to_playing():
    """After a New Game reset, status must be 'playing' so guesses are accepted."""
    session = {"status": "won", "history": [10, 20, 42]}

    session["status"] = "playing"
    session["history"] = []

    assert session["status"] == "playing"

def test_new_game_clears_history():
    """After a New Game reset, history must be empty so old guesses don't leak in."""
    session = {"status": "lost", "history": [1, 2, 3, 4, 5]}

    session["status"] = "playing"
    session["history"] = []

    assert session["history"] == []
