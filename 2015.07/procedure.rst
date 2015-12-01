2015.07 DefCore Testing
=======================

Testing against Defcore 2015.07 Capabilities
--------------------------------------------

https://git.openstack.org/cgit/openstack/defcore/tree/2015.07.json

Tempest can be run standalone, or under a test runner such as refstack-client
or rally. If only testing against Defcore capabilities, you can use the
--load-list argument and a file containing a list of the Defcore tests. If
run with the refstack-client, test output will be parsed to list only
passing tests in a json formatted file. We recommend running under
refstack-client.

The test names of the capabilities are derived from a recent release of
Tempest, from the time of capabilitiy approval. Keep in mind that Tempest
is under active development, and tests may move. If you're not seeing
full coverage, please consider reverting back to a Tempest sha that more
closely matches the capability release date. Please contact Chris Hoge
<interop@openstack.org> for assistance if needed.

It's important to run a recent version of Tempest, as major bugs related to
network provisioning have been fixed. Some tests are still flagged due to
outstanding bugs in the Tempest library, particularly tests that require SSH.
We are working on correcting these bugs upstream. Please note that
although some tests are flagged because of bugs, there is still an
expectation that the capabilities covered by the tests are available.

In addition to testing required capabilities, we are also interested
in collecting data on which API tests are being passed by production clouds.
This information will be very useful in determining which capabilities will be
used to define future releases.

Defcore Recommended Test Procedure

The following procedure is recommended, but not required for testing Defcore.
This procedure assumes you're running a Linux test platform (Ubuntu 14.04
or CentOS 7 have been verified) with administrator privileges.

* Download the refstack client:

  ``git clone https://git.openstack.org/openstack/refstack-client``

* In the refstack-client directory, install tempest and required dependencies.
  You may specify a specific tag of tempest with the -t option. refstack-client
  defaults to '98f62ee' as of this writing but the latest defcore requirement,
  2015.07 at the time of this writing, requires '26149b612d'.

  ``./setup_env``

* Download a list of tests from the Defcore site:
  http://git.openstack.org/cgit/openstack/defcore/tree/2015.07/2015.07.required.txt

* Configure tempest.conf for your cloud. If you need assistance in common
  parameters or settings contact interop@openstack.org. There is also a tempest
  configuration guide at
  https://git.openstack.org/cgit/openstack/tempest/tree/doc/source/configuration.rst

* You can run within the refstack, from the refstack-client directory:

  ./refstack-client test -c ~/tempest.conf -vv --test-list
  http://git.openstack.org/cgit/openstack/defcore/plain/2015.07/2015.07.required.txt

* Review the test results, and when you're satisfied, upload it to Refstack server
  then send them to interop@openstack.org.

  ./refstack-client upload <Path of results file>

* The results are stored in a json file in the directory. You can also check your
  result on the Refstack server https://refstack.openstack.org:

  ``.tempest/.testrepository``

* Every effort should be made to pass all of the required tests, but you
  will want to compare any lists of failed tests to the list of flagged tests.
  http://git.openstack.org/cgit/openstack/defcore/tree/2015.07/2015.07.flagged.txt

  The refstack.openstack.org also gives you result where you can easily identify
  exactly which tests still need to be passed.

Known Issues and Recommendations
--------------------------------

Currently after failures modes Tempest does not clean up test resources. We
strongly recommend that you run Tempest against a test OpenStack cloud
rather than a production cloud. Successful tests against test deployments that
are functionally equivalent to production clouds is acceptable for current
capabilities assessment.

You may find it useful to run Swift tests as a separate run, using the
``accounts.yaml`` framework to specify users with Swift-specific roles.
