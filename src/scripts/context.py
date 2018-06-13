import gdb
from builtins import str


class ContextCommand(BaseCommand):
    """Lists all symbols in the current context."""

    def __init__(self):
        super(ContextCommand, self).__init__("context")

    def action(self, arg, from_tty):
        frame = gdb.selected_frame()
        block = frame.block()
        names = set()
        variables = []
        while block:
            for symbol in block:
                name = symbol.name
                if (name not in names) and (symbol.is_argument or
                                            symbol.is_variable or symbol.is_function or
                                            symbol.is_constant):
                    scope = "local"
                    if block.is_global:
                        scope = "global"
                    elif block.is_static:
                        scope = "static"
                    elif symbol.is_argument:
                        scope = "argument"
                    names.add(name)
                    # value can be too big, and we dont use it, we use load_value
                    variables.append({
                        "name": symbol.name,
                        "type": str(symbol.type),
                        "scope": scope
                    })
            block = block.superblock
        return variables


gdbjsContext = ContextCommand()
