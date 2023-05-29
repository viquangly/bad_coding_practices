
import jinja2

long_sql = '''
    SELECT
        CUSTOMER_NAME,
        CAST(PHONE AS VARCHAR) AS NODE,
        'PHONE' AS EDGE_TYPE
    FROM PHONE_TABLE
    
    UNION ALL
    
    SELECT
        CUSTOMER_NAME,
        EMAIL AS NODE,
        'EMAIL' AS EDGE_TYPE
    FROM EMAIL_TABLE
    
    UNION ALL
    
    SELECT
        CUSTOMER_NAME,
        ADDRESS AS NODE,
        'ADDRESS' AS EDGE_TYPE
    FROM ADDRESS_TABLE
    
    UNION ALL
    
    SELECT
        CUSTOMER_NAME,
        SSN AS NODE,
        'SSN' AS EDGE_TYPE
    FROM SSN_TABLE
'''

print(
    jinja2.Template(
        '''
        {% for x in ['PHONE', 'EMAIL', 'ADDRESS', 'SSN'] %}
        SELECT
            CUSTOMER_NAME,
            {% if x == 'PHONE' %}
            CAST(PHONE AS VARCHAR) AS PII
            {% else %}
            {{x}} AS PII
            {% endif %}
        FROM {{x}}_TABLE
        
        {% if not loop.last %}
        UNION ALL
        {% endif %}
        
        {% endfor %}
        '''
    ).render()
)
