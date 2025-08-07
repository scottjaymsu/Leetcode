'''
The company needs to automatically categorize transactions into predefined categories (e.g. “Travel,” “Office,” “Food”).
Design a system to classify transactions based on their descriptions and merchant information.

Input:
"rules": [
{"category": "Travel", "keywords": ["airlines", "hotel", "flight", "uber"], "merchants": ["Delta", "Hilton"]},
{"category": "Office", "keywords": ["stationery", "printer", "software"], "merchants": ["Staples", "Microsoft"]},
{"category": "Food", "keywords": ["restaurant", "cafe", "bar"], "merchants": ["Starbucks", "McDonald's"]}
],
"transactions": [
{"id": "tx1", "description": "Delta Airlines Flight to NY", "merchant": "Delta"},
{"id": "tx2", "description": "Starbucks Coffee", "merchant": "Starbucks"},
{"id": "tx3", "description": "Buy printer paper", "merchant": "Office Depot"}
]

Output:
[  {"id": "tx1", "category": "Travel"},  {"id": "tx2", "category": "Food"},  {"id": "tx3", "category": "Office"}]

Psuedo:
1. Preprocess information using map
    merchantMap = {merchant : category}
    keywordMap = {keyword : category}
2. Perform intersection on maps and return
'''