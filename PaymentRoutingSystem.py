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
'''