from campusflow.tickets import generate_ticket_id

import unittest

# TODO: Import generate_ticket_id


class TestGenerateTicketId(unittest.TestCase):
    def test_empty_records(self):
        records = []
        actual = generate_ticket_id(records)
        self.assertEqual(actual,"T001")


    def test_generates_next_sequential_id(self):
        records = [
            {"id": "T001"},
            {"id" : "T002"},
            {"id" : "T003"},
        ]
        actual = generate_ticket_id(records)
        self.assertEqual(actual,"T004")

    def test_add_max_id(self):
        records = [
            {"id" : "T001"},
            {"id" : "T007"},
            {"id" : "T003"}
        ]
        actual = generate_ticket_id(records)
        self.assertEqual(actual,"T008")