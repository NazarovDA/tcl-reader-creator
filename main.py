# coding: UTF-8
import module


def do_smth():
    m = module.Module()
    m.read_file("example.tcl")
    m.write_to_tcl()
    m.write_to_json()


if __name__ == "__main__":
    do_smth()
