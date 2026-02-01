import csv

# List of pastry companies with their contact details
pastry_companies = [
    {
        "Name": "SweetTooth Confectioneries",
        "Phone": "+234 908 612 2222",
        "Address": "51 Tombia St, GRA2, Port Harcourt",
        "Email": "info@sweettooth-ng.com"
    },
    {
        "Name": "Buns & Batter",
        "Phone": "+234 816 296 1432",
        "Address": "45 King Perekule Road, GRA Phase II, Port Harcourt",
        "Email": "hello@bunsandbatter.com.ng"
    },
    {
        "Name": "Hearty Cakes",
        "Phone": "+234 903 665 3958",
        "Address": "Ogor street IGBOGO road, Choba, Port Harcourt",
        "Email": "contact@heartycakes.ng"
    },
    {
        "Name": "Vanessa’s BITE",
        "Phone": "+234 803 214 6147",
        "Address": "15 C.R.A Street, Elelenwo, Port Harcourt",
        "Email": "orders@vanessasbite.com"
    }
]

# File name for the export
filename = "pastry_contacts.csv"

# Writing to CSV
try:
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Phone", "Address", "Email"])
        writer.writeheader()
        writer.writerows(pastry_companies)
    print(f"Successfully exported {len(pastry_companies)} contacts to {filename}")
except Exception as e:
    print(f"An error occurred: {e}")
