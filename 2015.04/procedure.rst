Kilo Cycle DefCore Testing for Vancouver Summit.
================================================

Testing against Defcore 2015.04 Capabilities
--------------------------------------------

https://github.com/openstack/defcore/blob/master/2015.04.json

Tempest can be run standalone, or under a test runner such as refstack-client
or rally. If only testing against Defcore capabilities, you can use the
--load-list argument and a file containing a list of the Defcore tests. If
run with the refstack-client, test output will be parsed to list only
passing tests in a json formatted file. 

The test names of the capabilities are derived from a recent release of
Tempest, from the time of capabilitiy approval. Keep in mind that Tempest
is under active development, and tests may move. If you're not seeing
full coverage, please consider reverting back to a Tempest sha that more
closely matches the capability release date. Please contact Chris Hoge 
<chris@openstack.org> for assistance if needed.

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

  ``git clone https://gitub.com/stackforge/refstack-client``

* In the refstack-client directory, install tempest and required dependencies.
  You may specify a specific tag of tempest with the -t option. refstack-client
  defaults to '7c8fcc67'

  ``./setup-env``

* Download a list of tests from the Defcore site:
  https://github.com/openstack/defcore/blob/master/2015.03/2015.04.required.txt

* Configure tempest.conf for your cloud. If you need assistance in common
  parameters or settings contact chris@openstack.org.

* Once you have a working config, run tempest. You can run within the refstack
  client, or run tempest directly. For direct running, from the refstack-client
  directory:

  ``cd .tempest``
  ``./run_tempest -C  <your_tempest.conf> -- --load-list 2015.04.required.txt``

* Review the test results, and when you're satisfied, send them to
  chris@openstack.org. The results are stored in a json file in the directory

  ``.tempest/.testrepository``

Known Issues and Recommendations
--------------------------------
Currently after failures modes Tempest does not clean up test resources. We
strongly recommend that you run Tempest against a test OpenStack cloud
rather than a production cloud. Successful tests against test deployments that
are functionally equivalent to production clouds is acceptable for current
capabilities assessment.
