import argparse
from giza_datasets import DatasetsHub, DatasetsLoader
import os
import certifi
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


os.environ['SSL_CERT_FILE'] = certifi.where()

fecha_actual = datetime.now().date()
fecha_actual_str = fecha_actual.strftime('%Y-%m-%d')


def process_liquidity(df, chain=None, category=None, project=None, startdate=None, enddate=fecha_actual_str):

    if chain:
        df = df[df['chain'] == chain]
    if category:
        df = df[df['category'] == category]
    if project:
        df = df[df['project'] == project]
    if startdate and enddate:
        df = df[(df['date'] >= startdate) & (df['date'] <= enddate)]


    liquidez_total = df['totalLiquidityUSD'].sum()
    print(f'Total liquidity: ${liquidez_total:.2f}')

    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['totalLiquidityUSD'], marker='o', linestyle='-', color='b')
    plt.title('Liquidity by date')
    plt.xlabel('Date')
    plt.ylabel('Liquidity (USD)')
    plt.grid(True)
    plt.show()

def process_fees(df, chain=None, category=None, project=None, startdate=None, enddate=fecha_actual_str):

    if chain:
        df = df[df['chain'] == chain]
    if category:
        df = df[df['category'] == category]
    if project:
        df = df[df['project'] == project]
    if startdate and enddate:
        df = df[(df['date'] >= startdate) & (df['date'] <= enddate)]

    fees_total = df['fees'].sum()
    print(f'Total fees: ${fees_total:.2f}')

    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['fees'], marker='o', linestyle='-')
    plt.title('Fees by date')
    plt.xlabel('Date')
    plt.ylabel('Fees (USD)')
    plt.grid(True)
    plt.show()

def compare_liquidity(df, protocol1, protocol2, startdate=None, enddate=fecha_actual_str):

    df_chain1 = df
    df_chain2 = df
    if protocol1:
        df_chain1 = df_chain1[(df_chain1['chain'] == protocol1) | (df_chain1['category'] == protocol1) | (df_chain1['project'] == protocol1)]
    
    df_chain2 = df
    if protocol2:
        df_chain2 = df_chain2[(df_chain2['chain'] == protocol2) | (df_chain2['category'] == protocol2) | (df_chain2['project'] == protocol2)]

    if startdate and enddate:
        df_chain1 = df_chain1[(df['date'] >= startdate) & (df_chain1['date'] <= enddate)]
        df_chain2 = df_chain2[(df['date'] >= startdate) & (df_chain2['date'] <= enddate)]

    liquidez_total_chain1 = df_chain1['totalLiquidityUSD'].sum()
    print(f'Total liquidity ${protocol1}: ${liquidez_total_chain1:.2f}')

    liquidez_total_chain2 = df_chain2['totalLiquidityUSD'].sum()
    print(f'Total liquidity ${protocol2}: ${liquidez_total_chain2:.2f}')

    plt.figure(figsize=(10, 6))
    plt.plot(df_chain1['date'], df_chain1['totalLiquidityUSD'], label=protocol1, marker='o', linestyle='-', color='b')
    plt.plot(df_chain2['date'], df_chain2['totalLiquidityUSD'], label=protocol2, marker='o', linestyle='-', color='r')
    
    
    plt.title('Comparison of Liquidity between two protocols')
    plt.xlabel('Date')
    plt.ylabel('Liquidity (USD)')
    plt.legend()
    plt.grid(True)
    plt.show()

def compare_fees(df, protocol1, protocol2, startdate=None, enddate=fecha_actual_str):

    df_chain1 = df
    df_chain2 = df
    if protocol1:
        df_chain1 = df_chain1[(df_chain1['chain'] == protocol1) | (df_chain1['category'] == protocol1) | (df_chain1['project'] == protocol1)]
    
    df_chain2 = df
    if protocol2:
        df_chain2 = df_chain2[(df_chain2['chain'] == protocol2) | (df_chain2['category'] == protocol2) | (df_chain2['project'] == protocol2)]

    if startdate and enddate:
        df_chain1 = df_chain1[(df['date'] >= startdate) & (df_chain1['date'] <= enddate)]
        df_chain2 = df_chain2[(df['date'] >= startdate) & (df_chain2['date'] <= enddate)]

    liquidez_total_chain1 = df_chain1['fees'].sum()
    print(f'Total fees ${protocol1}: ${liquidez_total_chain1:.2f}')

    liquidez_total_chain2 = df_chain2['fees'].sum()
    print(f'Total fees ${protocol2}: ${liquidez_total_chain2:.2f}')

    plt.figure(figsize=(10, 6))
    plt.plot(df_chain1['date'], df_chain1['fees'], label=protocol1, marker='o', linestyle='-', color='b')
    plt.plot(df_chain2['date'], df_chain2['fees'], label=protocol2, marker='o', linestyle='-', color='r')
    
    
    plt.title('Comparison of Fees between two protocols')
    plt.xlabel('Date')
    plt.ylabel('Fees (USD)')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    
    parser = argparse.ArgumentParser(description='Ejemplo de script Python con argumentos.')
    loader = DatasetsLoader()
    df = loader.load('tvl-fee-per-protocol')
    chains = df['chain'].unique()
    categories = df['category'].unique()
    projects = df['project'].unique()

    # Agrega argumentos
    parser.add_argument('--action', required=True, choices=["protocol-liquidity", "protocol-fees", "compare-liquidity", "compare-fees"], help='Select the action to analyze')

    parser.add_argument('--chain', choices=chains, help='Select a chain')
    parser.add_argument('--category', choices=categories, help='Select a category')
    parser.add_argument('--project', choices=projects, help='Select a project')
    parser.add_argument('--startdate', help='Enter the start date')
    parser.add_argument('--enddate', help='Enter the end date')

    parser.add_argument('--protocol1', choices=[*chains,*categories, *projects], help='Enter the first chain/category/project to compare')
    parser.add_argument('--protocol2', choices=[*chains,*categories, *projects], help='Enter the second chain/category/project to compare')
    
    # Parsea los argumentos de la línea de comandos
    args = parser.parse_args()
    
    # Accede al valor del argumento
    action = args.action
    chain = args.chain
    category = args.category
    project = args.project
    startdate = args.startdate
    enddate = args.enddate
    protocol1 = args.protocol1
    protocol2 = args.protocol2

    df = df.to_pandas()
    df['date']= pd.to_datetime(df['date'])
    if action == "protocol-liquidity":
        if chain is None and category is None and project is None:
            print("Select a chain, category or project to analize the liquidity")
        else:
            process_liquidity(df, chain, category, project,startdate, enddate)

    if action == "protocol-fees":
        if chain is None and category is None and project is None:
            print("Select a chain, category or project to analize the fees")
        else:
            process_fees(df, chain, category, project,startdate, enddate)

    if action == "compare-liquidity":
        if protocol1 is None and protocol2 is None:
            print("Select the first and second chain, category or project to compare the liquidity")
        else:
            compare_liquidity(df, protocol1, protocol2 ,startdate, enddate)

    if action == "compare-fees":
        if protocol1 is None and protocol2 is None:
            print("Select the first and second chain, category or project to compare the fees")
        else:
            compare_fees(df, protocol1, protocol2 ,startdate, enddate)
    

if __name__ == "__main__":
    main()

