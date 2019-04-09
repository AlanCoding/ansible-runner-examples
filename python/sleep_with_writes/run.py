import time
import ansible_runner
import os


dest = '~/Documents/repos/ansible-runner-examples/python/sleep_with_writes/'

dest = os.path.expanduser(dest)


def my_event_handler(event_data):
    print("I have event!!!1 {}".format(time.time()))
    print(event_data)
    print('\n')


res = ansible_runner.interface.run(
    ident=42,  # ??
    private_data_dir=dest,
    project_dir=dest,
    event_handler=my_event_handler
)

