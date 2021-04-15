class Module:
    def __init__(self):
        self.settings: dict = {
            "module": {
                "property": {}
            }
        }

    def read_file(self, filename: str):
        if filename[-4:] != ".tcl":
            raise Exception(f"Unexpected format to open.\nExpected: .tcl\nReceived: {filename[-4:]}")
        with open(filename) as file:

            for e, row in enumerate(file):
                subrows = row.split(" ")
                command = subrows.pop(0).split("_")
                if command[0] == "add":
                    self.__add(
                        command=command,
                        row=subrows
                    )
                elif command[0] == "set":
                    self.__set(
                        command=command,
                        row=subrows
                    )
            # print(self.settings)

    def __add(self, command: list, row: list):
        if len(command) == 2:
            new_dict = {
                command[1]: {
                    "name": row[0]
                }
            }
            # print(f"__add\n{command}\n{row}\n\n")
            self.settings.update(new_dict)

        if len(command) == 3:
            self.settings[command[1]].update({
                "param1": row[0],
                "param2": row[1],
                "param3": row[2],
                "param4": row[3],
                "param5": row[4]
            })
            # print(f"__add\n{command}\n{row}\n\n")

    def __set(self, command: list, row: list):

        if len(row) == 2:
            try:
                property = self.settings[command[1]][command[2]]
            except KeyError:
                self.settings[command[1]][command[2]] = {

                }
                property = self.settings[command[1]][command[2]]

            property.update(
                {
                    row[0]: row[1][:-1]
                }
            )

        if len(row) == 3:
            print(f"__set\n{command}\n{row}\n\n")

            try:
                property = self.settings[command[1]][command[2]]

            except KeyError:
                self.settings[command[1]][command[2]] = {}
                property = self.settings[command[1]][command[2]]

            property.update(
                {

                }
            )
            
m = Module()
data = m.read_file("example.tcl")
