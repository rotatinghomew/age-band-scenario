import unittest

from inspect_inputs import read_tables


class SourceRecords(unittest.TestCase):
    def test_entry_point_distinguishes_choice_and_outcome(self):
        tables = read_tables()
        members = {(row['person'],row['season']) for row in tables['members']}
        for row in tables['choices']:
            self.assertIn((row['person'],row['season']),members)
            if row['season']=='2026':
                self.assertEqual('unobserved', row['outcome'])
        self.assertTrue(any('+' in row['available'] for row in tables['choices']))

    def test_existing_and_offered_positions_both_have_source_slots(self):
        tables = read_tables()
        old_slots = {row['slot'] for row in tables['entries']}
        new_slots = {row['slot'] for row in tables['offers']}
        intents = {row['intent']:row for row in tables['choices']}
        for row in tables['notices']:
            self.assertIn(row['old_slot'],old_slots)
            self.assertIn(row['new_slot'],new_slots)
            self.assertEqual(row['person'],intents[row['intent']]['person'])
        confirmations = [row for row in tables['notices'] if row['state']=='accepted']
        self.assertTrue(all(any(row['new_slot']==item['new_slot'] and row['received']>item['received'] and item['state']=='offered'
                                for item in tables['notices']) for row in confirmations))

    def test_migration_forms_have_distinct_team_and_venue_replies(self):
        tables = read_tables()
        requests = {row['request']:row for row in tables['migration_requests']}
        for remaining in requests.values():
            self.assertLessEqual(set(filter(None,remaining['requires'].split('+'))),set(requests))
        for reply in tables['migration_replies']:
            request = requests[reply['request']]
            self.assertEqual(reply['by'],request['release_by'] if reply['action']=='release' else request['person'])
        self.assertTrue(any(row['action']=='withdraw' for row in tables['migration_replies']))
