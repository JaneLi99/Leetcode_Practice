# Fraud Risk Assessment
# The fraud detection team at Stripe aims to reduce merchant fraud risk with minimal pain to good merchants.
# You are tasked with developing a system to assess fraud risk associated with transactions made to various merchants.
# Given:
# transactions_list — list of n transactions (1 ≤ n ≤ 1000), each a comma-separated string:
# merchant_id (string)
# amount (integer)
# customer_id (string)
# hour (integer, 0 ≤ hour ≤ 23)
#
# rules_list — list of n rules (1:1 with transactions), each a comma-separated string:
# min_transaction_amount (integer)
# multiplicative_factor (integer)
# additive_factor (integer)
# penalty (integer)
#
# merchants_list — list of m merchants (1 ≤ m ≤ 1000), each a comma-separated string:
# merchant_id (string)
# base_score (integer, 1 ≤ base_score ≤ 50)
#
# Scoring — applied in 3 separate passes:
# Pass 1 — Multiplicative:
# For each transaction, if amount > min_transaction_amount, multiply that merchant's current_score by multiplicative_factor.
# Pass 2 — Additive:
# Group transactions by (merchant_id, customer_id). For each group where the transaction count ≥ 3,
# cumulatively add the additive_factor of the 3rd, 4th, 5th... transactions to that merchant's score.
# Pass 3 — Penalty:
# Group transactions by (merchant_id, customer_id, hour). For each group where the transaction count ≥ 3, add or subtract the penalty:
#
# If hour < 12 (AM): subtract the penalty
# If hour ≥ 12 (PM): add the penalty
#
# Output:
# Return a list of comma-separated strings "merchant_id,score" sorted in lexicographical order by merchant_id.
from collections import defaultdict


def assess_fraud_risk(transactions_list, rules_list, merchants_list):
    merchants_dict = {}
    for merchant in merchants_list:
        m = merchant.split(",")
        merchants_dict[m[0]] = int(m[1])

    transactions = []
    for transaction, rule in zip(transactions_list, rules_list):
        t = transaction.split(",")
        r = rule.split(",")
        transactions.append({
            "merchant_id": t[0],
            "amount": int(t[1]),
            "customer_id": t[2],
            "hour": int(t[3]),
            "min_transaction_amount": int(r[0]),
            "multiplicative_factor": int(r[1]),
            "additive_factor": int(r[2]),
            "penalty": int(r[3])
        })
    # print(transactions)

    # Pass 1 — Multiplicative:
    for transaction in transactions:
        if transaction["amount"] > transaction["min_transaction_amount"]:
            merchants_dict[transaction["merchant_id"]] = merchants_dict[transaction["merchant_id"]] * transaction["multiplicative_factor"]
        else:
            continue
    # print("merchants_dict1: ", merchants_dict)

    # Pass 2 — Additive:
    customer_merchant_dict = defaultdict(int)
    for transaction in transactions:
        merchant = transaction["merchant_id"]
        customer = transaction["customer_id"]
        key = (merchant, customer)
        customer_merchant_dict[key] += 1
        if customer_merchant_dict[key] >= 3:
            merchants_dict[merchant] += transaction["additive_factor"]

    # print("merchants_dict2: ", merchants_dict)

    # Pass 3 — Penalty:
    customer_merchant_hour_dict = defaultdict(int)
    for transaction in transactions:
        merchant = transaction["merchant_id"]
        customer = transaction["customer_id"]
        hour = transaction["hour"]
        key = (merchant, customer, hour)
        customer_merchant_hour_dict[key] += 1
        if customer_merchant_hour_dict[key] >= 3:
            if hour < 12:
                merchants_dict[merchant] -= transaction["penalty"]
            else:
                merchants_dict[merchant] += transaction["penalty"]

    # print("merchants_dict3: ", merchants_dict)

    result = []
    for merchant in sorted(merchants_dict.keys()):
        result.append(f"{merchant},{int(merchants_dict[merchant])}")

    return result


# ── Example Input ──────────────────────────────────────────────
def main():
    transactions_list = [
        "merchant1,1200,customer1,10",
        "merchant1,500,customer1,10",
        "merchant2,2400,customer1,15",
        "merchant1,800,customer1,16",
        "merchant1,1000,customer2,17",
        "merchant1,1400,customer1,10",  # customer1→merchant1, hour=10: 3rd time this (merchant,cust,hour) combo
    ]

    rules_list = [
        "1000,2,8,15",
        "1400,5,3,19",
        "2300,3,17,3",
        "700,4,10,5",
        "900,2,6,12",
        "1300,3,9,20",
    ]

    merchants_list = [
        "merchant1,10",
        "merchant2,5",
    ]

    output = assess_fraud_risk(transactions_list, rules_list, merchants_list)
    print(output)
    # for line in output:
    #     print(line)

if __name__ == "__main__":
    main()