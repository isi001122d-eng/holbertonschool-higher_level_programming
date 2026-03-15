#!/usr/bin/python3
"""
Paskal Üçbucağı yaradan modul
"""


def pascal_triangle(n):
    """
    n ölçülü Paskal üçbucağını siyahı olaraq qaytarır
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        # Hər yeni sətir həmişə 1 ilə başlayır
        prev_row = triangle[i - 1]
        current_row = [1]

        # Orta elementləri hesabla (üst sətirdəki iki qonşu elementin cəmi)
        for j in range(1, i):
            current_row.append(prev_row[j - 1] + prev_row[j])

        # Hər yeni sətir həmişə 1 ilə bitir
        current_row.append(1)
        triangle.append(current_row)

    return triangle
