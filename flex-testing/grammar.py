grammar = """
space ::= " "?
boolean ::= ("true" | "false") space
string ::=  "\"" (
        [^"\\] |
        "\\" (["\\/bfnrt] | "u" [0-9a-fA-F] [0-9a-fA-F] [0-9a-fA-F] [0-9a-fA-F])
      )* "\"" space
personopplysningkategorier ::= "[" space (string ("," space string)*)? "]" space
root ::= "{" space "\"inneholder_personinfo\"" space ":" space boolean "," space "\"personopplysningkategorier\"" space ":" space personopplysningkategorier "}" space
"""