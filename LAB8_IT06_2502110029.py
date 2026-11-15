# Place this inside shoptools.py

def parse_safely(line):
    """Parses a line and returns (diameter, None) or (None, error_string)."""
    try:
        parts = line.split()
        dia = float(parts[1])
        shift = parts[2]
        return dia, None
    except AttributeError:
        return None, "AttributeError"
    except IndexError:
        return None, "IndexError"
    except ValueError:
        return None, "ValueError"

def run_tests():
    """Feeds all eight hostile inputs through the parser to self-certify."""
    hostile = [
        "X-001 twenty Day", "X-002", "", "X-004 25.01", 
        "   ", "X-006 25.0.1 Day", None, []
    ]
    
    print(f"{'Test Input':<20} | {'Test Status':<12} | {'Caught Exception'}")
    print("-" * 55)
    
    for test_case in hostile:
        result, error = parse_safely(test_case)
        
        # In a test suite, catching the expected error means the test PASSED
        status = "PASS (Handled)" if error else "FAIL (Crashed)"
        
        # Formatting for readability
        display_input = str(test_case) if test_case is not None else "None Object"
        if len(display_input) == 0 or display_input.isspace():
            display_input = "[Empty/Whitespace]"
            
        print(f"{display_input:<20} | {status:<12} | {error}")

# Run the test suite on demand
if __name__ == "__main__":
    run_tests()
