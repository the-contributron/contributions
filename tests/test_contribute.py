import unittest
from datetime import date, datetime

from contribute import is_contribution_day

class TestContribute(unittest.TestCase):
    def test_2026_dates(self):
        """
        Test that the correct contribution boolean value is returned for various dates in 2025/2026
        """

        test_cases = {
            # June 2025
            date(2025, 6, 1): False,  # Week 22, day 0
            date(2025, 6, 2): False,  # Week 22, day 1
            date(2025, 6, 3): False,  # Week 22, day 2
            date(2025, 6, 4): False,  # Week 22, day 3
            date(2025, 6, 5): False,  # Week 22, day 4
            date(2025, 6, 6): False,  # Week 22, day 5
            date(2025, 6, 7): False,  # Week 22, day 6
            date(2025, 6, 8): False,  # Week 23, day 0
            date(2025, 6, 9): False,  # Week 23, day 1
            date(2025, 6, 10): True,  # Week 23, day 2
            date(2025, 6, 11): True,  # Week 23, day 3
            date(2025, 6, 12): True,  # Week 23, day 4
            date(2025, 6, 13): True,  # Week 23, day 5
            date(2025, 6, 14): False, # Week 23, day 6
            date(2025, 6, 15): False, # Week 24, day 0
            date(2025, 6, 16): False, # Week 24, day 1
            date(2025, 6, 17): True,  # Week 24, day 2
            date(2025, 6, 18): False, # Week 24, day 3
            date(2025, 6, 19): False, # Week 24, day 4
            date(2025, 6, 20): False, # Week 24, day 5
            date(2025, 6, 21): False, # Week 24, day 6
            date(2025, 6, 22): False, # Week 25, day 0
            date(2025, 6, 23): False, # Week 25, day 1
            date(2025, 6, 24): False, # Week 25, day 2
            date(2025, 6, 25): True,  # Week 25, day 3
            date(2025, 6, 26): False, # Week 25, day 4
            date(2025, 6, 27): False, # Week 25, day 5
            date(2025, 6, 28): False, # Week 25, day 6
            date(2025, 6, 29): False, # Week 26, day 0
            date(2025, 6, 30): False, # Week 26, day 1

            # Some dates outside of the range of the 'Hi, mom!' text
            date(2025, 8, 6): True,    # Wednesday
            date(2025, 9, 10): True,   # Wednesday
            date(2025, 12, 24): True,  # Wednesday
            date(2025, 8, 8): False,   # Not Wednesday
            date(2025, 9, 9): False,   # Not Wednesday
            date(2025, 10, 10): False, # Not Wednesday

            # January 2026
            date(2026, 1, 1): False,  # Week 0, day 4
            date(2026, 1, 2): False,  # Week 0, day 5
            date(2026, 1, 3): False,  # Week 0, day 6
            date(2026, 1, 4): False,  # Week 1, day 0
            date(2026, 1, 5): True,   # Week 1, day 1
            date(2026, 1, 6): True,   # Week 1, day 2
            date(2026, 1, 7): True,   # Week 1, day 3
            date(2026, 1, 8): True,   # Week 1, day 4
            date(2026, 1, 9): True,   # Week 1, day 5
            date(2026, 1, 10): False, # Week 1, day 6
            date(2026, 1, 11): False, # Week 2, day 0
            date(2026, 1, 12): False, # Week 2, day 1
            date(2026, 1, 13): False, # Week 2, day 2
            date(2026, 1, 14): True,  # Week 2, day 3
            date(2026, 1, 15): False, # Week 2, day 4
            date(2026, 1, 16): False, # Week 2, day 5
            date(2026, 1, 17): False, # Week 2, day 6
            date(2026, 1, 18): False, # Week 3, day 0
            date(2026, 1, 19): False, # Week 3, day 1
            date(2026, 1, 20): False, # Week 3, day 2
            date(2026, 1, 21): True,  # Week 3, day 3
            date(2026, 1, 22): False, # Week 3, day 4
            date(2026, 1, 23): False, # Week 3, day 5
            date(2026, 1, 24): False, # Week 3, day 6
            date(2026, 1, 25): False, # Week 4, day 0
            date(2026, 1, 26): True,  # Week 4, day 1
            date(2026, 1, 27): True,  # Week 4, day 2
            date(2026, 1, 28): True,  # Week 4, day 3
            date(2026, 1, 29): True,  # Week 4, day 4
            date(2026, 1, 30): True,  # Week 4, day 5
            date(2026, 1, 31): False, # Week 4, day 6
        }
        
        for test_date, expected_value in test_cases.items():
            test_datetime = datetime.combine(test_date, datetime.min.time().replace(hour=12))
            actual_value = is_contribution_day(test_datetime)
            
            self.assertEqual(
                actual_value, 
                expected_value,
                f"Failed for {test_date} - expected {expected_value} but got {actual_value}."
            )
            
            # Print test details for debugging
            print(f"{test_date} - {'Contribute' if actual_value == True else 'Don\'t contribute'}.")

if __name__ == '__main__':
    unittest.main()
