'''
A company needs to route transactions to the payment gateway with the lowest cost.
Each gateway has a different fee structure (fixed fee + percentage fee)
and may have restrictions on transaction amount ranges.
Design an algorithm to select the optimal gateway for each transaction.

Input:
{   "gateways": [
                    {"name": "Stripe", "fixed_fee": 0.30, "percent_fee": 0.029, "min_amount": 0, "max_amount": 5000}
                    {"name": "PayPal", "fixed_fee": 0.40, "percent_fee": 0.025, "min_amount": 0, "max_amount": 10000}
                    {"name": "Square", "fixed_fee": 0.15, "percent_fee": 0.035, "min_amount": 0, "max_amount": 2000}
                ],
    "transactions": [100, 500, 2000, 15000]
}

Output:
[
    {"transaction": 100, "gateway": "Square", "total_fee": 3.65},
    {"transaction": 500, "gateway": "Stripe", "total_fee": 15.80},
    {"transaction": 2000, "gateway": "PayPal", "total_fee": 50.40},
    {"transaction": 15000, "gateway": "PayPal", "total_fee": 379.40}
]

Constraints:
 Example output includes a transaction (15000) exceeding the stated max_amount constraints;
 a real implementation should enforce those bounds.

 Pseudo:
 1. check if amount < max_amount
    2. calculate it's cost (fixed + percentage)
    3. if amount < max_amount and  { map the calculated cost to gateway }
        3a. cached min amount
    4. if final min amount == float('inf'), return empty map (edge case)
'''


def Routing(gateways, transactions):
    output = []
    # for each transaction
    for t in transactions:
        min_fee = float('inf')
        fee_map = {}
        # calculate cost for given gateway
        for g in gateways:
            cost = g["fixed_fee"] + (t * g["percent_fee"])
            # cost within boundaries
            if cost > g["max_amount"] or cost < g["min_amount"]:
                continue
            # cache smaller fee
            min_fee = min(min_fee, cost)
            # store cost info
            fee_map[cost] = {"transaction": t, "gateway": g["name"], "total_fee": cost}

        # edge case : emtpy map from all fees being out-of-bounds
        if not fee_map:
            output.append({})
        else:
            output.append(fee_map[min_fee])

    return output


gateways = [{"name": "Stripe", "fixed_fee": 0.30, "percent_fee": 0.029, "min_amount": 0, "max_amount": 5000},
            {"name": "PayPal", "fixed_fee": 0.40, "percent_fee": 0.025, "min_amount": 0, "max_amount": 10000},
            {"name": "Square", "fixed_fee": 0.15, "percent_fee": 0.035, "min_amount": 0, "max_amount": 2000}]

transactions = [100, 500, 2000, 15000]

print(Routing(gateways, transactions))
