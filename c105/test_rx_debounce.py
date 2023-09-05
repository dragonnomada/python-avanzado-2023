from reactivex import interval
from reactivex import operators

source = interval(0.15) # A (150ms) [0, 1, 2, 3, ...]

source_count = interval(1) # B (1,000ms) [0, 1, 2, 3, ...]

debounced_source = source.pipe( # A' (1,000ms) 
    operators.throttle_first(1) # 150ms -> 1,000ms 
)

zip_count_debounced = source_count.pipe(
    operators.zip(debounced_source),
    operators.take(20)
)

import asyncio

done = asyncio.Future()

loop = asyncio.get_event_loop()

from reactivex.scheduler.eventloop import AsyncIOScheduler

zip_count_debounced.subscribe(
    on_next=lambda x: print(x),
    on_completed=lambda: done.set_result("ok"),
    scheduler=AsyncIOScheduler(loop=loop)
)

async def main():
    await done

    print(done.result())

loop.run_until_complete(main())