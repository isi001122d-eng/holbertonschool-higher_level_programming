#!/usr/bin/python3
"""
CSV məlumatlarını JSON formatına çevirən modul
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    CSV faylını oxuyur və məlumatları data.json faylına yazır
    """
    try:
        # CSV faylını oxumaq
        with open(csv_filename, mode='r', encoding='utf-8') as csv_f:
            # DictReader hər sətri avtomatik lüğətə (dict) çevirir
            reader = csv.DictReader(csv_f)
            data_list = [row for row in reader]

        # JSON faylına yazmaq
        with open('data.json', mode='w', encoding='utf-8') as json_f:
            json.dump(data_list, json_f)

        return True

    except FileNotFoundError:
        # Fayl tapılmadıqda False qaytarır
        return False
    except Exception:
        # Digər gözlənilməz xətalar zamanı False qaytarır
        return False
