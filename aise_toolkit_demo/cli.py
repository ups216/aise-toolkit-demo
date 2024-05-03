import subprocess
import click
from click.testing import CliRunner
import os
import aise_toolkit_demo
from aise_toolkit_demo.app import app_utiles

@click.group()
@click.version_option(version='0.5')
def cli():
    "A set of tools to assist developer to use AI"

@cli.command(name="command")
@click.argument(
    "example"
)
@click.option(
    "-o",
    "--option",
    help="An example option",
)
def first_command(example, option):
    "Command description goes here"
    click.echo(f"Here is some output: {aise_toolkit_demo.get_message()}")
    click.echo(f"Here is some output: {aise_toolkit_demo.calculate()}")
    click.echo(f"Here is some output: {app_utiles.app_get_message()}")
    click.echo(f"Here is some output: {app_utiles.app_calculate()}")
    click.echo(f"Runing from PyInstaller bundle: {aise_toolkit_demo.is_running_in_pyinstaller_bundle()}")
    # if running from PyInstaller bundle, print the temp folder
    if aise_toolkit_demo.is_running_in_pyinstaller_bundle():
        click.echo(f"Temp folder: {aise_toolkit_demo.get_temp_folder()}")
    # wait for user input
    input("Press Enter to continue...")

@cli.command(name="start_app")
def start_app():
    """Start the Streamlit app from ./app/app.py"""
    # get the current directory
    current_dir = os.getcwd()
    click.echo(current_dir)

    # Path to the Streamlit app
    if aise_toolkit_demo.is_running_in_pyinstaller_bundle():
        app_path = os.path.join(aise_toolkit_demo.get_temp_folder(), "app", "app.py")
    else:
        app_path = os.path.join(current_dir, "aise_toolkit_demo", "app", "app.py")
    click.echo(app_path)

    # Run the Streamlit app
    subprocess.run(["streamlit", "run", app_path])

if __name__ == "__main__":
    cli()
