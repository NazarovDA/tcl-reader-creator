# coding: UTF-8
import json
import time

program_name = "i don't choose now"


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

    def write_to_tcl(self):
        with open(f"{self.settings['module']['property']['NAME']}.tcl", "w") as writeFile:
            writeFile.write(f"# TCL File Generated by {program_name}\n"
                            f"{time.asctime()}\n"
                            f"DO NOT MODIFY\n"
                            f"\n"
                            f"\n"
                            f"#\n"
                            f"# {self.settings['module']['property']['NAME']} "
                            f"{self.settings['module']['property']['NAME']} "
                            f"v{self.settings['module']['property']['VERSION']}\n"
                            f"# {time.asctime()}\n"
                            f"#\n"
                            f"#\n"
                            f"\n"
                            f"#\n"
                            f"# request TCL package from ACDS 16.1\n"
                            f"#\n"
                            f"package require -exact qsys 16.1\n"
                            f"\n"
                            f"\n")  # heading

            # module properties
            writeFile.write(f"#\n"
                            f"# module {self.settings['module']['property']['NAME']}\n"
                            f"#\n")
            for prop in self.settings['module']['property']:
                writeFile.write(f"set_module_property {prop} {self.settings['module']['property'][prop]}\n")

            # file sets
            try:
                writeFile.write(f"\n"
                                f"\n"
                                f"#\n"
                                f"#file sets\n"
                                f"#\n")
                d = self.settings['fileset']
                for fileset in d:
                    if fileset != "files":
                        empty_str = ""
                        writeFile.write(f'add_fileset {fileset} {fileset} "" "" \n')
                        actualDict = d[fileset]
                        for prop in actualDict['property']:
                            writeFile.write(f'set_fileset_property {fileset} {prop} {actualDict["property"][prop]}\n')
                    if fileset == 'files':
                        actualDict = d[fileset]
                        for file in actualDict:
                            writeFile.write(f"add_fileset_file {file}"
                                            f" {actualDict[file]['type']}"
                                            f" PATH {actualDict[file]['PATH']}"
                                            f"{' TOP_LEVEL_FILE' if actualDict[file]['status'] is not None else ''}")
                            writeFile.write('\n') if actualDict[file]['status'] is not None else writeFile.write('')
            except KeyError:
                pass

            try:
                writeFile.write(f"\n"
                                f"\n"
                                f"#\n"
                                f"#paramaters\n"
                                f"#\n")
                d = self.settings['parameter']
                for param in d:
                    print(f"{param} {d[param]}")
                    writeFile.write(f'add_parameter {param} {d[param]["property"]["TYPE"]} {d[param]["property"]["DEFAULT_VALUE"]}\n')
                    for prop in d[param]["property"]:
                        writeFile.write(f"set_parameter_property {param} {prop} {d[param]['property'][prop]}\n")

            except KeyError:
                pass


    def read_file(self, filename: str):
        if filename[-4:] != ".tcl":
            raise Exception(f"Unexpected format to open.\nExpected: .tcl\nReceived: {filename[-4:]}")
            # if we took not .tcl file
        elif filename[-4:] == ".tcl":
            return self.__read_tcl(filename=filename)

        elif filename[-5:] == ".json":
            with open(filename, "w") as file:
                self.settings = json.load(file)

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
                    d = self.settings[command[1]]["files"]
                except KeyError:
                    d = self.settings[command[1]]["files"] = {}
                try:
                    newDict: dict = d[row[0]]
                except KeyError:
                    newDict = d[row[0]] = {}

                newDict.update(
                    {
                        "type": row[1],
                        row[2]: row[3],
                        "status": row[4][:-1] if len(row) == 5 else None
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
