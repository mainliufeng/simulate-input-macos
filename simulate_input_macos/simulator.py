import sys
import os
import json
import codecs
import click


@click.command(help='input string')
@click.argument('content', nargs=1)
@click.option('--cmd', is_flag=True, default=False)  # with cmd down
def input(content, cmd):
    if cmd:
        cmd_format = """
        osascript -e 'tell application "System Events" to keystroke "{}" using {{command down}}'
        """
    else:
        cmd_format = """
        osascript -e 'tell application "System Events" to keystroke "{}"'
        """

    for char in content:
        os.system(cmd_format.format(char))
