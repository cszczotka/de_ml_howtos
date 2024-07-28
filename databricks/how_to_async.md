To be able run python asyncio you need to nest_asyncio

```python
import nest_asyncio
nest_asyncio.apply()
asyncio.run(run())
```