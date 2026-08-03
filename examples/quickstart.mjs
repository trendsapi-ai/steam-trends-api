// Trends API quickstart - Steam. Get a free key at https://trendsapi.ai/#get-key
const res = await fetch("https://api.trendsapi.ai/api", {
  method: "POST",
  headers: {
    Authorization: `Bearer ${process.env.TRENDSAPI_KEY}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    mode: "get_growth",
    source: "steam",
    keyword: "Baldur's Gate 3",
    percent_growth: ["3M", "12M"],
  }),
});
console.log(await res.json());
