class Province:
	name = ''
	key = ''

	def __init__(self, key, name):
		self.key = key
		self.name = name


def get_provinces():
	provinces = []
	provinces.append(Province('ON', 'Ontario'))
	provinces.append(Province('QC', 'Quebec'))
	provinces.append(Province('NS', 'Nova Scotia'))
	provinces.append(Province('NB', 'New Brunswick'))
	provinces.append(Province('MB', 'Manitoba'))
	provinces.append(Province('BC', 'British Columbia'))
	provinces.append(Province('PE', 'Prince Edward Island'))
	provinces.append(Province('SK', 'Saskatchewan'))
	provinces.append(Province('AB', 'Alberta'))
	provinces.append(Province('NL', 'Newfoundland & Labrador'))
	provinces.append(Province('NA', 'Not Applicable'))
	return provinces
