def square_root_bisection(square_target, tolerance=1e-7, max_iterations=10):
    if square_target < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    elif square_target == 0 or square_target == 1:
        print(f"The square root of {square_target} is {square_target}")
        return square_target

    # Set bounds depending on target
    if square_target < 1:
        low = square_target
        high = 1
    else:
        low = 0
        high = square_target

    iterations = 0

    while iterations < max_iterations:
        mid = (low + high) / 2
        mid_squared = mid * mid

        if mid_squared < square_target:
            low = mid
        else:
            high = mid

        # Stop if interval is smaller than tolerance
        if high - low <= tolerance:
            mid = (low + high) / 2
            print(f"The square root of {square_target} is approximately {mid}")
            return mid

        iterations += 1

    # If max_iterations reached and tolerance not met
    print(f"Failed to converge within {max_iterations} iterations")
    return None


    

    

square_root_bisection(0.001, 1e-7, 50)