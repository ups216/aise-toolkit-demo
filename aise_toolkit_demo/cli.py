import subprocess
import click
from click_default_group import DefaultGroup
from click.testing import CliRunner
import os
import aise_toolkit_demo
from aise_toolkit_demo.app import app_utiles

@click.group(
        cls=DefaultGroup,
        default="command",
        default_if_no_args=True,
)
@click.version_option(version='0.5')
def cli():
    "A set of tools to assist developer to use AI"

@cli.command(name="command")
@click.option(
    "-o",
    "--option",
    help="An example option",
)
def first_command(option):
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

@cli.command(name="second_command")
def second_command():
    "Second command description goes here"
    click.echo("This is the second command")

@cli.group(
        cls=DefaultGroup,
        default="start",
        default_if_no_args=True,
)
def app():
    "Commands for the Streamlit app"

@app.command(name="start")
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

    # Run the Streamlit app in the backgroup and get the process ID
    process = subprocess.Popen(["streamlit", "run", app_path])
    cli.echo(f"Streamlit app started with PID {process.pid}")

@app.command(name="stop")
def stop_app():
    """Stop the Streamlit app"""
    # Kill the Streamlit app
    subprocess.Popen(["pkill", "-f", "streamlit"])

@cli.group(
        cls=DefaultGroup,
        default="info",
        default_if_no_args=True,
)
def repo():
    "Commands for the repository"

@repo.command(name="info")
def repo_info():
    "Display repository information"
    click.echo("Repository information goes here")

@repo.command(name="list")
def repo_list():
    "List repository contents"
    click.echo("Repository contents goes here")

@repo.command(name="update")
def repo_update():
    "Update the repository"
    click.echo("Repository update goes here")

if __name__ == "__main__":
    cli()
