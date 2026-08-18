# Steam concurrent-player API

Steam player-interest trends via the Trends API. Monthly CCU history, growth, and live most-played. No Steam Web API key.

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/trendsapi-steam.svg)](https://pypi.org/project/trendsapi-steam/)
[![Python](https://img.shields.io/badge/python-3.9%2B-yellow.svg)](https://trendsapi.ai)

Key: [trendsapi.ai/#get-key](https://trendsapi.ai/#get-key). HTTP contract and every source: [trendsapi-ai/trendsapi](https://github.com/trendsapi-ai/trendsapi).

## Authentication

```bash
pip install trendsapi-steam
export TRENDSAPI_KEY=your_key
```

Python 3.9+. Same key as the HTTP API.

```python
from trendsapi_steam import TrendsAPI

client = TrendsAPI()                    # TRENDSAPI_KEY
# client = TrendsAPI(api_key="YOUR_KEY")
```

Keyword helpers default to `source: "steam"`. Pass `source=` to hit any other platform with the same client. Official full client (every source, no preset): [`trendsapi`](https://pypi.org/project/trendsapi/).

## Methods

| Method | REST `mode` | Returns |
|---|---|---|
| `get_time_series(keyword, source=, data_mode=)` | `get_time_series` | `list[TrendsDataPoint]` |
| `get_growth(keyword, percent_growth=, source=, data_mode=)` | `get_growth` | `GetGrowthResponse` |
| `get_live(limit=, offset=, category=)` | `get_top_trends` | `GetTopTrendsResponse` |
| `get_top_trends(type=, ...)` | `get_top_trends` | `GetTopTrendsResponse` |

`source` is lowercase (`steam`). `type` is exact (`Steam Most Played`). Mixing them is a 400.

```python
from trendsapi_steam import TrendsAPI

client = TrendsAPI()                    # TRENDSAPI_KEY
# client = TrendsAPI(api_key="YOUR_KEY")

series = client.get_time_series("counter-strike 2")
print(series[-1].date, series[-1].value)

growth = client.get_growth("counter-strike 2", percent_growth=["3M", "12M"])
print(growth.results[0].growth, growth.results[0].direction)

hot = client.get_live(limit=10)
print(hot.data)                         # [[1, "..."], ...]
```

## get_time_series

```python
points = client.get_time_series("counter-strike 2")
```

Each point:

| Field | Always | Meaning |
|---|---|---|
| `date` | yes | `YYYY-MM-DD` |
| `value` | yes | 0-100 index for this series |
| `keyword` | yes | Echo |
| `volume` | no | Absolute volume when available |
| `source` or `datatype` | no | Pipeline label |

Python returns `list[TrendsDataPoint]`. Use `.date` and `.value`, not `["date"]`.
JS returns the same fields as object properties.

## get_growth

```python
g = client.get_growth("counter-strike 2", percent_growth=["12M", "3M", "YTD"])
print(g.results[0].growth, g.results[0].direction)
```

`percent_growth` default: `["12M"]`. Presets: `7D` `14D` `30D` `1M` `2M` `3M` `6M` `9M` `12M`/`1Y` `18M` `24M`/`2Y` `36M`/`3Y` `48M` `60M`/`5Y` `MTD` `QTD` `YTD`. Custom: `{"name": "Launch", "recent": "2024-06-01", "baseline": "2024-01-01"}`.

| Field | Meaning |
|---|---|
| `search_term` | Keyword |
| `data_source` | Source |
| `results` | One object per window (`period`, `growth`, `direction`, dates, values) |
| `metadata` | Counts / success flag |

Several windows still count as one request. Python: `growth.results[0].growth`. JS: `growth.results[0].growth`.


## get_live

```python
hot = client.get_live(limit=10)
```

| Field | Meaning |
|---|---|
| `as_of_ts` | Snapshot time |
| `type` | Feed name |
| `limit`, `offset`, `count` | Pagination |
| `data` | `[rank, label]` rows |

Python: `hot.data`. JS: `hot.data`. Optional `offset=` and `category=` (`Amazon Best Sellers by Category`, `Top Websites` only).


## Async

```python
import asyncio
from trendsapi_steam import AsyncTrendsAPI

async def main():
    c = AsyncTrendsAPI()
    return await asyncio.gather(
        c.get_time_series("counter-strike 2"),
        c.get_time_series("counter-strike 2", source="google search"),
    )

asyncio.run(main())
```

Each 200 is one billed request.

## Pandas

```python
from dataclasses import asdict
import pandas as pd
from trendsapi_steam import TrendsAPI

df = pd.DataFrame(asdict(p) for p in TrendsAPI().get_time_series("counter-strike 2"))
df["date"] = pd.to_datetime(df["date"])
print(df.set_index("date")["value"].resample("ME").mean().tail())
```

## Call (curl)

| Field | Value |
|---|---|
| Endpoint | `POST https://api.trendsapi.ai/api` |
| Auth | `Authorization: Bearer $TRENDSAPI_KEY` |
| History | `source: steam` with `get_time_series` or `get_growth` |
| Keyword | Game display name, e.g. counter-strike 2 |
| Live `type` | Steam Most Played |

```bash
curl -sS -X POST https://api.trendsapi.ai/api \
  -H "Authorization: Bearer $TRENDSAPI_KEY" \
  -H "Content-Type: application/json" \
  -d '{"mode":"get_time_series","source":"steam","keyword":"counter-strike 2"}'
```

## Source notes

- The backend resolves the name via Steam store search. AppIDs are not a request field.
- Series is monthly. `value` is 0-100 vs that title, not raw CCU.
- `type: steam` is 400.

## Errors

| HTTP | Client |
|---|---|
| 200 | Parsed payload. Python dataclasses / JS typed objects |
| 400 | Raises. Fix `source` or `type` spelling |
| 401 | Raises. Check `TRENDSAPI_KEY` |
| 404 | Raises. No series for that keyword. Do not retry |
| 429 | Raises. Quota |
| 5xx | Client retries, then raises |

The HTTP `body` field is a JSON string. SDKs decode it. Raw curl must parse `body` a second time.

Site: [https://trendsapi.ai/trends/steam-trends](https://trendsapi.ai/trends/steam-trends).

## License

MIT. See [LICENSE](LICENSE).
