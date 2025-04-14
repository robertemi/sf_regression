from data_generation.LeadFactory import LeadFactory
import csv

def main():
    lf = LeadFactory()
    leads = lf.generate_leads(60000)

    file_path = r'C:\Proiecte\Proiecte_de_ale_mele\Python\sf_regression\leads.csv'

    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Company', 'Status', 'Rating', 'Source', 'Revenue', 'Number_of_Employees', 'Probability'])

        for lead in leads:
            writer.writerow([
                lead.name,
                lead.company,
                lead.status,
                lead.rating,
                lead.source,
                lead.revenue,
                lead.number_of_employees,
                lead.probability
            ])

    print(f"Leads exported to '{file_path}'")

# Run the main function
if __name__ == "__main__":
    main()