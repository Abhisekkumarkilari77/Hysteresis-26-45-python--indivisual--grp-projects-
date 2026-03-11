#!/usr/bin/env python
# main.py
from .controller import Controller

def run():
    ctl = Controller(); ctl.bootstrap(); ctl.submit_workload(); ctl.tick()
    ctl.fail_first_node(); ctl.tick(); ctl.report()

if __name__ == "__main__":
    run()
