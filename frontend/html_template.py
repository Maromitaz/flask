from sys import stderr
from colorama import Fore, Style
class HTML_Template():
    html_string = ""
    def __init__(self, file_name: str, token_list: list = None):
        """
        Initializes the object with the given file name and token list.
        
        Parameters:
            file_name (str): The name of the file to be opened.
            token_list (list, optional): A list of tokens to be assigned to the 'tokens' attribute. Defaults to None.
        """
        self.tokens = {}
        self.tokens = token_list
        with open("./templates/" + file_name) as file_contents:
            self.file_list = file_contents.read().split("\n")
        for line in self.file_list:
            self.html_string += self.__serialize_line(self.__tokenize_line(line))
    def __repr__(self):
        return self.html_string
    def __tokenize_line(self, string: str) -> list:
        """
        Tokenizes a given string by splitting it at every occurrence of the "{{" and "}}" delimiters.
        
        Parameters:
            string (str): The string to be tokenized.
        
        Returns:
            list: A list of tokens obtained after splitting the string.
        """
        tok_str = string.split("{{")
        if len(tok_str) > 1:
            sec_tok_str = tok_str[1].split("}}")
            if len(sec_tok_str) == 1:
                tok_str = []
                tok_str.insert(0, string)
                return tok_str
            tok_str.pop(1)
            tok_str += sec_tok_str
        return tok_str
    def __serialize_line(self, token_list: list) -> str:
        """
        Serializes a line of tokens into a string.

        Args:
            token_list (list): A list of tokens representing a line.

        Returns:
            str: The serialized string representation of the line.

        Raises:
            IndexError: If the token list at index 1 (second item in the list) is empty.
            KeyError: If a token in the token list does not exist in the tokens dictionary.
        """
        if len(token_list) == 1:
            return token_list[0]
        
        string = token_list[0]
        try:
            string += self.tokens[token_list[1]]
        except (IndexError, KeyError):
            print(Fore.RED, Style.BRIGHT, f"Token \"{token_list[1]}\" does not exist in token list.", Style.RESET_ALL, file=stderr)
            string += "NULL"
        string += token_list[2]
        return string
    