"""WEBHOOK_SECRET must be set and must not be the public demo value."""

import os
import unittest
from unittest import mock

from pydantic import ValidationError

from config import DEMO_WEBHOOK_SECRET, Settings


class WebhookSecretTests(unittest.TestCase):
    def _settings(self, **env):
        with mock.patch.dict(os.environ, env, clear=True):
            return Settings(_env_file=None)

    def test_unset_secret_refuses_to_start(self):
        with self.assertRaises(ValidationError):
            self._settings()

    def test_demo_secret_refuses_to_start(self):
        with self.assertRaises(ValidationError):
            self._settings(WEBHOOK_SECRET=DEMO_WEBHOOK_SECRET)

    def test_private_secret_is_accepted(self):
        self.assertEqual(self._settings(WEBHOOK_SECRET="s3cr3t-value").webhook_secret, "s3cr3t-value")


if __name__ == "__main__":
    unittest.main()
