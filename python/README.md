# Steam concurrent-player API

Steam player-interest trends via the Trends API. Monthly CCU history, growth, and live most-played. No Steam Web API key.

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/trendsapi-steam.svg)](https://pypi.org/project/trendsapi-steam/)

Key: [trendsapi.ai/#get-key](https://trendsapi.ai/#get-key). Full contract: [trendsapi-ai/trendsapi](https://github.com/trendsapi-ai/trendsapi).

## Install

```bash
pip install trendsapi-steam
```

```python
from trendsapi_steam import TrendsAPI

client = TrendsAPI()  # TRENDSAPI_KEY
series = client.get_time_series("counter-strike 2")
growth = client.get_growth("counter-strike 2", percent_growth=["12M"])
hot = client.get_live(limit=10)
```

Keyword helpers default to `source: "steam"`. Override `source=` for any other platform. Official full client: [`trendsapi`](https://pypi.org/project/trendsapi/).

## Call

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

The backend resolves the name via Steam store search. AppIDs are not a request field.

Series is monthly. `value` is 0-100 vs that title, not raw CCU.

`type: steam` is 400.

Site: [https://trendsapi.ai/trends/steam-trends](https://trendsapi.ai/trends/steam-trends). GitHub: [trendsapi-ai/steam-trends-api](https://github.com/trendsapi-ai/steam-trends-api).

## License

MIT. See [LICENSE](LICENSE).
