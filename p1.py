lt = 1000

max_3 = (lt - 1) / 3
max_5 = (lt - 1) / 5
max_15 = (lt - 1) / 15

sigma_3 = 3 * (max_3) * (max_3 + 1) / 2
sigma_5 = 5 * (max_5) * (max_5 + 1) / 2
sigma_15 = 15 * (max_15) * (max_15 + 1) / 2

print sigma_3 + sigma_5 - sigma_15
