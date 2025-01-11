def count_invocations(func):
    def wrapper(*args, **kwargs):
        wrapper.invocation_count += 1
        return func(*args, **kwargs)
    wrapper.invocation_count = 0  # Initialize the count
    return wrapper