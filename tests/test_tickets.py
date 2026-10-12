from campusflow.tickets import generate_ticket_id, create_and_store_ticket

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

class TestCreateAndStoreTicket(unittest.TestCase):
    def test_creates_and_stores_ticket(self):
        records = []
        ticket = create_and_store_ticket(records,"Wi-Fi unavailable", "Network", "high", 5)
        actual = len(records)
        ticket_id = records[0]["id"]
        ticket_status = records[0]["status"]
        self.assertEqual(actual, 1)
        self.assertEqual(ticket_id, "T001")
        self.assertEqual(ticket_status, "open")

class Test