#!/usr/bin/env python3
# -*- coding: utf8 -*-
# disable: byte-vector-replacer

from __future__ import annotations

import click

from .cli.gui import gui


@click.group()
@click.pass_context
def clitest(
    ctx,
) -> None:
    print("__main__.py clitest()")


clitest.add_command(gui, name="gui")


if __name__ == "__main__":
    # pylint: disable=E1120
    clitest()
