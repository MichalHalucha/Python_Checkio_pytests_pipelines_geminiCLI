from src import Variable_Declaration_and_Value_Setting

def test_variable_values_exist():
    """Check that variables are defined and have expected values."""
    assert Variable_Declaration_and_Value_Setting.cyborgs == 10
    assert Variable_Declaration_and_Value_Setting.robots == 2
    assert Variable_Declaration_and_Value_Setting.droids == 5

def test_type_annotations():
    """Check that annotated variables still keep correct types."""
    assert isinstance(Variable_Declaration_and_Value_Setting.cyborgs, int)
    assert isinstance(Variable_Declaration_and_Value_Setting.robots, int)
    assert isinstance(Variable_Declaration_and_Value_Setting.droids, int)
