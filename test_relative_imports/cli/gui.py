#!/usr/bin/env python3

import click
from eprint import eprint


@click.command()
def gui():
    eprint("gui()")
