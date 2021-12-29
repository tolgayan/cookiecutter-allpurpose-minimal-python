"""
file_explanation

If you are developing an api module, like fastapi, this file can be your api entry point.
"""

# =============================================================================
from logger import init_logger 
init_logger()
# =============================================================================


import argparse
import logging


logger = logging.getLogger(__name__)


def main(args):
    logger.info("Success.")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    main(args)