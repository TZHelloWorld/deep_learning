# -*- coding: UTF-8 -*-
r"""
@time : 2022/6/27 16:33
@Author : tz
@File : rich_terminal.py
@Description : rich的一些使用, https://rich.readthedocs.io/en/stable/protocol.html
"""
import time

from rich.console import Console

console = Console()
console.rule("[bold red]开始测试")

console.log("Hello, World!")
console.rule("")

console.print([1, 2, 3])
console.print("[blue underline]Looks like a link")
console.print(locals())
console.print("FOO", style=" green")

# console.log("Hello, World!")

from rich.json import JSON

console.log(JSON('["foo", "bar"]'))

console.out("Locals", locals())

# 异常打印处理
try:
    int("a")
except Exception:
    console.print_exception()
    # console.print_exception(show_locals=True)

from rich import print as rprint

rprint(locals())

from rich.progress import track

for step in track(range(100)):
    time.sleep(0.1)

from rich.progress import Progress, TextColumn, BarColumn, TimeElapsedColumn, TimeRemainingColumn
import time

with Progress(TextColumn("[progress.description]{task.description}"),
              BarColumn(),
              TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
              TimeRemainingColumn(),
              TimeElapsedColumn()) as progress:
    epoch_tqdm = progress.add_task(description="epoch progress", total=10)
    batch_tqdm = progress.add_task(description="batch progress", total=100)
    for ep in range(10):
        for batch in range(100):
            # print("ep: {} batch: {}".format(ep, batch))
            progress.advance(batch_tqdm, advance=1)
            time.sleep(0.1)
        progress.advance(epoch_tqdm, advance=1)
        progress.reset(batch_tqdm)
r"""
教程Progress



"""
