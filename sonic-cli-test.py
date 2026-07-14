#!/usr/bin/python3
import sys
from cli_client import ApiClient, Path
from rpipe_utils import pipestr
from scripts.render_cli import show_cli_output

def call_rest_cli_test(path, args):
    if len(args) > 0:
        #body = {"sonic-TEST_NEW_CLI:TEST_NEW_CLI":{"test":{"IP_PREFIX":args[0], "with":"with","IFNAME":args[1]}}}
        body = {
            "sonic-TEST_NEW_CLI:TEST_NEW_CLI": {
            "test": {
                        "IP_PREFIX": args[0],
                        "with": "with",
                        "IFNAME": args[1]
            }
        }
                                    }
        resp = ApiClient().patch(path, body)
        print(body)
    else:
        resp = ApiClient().get(path, ignore404=False)

    if not resp.ok():
        print(resp.error_message())
        return 1
    else:
        respJson = resp.content
        print(f'response: {respJson}')
    return 0

class Handlers:
    @staticmethod
    def set_cli_test(template, *args):
        allif_path = Path("/restconf/data/sonic-TEST_NEW_CLI:sonic-TEST_NEW_CLI/TEST_NEW_CLI")
        print(allif_path)
        return call_rest_cli_test(allif_path, args)

    @staticmethod
    def get_cli_test(template, *args):
        oneif_path = Path("/restconf/data/sonic-TEST_NEW_CLI:sonic-TEST_NEW_CLI/TEST_NEW_CLI")
        print(oneif_path)
        return call_rest_cli_test(oneif_path, args)

def run(func, args):
    return getattr(Handlers, func)(*args)

if __name__ == '__main__':
    pipestr().write(sys.argv)
    func = sys.argv[1]
    run(func, sys.argv[1:])
