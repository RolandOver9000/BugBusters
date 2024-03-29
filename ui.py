""" User Interface (UI) module """


def get_column_widths(table, title_list):
    extra_whitespace = 2
    title_lengths = [len(title) for title in title_list]
    column_widths = []
    for i, column in enumerate(zip(*table)):
        element_lengths = [len(element) for element in column]
        max_length = max(element_lengths)
        if title_lengths[i] > max_length:
            max_length = title_lengths[i]
        column_widths.append(max_length + extra_whitespace)
    return column_widths

def get_border_line(column_widths, delimiters):
    (left, middle, right) = (0, 1, 2)
    border_line = delimiters[left]
    for column_width in column_widths[:-1]:
        border_line += '-' * column_width + delimiters[middle]
    border_line += '-' * column_width + delimiters[right]
    return border_line


def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    column_widths = get_column_widths(table, title_list)
    top_border_line = get_border_line(column_widths, ['/', '-', '\\'])
    middle_border_line = get_border_line(column_widths, ['|', '|', '|'])
    bottom_border_line = get_border_line(column_widths, ['\\', '-', '/'])


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    option_indent = ' ' * 4
    print(title)
    for i, option in enumerate(list_options):
        print(f"{option_indent}({i+1}) {option}")
    print(f"{option_indent}(0) {exit_message}")


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []
    for label in list_labels:
        user_input = input(label)
        inputs.append(user_input)

    return inputs


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print(f"\nError: {message}\n")
