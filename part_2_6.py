def step_function_maker(start_time, end_time, value):
    """
    Takes in start_time, end_time, value,
    returns the inner function of my_fuction(time)
    """
    def my_function(time):
        """Validate the order of three parameters,
        returns value if parameter of my_fuction()
        which lies inbetween two other parameters or
        returns 0.0
        """
        if start_time <= time <= end_time:
            y = value
        else:
            y = 0.0
        return y

    return my_function
