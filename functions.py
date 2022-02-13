def take_input(promt: str):
    """
    The function takes an inpute from the user, where promt is the promt user sees in the terminal
    """
    x = input(promt)
    return x

def display(x: any):
    """
    The function to display any data we want 
    """
    print(x)
    
def replace_draws(col):
    """
    The function to process the data frame from the csv file
    """
    if col == 'draw':
        return 0
    else:
        return 1