======================
Feature Description
======================

This test specification describes interoperability testing as it is understood
by the Interop Working Group. An important goal of interoperability is that
end users of OpenStack should be able to expect certain APIs to be reliable
across clouds.

The spec aims to define how interoperability should be tested for OpenStack.
It provides guidelines for evaluating current tests and the need for new test
cases.

This document is a declaration of intent and looks at where interoperability
testing is heading, not just where it is today.

What is tested
==============

The focus of this test specification is functional and behavioral testing
of the OpenStack REST API of the OpenStack projects.

What is not tested
==================

- OpenStack clients
- Internal APIs
- Python APIs
- Performance testing

Interoperability Tests
======================

Goals
 #. The only requirement to run interop functional tests should be an endpoint
    and credentials necessary to run the tests. Tests should ideally discover
    the methods it needs to use to set up whatever is necessary to exercise the
    API under test. For example: a test for image-delete needs to have an image
    in the cloud to delete.  Ideally, the test should discover what method it needs
    to use to put an image in the cloud (image upload, image import, etc). Tests
    must favor direct API calls where they can. Discoverability for multiple
    implementations remains an open issue.

 #. The test should favor minimization. Test only the capability under
    test with as little set up as possible, using as few other resources
    as possible. For example, tests that don't actually need multiple user
    credentials or admin privileges shouldn't require them.

Guidelines
 #. Interop API functional tests should target and validate one
    capability. Some capabilities may require discovery calls
    and these should be included also in the test. Each capability
    should have at least one interop API functional test.

 #. Interop API functional tests should not use non-required
    capabilities.

 #. Interop scenario tests may use several capabilities to test end
    to end functionality and none of the capabilities used may be
    non-required capabilities.

 #. Tests must be reliable; race conditions must be avoided; tests
    should not be time dependent. If any of these problems occur the
    test will be flagged and either fixed or removed from the guidelines.

 #. Tests must be able to run consistently across all the releases
    covered by the Guidelines which are considered valid by the OpenStack
    Foundation for the OpenStack Powered program.

 #. Tests should not require more credentials than required to test the
    capability itself.

 #. Tests must not be harmful to the end user's environment, that is no
    changing credentials nor destroying user's data nor altering any
    other user resource other than those specifically created as part
    of the test.

 #. Test cases must setup any data they need to run and clean up after
    themselves. It is not acceptable to corrupt the user's environment
    or leave any test data or test configuration behind.
