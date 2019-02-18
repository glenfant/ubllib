"""
======
ubllib
======

Command line handling
"""

import argparse
import logging
import sys

from . import __version__, LOG


def main(argv=sys.argv):
    """Main function called from console command
    """
    logging.basicConfig()
    exit_code = 1
    try:
        app = Application(argv)
        app.run()
        exit_code = 0
    except KeyboardInterrupt:
        exit_code = 0
    except Exception as exc:
        LOG.exception(exc)
    sys.exit(exit_code)


class Application(object):
    """The main Application class

    :param argv: The command line as a list as ``sys.argv``
    """

    def __init__(self, argv):
        # FIXME: Customize your command
        ap = argparse.ArgumentParser()
        ap.add_argument('--version', action='version', version=__version__)
        self.args = ap.parse_args(args=argv[1:])
        """Arguments of your app"""

    def run(self):
        # FIXME: Replace below sample with your code
        print("Hey! It works ;o)")


if __name__ == '__main__':
    main()
