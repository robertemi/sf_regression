import string
import random
from data_generation.Lead import Lead

class LeadFactory:

    @staticmethod
    def random_name(length=12):
        return ''.join(random.choices(string.ascii_letters, k=length))

    @staticmethod
    def random_company(length=10):
        return ''.join(random.choices(string.ascii_letters, k=length))

    def create_random_lead(self):
        status = random.choice(['Open - Not Contacted',
                          'Working - Contacted',
                          'Closed - Converted',
                          'Closed - Not Converted'])

        rating = random.choice(['Hot', 'Warm', 'Cold'])

        source = random.choice(['Web', 'Phone Inquiry', 'Partner Referral',
                          'Purchased List', 'Other'])
        return Lead(
            name=LeadFactory.random_name(),
            company=LeadFactory.random_company(),
            status=status,
            rating=rating,
            source=source,
            revenue=random.randint(10000, 10000000),
            number_of_employees=random.randint(10, 10000),
            probability=random.randint(1,100)
        )

    def generate_leads(self, count):
        return [self.create_random_lead() for _ in range(count)]
