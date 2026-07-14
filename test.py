import click
import utilities_common.cli as clicommon
from natsort import natsorted
from tabulate import tabulate

from swsscommon.swsscommon import ConfigDBConnector
from utilities_common.cli import pass_db

@click.group(cls=clicommon.AbbreviationGroup, name='test', invoke_without_command=True)
@click.pass_context
def test(ctx):
    """Show test configuration --> """
    config_db= ConfigDBConnector()
    config_db.connect()
    ctx.obj = {'db': config_db}
    header = ["Test Info."]
    db = ctx.obj['db']

    tt = db.get_table('TEST_NEW_CLI')
    print(tt)
    #click.echo(tabulate([(ns,) for ns in tt.keys()], header, tablefmt='simple', stralign='right'))
