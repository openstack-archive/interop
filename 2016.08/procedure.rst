2016.08 Interoperability Guideline Testing
==========================================

Testing against 2016.08 Capabilities
-------------------------------------

https://opendev.org/openstack/interop/raw/branch/master/2016.08.json

Tempest can be run standalone, or under a test runner such as refstack-client
or rally. If only testing against required capabilities, you can use the
--load-list argument and a file containing a list of the required tests. If
run with the refstack-client, test output will be parsed to list only
passing tests in a JSON formatted file. We recommend running under
refstack-client.

The test names of the capabilities are derived from a recent release of
Tempest, from the time of capability approval. Keep in mind that Tempest
is under active development, and tests may move. If you're not seeing
full coverage, please consider reverting back to a Tempest sha that more
closely matches the capability release date. The git SHA of Tempest that was
known to be working at the time the Guideline was approved is listed in the
Guideline JSON document itself (just search for "git-sha").  Please contact
Chris Hoge <interop@openstack.org> for assistance if needed.

It's important to run a recent version of Tempest, as major bugs related to
network provisioning have been fixed. Some tests are still flagged due to
outstanding bugs in the Tempest library, particularly tests that require SSH.
We are working on correcting these bugs upstream. Please note that
although some tests are flagged because of bugs, there is still an
expectation that the capabilities covered by the tests are available.

In addition to testing required capabilities, we are also interested
in collecting data on which API tests are being passed by production clouds.
This information will be very useful in determining which capabilities will be
used to define future releases.  For that reason, we ask that you run all
tests rather than just the required subset when submitting results to
the OpenStack Foundation.

It is important to note that you MUST NOT modify the Tempest tests in any
way.  Modifying the tests means that Capability being tested is validated
in a different way on your cloud than it is on other clouds, which voids
any guarantee of interoperability.  If you're having problems passing
all required tests, please contact Chris Hoge <interop@openstack.org>
for assistance or consider filing a request to have the tests flagged.
Please refer to `HACKING <../HACKING.rst>`_ for information on valid
reasons to flag a test and how to file a flag request.  Results from
modified tests cannot be accpeted as valid for trademark licensing
purposes.

Recommended Test Procedure

The following procedure is recommended, but not required for testing.
This procedure assumes you're running a Linux test platform (Ubuntu 14.04
or CentOS 7 have been verified) with administrator privileges.

* Download the RefStack client:

  ``git clone https://opendev.org/openstack/refstack-client``

* In the refstack-client directory, install tempest and required dependencies.
  You may specify a specific tag of tempest with the -t option.

  ``./setup_env``

* Optionally, download a list of test from the RefStack site. We strongly
  encourage you to run the full set of api tests, as this not only qualifies
  you for the trademark but also gives the Interop Working Group (formerly
  the DefCore Committee) feedback on deployed capabilities to help us
  determine future guidelines.
  https://refstack.openstack.org/api/v1/guidelines/2016.08/tests?type=required

* Configure tempest.conf for your cloud. If you need assistance in common
  parameters or settings contact interop@openstack.org. The recommended
  configuration is to use one non-admin account, defined in account.yaml
  with dynamic credentials disabled. More information is available in the
  configuration guide at
  https://docs.openstack.org/tempest/latest/configuration.html

* You can run within the refstack, from the refstack-client directory either
  against all api tests or against the downloaded test list.

  ``./refstack-client test -c ~/tempest.conf``

  ``./refstack-client test -c ~/tempest.conf --test-list <test-list-file-name>``

* Review the test results, and when you're satisfied, upload it to RefStack server
  then send them to interop@openstack.org.

  ``./refstack-client upload <Path of results file>``

* The results are stored in a JSON file in the directory. You can also check your
  result on the RefStack server https://refstack.openstack.org:

  ``.tempest/.testrepository``

* Every effort should be made to pass all of the required tests, but you
  will want to compare any lists of failed tests to the list of flagged tests.
  The refstack server will automatically grade tests results, taking
  into account flagged tests.
