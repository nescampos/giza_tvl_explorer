# Giza TVL Explorer

**Giza TVL Explorer** is a small tool built with Python, to analize the liquidity and fees in chains and dApps, using [Giza Datasets](https://datasets.gizatech.xyz/).
With Giza TVL Explorer, you can:
- Analyze the liquidity by chain (like Ethereum, polygon, etc.) or by category (Liquid Staking for example), or by dApp (Uniswap, SushiSwap, etc.).
- Analyze the fees by chain (like Ethereum, polygon, etc.) or by category (Liquid Staking for example), or by dApp (Uniswap, SushiSwap, etc.).
- Compare the liquidity between 2 protocols (chains, dApps, category). You can compare between a chain and a dApp, and more.
- Compare the fees between 2 protocols (chains, dApps, category). You can compare between a chain and a dApp, and more.

## How to use

1. Install libraries:
```
pip install -r requirements.txt
```

2. Execute the tool:
```
python tvl_explorer.py
```

3. To check which chains and protocols you can select to analyze and compare, run the --help argument (Giza Datasets is constantly updated, so you should do this to check what options you have).
```
python tvl_explorer.py --help
```

### Analyze the liquidity

**protocol-liquidity**
```
python tvl_explorer.py --action "protocol-liquidity"
```

#### Arguments
You must select at least one of the following options:
- **--chain**: Enter the chain you want to analyze.
- **--category**: Enter the category (type of dApps) you want to analyze.
- **--project**: Enter the project (dApp) you want to analyze.

If you want to filter by date, select the start AND end dates.
- **startdate**: YYYY-MM-DD
- **enddate**: YYYY-MM-DD

#### Examples
```
python tvl_explorer.py --action "protocol-liquidity" --chain "ethereum"
python tvl_explorer.py --action "protocol-liquidity" --category "lending"
python tvl_explorer.py --action "protocol-liquidity" --project "uniswap-v3"
python tvl_explorer.py --action "protocol-liquidity" --chain "ethereum" --project "uniswap-v3" --startdate "2024-01-01" --enddate "2024-01-10"
```

### Analyze the fees

**protocol-fees**
```
python tvl_explorer.py --action "protocol-fees"
```

#### Arguments
You must select at least one of the following options:
- **--chain**: Enter the chain you want to analyze.
- **--category**: Enter the category (type of dApps) you want to analyze.
- **--project**: Enter the project (dApp) you want to analyze.

If you want to filter by date, select the start AND end dates.
- **startdate**: YYYY-MM-DD
- **enddate**: YYYY-MM-DD

#### Examples
```
python tvl_explorer.py --action "protocol-fees" --chain "ethereum"
python tvl_explorer.py --action "protocol-fees" --category "lending"
python tvl_explorer.py --action "protocol-fees" --project "uniswap-v3"
python tvl_explorer.py --action "protocol-fees" --chain "ethereum" --project "uniswap-v3" --startdate "2024-01-01" --enddate "2024-01-10"
```


### Compare the liquidity
**compare-liquidity**
```
python tvl_explorer.py --action "compare-liquidity"
```

#### Arguments
You must select at least one of the following options:
- **--protocol1**: Enter the first chain/category/project to compare.
- **--protocol2**: Enter the second chain/category/project to compare.

If you want to filter by date, select the start AND end dates.
- **startdate**: YYYY-MM-DD
- **enddate**: YYYY-MM-DD

#### Examples
```
python tvl_explorer.py --action "compare-liquidity" --protocol1 "ethereum" --protocol2 "oasis" --startdate "2024-01-01" --enddate "2024-01-31"
```

### Compare the fees
**compare-fees**
```
python tvl_explorer.py --action "compare-fees"
```

#### Arguments
You must select at least one of the following options:
- **--protocol1**: Enter the first chain/category/project to compare.
- **--protocol2**: Enter the second chain/category/project to compare.

If you want to filter by date, select the start AND end dates.
- **startdate**: YYYY-MM-DD
- **enddate**: YYYY-MM-DD

#### Examples
```
python tvl_explorer.py --action "compare-fees" --protocol1 "uniswap-v3" --protocol2 "oasis"
```
