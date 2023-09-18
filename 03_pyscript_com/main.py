from random import randint
from pyscript import when, document


def to_int(value: str) -> int:
    """Simple function to cast a string to an int, in a BAFTP fashion."""
    try:
        int_v = int(value)
    except ValueError:
        return 0
    else:
        return int_v


@when("click", "#droll_btn")
def dice_roll():
    # Select the two input elements
    n_rolls_el = document.querySelector("#n_rolls")
    n_sides_el = document.querySelector("#n_sides")

    n_rolls = to_int(n_rolls_el.value)
    n_sides = to_int(n_sides_el.value)

    if not n_rolls or not n_sides:
        result = "<span style='color:red'>Please check input values</span>"
    else:
        rolls = [f"<li>{randint(1, n_sides)}</li>" for _ in range(n_rolls)]
        result = f"<ul>{''.join(rolls)}</ul>"

    # Select outcome Element
    outcome_el = document.querySelector("#outcome")
    outcome_el.innerHTML = result  # modify innerHTML property
