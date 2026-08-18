# Steam concurrent-player API

Monthly CCU history and the live most-played board. No Steam Web API key.

Key: [trendsapi.ai/#get-key](https://trendsapi.ai/#get-key). Contract: [trendsapi-ai/trendsapi](https://github.com/trendsapi-ai/trendsapi).

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Source](https://img.shields.io/badge/source-steam-blue.svg)](https://trendsapi.ai/trends/steam-trends)

## Call

| Field | Value |
|---|---|
| Endpoint | `POST https://api.trendsapi.ai/api` |
| Auth | `Authorization: Bearer $TRENDSAPI_KEY` |
| History | `source: steam` with `get_time_series` or `get_growth` |
| Keyword | Game **display name**, e.g. `counter-strike 2` or `Elden Ring` |
| Live `type` | `Steam Most Played` |

The backend resolves the name via Steam store search. First result wins. AppIDs are not a request field.

```bash
curl -sS -X POST https://api.trendsapi.ai/api \
  -H "Authorization: Bearer $TRENDSAPI_KEY" \
  -H "Content-Type: application/json" \
  -d '{"mode":"get_growth","source":"steam","keyword":"counter-strike 2","percent_growth":["3M","12M"]}'
```

```bash
curl -sS -X POST https://api.trendsapi.ai/api \
  -H "Authorization: Bearer $TRENDSAPI_KEY" \
  -H "Content-Type: application/json" \
  -d '{"mode":"get_top_trends","type":"Steam Most Played","limit":20}'
```

Series is monthly, not hourly SteamDB candles. `value` is 0-100 vs that title's window, not raw CCU. `type: steam` is 400.

Site: [trendsapi.ai/trends/steam-trends](https://trendsapi.ai/trends/steam-trends).

## License

MIT. See [LICENSE](LICENSE).
