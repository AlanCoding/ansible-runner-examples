### Python event lag bug identification

From runner directory

```
python ~/Documents/repos/ansible-runner-examples/python/sleep_with_writes/run.py
```

Example output pre-fix:

```
$ python ~/Documents/repos/ansible-runner-examples/python/sleep_with_writes/run.py 
hi world

goodby world

I have event!!!1 1554823620.95646
{'event': 'verbose', 'uuid': '88af9170-57c4-4f48-895a-1bc373d174d9', 'counter': 1, 'stdout': 'hi world', 'start_line': 0, 'end_line': 1, 'runner_ident': '42'}


I have event!!!1 1554823620.9566422
{'event': 'verbose', 'uuid': '6984d341-ba4a-45a0-b64b-0280297c01c1', 'counter': 2, 'stdout': 'goodby world', 'start_line': 1, 'end_line': 2, 'runner_ident': '42'}


```
