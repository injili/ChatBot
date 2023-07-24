import random

R_EATING = ""
R_ADVICE = ""


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
                random.randrange(4)]
    return response
