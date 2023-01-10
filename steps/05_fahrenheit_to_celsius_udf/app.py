#------------------------------------------------------------------------------
# Hands-On Lab: Data Engineering with Snowpark
# Script:       05_fahrenheit_to_celsius_udf/app.py
# Author:       Caleb Baechtold, Jeremiah Hansen
# Last Updated: 1/9/2023
#------------------------------------------------------------------------------

import sys


def main(temp_f: float) -> float:
    return (float(temp_f) - 32) * (5/9)


# For local debugging
# Be aware you may need to type-convert arguments if you add input parameters
if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(main(*sys.argv[1:]))  # type: ignore
    else:
        print(main())  # type: ignore