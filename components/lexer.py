import sys
import re
program_filepath = sys.argv[1]


class Lexer:
    def __init__(self, program_filepath):
        # init obj using a file path to the program.
        self.lines = self.program_lines(program_filepath)
        self.tokens = []; self.tokenize()
        self.current_line = 0
        self.current_char = 0

    def program_lines(self, filepath):
        # Read the program file and return a list of lines.
        with open(filepath, 'r') as file:
            return [line.strip() for line in file.readlines()]
        
    def tokenize_line(self, line) -> None:
        if(line == "" or line.startswith("note") or line.startswith("//")):
            pass
        # Tokenize a single line of the program.
        if(line.startswith("str")):
            self.tokens.append({"type":"TYPE", "value":"str"})

            # Matches: ^str <one-or-more-spaces> <one-or-more-word-chars> ...
            id_match = re.compile(r'^str\s+(\w+)').match(line)
            self.tokens.append({"type":"ID", "value":id_match.group(1)})

            operator_match = re.compile(r'\s*(=|\+=|\-=|\*=|/=|\*\*=|%=)').search(line, id_match.end())
            self.tokens.append({"type":"ASSIGN", "value":operator_match.group(1)})
            self.tokens.append({"type":"STRING", "value":line.split(" ")[3]})

        elif(line.startswith("int")):
            self.tokens.append({"type":"TYPE", "value":"int"})
            self.tokens.append({"type":"ID", "value":line.split(" ")[1]})
            

        elif(line.startswith("float")):
            self.tokens.append({"type":"TYPE", "value":"float"})
            self.tokens.append({"type":"ID", "value":line.split(" ")[1]})

        elif(line.startswith("bool")):
            self.tokens.append({"type":"TYPE", "value":"bool"})
            self.tokens.append({"type":"ID", "value":line.split(" ")[1]})
            self.tokens.append({"type":"ASSIGN", "value":"="})
            self.tokens.append({"type":"BOOL", "value":line.split(" ")[3]})
            

    
    def tokenize(self):
        # Tokenize the program lines.
        for line in self.lines:
            self.tokenize_line(line)
    
    def __str__(self):
        return str(self.tokens)
    
if __name__ == '__main__':
    lexer = Lexer(program_filepath)
    print(lexer)