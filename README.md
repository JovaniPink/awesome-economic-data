# Awesome Economic Data & Indicators [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated, U.S.-focused catalog of high-frequency and alternative economic indicators, data portals, and learning resources. Descriptions identify what each source measures and where interpretation requires care.

Catalog structure reviewed: August 2026.

External sources are reviewed when added or materially changed. A catalog-wide source recency review has not yet been recorded.

The [alternative economic and financial data review](docs/alternative-financial-data-review.md) records the September 2026 additions, access evidence, methodological dependencies, and deferred learning datasets.

The [household wealth and community data review](docs/household-wealth-community-data-review.md) records six additions for studying household resources, unpaid work, civic participation, and housing supply.

The [machine-readable resource index](catalog/resources.v1.json) assigns stable public identifiers while preserving the catalog boundary: inclusion is curation, not endorsement, permission, maintenance proof, or model fitness proof. The index uses schema version 1.1 and retains unknown access and source authority until reviewed evidence is supplied. See the [resource index contract](docs/knowledge-resource-index.md) before using an entry in a model or lab.

## Contents

- [Labor & Hiring](#labor--hiring)
- [Prices & Inflation](#prices--inflation)
- [Housing & Shelter](#housing--shelter)
- [Consumer Spending & Mobility](#consumer-spending--mobility)
- [Household Financial Health](#household-financial-health)
- [Unpaid Work & Civic Life](#unpaid-work--civic-life)
- [Goods Flow & Logistics](#goods-flow--logistics)
- [Trade & Shipping Rates](#trade--shipping-rates)
- [Market-Implied Macro](#market-implied-macro)
- [Corporate Financials & Financial Accounts](#corporate-financials--financial-accounts)
- [Financial Markets & Returns](#financial-markets--returns)
- [Remote Sensing & Alternative Data](#remote-sensing--alternative-data)
- [Behavioral & Company Proxies](#behavioral--company-proxies)
- [Composite Trackers](#composite-trackers)
- [Regional Economic Modeling Data](#regional-economic-modeling-data)
- [Portals](#portals)
- [Finance, Economics & Systems Channels](#finance-economics--systems-channels)
- [Machine Learning and Economic Simulation](#machine-learning-and-economic-simulation)
- [Learning & Methods](#learning--methods)

## Labor & Hiring

Measures of hiring, advertised pay, and received earnings with different worker and employer coverage.

- [ADP National Employment Report](https://adpemploymentreport.com/) - Provides a monthly estimate of private-sector employment and pay based on ADP payroll data.
- [Conference Board-Lightcast Help Wanted OnLine](https://www.conference-board.org/topics/help-wanted-online/) - Models monthly job openings from online job advertisements as an early view of labor demand.
- [Indeed Wage Tracker](https://github.com/hiring-lab/indeed-wage-tracker) - Publishes monthly advertised wage-growth CSVs by country and occupational sector under CC BY 4.0; job-title comparisons measure offers rather than pay received by individual workers.
- [Gusto Real Time Economic Data](https://gusto.com/resources/gusto-insights/real-time-economic-data) - Offers monthly small-business payroll earnings and hiring series as CSVs; estimates use QCEW calibration and revisions, so independently collected payroll is not an independent national benchmark.
- [Square Payroll Index](https://squareup.com/us/en/the-bottom-line/tools/square-payroll-index) - Reports monthly retail and food-service base wages and hourly earnings including tips and overtime; public charts cover Square employers, and bulk export remains unverified.

## Prices & Inflation

Fast-moving price measures that lead or complement CPI and PCE.

- [Truflation US Aggregate Inflation](https://truflation.com/marketplace/us-inflation-rate) - Provides a daily model-based inflation estimate whose basket and methodology differ from official CPI.
- [Manheim Used Vehicle Value Index](https://site.manheim.com/en/services/consulting/used-vehicle-value-index.html) - Tracks wholesale used-vehicle prices that can lead the used-vehicle component of CPI.
- [Visa Spending Momentum Index on FRED](https://fred.stlouisfed.org/release?rid=736) - Reports a monthly card-spending momentum index derived from Visa payments data.
- [Copper Futures](https://www.cmegroup.com/markets/metals/base/copper.html) - Provides market pricing commonly used as a noisy signal of global industrial demand.
- [Big Mac Index](https://www.economist.com/interactive/big-mac-index) - Compares burger prices as an informal purchasing-power-parity and currency-valuation measure.
- [Big Mac Index Data](https://github.com/TheEconomist/big-mac-data) - Publishes the Economist's underlying Big Mac Index dataset and methodology notes.
- [USDA Advertised Grocery Prices](https://mymarketnews.ams.usda.gov/viewReport/3324) - Publishes weekly specialty-crop grocery advertisement reports with product and regional detail through Market News; promotional offers are not transaction prices or a complete grocery basket.
- [Open Prices](https://huggingface.co/datasets/openfoodfacts/open-prices) - Provides community-contributed dated product prices and proof metadata in Parquet under ODbL; irregular observations and geographic selection prevent assuming a representative U.S. price index.
- [EIA Electricity Prices and Bills](https://www.eia.gov/electricity/sales_revenue_price/) - Publishes annual electricity sales, revenues, average prices, and residential bills in spreadsheets; bills reflect consumption as well as unit prices and exclude other utilities.

## Housing & Shelter

Asking-rent series and housing-supply data describe different aspects of shelter costs and availability.

- [Apartment List National Rent Data](https://www.apartmentlist.com/research/national-rent-data) - Publishes monthly asking-rent estimates with metro-level cuts and downloadable time series.
- [Zillow Data](https://www.zillow.com/research/data/) - Provides ZORI repeat-rent estimates and other housing datasets with published methodology.
- [Census Characteristics of New Housing](https://www.census.gov/construction/chars/index.html) - Publishes annual Survey of Construction tables and microdata on new-home size, features, and prices; new construction does not represent the entire housing stock or establish affordability near jobs.

## Consumer Spending & Mobility

Near-real-time indicators of services activity and travel.

- [OpenTable State of the Industry](https://www.opentable.com/c/state-of-industry/) - Reports year-over-year changes in seated diners as a narrow restaurant-activity signal.
- [TSA Checkpoint Travel Numbers](https://www.tsa.gov/travel/passenger-volumes) - Publishes daily airport-screening throughput for current and comparison years.

## Household Financial Health

Survey responses, credit aggregates, tax records, and utility payment events describe different populations and forms of financial pressure.

- [Federal Reserve SHED Data](https://www.federalreserve.gov/consumerscommunities/shed_data.htm) - Provides annual financial well-being survey microdata as CSV and Stata files with codebooks; weights, revised files, and changing questions matter when comparing self-reported hardship.
- [New York Fed Consumer Data Bank](https://www.newyorkfed.org/microeconomics/databank) - Offers quarterly household credit aggregates and separate consumer-expectations survey downloads with module-specific cadences; public credit workbooks do not expose underlying Consumer Credit Panel microdata.
- [IRS ZIP-Code Income Data](https://www.irs.gov/statistics/soi-tax-stats-individual-income-tax-statistics-zip-code-data-soi) - Provides annual income and wage aggregates by ZIP code and income bracket in CSV and Excel; delayed tax-return statistics exclude nonfilers and do not measure individual worker raises.
- [EIA Utility Disconnections](https://www.eia.gov/analysis/requests/residential/utility/) - Provides downloadable utility-level monthly nonpayment notices, disconnections, and reconnections for 2024; this limited collection cannot establish a trend since 2020 or count unique affected households.
- [Federal Reserve Survey of Consumer Finances](https://www.federalreserve.gov/econres/scfindex.htm) - Provides triennial household wealth and debt survey files, CSV extracts, and codebooks; weights and multiple imputations are essential, and broad age-group comparisons do not follow the same families.
- [Census Survey of Income and Program Participation](https://www.census.gov/programs-surveys/sipp/data/datasets.html) - Offers annual public-use income, assets, benefits, and household-transition files with documentation; reference years differ from survey labels, and redesigns and attrition complicate historical comparisons.

## Unpaid Work & Civic Life

Household-production estimates and surveys of participation complement monetary measures without directly measuring every form of social well-being.

- [BEA Household Production](https://www.bea.gov/data/special-topics/household-production) - Publishes periodically updated annual estimates of unpaid household work in Excel with methods; time-use inputs and wage-based valuations make these constructed estimates rather than independent observations of social welfare.
- [NORC General Social Survey](https://gss.norc.org/get-the-data.html) - Offers repeated social-attitude and participation surveys, generally biennial since 1994, in SAS, Stata, and SPSS; attribution terms, changing modes, restricted geography, and revised variable coding require care.
- [Census Volunteering and Civic Life Supplement](https://www.census.gov/data/datasets/2023/demo/cps/cps-volunteer.html) - Provides 2023 volunteering and informal-helping survey files in CSV and compressed formats with replicate weights; this periodic CPS supplement shares survey infrastructure and requires comparable questions across waves.

## Goods Flow & Logistics

Freight, port, rail, and packaging measures that can move before retail-sales releases.

- [Cass Freight Index](https://www.cassinfo.com/freight-audit-payment/cass-transportation-indexes/cass-freight-index) - Reports monthly North American shipment volumes and freight expenditures across transportation modes.
- [AAR Rail Traffic Data Center](https://www.aar.org/data-center/) - Publishes weekly U.S. rail carload and intermodal counts by commodity.
- [Port of Los Angeles Container Statistics](https://www.portoflosangeles.org/business/statistics/container-statistics) - Provides monthly loaded and empty container volumes for the Port of Los Angeles.
- [DAT Trendlines](https://www.dat.com/trendlines) - Reports weekly truckload spot rates and load-to-truck ratios as freight-market signals.
- [Fibre Box Association Data and Research](https://www.fibrebox.org/data-and-research) - Publishes U.S. corrugated-industry shipment and capacity statistics as packaging-demand context.
- [Corrugated and Solid Fiber Box Manufacturing PPI](https://fred.stlouisfed.org/series/PCU322211322211P) - Provides the BLS producer price index for corrugated and solid fiber box manufacturing.
- [Paper and Paperboard Mills Industrial Production](https://fred.stlouisfed.org/series/IPG3221N) - Provides the Federal Reserve industrial production index for paper and paperboard mills.

## Trade & Shipping Rates

Costs and volumes for dry bulk, containerized trade, and air cargo.

- [Baltic Exchange Indices](https://www.balticexchange.com/en/index.html) - Provides dry-bulk and other freight-market benchmarks, including the Baltic Dry Index.
- [Harpex](https://www.harperpetersen.com/container) - Publishes a weekly container-ship charter-rate index.
- [Freightos Baltic Index](https://www.freightos.com/freightos-baltic-index/) - Reports daily container prices across major global trade lanes using commercial transaction data.
- [IATA Economics](https://www.iata.org/en/publications/economics/) - Publishes recurring air-cargo market analysis, including cargo tonne-kilometer trends.

## Market-Implied Macro

Market prices and models used to assess growth and recession risk.

- [10-Year Treasury Minus 3-Month Treasury](https://fred.stlouisfed.org/series/T10Y3M) - Provides the term spread used by the New York Fed's recession-probability model.
- [10-Year Treasury Minus 2-Year Treasury](https://fred.stlouisfed.org/series/T10Y2Y) - Provides a widely followed alternative term spread that can differ from the model benchmark.
- [New York Fed Yield Curve Model FAQ](https://www.newyorkfed.org/research/capital_markets/ycfaq) - Explains the yield-curve recession model, inputs, interpretation, and limitations.

## Corporate Financials & Financial Accounts

Company filings, industry accounting estimates, and sector balance sheets require compatible populations, periods, and revision histories.

- [SEC Financial Statement Data Sets](https://www.sec.gov/data-research/sec-markets-data/financial-statement-data-sets) - Publishes quarterly ZIPs of financial-statement facts extracted from company filings; fiscal periods, tags, restatements, and coverage require reconciliation before comparing margins or aggregate profits.
- [Census Quarterly Financial Report](https://www.census.gov/econ/qfr/historic.html) - Offers quarterly industry financial estimates through historical spreadsheets and publications; sector and firm-size coverage vary, and shared inputs limit independence from national profit estimates.
- [Federal Reserve Financial Accounts Z.1](https://www.federalreserve.gov/releases/z1/) - Publishes quarterly sector financial flows and balance sheets with CSV and XML downloads; multi-source estimates and revisions distinguish these accounts from direct household or company observations.

## Financial Markets & Returns

Fund disclosures, funding benchmarks, mixed-source indicators, and constructed research returns answer different financial questions.

- [SEC Form N-PORT Data Sets](https://www.sec.gov/data-research/sec-markets-data/form-n-port-data-sets) - Offers quarterly ZIPs of publicly disseminated fund portfolio filings; disclosure delays and fund coverage prevent treating the files as complete current holdings.
- [New York Fed Reference Rates](https://www.newyorkfed.org/markets/reference-rates) - Publishes daily overnight funding benchmarks with historical data and API access; transaction-based rates such as SOFR describe wholesale funding rather than household borrowing costs or forecasts.
- [OFR Short-Term Funding Monitor API](https://www.financialresearch.gov/short-term-funding-monitor/api/) - Provides unauthenticated JSON queries and metadata for funding indicators with series-specific frequencies; mixed observation sources and derived measures require checking upstream definitions and terms.
- [Kenneth French Data Library](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html) - Offers downloadable daily, weekly, and monthly factor and portfolio research returns in CSV and text; constructed CRSP-derived histories can revise and are not raw tradable security prices.

## Remote Sensing & Alternative Data

Satellite-derived measures and research methods that help fill local data gaps.

- [VIIRS Nighttime Lights](https://eogdata.mines.edu/products/vnl/) - Provides nighttime-light composites that researchers use as a noisy proxy for regional activity.
- [NASA Black Marble](https://blackmarble.gsfc.nasa.gov/) - Provides daily nighttime-light products used for disaster, recovery, and economic-activity research.
- [Using Satellite Imagery to Understand and Promote Sustainable Development](https://www.aeaweb.org/articles?id=10.1257/aeri.20210422) - Evaluates machine-learning methods that infer local economic conditions from daytime satellite imagery.

## Behavioral & Company Proxies

Indirect and company-specific signals that should be treated as context rather than broad economic measures.

- [Lipstick Effect Research](https://www.sciencedirect.com/science/article/abs/pii/S2214804319304884) - Examines the debated hypothesis that some consumers shift toward small luxury purchases during economic stress.
- [FirstCash Investor Relations](https://investors.firstcash.com/) - Provides company filings and results that can offer a narrow, company-specific view of pawn lending and retail activity.
- [EZCORP Investor Relations](https://www.ezcorp.com/investor-relations) - Provides company filings and results that can offer a second narrow view of pawn lending and retail activity.

## Composite Trackers

Multi-source dashboards and recurring composite indicators.

- [Economic Tracker](https://economictracker.org/) - Visualizes high-frequency spending, employment, and small-business measures by geography and income group.
- [Economic Tracker Data](https://github.com/OpportunityInsights/EconomicTracker) - Publishes downloadable data and documentation used by the Economic Tracker.
- [ISM PMI Reports](https://www.ismworld.org/supply-management-news-and-reports/reports/ism-pmi-reports/) - Publishes manufacturing and services diffusion indices with industry and subcomponent detail.
- [S&P Global US PMI Releases](https://www.pmi.spglobal.com/Public/Release/PressReleases) - Publishes flash and final U.S. purchasing managers' indices using a globally comparable methodology.
- [EIA Hourly Electric Grid Monitor](https://www.eia.gov/electricity/gridmonitor/) - Reports hourly electricity demand and generation as a weather-sensitive activity signal.
- [Atlanta Fed GDPNow](https://www.atlantafed.org/research-and-data/data/gdpnow) - Publishes a model-based running estimate of current-quarter real GDP growth; it is not an official Atlanta Fed forecast, receives no subjective adjustment, and can retain substantial error near the advance GDP release.
- [Dallas Fed Weekly Economic Index](https://www.dallasfed.org/research/wei) - Models the common component of ten daily and weekly series, updates weekly, and scales the result to four-quarter GDP growth; weights and past values may be revised.
- [Philadelphia Fed ADS Index](https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/ads) - Publishes a model-based daily business-conditions estimate plus real-time vintages; it combines inputs at mixed frequencies and is not a directly observed daily measure.

## Regional Economic Modeling Data

First-party sources for a point-in-time state and Washington, DC expert system. Inclusion identifies a promising input, not a completed historical-vintage audit or a claim that the source improves forecasts. The [regional modeling data map](docs/regional-economic-modeling-data.md) records measures, frequency, access, revision behavior, model role, and admission status. Its seven-record [source-admission manifest](catalog/source-admission.v1.json) has a narrow QCEW final-outcome timing admission backed by [2019-2024 BLS release records](catalog/evidence/qcew-2019-2024-release-timing.v1.json); it does not establish historical file vintages or source terms. QCEW industry, BEA, FHFA, Census BFS, Census building permits, and Treasury yields remain pending at their stated scopes.

- [QCEW Data Files](https://www.bls.gov/cew/downloadable-data-files.htm) - Provides quarterly state employment, establishment, and wage data with industry detail; historical forecasts require publication vintages because later releases can revise earlier values.
- [Census Business Formation Statistics](https://www.census.gov/econ/bfs/data.html) - Provides monthly state business applications and projected formations as leading business-activity signals, with methodology and seasonal revisions that can restate history.
- [Building Permits by State](https://www.census.gov/construction/bps/statemonthly.html) - Publishes monthly state residential permits by structure type, while late reports and corrections can make cumulative values differ from sums of earlier monthly releases.
- [BEA Regional Economic Accounts](https://www.bea.gov/data/economic-accounts/regional) - Publishes state GDP and personal income with industry and component detail; honest historical forecasts require archived releases rather than current revised values alone.
- [FHFA House Price Index Datasets](https://www.fhfa.gov/house-price-index?tab=HPI+Datasets) - Provides state purchase-only house-price indexes and other HPI variants, but historical values are revised and the variants have different coverage and methods.
- [EIA API v2](https://www.eia.gov/opendata/documentation.php) - Provides state and sector electricity sales, prices, customers, and generation; reliable use requires an API key, pagination, units, and prospective vintage capture.
- [Census Quarterly Workforce Indicators](https://www.census.gov/data/developers/data-sets/qwi.html) - Provides quarterly hires, separations, job creation, job destruction, and wages by geography and worker or firm characteristics, but historical publication vintages must be established before point-in-time use.
- [FDIC Data Downloads](https://www.fdic.gov/bank-data-guide/data-downloads) - Provides quarterly institution financials back to 1992 and annual branch deposits, while mergers and borrower geography complicate state credit measures.
- [Treasury Interest Rate Statistics](https://home.treasury.gov/policy-issues/financing-the-government/interest-rate-statistics) - Publishes daily par yields derived from indicative market quotations for national gate context; methodology changes and the lack of state variation limit direct expert use.

Additional sources can improve timing, structure, credit, agriculture, or shock context after the core point-in-time baseline is verified.

- [BLS State and Area Employment](https://www.bls.gov/sae/) - Provides monthly state payroll employment, hours, and earnings by industry, with monthly and benchmark revisions that prevent treating the current history as the original release.
- [BLS Local Area Unemployment Statistics](https://www.bls.gov/lau/) - Provides official monthly state labor-force, employment, unemployment, and unemployment-rate estimates that are model-based and annually re-estimated with revised inputs and population controls.
- [BLS State JOLTS](https://www.bls.gov/jlt/jlt_statedata.htm) - Publishes state job openings, hires, quits, and separations as model-assisted estimates whose benchmarked history incorporates JOLTS, QCEW, and regional information.
- [Census County Business Patterns](https://www.census.gov/programs-surveys/cbp/data/datasets.html) - Provides annual establishment, employment, and payroll statistics by detailed industry and geography, with suppression and a slow release cadence limiting short-horizon use.
- [Census Business Dynamics Statistics](https://www.census.gov/programs-surveys/bds/data.API.html) - Provides annual job creation and destruction, births, deaths, startups, and shutdowns by geography and firm characteristics through an API key-protected service.
- [American Community Survey API](https://www.census.gov/programs-surveys/acs/data/data-via-api.html) - Provides annual demographic, economic, and housing estimates for structural context, with sampling uncertainty, margins of error, population thresholds, and changing vintages to preserve.
- [IRS Migration Data](https://www.irs.gov/statistics/soi-tax-stats-migration-data) - Measures state and county inflows and outflows from tax-return address changes, with coverage limits and a methodology break beginning with the 2022-2023 data.
- [SBA 7(a) and 504 Public Data](https://data.sba.gov/dataset/7a-504-foia) - Publishes quarterly loan-level approvals since fiscal year 1991 as a small-business credit signal, but the programs do not represent all small-business borrowing.
- [USDA NASS Quick Stats](https://www.nass.usda.gov/Quick_Stats/) - Provides state agricultural production and prices by commodity and period, while API credentials, changing definitions, and suppression require source-specific handling.
- [NOAA Climate Data Online API](https://www.ncdc.noaa.gov/cdo-web/webservices/v2) - Provides station and location weather and climate observations for shock context, with token limits, station coverage, units, and aggregation choices that must remain explicit.
- [OpenFEMA Disaster Declarations](https://www.fema.gov/about/openfema/disaster-declarations-summaries) - Lists federal disaster declarations and affected geographies, but administrative timing, partial older records, and historical entry errors prevent treating declarations as direct economic-loss measures.

## Portals

Research indexes and data services for finding economic series and literature.

- [IDEAS/RePEc](https://ideas.repec.org/) - Indexes economics working papers, articles, books, software components, and author profiles.
- [BLS Public Data API](https://www.bls.gov/developers/) - Provides programmatic access to published U.S. labor-market and price data with documented query limits, citation requirements, and terms for secondary use.
- [Federal Reserve Bank of St. Louis Resources](https://research.stlouisfed.org/resources.html) - Links to FRED, ALFRED, FRASER, and related economic data and archival services.
- [BEA Data API](https://apps.bea.gov/api/signup/) - Provides registered, API-key access to a subset of published GDP, income, industry, regional, trade, and investment statistics plus metadata; terms acceptance is required.
- [Census Economic Indicators API](https://www.census.gov/data/developers/data-sets/economic-indicators.html) - Provides monthly and quarterly retail, housing, manufacturing, trade, services, and construction series; every query requires an API key, Census attribution, originating-program attribution, and preservation of published precision.
- [FRED and ALFRED API](https://fred.stlouisfed.org/docs/api/fred/overview.html) - Requires a registered API key to retrieve current and vintage series by source, release, category, and series; it is an aggregation layer, so original-source definitions, revisions, and terms remain controlling.
- [U.S. Treasury Fiscal Data](https://fiscaldata.treasury.gov/) - Provides machine-readable debt, revenue, spending, deficit, and Treasury operations datasets with dataset-specific cadences, units, accounting definitions, metadata, and APIs.
- [DBnomics Web API](https://docs.db.nomics.world/web-api/) - Normalizes access across many economic providers; provider codes and original sources remain authoritative, and the API is intended for focused queries rather than indiscriminate bulk downloads.

## Finance, Economics & Systems Channels

Research-oriented video resources for learning how practitioners and educators analyze markets, companies, economic policy, and technical systems. Creator credentials and teaching claims were checked against official biographies or institutional profiles in August 2026. Inclusion is a curation decision, not an endorsement or investment advice; follow the primary sources cited by each creator and distinguish observed evidence from interpretation.

### Finance and economics

- [Patrick Boyle On Finance](https://www.youtube.com/channel/UCASM0cgfkJxQ1ICmRilfHLw) - Explains quantitative finance, markets, and financial history from the perspective of a former hedge-fund founding partner and visiting finance professor.
- [Ben Felix](https://www.youtube.com/@BenFelixCSI) - Connects investing and personal-finance questions to academic research as PWL Capital's chief investment officer.
- [Aswath Damodaran on Valuation](https://www.youtube.com/@AswathDamodaranonValuation) - Publishes NYU Stern lectures and practical materials on corporate finance, valuation, accounting, and investment philosophy.
- [PensionCraft](https://www.youtube.com/@Pensioncraft) - Explains investing, asset allocation, macroeconomics, and markets with data-oriented lessons from former investment-bank strategist Ramin Nakisa; free videos sit alongside commercial memberships, courses, and coaching.
- [Money & Macro](https://www.youtube.com/@MoneyMacro) - Uses research, data, and economic models to explain macroeconomics, monetary policy, financial markets, and global institutions; host Joeri Schasfoort holds a PhD in economics and is a former university lecturer.
- [The Plain Bagel](https://www.youtube.com/@ThePlainBagel) - Provides beginner-friendly education on investing, economics, and personal finance from portfolio manager Richard Coffin, CFA, CFP.
- [Marginal Revolution University](https://www.youtube.com/@MarginalRevolutionUniversity) - Offers free economics courses, short videos, and classroom resources founded by George Mason University economists Tyler Cowen and Alex Tabarrok as a nonprofit project housed at the Mercatus Center.

### Technology and adjacent evidence review

- [Asianometry](https://www.youtube.com/@Asianometry) - Produces researched video essays on Asian technology, business history, semiconductor manufacturing, supply chains, and economics.
- [Sabine Hossenfelder](https://www.youtube.com/@SabineHossenfelder) - Applies cited, peer-reviewed research and fact-checking to science and technology claims; included as an adjacent media-literacy resource rather than a finance authority.

## Machine Learning and Economic Simulation

Discovery resources for prediction, causal machine learning, and economic simulation. The two community catalogs below did not expose a recognized license when reviewed on August 30, 2026, so this repository links to them without copying their text or bibliographies. Simulated outcomes require separate calibration, identification, and external-validity evidence before they support claims about the real economy.

- [Awesome Machine Learning in Economics and Finance](https://github.com/cwyalpha/Awesome-Machine-Learning-in-Economics-and-Finance) - Offers a small mixed-language discovery list of researchers, papers, courses, frameworks, and examples, but it is not a reviewed source authority and each linked item requires independent verification.
- [Machine Learning: An Applied Econometric Approach](https://www.aeaweb.org/articles?id=10.1257/jep.31.2.87) - Explains how prediction-oriented machine learning differs from conventional parameter-focused econometrics and why empirical design still controls interpretation.
- [EconML](https://github.com/py-why/EconML) - Provides Python estimators for heterogeneous treatment effects using machine-learning components, but software output does not repair weak identification or establish external validity.
- [DoubleML](https://docs.doubleml.org/stable/) - Implements double and debiased machine-learning methods for causal parameters under stated orthogonality, nuisance-estimation, sampling, and identification assumptions.
- [Awesome Economic World Models](https://github.com/FreedomIntelligence/Awesome-Economic-World-Models) - Organizes a broad research taxonomy for agent-based and adaptive economic simulations, which are not observed economic data, validated counterfactuals, or forecasts by default.
- [Economic World Models Systems Blueprint](https://arxiv.org/abs/2608.06020) - Proposes a capability ladder, runtime architecture, engineering path, and evaluation systems blueprint for agentic economies; it is a research agenda, not empirical validation of a real economic twin.
- [ABIDES-Economist](https://arxiv.org/abs/2402.09563) - Describes an agent-based simulator for economic systems with learning agents, useful for controlled experiments but separate from observed-market evidence or trading validation.

## Learning & Methods

Open and structured resources for learning economic concepts and interpreting data.

- [AI Research Writing for Economics](https://github.com/uinue2010/awesome-ai-research-writing-economics) - Organizes Chinese-language prompts for economics research and writing and identifies an upstream prompt collection; use it as workflow inspiration because no recognized license was present at the August 30, 2026 review.
- [MIT OpenCourseWare Economics](https://ocw.mit.edu/search/?d=Economics&s=department_course_numbers.sort_coursenum) - Provides self-paced undergraduate and graduate economics course materials.
- [edX Economics](https://www.edx.org/learn/economics) - Lists economics courses from universities and other education providers with varying access terms.
- [Khan Academy Economics](https://www.khanacademy.org/economics-finance-domain) - Provides introductory microeconomics, macroeconomics, and finance lessons and exercises.

The [original English AI-assisted economics research and writing guide](docs/ai-assisted-economic-research-writing.md) turns those workflow categories into evidence-bounded checklists and prompt patterns without translating or republishing the source collection.

## Contributing

See [contributing.md](contributing.md) before proposing a source. The automated gate checks catalog structure; contributors must separately verify source quality, access, recency, and the claims in each description.
