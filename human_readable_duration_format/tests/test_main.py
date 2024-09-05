# TDD and trying to keep our initial testing simple (a reason for this is because we might not know where our code takes us)
# Think about inputs and outputs of the function. How might you test these?
# If the input is 0, the output is "Now"
# If the input is 1, the output is "1 second"
# If the input is 5, the output is "5 seconds"

def format_duration(seconds):
    if seconds > 1:
        return f"{seconds}" + " seconds"
    elif seconds == 1:
        return "1 second"
    return "now"


def test_input_0_output_now():
    #arrange
    something_else = 0
    #act
    output = format_duration(something_else)
    #assert
    assert output == "now"

def test_input_1_output_1_second():
    #arrange
    test_input = 1
    #act
    output = format_duration(test_input)
    #assert
    assert output == "1 second"

def test_input_2_output_1_seconds():
    assert format_duration(2) == "2 seconds"

def test_input_20_output_20_seconds():
    assert format_duration(20) == "20 seconds"
