
"""
hub-pip
Usage:
  hub-pip 
        [
        (-c <hub_config.ini>) 
        --Hub.Url=<huburl>
        --Hub.Username=<username>
        --Hub.Password=<password>
        --Hub.Proxy.Host=<None>
        --Hub.Proxy.Port=<None>
        --Hub.Proxy.Username=<None>
        --Hub.Proxy.Password=<None>
        --Hub.Timeout=<120>
        --Hub.ScanTimeout=<300>
        --Hub.CodeLocationName=<None>
        --OutputDirectory=<build/output/>
        --IgnoreFailure=<False>
        --CreateFlatDependencyList=<True>
        --CreateTreeDependencyList=<True>
        --CreateHubBdio=<True>
        --DeployHubBdio=<True>
        --CheckPolicies=<True>
        ]

Options:
    -h --help                            Show this screen.
    --version                            Show version.
    (-c <hub_config.ini>)                Path to hub configuration file
Examples:
  hub-pip test
Help:
  For help using this tool, please open an issue on the Github_pip repository:
  https://github.com/BlackDuckSoftware/hub-python-plugin
"""


from inspect import getmembers, isclass

from docopt import docopt
from hub_pip.BlackDuckPlugin import BlackDuckCommand

from . import __version__ as VERSION
from .BlackDuckConfig import BlackDuckConfig


def main():
    """Main CLI entrypoint."""
    import hub_pip.commands

    options = docopt(__doc__, version=VERSION)

    config_str = "[Black Duck Config]\n"

    for key, value in options.iteritems():
        if "--" in key and value is not None:
            field = key.replace("--", "")
            config_option = field + " = " + str(value) + "\n"
            config_str += config_option

    config = None
    if options["-c"]:
        config_file_path = options["<hub_config.ini>"]
        config = BlackDuckConfig.from_file(config_file_path)

    config = BlackDuckConfig.from_string(config_str, black_duck_config=config)
