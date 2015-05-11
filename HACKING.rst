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
  in an approved capability list, add it to the "flagged" section but do
  not remove it from the "tests" section.
- [D302] If a capability is found to not meet the `Core Criteria
  <./process/CoreCriteria.rst>`_ after the Board has approved a guideline,
  the corresponding tests should be added to the "flagged" section of
  the relevant Board-approved guidelines and removed from the "tests"
  section of the .next.json file.
- [D303] Tests that are found to inadequately test the underlying
  Capability, due to bugs or design flaws should be added to the
  "flagged" section of the most recent Board-approved guideline and the
  .next.json list.
- [D304] When the Board approves the capabilities listed in the
  .next.json file, a committee member will submit a patch that copies
  the .next.json file to an appropriately named new file, updates the
  "status", "replaces", and "id" fields, and updates the "guidelines"
  field within each capability.  These fields shouldn't be adjusted
  until the Board has approved the list.
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
