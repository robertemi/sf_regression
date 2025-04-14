class Lead:
    """
    Relevant fields (* = mandatory field)
    Last Name*, Company*, Lead Status, Rating, Source, Annual Revenue, No. of Employees
    """
    def __init__(self, name, company, status, rating, source, revenue, number_of_employees, probability):

        if status not in ['Open - Not Contacted',
                          'Working - Contacted',
                          'Closed - Converted',
                          'Closed - Not Converted']:

            raise AttributeError('Invalid Lead Status value!')

        if rating not in ['Hot', 'Warm', 'Cold']:
            raise AttributeError('Invalid Rating value!')

        if source not in ['Web', 'Phone Inquiry', 'Partner Referral',
                          'Purchased List', 'Other']:
            raise AttributeError('Invalid Source value!')

        if probability < 1 or probability > 100:
            raise AttributeError('Invalid Probability value!')

        self.name = name
        self.company = company
        self.status = status
        self.rating = rating
        self.source = source
        self.revenue = revenue
        self.number_of_employees = number_of_employees
        self.probability = probability


