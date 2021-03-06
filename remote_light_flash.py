#!/usr/bin/python3
"""Simple executable to demonstrate a remote light flash."""

import argparse
import logging
from bimmer_connected.account import ConnectedDriveAccount


def main():
    """Main function."""
    logging.basicConfig(level=logging.DEBUG)

    parser = argparse.ArgumentParser()
    parser.add_argument('username')
    parser.add_argument('password')
    parser.add_argument('vin')
    parser.add_argument('country')
    args = parser.parse_args()

    account = ConnectedDriveAccount(args.username, args.password, args.country)
    vehicle = account.get_vehicle(args.vin)

    status = vehicle.remote_services.trigger_remote_light_flash()
    print(status.state)


if __name__ == '__main__':
    main()
