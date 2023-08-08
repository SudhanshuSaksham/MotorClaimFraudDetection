# Hierarchy level for ordinal encoding
ordinal_insured_education_level_hierarchy = ['High School', 'College', 'Associate', 'JD', 'MD', 'Masters', 'PhD']
ordinal_incident_severity_hierarchy = ['Trivial Damage', 'Minor Damage', 'Major Damage', 'Total Loss']
ordinal_categories_list = [ordinal_insured_education_level_hierarchy, ordinal_incident_severity_hierarchy]

# Binning for continuous features
months_as_customer_bins = [0, 100, 200, 300, 400, 500]
months_as_customer_labels = ['very new customer', 'new customer', 'regular customer', 'old customer',
                             'very old customer']

age_bins = [1, 19, 30, 50, 100]
age_labels = ['minor', 'young', 'old', 'very old']

if __name__ == '__main__':
    pass
