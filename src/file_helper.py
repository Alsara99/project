import pandas as pd


def read_csv_file(path):
    """происходит считывание финансовых операций из csv-файла"""
    data = pd.read_csv(path, encoding='UTF-8', delimiter=';')
    transactions = data.to_dict(orient='records')
    return transactions


def read_excel_file(path):
    """происходит считывание финансовых операция их xlsx-файла"""
    data = pd.read_excel(path)
    transactions = data.to_dict(orient='records')
    return transactions
