### Example that writes to stdout and sleeps

Invoking on its own:

```
$ ~/Documents/repos/ansible-runner-examples/non_playbook/sleep_with_writes/sleep_and_write.sh 
hi world
goodby world
```

Invoking with runner:

```
$ ansible-runner run ~/Documents/repos/ansible-runner-examples/non_playbook/sleep_with_writes/
hi world

goodby world

```

List artifacts from this:

```
ls ~/Documents/repos/ansible-runner-examples/non_playbook/sleep_with_writes/artifacts/
```

content therein:

```
$ cat ~/Documents/repos/ansible-runner-examples/non_playbook/sleep_with_writes/artifacts/5c8a660a-c941-4d2d-b945-5bd15bec202b/stdout
hi world

goodby world

```
