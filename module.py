# coding: UTF-8
import json


class Module:
    def __init__(self):
        self.settings: dict = {
            "module": {
                "property": {}
            }
        }

    def write_to_json(self):
        with open(f"{self.settings['module']['property']['NAME']}.json", "w") as writeFile:
            json.dump(self.settings, writeFile)

    def read_file(self, filename: str):
        if filename[-4:] != ".tcl":
            raise Exception(f"Unexpected format to open.\nExpected: .tcl\nReceived: {filename[-4:]}")
            # if we took not .tcl file
        elif filename[-4:] == ".tcl":
            return self.__read_tcl(filename=filename)

        # TODO reading own jsons

    def __read_tcl(self, filename):
        with open(filename) as file:
            for row in file:
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

            return self.settings

    def __add(self, command: list, row: list):
        if len(command) == 2:
            try:
                newDict = self.settings[command[1]]
            except KeyError:
                newDict = self.settings[command[1]] = {}

            commandDict = newDict[row[0]] = {}

        elif len(command) == 3:
            if command[1] == 'fileset' and command[2] == 'file':
                try:
                    newDict = self.settings[command[1]][row[0]]
                except KeyError:
                    newDict = self.settings[command[1]][row[0]] = {}

                newDict.update(
                    {
                        "type": row[1],
                        row[2]: row[3],
                        "status": row[4][:-1]
                    }
                )

            else:
                try:
                    newDict = self.settings[command[1]][row[0]]
                except KeyError:
                    newDict = self.settings[command[1]][row[0]] = {}

                newDict.update(
                    {
                        "IO_type": row[3],
                        "name": row[1],
                        "value": row[4][:-1],
                    }
                )

    def __set(self, command: list, row: list):
        if len(row) == 2:
            try:
                newDict = self.settings[command[1]][command[2]]

                newDict.update(
                    {
                        row[0]: row[1][:-1]
                    }
                )
            except Exception:
                print(Exception)

        elif len(row) == 3:
            try:
                newDict = self.settings[command[1]][row[0]][command[2]]
            except KeyError:
                newDict = self.settings[command[1]][row[0]][command[2]] = {}

            newDict.update(
                {
                    row[1]: row[2][:-1]
                }
            )

    """
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
    """
