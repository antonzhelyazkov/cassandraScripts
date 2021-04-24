import json
import os
import sys
import subprocess

config_file_name = os.path.basename(sys.argv[0]).split('.')[0]
CONFIG_FILE = f"/etc/check_mk/{config_file_name}"


def main():
    print(f'<<<{config_file_name}>>>')
    try:
        config_handler = open(CONFIG_FILE, 'r')
        config_raw = config_handler.read()
    except OSError as err:
        print(f"ERROR miss {err}")
        return False

    try:
        config = json.loads(config_raw)
    except json.decoder.JSONDecodeError as conf_err:
        print(f"ERROR config {conf_err}")
        return False

    service = filter(lambda seq: config[seq]['type'] == 'service', config.keys())
    print(list(service))


if __name__ == "__main__":
    main()
