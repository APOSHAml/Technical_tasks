smartphones = [
    "Xiaomi Redmi Note 10S",
    "Смартфон Xiaomi Redmi Note 10 Pro",
    "Apple iPhone 13",
    "Apple iPhone 11",
    "Huawei nova Y70",
    "Смартфон Apple iPhone 13 Pro",
]


def select_only_apple_samrtphones(smartphones: list[str]) -> list:

    apple_smartphone: list[str] = []
    for smartphone in smartphones:
        assert isinstance(smartphone, str), "Element In List No String"
        if "apple" in smartphone.lower():
            apple_smartphone.append(smartphone)
    return apple_smartphone


print(select_only_apple_samrtphones(smartphones))
