import datetime
from typing import Dict, Optional, Tuple

GOVERNORATE_CODES = {
    '01': 'Cairo',
    '02': 'Alexandria',
    '03': 'Port Said',
    '04': 'Suez',
    '11': 'Damietta',
    '12': 'Dakahlia',
    '13': 'Ash Sharqia',
    '14': 'Kaliobeya',
    '15': 'Kafr El Sheikh',
    '16': 'Gharbia',
    '17': 'Monufia',
    '18': 'Beheira',
    '19': 'Ismailia',
    '21': 'Giza',
    '22': 'Beni Suef',
    '23': 'Fayoum',
    '24': 'Minya',
    '25': 'Asyut',
    '26': 'Sohag',
    '27': 'Qena',
    '28': 'Aswan',
    '29': 'Luxor',
    '31': 'Red Sea',
    '32': 'New Valley',
    '33': 'Matrouh',
    '34': 'North Sinai',
    '35': 'South Sinai',
    '88': 'Foreign'
}
def validate_egyptian_id(id_number: str) -> Tuple[bool, Optional[str]]:
    """
    Validate Egyptian national ID number.
    Returns tuple of (is_valid, error_message)
    """
    if not id_number.isdigit():
        return False, "ID must contain only digits"
    
    if len(id_number) != 14:
        return False, "ID must be 14 digits long"
    
    # Extract components
    century_code = id_number[0]
    year = id_number[1:3]
    month = id_number[3:5]
    day = id_number[5:7]
    governorate_code = id_number[7:9]
    
    # Validate century
    if century_code not in ('2', '3'):
        return False, "Invalid century code"
    
    # Validate date
    try:
        full_year = 1900 + int(year) if century_code == '2' else 2000 + int(year)
        datetime.datetime(year=full_year, month=int(month), day=int(day))
    except ValueError:
        return False, "Invalid birth date"
    
    # Validate governorate
    if governorate_code not in GOVERNORATE_CODES:
        return False, "Invalid governorate code"
    
    return True, None

def extract_data_from_id(id_number: str) -> Dict:
    """Extract information from valid ID number"""
    century_code = id_number[0]
    year = id_number[1:3]
    month = id_number[3:5]
    day = id_number[5:7]
    governorate_code = id_number[7:9]
    sequence = id_number[9:12]
    gender_digit = id_number[12]
    
    full_year = 1900 + int(year) if century_code == '2' else 2000 + int(year)
    gender = 'male' if int(gender_digit) % 2 == 1 else 'female'
    
    return {
        'birth_date': f"{full_year}-{month}-{day}",
        'governorate': GOVERNORATE_CODES.get(governorate_code, 'Unknown'),
        'gender': gender,
        'sequence_number': sequence
    }