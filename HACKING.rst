Interop Working Group Commandments
===================================

- Step 1: Read the OpenStack Style Commandments
  https://docs.openstack.org/hacking/latest/
- Step 2: Read the following Interop Working Group process
  documents in the following recommended order:

  - `Core Definition <doc/source/process/CoreDefinition.rst>`_
  - `OpenStack Interop WG Process 2016A <doc/source/process/2016A.rst>`_

- Step 3: Read on

Interop Working Group Specific Commandments
--------------------------------------------

- [D300] When adding tests to "flagged" lists, generally only the most
  current Board-approved .json file and the .next.json file should be
  modified.  There is no need to modify older Guidelines unless the most
  current Board-approved Guideline doesn't cover the OpenStack release
  you are concerned with.
- [D301] The "tests" lists in the .json capabilities lists are immutable
  once approved by the Board.  Therefore if you desire to flag a test,
  in an approved capability list, add a "flagged" block to the test.  Do
  _not_ remove it from the "tests" section.
- [D302] If a Capability is found to not meet the `Core Criteria
  <doc/source/process/CoreCriteria.rst>`_ after the Board has approved
  a Guideline, the corresponding tests should have a "flagged" block added
  to the the relevant tests in the "tests" section of the relevant
  Board-approved Guidelines.

    - See [D307] and [D309] for details about format requirements.
    - See [D308] for conditions on also adding to the .next.json.

- [D303] Tests that are found to inadequately test the underlying
  Capability due to bugs or design flaws, should have a "flagged"
  block added to the section for the test in the "tests" section of
  the most recent Board-approved Guideline.
- [D304] Before the Board approves the capabilities listed in the
  .next.json file, a committee member will submit a patch that copies
  the .next.json file to an appropriately named new file, updates the
  "status", "replaces", and "id" fields, and updates the "required-since"
  field within newly required capabilities.  The patch should include the
  matching generated RST version of the JSON file.  This patch should be
  marked as -1 workflow until after approval.
- [D305] Interop Guidelines generally cover the most recent three
  releases of OpenStack, though the Interop Working Group has the
  power to determine otherwise.  The "releases" section of the .next.json file
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
- [D309] The "reason" field of the "flagged" section must begin with the
  flag type. For example:

  ``"reason" : "[D400] The Foo test doesn't meet Core Criteria because ..."``

- [D310] If you believe a test needs to be flagged but the reason for doing
  so doesn't appear in the list below, you must do the following:

  #. Submit the test for flagging using [D404] as the flag type. Please also
     provide the reason you believe this test needs to be flagged; see [D309]
     above for details. [D404] indicates that you are uncertain about which
     flag to use or believe that a new reason for considering flags needs to be
     discussed. *[D404] is only a placeholder to facilitate this discussion.*
  #. In that same proposed change, also submit a patch against the HACKING
     file adding your proposed new flag to the list below.
  #. If at all possible, please include a link to code and/or test runs which
     demonstrate the reason a new flag type is needed.
  #. The Interop Working Group will discuss and consider the flagging
     proposal as well as the proposed new reason. They may accept or decline
     either proposal.
- [D311] Once a test has been flagged, it will remain flagged for that Guideline.
- [D312] When a new Guideline is proposed for Board approval, no flagged tests
  will be included in the Guideline. Flags will be added in subsequent patches.

Interop Working Group Test Flagging Guidelines
-----------------------------------------------

The Interoper Working Group may "flag" tests to mark them as not
required for a given Guideline. There are different flag types; each flag
type indicates a fairly narrow category of reasons for flagging a given test.

Valid reasons for flagging a test are limited to the following:

- [D400] The test is for a Capability that fails to meet the Criteria
  as set out in the
  `Core Criteria document <doc/source/process/CoreCriteria.rst>`_.
- [D401] The test fails or is skipped due to a bug in the test and the bug is
  accepted by the OpenStack project which maintains the test.
- [D402] The test fails or is skipped due to a bug in the code that provides
  the Capability and the bug is accepted by the OpenStack project which
  maintains the Capability.
- [D403] The test fails because other non-required Capabilities are also
  tested.
- [D404] Flag Not Found - Use this flag if none of the others fit.
- [D405] The test reflects an implementation choice that is not widely
  deployed even if the Capability is widely deployed.
- [D406] Test removed permanently from test suite.

To file a flag request for a test, follow these steps:

#. Make sure you have a development environment set up accoring to the
   `Developer's Guide
   <https://docs.openstack.org/infra/manual/developers.html>`_.

#. Clone the defcore repo by running:

   .. code-block:: console

      $ git clone https://git.openstack.org/openstack/defcore.git

#. Open the relevant Guideline or Guidelines in your favorite text
   editor and locate the tests you want to flag.

#. Add a flag block to the test using the rationale above.  For
   example, if I want to flag this test:

   .. code-block:: json

      "tempest.api.compute.servers.test_list_server_filters.ListServerFiltersTestJSON.test_list_servers_filtered_by_ip": {
         "idempotent_id": "id-43a1242e-7b31-48d1-88f2-3f72aa9f2077"
      },

   I might modify the section to read:

   .. code-block:: json

      "tempest.api.compute.servers.test_list_server_filters.ListServerFiltersTestJSON.test_list_servers_filtered_by_ip": {
         "idempotent_id": "id-43a1242e-7b31-48d1-88f2-3f72aa9f2077",
         "flagged": {
           "date": "2016-06-13",
           "reason": "[D401] This test is skipped by Tempest due to bug https://bugs.launchpad.net/tempest/+bug/1600349.",
           "action": "Remove flag when Tempest fix is in place."
         }
      },

#. Once you've saved your changes, commit the chage locally:

   .. code-block:: console

     $ git commit -a

   Be sure to write a useful commit message explaning your change.

#. Push the change to gerrit, where your request can be reviewed:

   .. code-block:: console

     $ git review

Please note that if you're having trouble setting up a development
environment, you can also talk to the OpenStack Foundation's
Interoperability Engineer <interop@openstack.org> or contact the
Interop Working Group (formerly DefCore Committee) via email
<defcore-committee@lists.openstack.org>.  We'll be happy to try to
assist you or help file a request on your behalf.
