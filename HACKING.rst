DefCore Style Commandments
==========================

- Step 1: Read the OpenStack Style Commandments
  http://docs.openstack.org/developer/hacking/
- Step 2: Read on

DefCore Specific Commandments
-----------------------------

- [D300] When adding tests to "flagged" lists, generally only the most
  current Board-approved .json file and the .next.json file should be
  modified.  There is no need to modify older guidelines unless the most
  current Board-approved guideline doesn't cover the OpenStack release
  you are concerned with.
- [D301] The "tests" lists in the .json capabilities lists are immutable
  once approved by the Board.  Therefore if you desire to flag a test,
  in an approved capability list, add a "flagged" block to the test.  Do
  _not_ remove it from the "tests" section.
- [D302] If a test is found to not meet the DefCore Flagging Criteria
  defined in this document after the Board has approved a Guideline,
  the corresponding tests should have a "flagged" block added to the
  the relevant tests in the "tests" section of the relevant Board-approved
  Guidelines.
    - See [D307] for details about format requirements.
    - See [D308] for conditions on also adding to the .next.json.
- [D303] Tests that are found to inadequately test the underlying
  Capability, due to bugs or design flaws, should have a "flagged"
  block added to the section for the test in the "tests" section of
  the most recent Board-approved Guideline.
- [D304] Before the Board approves the capabilities listed in the
  .next.json file, a committee member will submit a patch that copies
  the .next.json file to an appropriately named new file, updates the
  "status", "replaces", and "id" fields, and updates the "required-since"
  field within newly required capabilities.  The patch should include the
  matching generated RST version of the JSON file.  This patch should be
  marked as -1 workflow until after approval.
- [D305] DefCore guidelines generally cover the most recent three
  releases of OpenStack, though the DefCore Committee has the power to
  determine otherwise.  The "releases" section of the .next.json file
  should generally be updated shortly after the Board approves a release
  so that contributors can see what releases the proposed Guideline
  targets.
- [D306] When modifying "comment" and "guidance" sections, refer to
  definitions and processes found in the "process" directory of the
  repository rather than duplicating or restating them.  This helps us
  avoid the appearance of having multiple sources of truth.
- [D307] When adding a "flagged" section to a json file, all fields
  listed in the relevant schema document for the "flagged" section are
  required.
- [D308] If the reason for adding a "flagged" block is not expected
  to be resolved before the next Guideline is submitted to tbe Board
  for approval, then matching entries should also be made in the
  .next.json Guideline.
