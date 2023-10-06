def select_file(title, default_path):
    """
    Opens a file dialog and returns the path to the selected file.

    Args:
        title (str): The title of the file dialog.
        default_path (str): The default path to the file.

    Returns:
        str: The path to the selected file.
    """
    from tkinter.filedialog import askopenfilename
    filename = askopenfilename(title=title, initialdir=default_path)
    return filename

if __name__ == '__main__':
    filename = select_file("Select a file", "/home/user")
    print(filename)