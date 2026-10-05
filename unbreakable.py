# unbreakable.py
from safe_tools import safe_divide, safe_number, get_field

def run_pipeline():
    print("--- Running Unbreakable Pipeline ---")
    
    # Testing division
    print("10 / 2 =", safe_divide(10, 2))
    print("10 / 0 =", safe_divide(10, 0))

    # Testing string conversion
    print("Number '42':", safe_number("42"))
    print("Number 'abc':", safe_number("abc"))

    # Testing dictionary lookups
    learner = {"name": "Amina", "score": 82}
    print("Score:", get_field(learner, "score"))
    print("Email:", get_field(learner, "email"))

if __name__ == "__main__":
    run_pipeline()