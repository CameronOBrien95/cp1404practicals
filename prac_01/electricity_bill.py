TARRIF_11 = 0.244618
TARRIF_31 = 0.136928

print("electricity bill estimator")
tarrif_choice = int(input("Which Tarrif ? 11 or 31 ?"))
while tarrif_choice != 11 and tarrif_choice != 31:
    print("invalid tarrif, please re-enter ")
    tarrif_choice = input("Which Tarrif, 11 or 31 ? ")
hours_per_day = float(input("daily use of kWh: "))
days_per_billing = int(input("days in billing period: "))
if tarrif_choice == 11:
    cents_per_billing = TARRIF_11 * hours_per_day * days_per_billing
    print("Estimated bill: ${:.2f}".format(cents_per_billing))
else:
    cents_per_billing = TARRIF_31 * hours_per_day * days_per_billing
    print("Estimated bill: ${:.2f}".format(days_per_billing))



