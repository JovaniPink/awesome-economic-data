# Awesome Economic Data & Indicators [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of high-frequency and alternative economic indicators for the U.S. outlook. Short descriptions tell you what each source proxies and why it’s useful.

## Contents

- [Labor & Hiring](#labor--hiring)
- [Prices & Inflation](#prices--inflation)
- [Housing & Shelter](#housing--shelter)
- [Consumer Spending & Mobility](#consumer-spending--mobility)
- [Goods Flow & Logistics](#goods-flow--logistics)
- [Trade & Shipping Rates](#trade--shipping-rates)
- [Market-Implied Macro](#market-implied-macro)
- [Remote Sensing & Alt-Data](#remote-sensing--alt-data)
- [Quirky / Behavioral](#quirky--behavioral)
- [Composite Trackers](#composite-trackers)
- [Contribute](#contribute)

---

## Labor & Hiring

About this section. Directional reads on hiring before official BLS releases.

- [ADP National Employment Report](https://adpemploymentreport.com/) — Early read on private payroll growth (sector & pay breakdowns), two days before NFP.
- [Conference Board–Lightcast HWOL](https://www.conference-board.org/topics/help-wanted-online/) — Job-posting index; pulse on labor demand ahead of JOLTS.

---

## Prices & Inflation

About this section. Fast movers that lead or complement CPI/PCE.

- [Truflation US Aggregate Inflation](https://truflation.com/marketplace/us-inflation-rate) — Daily model-based inflation nowcast; basket differs from CPI.
- [Manheim Used Vehicle Value Index](https://site.manheim.com/en/services/consulting/used-vehicle-value-index.html) — Wholesale used-car prices; leads CPI used cars.
- [Visa Spending Momentum Index (FRED)](https://fred.stlouisfed.org/release?rid=736) — Card-spend momentum as a high-frequency proxy for PCE.
- [Mastercard SpendingPulse (press hub)](https://www.mastercard.com/us/en/news-and-trends/press/) — Retail sales estimates across tender types (monthly).
- [Copper (CME Futures)](https://www.cmegroup.com/markets/metals/base/copper.html) — “Dr. Copper” barometer for global industrial demand.
- [Forbes Cost of Living Extremely Well Index (CLEWI)](https://www.forbes.com/sites/andreamurphy/2024/12/24/living-like-a-billionaire-is-more-expensive-than-ever/) — Ultra-luxury basket; useful for top-tail price pressure.
- [Big Mac Index (interactive)](https://www.economist.com/interactive/big-mac-index) — PPP & currency valuation; light read on local price levels.
  - [Big Mac Data (GitHub)](https://github.com/TheEconomist/big-mac-data)

---

## Housing & Shelter

About this section. Asking-rent series that lead official shelter inflation.

- [Apartment List National Rent Data](https://www.apartmentlist.com/research/national-rent-data) — Monthly asking rents; metro cuts and time series.
- [Zillow Data Hub (ZORI)](https://www.zillow.com/research/data/) — Repeat-rent index and housing datasets; useful for shelter disinflation path.

---

## Consumer Spending & Mobility

About this section. Near-real-time indicators of services activity & travel.

- [OpenTable State of the Industry](https://www.opentable.com/c/state-of-industry/) — YoY change in seated diners; local services pulse.
- [TSA Checkpoint Travel Numbers](https://www.tsa.gov/travel/passenger-volumes) — Daily passenger throughput; leisure/business travel momentum.

---

## Goods Flow & Logistics

About this section. What’s moving through the pipeline before retail sales hit.

- [Cass Freight Index](https://www.cassinfo.com/freight-audit-payment/cass-transportation-indexes/cass-freight-index) — Shipments & expenditures across modes (monthly).
- [AAR Rail Traffic Data Center](https://www.aar.org/data-center/) — Weekly carloads & intermodal by commodity; industrial heartbeat.
- [Port of Los Angeles — Container Statistics](https://www.portoflosangeles.org/business/statistics/container-statistics) — Monthly TEUs; early read on inbound goods.
- [DAT Trendlines (Truckload Spot Rates)](https://www.dat.com/trendlines) — Weekly spot rates & load/ truck ratios; freight tightness & goods inflation.
- **“Cardboard Box” Proxies** — Early packaging demand signals:
  - [Fibre Box Association (industry stats)](https://www.fibrebox.org/data-and-research/)
  - [FRED — PPI Corrugated Boxes](https://fred.stlouisfed.org/series/PCU322211322211P)
  - [FRED — IP Paper/Paperboard Mills](https://fred.stlouisfed.org/series/IPG3221N)

---

## Trade & Shipping Rates

About this section. Costs & volumes for dry bulk and containerized trade.

- [Baltic Exchange — Indices](https://www.balticexchange.com/) — Baltic Dry Index (dry bulk charter rates) as a raw-materials demand proxy.
- [Harpex](https://www.harperpetersen.com/container) — Weekly container ship charter rates; finished-goods pipeline tightness.
- [Freightos Baltic Index (FBX)](https://www.freightos.com/freightos-baltic-index/) — Daily container spot rates by lane; disruptions show up fast.
- [IATA Air Cargo (press/data)](https://www.iata.org/en/pressroom/) — Monthly cargo tonne-kilometers; high-value trade momentum.

---

## Market-Implied Macro

About this section. What markets are pricing about growth and recession risk.

- [FRED — 10Y–3M Yield Curve](https://fred.stlouisfed.org/series/T10Y3M) — Benchmark term spread used in recession-probability models.
- [FRED — 10Y–2Y Yield Curve](https://fred.stlouisfed.org/series/T10Y2Y) — Popular but noisier term spread.
- [NY Fed Yield Curve Recession Model (FAQ)](https://www.newyorkfed.org/research/capital_markets/ycfaq) — Methodology & background.

---

## Remote Sensing & Alt-Data

About this section. Satellite-based measures and ML that fill data gaps.

- [NOAA/NGDC VIIRS Nighttime Lights (VNL)](https://eogdata.mines.edu/products/vnl/) — Regional activity proxy; use composites to reduce noise.
- [NASA Black Marble](https://blackmarble.gsfc.nasa.gov/) — Daily/nightly lights & derived products; disaster & recovery tracking.
- **ML on Daytime Satellite Imagery** — Predict local income/population change:
  - [Khachiyan et al., AER: Insights](https://www.aeaweb.org/articles?id=10.1257/aeri.20210422)

---

## Quirky / Behavioral

About this section. Directional anecdotal indicators—use as color, not gospel.

- [Hemline Index (primer)](https://en.wikipedia.org/wiki/Hemline_index) — Fashion “mood ring”; folklore but persistent.
- **Lipstick Effect** — Small-luxury splurge in downturns:
  - [Example Research (Elsevier)](https://www.sciencedirect.com/science/article/abs/pii/S2214804319304884)
- **Pawn Shop Stress Proxies** — Household liquidity pressure:
  - [National Pawnbrokers Association](https://www.nationalpawnbrokers.org/)
  - [FirstCash Investor Relations](https://investors.firstcash.com/)
  - [EZCORP Investor Relations](https://www.ezcorp.com/investor-relations)
- **Men’s Underwear Index** — Trivial but famous retail tell:
  - [Hanesbrands IR](https://ir.hanesbrands.com/)
  - [Gildan–Hanesbrands Deal](https://gildancorp.com/en/media/news/gildan-and-hanesbrands-agree-to-combine/)

---

## Composite Trackers

About this section. Multi-source dashboards with downloadable series.

- [Opportunity Insights Economic Tracker](https://tracktherecovery.org/) — Real-time spending, employment & SMB revenue by income & locale.
  - [Economic Tracker Data (GitHub)](https://github.com/OpportunityInsights/EconomicTracker)
- [ISM PMI Reports](https://www.ismworld.org/supply-management-news-and-reports/reports/ism-pmi-reports/) — Manufacturing & Services diffusion indices with sub-components.
- [S&P Global US PMI Press Releases](https://www.pmi.spglobal.com/Public/Release/PressReleases) — Flash & final PMIs; globally comparable methodology.
- [EIA Hourly Electric Grid Monitor](https://www.eia.gov/electricity/gridmonitor/) — Real-time load/generation; proxy for industrial/commercial activity (weather-adjust).

---

## Contribute

Contributions welcome! Open a PR with a short, neutral description and a working public link. Keep it actionable (download/API if available), note cadence, and include a one-line “gotcha” if there is one.
