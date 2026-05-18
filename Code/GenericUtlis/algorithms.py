def binary_search(data: list, key: str, value) -> dict | None:
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid][key] == value:
            return data[mid]
        elif data[mid][key] < value:
            start = mid + 1
        else:
            end = mid - 1

    return None


def linear_search_name(data: list, value, primary_key: str = "name") -> list | None:
    results = []
    for item in data:
        full_name = (
            f"{item[primary_key]['first_name']} {item[primary_key]['last_name']}"
        )
        if value.lower() in full_name.lower():
            results.append(item)

    return results if results else None


def bubble_sort(data: list, key: str, reverse: bool) -> None:

    n = len(data)

    for i in range(n):
        swapped = False

        if not reverse:
            for j in range(0, n - i - 1):
                # Swap if right element is smaller than left (cending)
                if data[j][key] > data[j + 1][key]:
                    data[j], data[j + 1] = data[j], data[j + 1]
                    swapped = True

        else:
            for j in range(0, n - i - 1):
                # Swap if left element is smaller than right (descending)
                if data[j][key] < data[j + 1][key]:
                    data[j], data[j + 1] = data[j], data[j + 1]
                    swapped = True

        if not swapped:
            break


def quick_sort(
    data: list, key: str, reverse: bool, low: int = 0, high: int = None
) -> None:
    if high is None:
        high = len(data) - 1

    if low < high:
        pi = partition(data, key, reverse, low, high)

        quick_sort(data, key, reverse, low, pi - 1)
        quick_sort(data, key, reverse, pi + 1, high)


def partition(data: list, key: str, reverse: bool, low: int, high: int) -> int:
    pivot = data[high][key]
    i = low - 1

    for j in range(low, high):
        if not reverse:
            condition = data[j][key] <= pivot
        else:
            condition = data[j][key] >= pivot

        if condition:
            i += 1
            data[i], data[j] = data[j], data[i]

    data[i + 1], data[high] = data[high], data[i + 1]
    return i + 1
