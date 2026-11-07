import { strict as assert } from "node:assert";
import { test } from "node:test";

import { DEMO_WEBHOOK_SECRET, requireWebhookSecret } from "./config.js";

test("an unset secret refuses to start", () => {
  assert.throws(() => requireWebhookSecret(undefined));
  assert.throws(() => requireWebhookSecret(""));
});

test("the public demo secret refuses to start", () => {
  assert.throws(() => requireWebhookSecret(DEMO_WEBHOOK_SECRET));
});

test("a private secret is accepted", () => {
  assert.equal(requireWebhookSecret("s3cr3t-value"), "s3cr3t-value");
});
