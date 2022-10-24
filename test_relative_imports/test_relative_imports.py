#!/usr/bin/env python3
# -*- coding: utf8 -*-
# disable: byte-vector-replacer

from __future__ import annotations

import click
from eprint import eprint

from .cli.gui import gui


@click.group()
@click.pass_context
def clitest(
    ctx,
) -> None:
    eprint("clitest()")


clitest.add_command(gui, name="gui")
