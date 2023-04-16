
bad = '''
    SELECT acct_nbr, transaction_date, SUM(amount) AS total_amount FROM
    transaction_table WHERE transaction_date >= '2022-08-01' AND
    transaction_date <= '2022-08-31' AND transaction_type = 'Credit Card' GROUP BY
    transaction_date ORDER BY acct_nbr, transaction_date
'''


good = '''
    SELECT
        acct_nbr,
        transaction_date,
        SUM(amount) AS total_amount
    FROM 
        transaction_table
    WHERE
        transaction_date >= '2022-08-01'
        AND transaction_date <= '2022-08-31' 
        AND transaction_type = 'Credit Card'
    GROUP BY
        transaction_date 
    ORDER BY 
        acct_nbr, transaction_date
'''
